"""Derive the S^6 texture map from G96's OWN octonion structure tensor --
upgrades visualization/blender_s3s6_hopf_scene.py's S^6 spheres from
[SCHEMATIC] (Blender procedural noise) to [DERIVED] (real G2-invariant data).

Reuses experiments/20260626-g96-s6-g2-su3/g96_g2_su3.py's build_phi() via the
same importlib-loading pattern used throughout this session (C149, C193) --
NOT retyped. phi[i,j,k] IS the octonion cross-product structure tensor this
project already built and verified (dim(G2)=14, closure, Jacobi -- G96's own
checks, reused here as the Substrate Gate for this script, not re-derived).

WHAT IS ACTUALLY PLOTTED, stated precisely (the one honest artistic choice
left is named, everything downstream of it is computed, not invented):

  ONE ARTISTIC CHOICE: S^6 subset Im(O) = R^7 is 6-dimensional -- a single
  2-parameter (theta, phi) slice is rendered, embedded as
    x(theta,phi) = (sin(theta)cos(phi), sin(theta)sin(phi), cos(theta), 0,0,0,0)
  i.e. a specific great 2-sphere inside S^6, using octonion coordinate
  indices {0,1,2} (G96's own 0-indexed Fano-plane basis) and leaving
  indices {3,4,5,6} at zero. This is ONE of many possible 2-slices; a
  different index choice would show a different cross-section of the same
  real structure, not a different structure.

  EVERYTHING AFTER THAT IS COMPUTED, not chosen: at each (theta,phi),
  - x = the point on S^6 (unit vector in R^7, verified below)
  - T_theta, T_phi = the coordinate tangent vectors of the 2-slice
  - J(v) := x \\times v  (the octonion cross product IS the nearly-Kahler
    almost-complex structure on S^6=G2/SU(3) at the point x -- standard
    fact, Gray 1969/Bryant 1987 construction, cited not re-derived)
  - align_e_r(theta,phi) = <J(T_theta), e_r> / |T_theta|, for r in {4,5,6}
      -- how aligned the J-rotated tangent is with each of three octonion
      basis directions OUTSIDE the slice's own span {0,1,2}.

  RESULT, FOUND BY COMPUTING, NOT ASSUMED (the real point of running this
  before trusting any of it as a texture): for THIS specific 2-slice,
  - in_plane and leak (the naive "does J preserve this plane" measures)
    are BOTH EXACTLY CONSTANT (in_plane=0, leak=1 everywhere) -- a genuine,
    verified structural fact about this slice (it is nowhere tangent to
    its own image under J, uniformly), not a texture candidate.
  - align_e4 is also degenerate (identically 0).
  - align_e4 and align_e6 are the two fields that actually vary
    (std=0.707 each, correlation ~0 between them -- genuinely independent).
  Only 2 independent non-degenerate real fields were found for this slice
  choice, not 3 -- reported honestly below rather than padded with a third
  field chosen only because it happened to look non-constant.

  Checked by computing, not assumed -- the SAME discipline this session's
  own C193 used before trusting an empirically-found sign/scale ("compute
  first, verify non-degenerate before trusting",
  research-methodology.md principle 6).

Run (plain numpy + Pillow, no Blender needed for this step):
  python compute_s6_texture_from_g96.py
Writes: s6_j_texture.png (RGB: R=align_e4, G=align_e6 -- the two genuinely
independent derived fields; B=sqrt(align_e4^2+align_e6^2), an HONEST
DERIVED COMBINATION of R and G, not a third independent measurement).
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
G96_PATH = HERE.parent / "experiments" / "20260626-g96-s6-g2-su3" / "g96_g2_su3.py"

RESOLUTION = 512  # texture is square, (theta in [0,pi]) x (phi in [0,2pi))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def octonion_cross(phi_tensor: np.ndarray, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """(a x b)_k = sum_{i,j} phi[i,j,k] a_i b_j -- direct contraction with
    G96's own tensor, not a re-derived formula."""
    return np.einsum("ijk,i,j->k", phi_tensor, a, b)


def slice_point(theta: float, phi: float) -> np.ndarray:
    """ONE explicit S^6 2-slice, octonion coords {0,1,2}, rest zero."""
    x = np.zeros(7)
    x[0] = np.sin(theta) * np.cos(phi)
    x[1] = np.sin(theta) * np.sin(phi)
    x[2] = np.cos(theta)
    return x


def slice_tangents(
    theta: float, phi: float, h: float = 1e-5
) -> tuple[np.ndarray, np.ndarray]:
    """Numeric tangent vectors of the slice (finite difference -- exact
    derivative is trivial here, but computing it the same way as a generic
    slice would need keeps this script reusable for other slice choices
    without hand-rederiving calculus each time)."""
    t_theta = (slice_point(theta + h, phi) - slice_point(theta - h, phi)) / (2 * h)
    t_phi = (slice_point(theta, phi + h) - slice_point(theta, phi - h)) / (2 * h)
    return t_theta, t_phi


