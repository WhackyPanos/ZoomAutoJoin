import sys
import subprocess

def startMeeting(meetingId, hashPwd):
    subprocess.Popen(["/bin/xdg-open", "zoommtg://tuc-gr.zoom.us/join?confno=" + meetingId + "&pwd=" + hashPwd])

def findWindowId():
    start = "xwininfo: Window id: "
    try:
        output = subprocess.check_output("xwininfo -name \"Zoom Meeting\"", shell=True)
    except:
        return -1
    else:
        windowId = output[output.find(start)+len(start):output.find(start)+len(start)+9]
        return windowId

def meetingDone():
    try:
        output = subprocess.check_output("xwininfo -name \"Leave Meeting\"", shell=True)
    except:
        return False
    else:
        return True
