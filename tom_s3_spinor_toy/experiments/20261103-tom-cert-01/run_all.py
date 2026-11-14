"""TOM-CERT-01 end-to-end run from a CLEAN COPY of the three source files.

Steps (each logged with the real command and exit code to logs/run_all.txt):
  S0 static checks on verifier.py: stdlib-only imports, no inexact-number tokens, no builder import
  S1 copy build_certificate.py, verifier.py, negative_controls.py into an empty temp directory
  S2 build certificate.json there          (needs sympy)
  S3 verify it with the independent verifier (exit 0 expected)
  S4 run the negative controls              (exit 0 expected = every control behaved as declared)
  S5 compare sha256 of the freshly built certificate with the certificate.json stored here
Usage: python run_all.py        exit 0 only if every step behaves as declared
"""

import ast
import hashlib
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = ["build_certificate.py", "verifier.py", "negative_controls.py"]
ALLOWED_IMPORTS = {"json", "re", "sys", "fractions"}
LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    shown = " ".join(Path(c).name if i == 0 or c.endswith(".py") else c for i, c in enumerate(cmd))
    log(f"$ {shown}   (cwd = clean copy)")
    for line in (p.stdout + p.stderr).rstrip().splitlines():
        log("  " + line)
    log(f"  -> exit code {p.returncode}")
    return p.returncode


def static_checks():
    src = (HERE / "verifier.py").read_text(encoding="utf-8")
    tree = ast.parse(src)
    imported = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            imported |= {a.name.split(".")[0] for a in n.names}
        elif isinstance(n, ast.ImportFrom):
            imported.add((n.module or "").split(".")[0])
    probs = []
    if not imported <= ALLOWED_IMPORTS:
        probs.append(f"non-stdlib/unexpected imports: {sorted(imported - ALLOWED_IMPORTS)}")
    for token in ("float", "numpy", "sympy", "build_certificate", "decimal", "math"):
        if token in src:
            probs.append(f"forbidden token in verifier.py: {token!r}")
    log(f"S0 static checks on verifier.py: imports = {sorted(imported)}")
    log(f"  -> {'OK' if not probs else 'PROBLEMS: ' + '; '.join(probs)}")
    return not probs


def main():
    import sympy

    log(
        f"TOM-CERT-01 run_all  python {platform.python_version()}  sympy {sympy.__version__}  {platform.platform()}"
    )
    ok = static_checks()
    with tempfile.TemporaryDirectory() as td:
        for name in SOURCES:
            shutil.copy2(HERE / name, td)
        log(f"S1 clean copy of {SOURCES} in an empty temp directory")
        py = sys.executable
        ok &= run([py, "build_certificate.py", "certificate.json"], td) == 0
        ok &= run([py, "verifier.py", "certificate.json"], td) == 0
        ok &= run([py, "negative_controls.py", "certificate.json"], td) == 0
        fresh = sha(Path(td) / "certificate.json")
    stored = HERE / "certificate.json"
    same = stored.exists() and sha(stored) == fresh
    log(f"S5 sha256 fresh certificate  {fresh}")
    log(f"   sha256 stored certificate {sha(stored) if stored.exists() else 'MISSING'}")
    log(f"  -> {'IDENTICAL' if same else 'DIFFERENT'}")
    ok &= same
    log(f"RUN_ALL: {'ALL STEPS AS DECLARED' if ok else 'FAILED'}")
    (HERE / "logs").mkdir(exist_ok=True)
    (HERE / "logs" / "run_all.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
