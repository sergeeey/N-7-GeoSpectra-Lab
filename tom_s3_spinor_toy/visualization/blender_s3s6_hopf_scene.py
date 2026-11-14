"""Cinematic Blender scene for Tom Lawrence's S^3 x S^6 compactification.

HONESTY LABEL (read before running, matches this project's own evidence-marker
discipline -- a visualization is not a claim.md, but "what is exact math vs
artistic license" still needs to be stated, not left implicit):

  [EXACT]    S^3 Hopf fibration -- the torus/circle curves below are a real,
             standard stereographic-projection rendering of the Hopf map
             S^3 -> S^2 (Clifford-parallel circles, Villarceau-circle family).
             Not a metaphor: this is genuinely what the Hopf fibration looks
             like when projected to R^3.
  [DERIVED] (upgraded 2026-10-02, was [SCHEMATIC]) S^6's G2/SU(3)
             near-Kahler structure -- the glowing sphere surface now maps
             `s6_j_texture.png`, produced by
             `compute_s6_texture_from_g96.py` by contracting G96's OWN
             verified octonion structure tensor (`build_phi()`, reused via
             import, not retyped) with the real nearly-Kahler almost-
             complex structure J(v) = x \\times v at points of an explicit
             S^6 2-slice. ONE artistic choice remains, named precisely in
             that script's own docstring: WHICH 2-dimensional slice of the
             genuinely 6-dimensional S^6 is rendered (one of many possible
             choices -- a different slice shows a different real
             cross-section, not a different structure). Everything
             downstream of that one choice is computed, not invented, and
             was checked for non-degeneracy before being trusted (2 of the
             3 originally-tried alignment channels turned out IDENTICALLY
             CONSTANT for this slice -- a real, verified structural fact,
             reported honestly rather than hidden; only 2 independent
             non-constant fields exist for this particular embedding, so
             the texture's 3rd (blue) channel is a declared DERIVED
             combination of the other two, not a third independent
             measurement). Falls back to the old procedural pattern if
             `s6_j_texture.png` is missing -- run
             `compute_s6_texture_from_g96.py` first (plain numpy+Pillow,
             no Blender needed for that step).
  [SCHEMATIC] The 3-fold braided light trails representing N_gen=3 -- the
             COUNT (3) and the SYMMETRY (exact 120-degree rotational copies)
             are real, derived facts about this project's triality result.
             The specific curve SHAPE each trail follows is artistic, not
             computed from the actual triality-channel data.

Nothing here is a research claim -- it is a presentation artifact. No FL
ladder, no claim.md: Structure-Bias Guard applies (this is an output
contract for a RENDER, not a falsifiable physics statement).

REQUIREMENTS: Blender 4.x (free, blender.org). This project's own machine
has no local Blender install (checked 2026-10-02) -- run this on whatever
machine has Blender, or install it first.

USAGE:
  GUI:       open Blender -> Scripting tab -> open this file -> Run Script
  headless:  blender --background --python blender_s3s6_hopf_scene.py \
                 -- --frames 1          (still)
             blender --background --python blender_s3s6_hopf_scene.py \
                 -- --frames 240 --render   (8s turntable @30fps, then render)

Tunables are in the CONFIG block below -- resolution, colors, Hopf fiber
density, whether to render a turntable animation or a single hero frame.
"""

import math
import sys
from pathlib import Path

import bpy
import mathutils

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
CONFIG = {
    "resolution": (2560, 1440),
    "samples": 256,  # Cycles samples; raise for a final render (512-1024)
    "hopf_fiber_count": 28,  # how many Hopf circles to draw (density)
    "hopf_tube_radius": 0.012,
    "s6_orbit_count": 10,  # small "S^6 fiber" spheres riding the Hopf torus
    "s6_sphere_radius": 0.09,
    "generation_trail_count": 3,  # N_gen = 3, do not change without reason
    "background_color": (0.01, 0.01, 0.018, 1.0),
    "turntable": False,  # True -> animate camera orbit, render --frames N
    "frames": 1,
}

# simple CLI override: `-- --frames 240 --render`
argv = sys.argv
if "--" in argv:
    extra = argv[argv.index("--") + 1 :]
    if "--frames" in extra:
        CONFIG["frames"] = int(extra[extra.index("--frames") + 1])
        CONFIG["turntable"] = CONFIG["frames"] > 1
    DO_RENDER = "--render" in extra
else:
    DO_RENDER = False


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for block_collection in (bpy.data.meshes, bpy.data.curves, bpy.data.materials):
        for block in list(block_collection):
            if block.users == 0:
                block_collection.remove(block)


