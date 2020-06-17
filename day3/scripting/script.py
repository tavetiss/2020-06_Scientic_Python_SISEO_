# MASTER SCRIPT
import sys
import os


args = sys.argv
v = int(args[1])
print("v=", v)
print("# LAUNCHING SUBSCRIPT")
os.system("python subprocess.py {0}".format(v))
print("# SUBPROCESS FINISHED")
