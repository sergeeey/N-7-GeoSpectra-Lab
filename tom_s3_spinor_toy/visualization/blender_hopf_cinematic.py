"""Cinematic single-subject render: the Hopf fibration ALONE, pushed for
visual impact instead of scientific completeness.

Why this file exists, separate from blender_s3s6_hopf_scene.py: the user's
own verdict on the first full scene was "looks like an Obsidian graph, not
cinematic" -- correct. The first scene optimized for showing all three real
layers at once (Hopf fibration + S^6 spheres + generation trails) and ended
up visually cluttered and flat (plain emission tubes, no atmosphere, no
depth cue, camera too close). This file drops two of the three layers and
spends the whole visual budget on making ONE real, exact mathematical
object (the Hopf fibration, [EXACT] -- same status as before, not weakened)
actually look like the "ATSMATRIX"-grade reference the user is after.

Techniques added, found by actually researching current practice (not
assumed from memory), each cited:
  - Fog Glow in the Cycles compositor (Blender docs, Glare Node) -- cheap
    bloom, the single biggest "flat CG -> glowing" lever.
  - Volume scatter on a world shader for atmospheric depth
    (Creative Shrimp / BlenderNation volumetric lighting tutorials, 2025).
  - Camera depth of field (one sharp focal ring, rest soft) -- standard
    cinematography cue absent from the first render entirely.
  - Fewer, THICKER, more saturated tubes -- most "awesome" Hopf-fibration
    renders found (samuelj.li/hopf-fibration, For-The-Wolf/HopfFibration
    on GitHub) use 6-12 fibers, not 28 -- density was fighting itself in
    the first render, not adding information.

Run:
  blender --background --python blender_hopf_cinematic.py -- --render
"""

import math
import sys

import bpy
import mathutils

CONFIG = {
    "resolution": (1920, 1080),
    "samples": 256,
    "n_fibers": 8,
    "tube_radius": 0.028,  # ~2.3x the old scene's radius -- bold, not wiry
    "background_color": (0.004, 0.004, 0.01, 1.0),
}

DO_RENDER = "--render" in sys.argv


def clear_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def hopf_fiber_points(theta, phi, n=160):
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


def hsv_color(hue):
    c = mathutils.Color()
    c.hsv = (hue % 1.0, 0.75, 1.0)
    return (c.r, c.g, c.b)


def make_glow_material(name, color, strength):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs["Color"].default_value = (*color, 1.0)
    emission.inputs["Strength"].default_value = strength
    output = nodes.new("ShaderNodeOutputMaterial")
    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return mat


def build_fiber(theta, phi, index, n_total):
    pts = hopf_fiber_points(theta, phi)
    curve_data = bpy.data.curves.new(f"hopf_{index}", type="CURVE")
    curve_data.dimensions = "3D"
    curve_data.bevel_depth = CONFIG["tube_radius"]
    curve_data.bevel_resolution = 6
    spline = curve_data.splines.new("POLY")
    spline.points.add(len(pts) - 1)
    for i, p in enumerate(pts):
        spline.points[i].co = (p.x, p.y, p.z, 1.0)
    spline.use_cyclic_u = True
    obj = bpy.data.objects.new(f"HopfFiber_{index}", curve_data)
    bpy.context.collection.objects.link(obj)
    hue = index / n_total
    color = hsv_color(hue)
    strength = 6.0  # lowered from 14 -- v2 washed out to near-white under
    mat = make_glow_material(f"hopf_mat_{index}", color, strength)
    obj.data.materials.append(mat)
    return obj


def build_fibers():
    n = CONFIG["n_fibers"]
    golden_angle = math.pi * (3 - math.sqrt(5))
    for i in range(n):
        z = 1 - 2 * (i + 0.5) / n
        theta = math.acos(max(-1.0, min(1.0, z)))
        phi = (i * golden_angle) % (2 * math.pi)
        build_fiber(theta, phi, i, n)


def setup_world_with_volume():
    world = bpy.context.scene.world
    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links
    nodes.clear()
    bg = nodes.new("ShaderNodeBackground")
    bg.inputs["Color"].default_value = CONFIG["background_color"]
    bg.inputs["Strength"].default_value = 1.0
    # [Creative Shrimp / BlenderNation 2025 volumetric-lighting technique]
    # a faint volume scatter on the world itself gives every glowing tube
    # a soft atmospheric halo -- absent entirely from the first render.
    vol = nodes.new("ShaderNodeVolumeScatter")
    vol.inputs["Density"].default_value = 0.012
    vol.inputs["Color"].default_value = (0.05, 0.05, 0.09, 1.0)
    output = nodes.new("ShaderNodeOutputWorld")
    links.new(bg.outputs["Background"], output.inputs["Surface"])
    links.new(vol.outputs["Volume"], output.inputs["Volume"])


