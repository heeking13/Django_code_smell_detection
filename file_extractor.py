#This is the python file extractor from the Django project
import os

#take the python files from the Danjo project
def walk_path(rootdir):
  for root, _, files in os.walk(rootdir):
    for name in files:
        if (os.path.splitext(name)[1][1:] == 'py'):
            yield os.path.join(root,name)