import os, glob

filelist = ""
filecount = 0

for dirname, dirnames, filenames in os.walk(os.path.join(".", "input")):
    for filename in filenames:
        if filename != "Thumbs.db" and filename != "README":
            filecount = filecount + 1
            filelist += '"' + os.path.join(dirname, filename) + '" '

print("Will convert {filecount} files.".format_map(locals()))

threshold = input("Choose a classification threshold for symbol coder (default: 0.85): ")
if threshold == "":
  threshold = "0.85"

bwThreshold = input("Choose a 1 bpp threshold (default: 188): ")
if bwThreshold == "":
  bwThreshold = "188"

upsample = input("Choose upsampling from 0, 2 or 4 (default: 0): ")
if upsample == "0" or upsample == "":
  upsample = ""
elif upsample == "2":
  upsample = "-2"
elif upsample == "4":
  upsample = "-4"
else:
  print("Wrong upsampling selected. Enter 0, 2 or 4.")
  exit(1)

jbig2 = os.path.join(".", "jbig2")
cmd = "{jbig2} -t {threshold} -T {bwThreshold} {upsample} -s -p {filelist}".format_map(locals())
print("Converting to JBIG2 with: {cmd}".format_map(locals()))
os.system(cmd)

print("Converting to PDF....")
from pdf import main
main("output.sym", glob.glob("output.[0-9]*"))
