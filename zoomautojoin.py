import os
import subprocess
import sys

meetingid = "538877853"
hashpwd = "Z0VpWDllWGM5MU85eHZxbkQwc3BKZz09"

start = "xwininfo: Window id: "

os.system("/bin/xdg-open " + "\"zoommtg://tuc-gr.zoom.us/join?confno=" + meetingid + "&pwd=" + hashpwd + "\"")

try:
    result = subprocess.check_output("xwininfo -name \"Zoom Meeting\"", shell=True)
except:
    print("Window not found!")
    sys.exit(100)
print(result[result.find(start)+len(start):result.find(start)+len(start)+9])
