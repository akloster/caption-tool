Captions Tool
=============

This is a simple command line tool to create captions for Video Editing from .blend file templates.

The templates are blend files in the blends subdirectory. You can modify the only existing template or create your own one. The only important thing is that the Text object is called "Text" and the output format is png. The resolution is set to 1900x1080.

Under Linux you can run the bash script from the directory:

    > caption_tool --template="caption_1" --output="test.png" --text="Hello World"

Alternatively you can symlink it to an executable path. The script then tries to find the python script in the project path. If this doesn't work for you, then you may need to modify caption_tool.sh to include the correct path.

The script assumes that there is a 'blender' binary on the path.

`--template` specifies the template filename without extension and directory. The files are assumed to be in a subdirectory called "blends" of the directory the 'make_caption.py'  is in.

`--output` sets the output name for the rendered image

`--text` sets the text for the text object called "Text"

If you can figure out a good way to use this in Windows or Mac, pleases let me know or make a pull request!