def setup_camera_with_dof():
    bpy.ops.object.camera_add(location=(3.6, -3.6, 2.4))
    cam = bpy.context.active_object
    cam.rotation_euler = (math.radians(63), 0, math.radians(45))
    bpy.context.scene.camera = cam
    cam.data.lens = 50
    cam.data.dof.use_dof = True
    cam.data.dof.aperture_fstop = 1.4
    empty = bpy.data.objects.new("FocusTarget", None)
    empty.location = (0, 0, 0)
    bpy.context.collection.objects.link(empty)
    cam.data.dof.focus_object = empty

    key = bpy.data.objects.new("KeyLight", bpy.data.lights.new("KeyLight", type="AREA"))
    key.location = (4, -4, 5)
    key.data.energy = 300
    key.data.size = 5
    bpy.context.collection.objects.link(key)

    rim = bpy.data.objects.new("RimLight", bpy.data.lights.new("RimLight", type="AREA"))
    rim.location = (-4, 3, -2)
    rim.data.energy = 150
    rim.data.color = (0.4, 0.6, 1.0)
    rim.data.size = 6
    bpy.context.collection.objects.link(rim)


def setup_compositor_glare():
    """[API VERIFIED LIVE, not assumed] Blender 5.2 moved the compositor
    tree off `Scene.node_tree` (removed) onto `Scene.compositing_node_group`
    (a CompositorNodeTree node GROUP you create and assign yourself), and
    the Glare node's Type/Quality/Threshold/Size are now INPUT SOCKETS
    (MENU/VALUE), not node properties -- `glare.glare_type` etc. no longer
    exist. Confirmed by probing a live Blender 5.2 session before writing
    this (probe_glare_api*.py, not committed -- throwaway). Enum values are
    title-case with spaces ("Fog Glow", "High"), not the old
    SCREAMING_SNAKE_CASE ("FOG_GLOW") -- also confirmed live, the first
    guess (FOG_GLOW) raised a real enum-not-found error."""
    scene = bpy.context.scene
    scene.use_nodes = True
    ng = bpy.data.node_groups.new("Compositing", "CompositorNodeTree")
    scene.compositing_node_group = ng
    render_layers = ng.nodes.new("CompositorNodeRLayers")
    glare = ng.nodes.new("CompositorNodeGlare")
    glare.inputs["Type"].default_value = "Fog Glow"
    glare.inputs["Quality"].default_value = "High"
    glare.inputs["Threshold"].default_value = 1.1  # raised from 0.6 (v2 blew out)
    glare.inputs["Size"].default_value = 6  # lowered from 8 (v2 bloom too wide)
    # [API VERIFIED LIVE] CompositorNodeComposite no longer exists in 5.2 --
    # the compositor tree is a real node GROUP now (like geometry nodes),
    # needing an explicit interface output socket + NodeGroupOutput node,
    # not a dedicated Composite node. Confirmed live before writing this.
    ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
    group_output = ng.nodes.new("NodeGroupOutput")
    ng.links.new(render_layers.outputs["Image"], glare.inputs["Image"])
    ng.links.new(glare.outputs["Image"], group_output.inputs["Image"])


def setup_render():
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = CONFIG["samples"]
    scene.cycles.use_denoising = True
    scene.render.resolution_x, scene.render.resolution_y = CONFIG["resolution"]
    try:
        scene.cycles.device = "GPU"
    except Exception:  # noqa: BLE001, S110 -- GPU optional; CPU fallback is intended
        pass
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = "//render/hopf_cinematic.png"


def main():
    clear_scene()
    build_fibers()
    setup_world_with_volume()
    setup_camera_with_dof()
    setup_compositor_glare()
    setup_render()
    print("Cinematic Hopf scene built. Objects:", len(bpy.context.scene.objects))
    if DO_RENDER:
        bpy.ops.render.render(write_still=True)
        print("Render written to", bpy.context.scene.render.filepath)


if __name__ == "__main__":
    main()
