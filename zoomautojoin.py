import time
import subprocess
import sys
import record
import zoom

# Meeting setup for testing
# TODO read from JSON
meetingId = "538877853"
hashPwd = "Z0VpWDllWGM5MU85eHZxbkQwc3BKZz09"


# Start zoom
zoom.startMeeting(meetingId, hashPwd)

# Grab window id from X
