import sys,os,pysap
import ctypes as c
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

base_dir=cur_file_dir()
print base_dir
try:
    librfc=c.cdll.LoadLibrary
    print librfc
except Exception:
    print '%s' % Exception