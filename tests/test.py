import subprocess
import time
import gst
import gi
import sys

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk

meetingId = "538877853"
hashPwd = "Z0VpWDllWGM5MU85eHZxbkQwc3BKZz09"

subprocess.Popen(["ls", "-l"])
#szoom = subprocess.Popen(["/bin/xdg-open", "zoommtg://tuc-gr.zoom.us/join?confno=" + meetingId + "&pwd=" + hashPwd])
windowId = "0x5e00001"
#myPipeline = "ximagesrc xid=" + windowId + " ! video/x-raw,framerate=5/1 ! videoconvert ! queue ! x264enc pass=5 quantizer=26 speed-preset=6 ! mp4mux fragment-duration=500 ! filesink location=capture.mp4"



Gst.init(sys.argv)
#pipeline = Gst.parse_launch(myPipeline)
pipeline = Gst.parse_launch ("ximagesrc startx=0 use-damage=0 xid=" + windowId + " ! video/x-raw,framerate=30/1 ! videoscale method=0 ! video/x-raw,width=1920,height=1080  ! videoconvert ! x264enc ! avimux ! filesink location=output4.avi")
pipeline.set_state(Gst.State.PLAYING)
time.sleep(15)
pipeline.set_state(Gst.State.NULL)
