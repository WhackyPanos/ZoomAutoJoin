import requests
import os
from bs4 import BeautifulSoup
import subprocess
import string
headers= {

    'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'

}

Data={
    'j_username':'usrname',
    'j_password':'pass',
    '_eventId_proceed':''
}

Data2= {

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


with requests.Session() as s:
    url = 'https://tuc-gr.zoom.us/saml/login?from=desktop&zm-cid=S5p2ZM2jEycJ2410g0nh8%2FpSsjPMj5cYAGgiR8a5vNU%3D'
    r = s.get(url, headers=headers, allow_redirects=True)

    r = s.post(r.url, data=Data, headers=headers)

    r = s.post(r.url, data=Data2, headers=headers)

    soup = BeautifulSoup(r.content, 'html5lib')
    button = soup.find('input', attrs={'name':'SAMLResponse'})['value']
    print(button)
    print(r.content)
    r= s.post('https://tuc-gr.zoom.us/saml/SSO', data={'SAMLResponse':button}, headers=headers)
    print(r.content)
    soup = BeautifulSoup(r.content, 'html5lib')
    tokenLink = soup.find('a', attrs={'id':'sso-button'})['href']

    print (tokenLink)

subprocess.Popen(['/bin/xdg-open', tokenLink])
