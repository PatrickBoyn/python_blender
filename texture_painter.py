'''Renders text from a text file to textures 
   and applies them to multiple objects. 
   Use these when starting blender:
   import os, sys, importlib; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
   After running the above:
   importlib.reload(texture_painter)
   '''

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
     print("Texture Painter is working!")
     get_text(r'C:\Users\dakil\Desktop\Repos\python_blender\crawl.txt')
     print("Finished!")
