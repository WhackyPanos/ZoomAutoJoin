import sys
import subprocess
import string
import requests
from bs4 import BeautifulSoup
import psutil
import record
import time

def startMeeting(meetingId, hashPwd, fileName, zmUsername, zmPassword):
    killZoom()
    time.sleep(2)
    if login(zmUsername, zmPassword) == False:
        return False
    time.sleep(5)
    subprocess.Popen(["/bin/xdg-open", "zoommtg://tuc-gr.zoom.us/join?confno=" + meetingId + "&pwd=" + hashPwd])
    time.sleep(8)
    if not fileName == -1:
        windowId = findWindowId()
        if windowId == -1:
            return False
        myPipeline = record.startRecording(windowId, fileName)
        return myPipeline
    return True

def findWindowId():
    start = "xwininfo: Window id: "
    try:
        output = subprocess.check_output("xwininfo -name \"Zoom Meeting\"", shell=True)
        output = str(output)
    except:
        return -1
    else:
        windowId = output[output.find(start)+len(start):output.find(start)+len(start)+9]
        return windowId

def meetingDone():
    try:
        output = subprocess.check_output("xwininfo -name \"Zoom Meeting\"", shell=True)
    except:
        return True
    else:
        return False

def stopMeeting(myPipeline):
    record.stopRecording(myPipeline)
    time.sleep(5)
    killZoom()

def killZoom():
    ok = False
    for proc in psutil.process_iter():
        if proc.name()=="zoom":
            #print("Killing zoom process")
            proc.kill()
            ok = True
    return ok

def login(username, password):

    headers = {
        'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }

    credentials = {
        'j_username':username,
        'j_password':password,
        '_eventId_proceed':''
    }

    consent = {
        '_shib_idp_consentIds': 'department',
        '_shib_idp_consentIds': 'displayName',
        '_shib_idp_consentIds': 'eduPersonAffiliation',
        '_shib_idp_consentIds': 'employeeid',
        '_shib_idp_consentIds': 'givenName',
        '_shib_idp_consentIds': 'mail',
        '_shib_idp_consentIds': 'surname',
        '_shib_idp_consentOptions': '_shib_idp_rememberConsent',
        '_eventId_proceed': 'Accept'
    }

    try:
        with requests.Session() as s:
            url = 'https://tuc-gr.zoom.us/saml/login?from=desktop&zm-cid=S5p2ZM2jEycJ2410g0nh8%2FpSsjPMj5cYAGgiR8a5vNU%3D'

            # Load Zoom login page
            r = s.get(url, headers=headers, allow_redirects=True)

            # Post credentials to TUC page
            r = s.post(r.url, data=credentials, headers=headers)

            # Post consent to TUC
            r = s.post(r.url, data=consent, headers=headers)

            # Find SAMLResponse
            soup = BeautifulSoup(r.content, 'html5lib')
            button = soup.find('input', attrs={'name':'SAMLResponse'})['value']

            # Post SAMLResponse back to Zoom
            r = s.post('https://tuc-gr.zoom.us/saml/SSO', data={'SAMLResponse':button}, headers=headers)

            # Find token
            soup = BeautifulSoup(r.content, 'html5lib')
            tokenLink = soup.find('a', attrs={'id':'sso-button'})['href']
    except TypeError:
        print("Wrong credentials or no internet connection available")
        return False
    except Exception as e:
        print("Unknown error occurred: " + str(e))
        return False
    else:
        # Launch Zoom
        subprocess.Popen(['/bin/xdg-open', tokenLink])
        return True
