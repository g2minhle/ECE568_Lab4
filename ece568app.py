''' Provided '''
import sys, SocketServer 
from bottle import route, run, template, redirect, request
import ece568helper

@route('/hello')
def hello():
    print 'hello invoked'
    return "Hello World!"

''' Implement Here '''

login_scope = 'profile'
email_scope = 'https://www.googleapis.com/auth/plus.profile.emails.read'

@route('/login.html')
def login():
    return ece568helper.get_login_html(_addr, _port, _cid, login_scope, email_scope)

@route('/auth.html')
def auth():
    return ece568helper.get_auth_html(_cid)

import oauth2client
from oauth2client import client
import json
import apiclient
from apiclient.discovery import build
from apiclient import errors
from apiclient.http import MediaFileUpload
import httplib2

SCOPES = [
	"https://www.googleapis.com/auth/drive.file", "profile"
]

@route('/drive.html')
def drive():
	# Initialize client object to use Google api.
	# You need client_secrets.json downloaded and stored
	# in the current working directory
	 
	flow = ece568helper.get_client_object(_addr, _port, SCOPES)
	auth_uri = flow.step1_get_authorize_url()
	if 'error' in request.query:
		return template('drive', result=request.query.error) 
		
	if 'code' not in request.query:
		auth_uri = flow.step1_get_authorize_url()
		redirect(auth_uri)
	else:
		auth_code = request.query.code
		credentials = flow.step2_exchange(auth_code)
		ece568helper.output_helper("credentials", credentials)
		http_auth = credentials.authorize(httplib2.Http())
		plusService = build("plus", "v1", http=http_auth)
		driveService = build("drive", "v2", http=http_auth)
		people_document = plusService.people().get(userId = "me").execute()
		ece568helper.output_helper('profile', people_document)
		mediaBody = MediaFileUpload('profile.out', mimetype='text/plain', resumable=True)
		requestBody = {
			'title': 'profile.out',
			'description': 'myProfile',
			'mimeType': 'text/plain'
		}
		try:
			uploadedFile = driveService.files().insert(
				body = requestBody, 
				mediaBody = media_body
			).execute()
			return template('drive', result = 'Upload done with result: \n %s' % uploadedFile) 
		except errors.HttpError, error:
			return template('drive', result = 'An error occured: %s' % error) 

''' Provided '''

try:
    _addr = sys.argv[1]
    _port = sys.argv[2]
    _cid = sys.argv[3]
    run(host=_addr, port=_port, debug=True)
except IndexError:
    print 'Usage: python ece568app.py <IP address> <Port> <Client ID>'
except SocketServer.socket.error:
    print '[Fail] port ' + str(_port) + ' is already in use\n' 

