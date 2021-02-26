import time
import sys
import record
import zoom

# Meeting setup for testing
# TODO read from JSON
#meetingId = "538877853"
meetingId = "89340789482"

#hashPwd = "Z0VpWDllWGM5MU85eHZxbkQwc3BKZz09"
hashPwd = "YlN5QjhZcnp1U25UY3BEQnlQRzl3UT09"

# Start zoom meeting
zoom.startMeeting(meetingId, hashPwd)

time.sleep(15)

myPipeline = record.startRecording(zoom.findWindowId(), "output1")

while not zoom.meetingDone():
    time.sleep(15)

print("Meeting done!")
record.stopRecording(myPipeline)
