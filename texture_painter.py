'''Renders text from a CSV file to textures 
   and applies them to multiple objects. 
   Use these when starting blender:
   import os, sys importlib; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
   After running the above:
   importlib.reload(texture_painter)
   '''
import codecs


def get_text(csv_filename):
    text = codecs.open(r'C:\Users\dakil\Desktop\Repos\python_blender\\' + csv_filename)

def go():
     print("Texture Painter is working!")
     get_text('crawl.txt')