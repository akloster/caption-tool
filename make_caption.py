import os
import sys
import argparse

try:
    import bpy
except ImportError:
    print("Module 'bpy' could not be imported. This probably means you are not using Blender to run this script.")
    sys.exit(1)

prog_name = "Captions Tool "

if '--' not in sys.argv:
    print(prog_name + "No '--' found in command line arguments. '--' is needed to pass arguments to this script.")
    sys.exit(1)

# Parse arguments
arguments = sys.argv[sys.argv.index("--")+1:]
parser = argparse.ArgumentParser(description="Create captions")
parser.add_argument('--template')
parser.add_argument('--text')
parser.add_argument('--output')

args = parser.parse_args(arguments)
text = args.text
output = args.output
template = args.template

# Open template .blend
path = os.path.dirname(__file__)
template_path="/"+os.path.join(path,"blends",template+".blend")
if not os.path.exists(template_path):
    print(prog_name + "could not find this template file: '%s'" % template_path)
    sys.exit(1)
bpy.ops.wm.open_mainfile(filepath=template_path)


# Change text
bpy.data.objects["Text"].data.body = text


# Render output image
bpy.context.scene.render.filepath = output
bpy.context.scene.render.resolution_x = 1900
bpy.context.scene.render.resolution_y = 1080
bpy.ops.render.render(write_still=True)
