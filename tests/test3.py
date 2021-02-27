import zoom
import time

username = "pskoulaxinos"
password = "taspao13gate13"
meetingId = "84659268274"
meetingPass = "ZERtM1FuRisyK2JUY0JoTjl6Qm5mdz09"

print(zoom.startMeeting(meetingId, meetingPass, -1, username, password))
