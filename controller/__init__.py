import os
import glob # for listing files in a directory

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")] 
# __all__ is a list of all the modules in the directory