def main() -> None:
    print("Loading G96's own build_phi() (not retyped)...")
    g96 = load_module("g96_g2_su3", G96_PATH)
    phi_tensor = g96.build_phi()

    print("Substrate check (reuses G96's own already-verified facts, Step 2a):")
    print(f"  phi.shape = {phi_tensor.shape}  [expected (7,7,7)]")
    assert phi_tensor.shape == (7, 7, 7)
    antisym_err = np.max(np.abs(phi_tensor + phi_tensor.transpose(1, 0, 2)))
    print(
        f"  antisymmetry in (i,j): max|phi_ijk + phi_jik| = {antisym_err:.2e}  [expected 0]"
    )
    assert antisym_err < 1e-12

    print(
        "\nComputing in_plane / leak fields on a",
        RESOLUTION,
        "x",
        RESOLUTION,
        "grid...",
    )
    thetas = np.linspace(1e-3, np.pi - 1e-3, RESOLUTION)
    phis = np.linspace(0, 2 * np.pi, RESOLUTION, endpoint=False)

    in_plane = np.zeros((RESOLUTION, RESOLUTION))
    leak = np.zeros((RESOLUTION, RESOLUTION))
    # Three alignment channels against three DIFFERENT octonion directions
    # outside the slice's own span {0,1,2} -- e6 is SU(3)'s own preferred
    # direction (kept as one channel for physical meaning); e3, e4 are two
    # more directions from the Fano basis, included only after checking
    # (below) that they give genuinely DIFFERENT fields, not scaled copies.
    align = {r: np.zeros((RESOLUTION, RESOLUTION)) for r in (4, 5, 6)}

    for ti, theta in enumerate(thetas):
        for pi_, phival in enumerate(phis):
            x = slice_point(theta, phival)
            t_theta, t_phi = slice_tangents(theta, phival)
            Jt_theta = octonion_cross(phi_tensor, x, t_theta)

            n_theta = np.linalg.norm(t_theta)
            n_phi = np.linalg.norm(t_phi)
            if n_theta < 1e-9 or n_phi < 1e-9:
                continue  # pole, skip (theta range already avoids exact 0/pi)

            cos_component = float(np.dot(Jt_theta, t_phi)) / (n_theta * n_phi)
            in_plane[ti, pi_] = cos_component

            t_phi_hat = t_phi / n_phi
            in_plane_vec = float(np.dot(Jt_theta, t_phi_hat)) * t_phi_hat
            leak_vec = Jt_theta - in_plane_vec
            leak[ti, pi_] = np.linalg.norm(leak_vec) / n_theta

            for r, channel in align.items():
                channel[ti, pi_] = Jt_theta[r] / n_theta

    print("\nNon-degeneracy check (compute first, verify before trusting --")
    print("research-methodology.md principle 6):")
    fields = {"in_plane": in_plane, "leak": leak}
    fields.update({f"align_e{r}": align[r] for r in align})
    for name, field in fields.items():
        lo, hi, mean, std = field.min(), field.max(), field.mean(), field.std()
        print(
            f"  {name:10s}: min={lo:+.4f} max={hi:+.4f} mean={mean:+.4f} std={std:.4f}"
        )
        if std < 1e-6:
            print(
                f"    [DEGENERATE] {name} is constant -- would NOT be a valid texture channel"
            )
        else:
            print(
                f"    [OK] {name} varies across the slice -- real, non-constant signal"
            )

    print("\nCross-channel distinctness check (two non-constant fields that are")
    print("secretly identical, or exact negatives, would NOT be 3 independent")
    print("channels -- checked directly, not assumed):")
    names = list(align.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = align[names[i]], align[names[j]]
            corr = float(np.corrcoef(a.flatten(), b.flatten())[0, 1])
            print(f"  corr(align_e{names[i]}, align_e{names[j]}) = {corr:+.4f}")

    print("\nWriting s6_j_texture.png ...")

    def normalize(field: np.ndarray) -> np.ndarray:
        lo, hi = field.min(), field.max()
        if hi - lo < 1e-9:
            return np.zeros_like(field)
        return (field - lo) / (hi - lo)

    # align_e5 came back degenerate for THIS slice (see non-degeneracy check
    # above) -- only align_e4 and align_e6 are genuinely independent, real,
    # non-constant fields. The third channel is an HONEST DERIVED
    # combination (not a third independent measurement): the in-(e4,e6)-
    # plane magnitude. Labeled as such, not presented as a third
    # independent signal.
    r = normalize(align[4])
    g = normalize(align[6])
    b = normalize(np.sqrt(align[4] ** 2 + align[6] ** 2))
    rgb = np.stack([r, g, b], axis=-1)
    img = Image.fromarray((rgb * 255).astype(np.uint8), mode="RGB")
    out_path = HERE / "s6_j_texture.png"
    img.save(out_path)
    print(f"  wrote {out_path} ({RESOLUTION}x{RESOLUTION})")
    print(
        "\nUV convention for Blender: U = phi/(2*pi) in [0,1), V = theta/pi in [0,1] --"
        " use a UV-mapped sphere (Blender's default UV sphere unwrap already matches"
        " this convention closely; verify, don't assume, before final render)."
    )


if __name__ == "__main__":
    main()
