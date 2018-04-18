'''Renders text from a text file to textures 
   and applies them to multiple objects. 
   Use these when starting blender:
   import os, sys, importlib; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
   After running the above:
   importlib.reload(texture_painter)
   '''
from time import time
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


def go():
    start = time()
    print("Texture Painter is working!")
    get_text(r'C:\Users\dakil\Desktop\Repos\python_blender\crawl.txt')
    print("Finished!")
    end = time()
    time_elapsed = end - start
    print("The program took: " + str(round(time_elapsed,4)))
     
