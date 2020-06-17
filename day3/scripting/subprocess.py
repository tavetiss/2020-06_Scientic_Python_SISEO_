# A SUBPROCESS
import sys

print("# SUBPROCESS RUNING")
args = sys.argv
v = int(args[1])
print("v=", v)
out = " ".join([ str(i) for i  in range(v)])
print("PRINTING FILE")
f = open("report.dat", "w").write(out)
print("PRINTING FILE DONE")
