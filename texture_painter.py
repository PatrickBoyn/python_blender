'''Renders text from a text file to textures 
   and applies them to multiple objects. 
   Use these when starting blender:
   import os, sys, importlib; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
   After running the above:
   texture_painter.go()
   importlib.reload(texture_painter)
   '''
from time import time
from PIL import Image, ImageFont, ImageDraw

# Please note that this only works inside blender. Running this code outside produces None objects.
def get_text(text_file):

    with open(text_file) as fp:
        line = fp.readline()
        count = 1

        while line:
            print(line)
            line = fp.readline()
            count +-1

        return fp


def render_to_text(text):
    image = Image.new('RGB', (128,128))
    draw =  ImageDraw.Draw(image)
    fnt =   ImageFont.truetype('arial.ttf', 50)
    draw.text((0,0), text, font=fnt, fill=(255,0,0))
    image.save(r"C:\Users\dakil\Desktop\Repos\python_blender\test.png")


def go():
    start = time()
    print("Texture Painter is working!")
    get_text(r'C:\Users\dakil\Desktop\Repos\python_blender\crawl.txt')
    render_to_text("Haha")
    print("Finished!")
    end = time()
    time_elapsed = end - start
    print("The program took: " + str(round(time_elapsed,4)))
     