import gi
import sys
gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gst, GObject, Gtk

def startRecording(windowId, fileName):
    Gst.init(sys.argv)
    #pipeline = Gst.parse_launch(myPipeline)
    pipeline = Gst.parse_launch ("ximagesrc startx=0 use-damage=0 xid=" + windowId + " ! video/x-raw,framerate=30/1 ! videoscale method=0 ! video/x-raw,width=1920,height=1080  ! videoconvert ! x264enc ! avimux ! filesink location=" + fileName + ".avi")
    pipeline.set_state(Gst.State.PLAYING)
    return pipeline

def stopRecording(pipeline):
    pipeline.set_state(Gst.State.NULL)
