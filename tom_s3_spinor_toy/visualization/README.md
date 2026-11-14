# S³×S⁶ cinematic scene — setup

**Status (updated 2026-10-03):** both scripts were run headless on **Blender
5.2.2 LTS** on this machine and rendered (`[VERIFIED]`: `blender_s3s6_hopf_scene.py`
built 132 objects and rendered a 2560×1440 frame in ~52 s; `blender_hopf_cinematic.py`
rendered 1920×1080 in ~80–100 s, CPU). The first draft of this README said "not run,
targets 4.x" — that is superseded. Blender 5.x broke parts of the 4.x API (the compositor
moved to `Scene.compositing_node_group` with a node-group interface, Glare parameters became
input sockets with title-case enum values); `blender_hopf_cinematic.py` is written for 5.x and
documents those changes inline. **Still `[UNKNOWN]`:** whether the S⁶ texture's UV orientation
matches `compute_s6_texture_from_g96.py`'s (θ,φ) convention pixel-for-pixel (not inspected on
the render), and GPU rendering (CPU fallback was used).

**Which script to use:** `blender_hopf_cinematic.py` is the polished one — the Hopf
fibration alone (exact math), glow/bloom, volumetric haze, depth of field. The earlier
`blender_s3s6_hopf_scene.py` (Hopf + S⁶ spheres + generation trails) renders correctly but was
judged visually flat/cluttered; kept for its S⁶-texture wiring.

## What this is, and isn't

Not a research artifact — no `claim.md`, no FL ladder, this is a
presentation render. What's mathematically exact vs. artistic license is
labeled inline in `blender_s3s6_hopf_scene.py`'s own docstring — read it
before presenting the output as "this is what the theory says," since part
of it (the S⁶ near-Kähler structure, the generation-trail curve shapes) is
schematic, not derived from the project's own computed data.

## Setup (one-time)

1. Install Blender (free; tested here on 5.2.2): https://www.blender.org/download/
2. GPU render is much faster — if you have an NVIDIA/AMD GPU, enable it in
   Blender: Edit → Preferences → System → Cycles Render Devices.

## S⁶ texture — now `[DERIVED]`, run this BEFORE Blender

`s6_j_texture.png` already exists in this folder (generated and committed) —
you don't have to run this yourself to get a derived texture. But if you
want to experiment with a different S⁶ slice (see caveats below), re-run:
```
python compute_s6_texture_from_g96.py
```
Pure numpy+Pillow, no Blender needed — ran and verified in-session (not
`[UNKNOWN]` like the Blender half). What it actually computes, verified by
running it, not assumed: contracts `experiments/20260626-g96-s6-g2-su3/
g96_g2_su3.py`'s own already-verified octonion structure tensor against an
explicit 2-dimensional slice of the real (6-dimensional) S⁶, producing the
nearly-Kähler almost-complex structure's action on that slice's tangent
frame. **Caveat found by computing, not assumed:** for the specific slice
chosen (octonion coordinates {0,1,2}), the "does J preserve this slice"
measure came back exactly constant (a real structural fact, not a bug —
this 2-plane is uniformly non-J-invariant), and only 2 of the 3 originally
tried "alignment" channels were non-degenerate — so the texture's blue
channel is an honest derived combination of the other two, not a third
independent measurement. The resulting pattern varies only along longitude
(φ), not latitude (θ) — also a real, verified fact about this slice, not a
rendering bug; it'll read as vertical stripes/bands on the sphere, not 2D
noise. A different slice (edit `slice_point()`'s index choice, e.g. {1,3,5}
instead of {0,1,2}) would very likely give richer 2D variation — untried
here, named as the natural next iteration if the striped look isn't what
you want.

## Run it

**GUI (easiest, see it live first):**
1. Open Blender → `Scripting` tab (top menu).
2. `Open` → select `blender_s3s6_hopf_scene.py`.
3. Click `Run Script` (▶). The scene builds in the viewport — switch to
   Rendered shading (top-right sphere icon) to see the actual Cycles look.
4. Adjust `CONFIG` at the top of the file (fiber density, colors, resolution)
   and re-run as needed, before committing to a full render.

**Polished single-subject render (recommended), headless:**
```
blender --background --python blender_hopf_cinematic.py -- --render
```
Writes `render/hopf_cinematic.png` (1920×1080). The tunables that mattered in practice are in
the script: emission `strength` (14 washed colors out to near-white, 6 keeps them distinct) and
the Glare `Threshold`/`Size` (1.1 / 6).

**Headless, single hero frame (older multi-layer scene):**
```
blender --background --python blender_s3s6_hopf_scene.py -- --frames 1 --render
```
Writes `render/s3s6_hero_frame.png` next to the `.blend` save location.

**Headless, 8-second turntable (240 frames @ 30fps):**
```
blender --background --python blender_s3s6_hopf_scene.py -- --frames 240 --render
```
Writes `render/s3s6_turntable.mp4`. This will take a while — 240 frames ×
`CONFIG["samples"]=256` Cycles samples each, no estimate given since render
time depends entirely on your GPU, not something I can predict from here.

## If it breaks

Most likely failure points, in order of probability:
1. **API drift** — `Transmission Weight` / `IOR` input names on
   `ShaderNodeBsdfPrincipled` have changed across Blender 3.x→4.x versions.
   If you're on an older Blender, open the Shading tab on one `S6_fiber_*`
   object and check the actual input names on its Principled BSDF node.
2. **`ShaderNodeMix` (RGBA mode) on the texture-tint nodes** — this is the
   Blender 4.x unified Mix node (`data_type="RGBA"`, sockets `A`/`B`/
   `Result`). On Blender 3.x the equivalent node is `ShaderNodeMixRGB` with
   different socket names (`Color1`/`Color2`/`Color`) — if you're on 3.x,
   `make_glass_glow_material`'s texture-tint block will need those names
   swapped in.
3. **UV mapping may not match `compute_s6_texture_from_g96.py`'s own
   (θ,φ) convention exactly** — `primitive_uv_sphere_add()` auto-generates
   a UV map close to spherical coordinates, used here via `ShaderNodeUVMap`
   with no explicit layer name (so it uses the object's active/default UV
   map) — not verified pixel-exact against the texture script's own
   `U=phi/2π, V=theta/π` convention. If the pattern looks seam-shifted or
   mirrored on the sphere, that's the first thing to check, not a sign the
   texture itself is wrong.
4. **GPU device not found** — the `try/except` around `cycles.device = "GPU"`
   silently falls back to CPU; render will just be slow, not broken.
5. **Empty/parent keyframing for the turntable** — if the camera doesn't
   orbit, check `CamOrbit`'s rotation F-curve in the Graph Editor.
6. **`s6_j_texture.png` not found** — `make_glass_glow_material` falls back
   to flat color automatically (prints one `[WARN]` line, doesn't crash);
   run `compute_s6_texture_from_g96.py` first if you see that warning.
