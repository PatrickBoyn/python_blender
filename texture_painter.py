'''Renders text from a CSV file to textures 
   and applies them to multiple objects. 
   Use these when starting blender:
   import os, sys, importlib; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
   After running the above:
   importlib.reload(texture_painter)
   '''
import codecs
import csv 

# Please note that this only works inside blender. Running this code outside produces None objects.
def get_text(csv_filename):
    with codecs.open(csv_filename, 'r', 'utf-8') as stream:
        iterable = csv.reader(csv_filename)
        header = iterable
        for i in header:
            print(i)

        return stream


def go():
     print("Texture Painter is working!")
     get_text(r'C:\Users\dakil\Desktop\Repos\python_blender\crawl.txt')