def make_emission_material(name, color, strength=4.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Color"].default_value = (*color, 1.0)
    emission.inputs["Strength"].default_value = strength
    output = nodes.new("ShaderNodeOutputMaterial")
    mat.node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return mat


S6_TEXTURE_PATH = Path(__file__).resolve().parent / "s6_j_texture.png"
_S6_TEXTURE_WARNED = False


def _load_s6_texture_image():
    """Load s6_j_texture.png once, reused across all S^6 sphere materials.
    Returns None (and prints a one-time warning) if the file is missing --
    the caller falls back to flat color, this is graceful degradation per
    context-loading.md, not a hard failure."""
    global _S6_TEXTURE_WARNED
    if not S6_TEXTURE_PATH.exists():
        if not _S6_TEXTURE_WARNED:
            print(
                f"[WARN] {S6_TEXTURE_PATH.name} not found -- run"
                " compute_s6_texture_from_g96.py first. Falling back to flat"
                " color for S^6 spheres (SCHEMATIC, not DERIVED)."
            )
            _S6_TEXTURE_WARNED = True
        return None
    name = S6_TEXTURE_PATH.name
    if name in bpy.data.images:
        return bpy.data.images[name]
    return bpy.data.images.load(str(S6_TEXTURE_PATH))


def make_glass_glow_material(name, color, use_derived_texture=True):
    """For the S^6 fiber spheres: translucent core + faint glow, not flat emission.

    [DERIVED, upgraded from SCHEMATIC] when use_derived_texture and
    s6_j_texture.png exists (produced by compute_s6_texture_from_g96.py,
    which contracts G96's OWN verified octonion structure tensor against a
    specific S^6 2-slice -- see that script's docstring for exactly what is
    plotted and the one named artistic choice: WHICH 2-slice of the real
    6-dimensional S^6). Falls back to flat `color` if the texture is
    missing -- graceful degradation, not a hard failure, per
    context-loading.md's own convention."""
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Transmission Weight"].default_value = 0.85
    bsdf.inputs["Roughness"].default_value = 0.05
    bsdf.inputs["IOR"].default_value = 1.33
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Color"].default_value = (*color, 1.0)
    emission.inputs["Strength"].default_value = 1.5

    image = _load_s6_texture_image() if use_derived_texture else None
    if image is not None:
        uv_map = nodes.new("ShaderNodeUVMap")
        tex = nodes.new("ShaderNodeTexImage")
        tex.image = image
        tex.interpolation = "Cubic"
        links.new(uv_map.outputs["UV"], tex.inputs["Vector"])
        # Modulate both the base color and the emission color by the
        # DERIVED texture (tint, not replace -- keeps each S^6 sphere's own
        # per-rider hue from the Hopf-fiber color-coding, Section A above,
        # while the real G2-derived pattern shows as surface variation).
        mix_base = nodes.new("ShaderNodeMix")
        mix_base.data_type = "RGBA"
        mix_base.blend_type = "MULTIPLY"
        mix_base.inputs["Factor"].default_value = 0.8
        links.new(tex.outputs["Color"], mix_base.inputs["B"])
        mix_base.inputs["A"].default_value = (*color, 1.0)
        links.new(mix_base.outputs["Result"], bsdf.inputs["Base Color"])

        mix_em = nodes.new("ShaderNodeMix")
        mix_em.data_type = "RGBA"
        mix_em.blend_type = "MULTIPLY"
        mix_em.inputs["Factor"].default_value = 0.8
        links.new(tex.outputs["Color"], mix_em.inputs["B"])
        mix_em.inputs["A"].default_value = (*color, 1.0)
        links.new(mix_em.outputs["Result"], emission.inputs["Color"])

    mix = nodes.new("ShaderNodeMixShader")
    mix.inputs["Fac"].default_value = 0.35
    output = nodes.new("ShaderNodeOutputMaterial")
    links.new(bsdf.outputs["BSDF"], mix.inputs[1])
    links.new(emission.outputs["Emission"], mix.inputs[2])
    links.new(mix.outputs["Shader"], output.inputs["Surface"])
    return mat


# ---------------------------------------------------------------------------
# [EXACT] Hopf fibration, stereographically projected S^3 -> R^3
#
# A point of S^2 at (theta, phi) lifts to a Hopf circle in S^3. Using the
# standard quaternionic parametrization, the Hopf fiber over (theta, phi) is
#   q(t) = (cos(theta/2) cos(t), cos(theta/2) sin(t),
#            sin(theta/2) cos(t+phi), sin(theta/2) sin(t+phi))   t in [0,2pi)
# then stereographically projected from the point (-1,0,0,0) into R^3:
#   P(x0,x1,x2,x3) = (x1,x2,x3) / (1+x0)
# This reproduces the well-known linked-torus / Villarceau-circle picture.
# ---------------------------------------------------------------------------


def hopf_fiber_points(theta, phi, n=128):
    pts = []
    for i in range(n + 1):
        t = 2 * math.pi * i / n
        x0 = math.cos(theta / 2) * math.cos(t)
        x1 = math.cos(theta / 2) * math.sin(t)
        x2 = math.sin(theta / 2) * math.cos(t + phi)
        x3 = math.sin(theta / 2) * math.sin(t + phi)
        denom = 1 + x0
        if abs(denom) < 1e-4:
            denom = 1e-4 if denom >= 0 else -1e-4
        pts.append(mathutils.Vector((x1 / denom, x2 / denom, x3 / denom)))
    return pts


def build_hopf_curve(theta, phi, radius, color, strength, index):
    pts = hopf_fiber_points(theta, phi)
    curve_data = bpy.data.curves.new(f"hopf_curve_{index}", type="CURVE")
    curve_data.dimensions = "3D"
    curve_data.bevel_depth = radius
    curve_data.bevel_resolution = 4
    spline = curve_data.splines.new("POLY")
    spline.points.add(len(pts) - 1)
    for i, p in enumerate(pts):
        spline.points[i].co = (p.x, p.y, p.z, 1.0)
    spline.use_cyclic_u = True
    obj = bpy.data.objects.new(f"HopfFiber_{index}", curve_data)
    bpy.context.collection.objects.link(obj)
    mat = make_emission_material(f"hopf_mat_{index}", color, strength)
    obj.data.materials.append(mat)
    return obj, pts


def hsv_for_base_point(theta, phi):
    """Color-code each Hopf circle by its base point on S^2 -- standard
    convention in Hopf-fibration visualizations (e.g. Niles Johnson's)."""
    hue = (phi % (2 * math.pi)) / (2 * math.pi)
    sat = 0.55 + 0.45 * (theta / math.pi)
    val = 1.0
    c = mathutils.Color()
    c.hsv = (hue, sat, val)
    return (c.r, c.g, c.b)


def build_s3_hopf_bundle():
    """Draws CONFIG['hopf_fiber_count'] Hopf circles spread over S^2's
    (theta, phi), plus small glowing 'S^6 fiber' spheres riding a subset of
    them -- the S^3 x S^6 product structure, shown as fiber-over-fiber."""
    n_fibers = CONFIG["hopf_fiber_count"]
    all_fiber_pts = []
    golden_angle = math.pi * (3 - math.sqrt(5))  # Fibonacci sphere spacing
    for i in range(n_fibers):
        z = 1 - 2 * (i + 0.5) / n_fibers
        theta = math.acos(max(-1.0, min(1.0, z)))
        phi = (i * golden_angle) % (2 * math.pi)
        color = hsv_for_base_point(theta, phi)
        _obj, pts = build_hopf_curve(
            theta, phi, CONFIG["hopf_tube_radius"], color, strength=3.0, index=i
        )
        all_fiber_pts.append((pts, color))

    # [SCHEMATIC] S^6 "fiber spheres": ride a few Hopf circles, representing
    # that at every point of S^3 there sits a whole S^6 -- the product
    # manifold, not a literal 6-sphere rendering.
    s6_mat_cache = {}
    riders = all_fiber_pts[:: max(1, len(all_fiber_pts) // CONFIG["s6_orbit_count"])]
    for ridx, (pts, color) in enumerate(riders):
        step = max(1, len(pts) // 6)
        for j in range(0, len(pts), step):
            p = pts[j]
            key = ridx
            if key not in s6_mat_cache:
                s6_mat_cache[key] = make_glass_glow_material(
                    f"s6_mat_{ridx}", tuple(min(1.0, c * 1.3) for c in color)
                )
            bpy.ops.mesh.primitive_uv_sphere_add(
                radius=CONFIG["s6_sphere_radius"],
                location=p,
                segments=24,
                ring_count=12,
            )
            sphere = bpy.context.active_object
            sphere.name = f"S6_fiber_{ridx}_{j}"
            sphere.data.materials.append(s6_mat_cache[key])
            bpy.ops.object.shade_smooth()


# ---------------------------------------------------------------------------
# [SCHEMATIC, count/symmetry EXACT] three braided generation trails (N_gen=3)
# ---------------------------------------------------------------------------


def build_generation_trails():
    n = CONFIG["generation_trail_count"]
    colors = [(1.0, 0.25, 0.25), (0.3, 1.0, 0.4), (0.3, 0.55, 1.0)]
    for k in range(n):
        offset = 2 * math.pi * k / n  # exact 120-degree triality symmetry
        curve_data = bpy.data.curves.new(f"gen_trail_{k}", type="CURVE")
        curve_data.dimensions = "3D"
        curve_data.bevel_depth = 0.02
        curve_data.bevel_resolution = 4
        spline = curve_data.splines.new("NURBS")
        n_pts = 80
        spline.points.add(n_pts - 1)
        for i in range(n_pts):
            t = i / (n_pts - 1)
            radius = 2.3 + 0.6 * math.sin(6 * math.pi * t)
            ang = offset + 4 * math.pi * t
            x = radius * math.cos(ang)
            y = radius * math.sin(ang)
            z = 1.4 * math.sin(2 * math.pi * t) * math.cos(offset)
            spline.points[i].co = (x, y, z, 1.0)
        spline.use_endpoint_u = True
        obj = bpy.data.objects.new(f"GenerationTrail_{k}", curve_data)
        bpy.context.collection.objects.link(obj)
        mat = make_emission_material(f"gen_mat_{k}", colors[k % 3], strength=6.0)
        obj.data.materials.append(mat)


def setup_world():
    world = bpy.context.scene.world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = CONFIG["background_color"]
    bg.inputs["Strength"].default_value = 1.0


def setup_camera_and_light():
    bpy.ops.object.camera_add(location=(6.5, -6.5, 4.2))
    cam = bpy.context.active_object
    cam.rotation_euler = (math.radians(63), 0, math.radians(45))
    bpy.context.scene.camera = cam

    bpy.ops.object.light_add(type="AREA", location=(5, -5, 6))
    key = bpy.context.active_object
    key.data.energy = 400
    key.data.size = 4

    bpy.ops.object.light_add(type="AREA", location=(-5, 4, -3))
    fill = bpy.context.active_object
    fill.data.energy = 120
    fill.data.color = (0.5, 0.7, 1.0)
    fill.data.size = 5

    if CONFIG["turntable"]:
        empty = bpy.data.objects.new("CamTarget", None)
        bpy.context.collection.objects.link(empty)
        cam.constraints.new("TRACK_TO").target = empty
        parent = bpy.data.objects.new("CamOrbit", None)
        bpy.context.collection.objects.link(parent)
        cam.parent = parent
        parent.rotation_euler = (0, 0, 0)
        scene = bpy.context.scene
        scene.frame_start = 1
        scene.frame_end = CONFIG["frames"]
        parent.rotation_euler = (0, 0, 0)
        parent.keyframe_insert(data_path="rotation_euler", index=2, frame=1)
        parent.rotation_euler = (0, 0, 2 * math.pi)
        parent.keyframe_insert(
            data_path="rotation_euler", index=2, frame=CONFIG["frames"]
        )
        for fcurve in parent.animation_data.action.fcurves:
            for kp in fcurve.keyframe_points:
                kp.interpolation = "LINEAR"


def setup_render():
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = CONFIG["samples"]
    scene.cycles.use_denoising = True
    scene.render.resolution_x, scene.render.resolution_y = CONFIG["resolution"]
    scene.render.film_transparent = False
    try:
        scene.cycles.device = "GPU"
    except Exception:  # noqa: BLE001, S110 -- GPU optional; CPU fallback is intended
        pass
    if CONFIG["turntable"]:
        scene.render.image_settings.file_format = "FFMPEG"
        scene.render.ffmpeg.format = "MPEG4"
        scene.render.filepath = "//render/s3s6_turntable.mp4"
    else:
        scene.render.image_settings.file_format = "PNG"
        scene.render.filepath = "//render/s3s6_hero_frame.png"


def main():
    clear_scene()
    setup_world()
    build_s3_hopf_bundle()
    build_generation_trails()
    setup_camera_and_light()
    setup_render()
    print("Scene built. Objects:", len(bpy.context.scene.objects))
    if DO_RENDER:
        if CONFIG["turntable"]:
            bpy.ops.render.render(animation=True)
        else:
            bpy.ops.render.render(write_still=True)
        print("Render written to", bpy.context.scene.render.filepath)


if __name__ == "__main__":
    main()
