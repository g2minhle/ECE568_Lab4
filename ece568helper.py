from bottle import route, run, template, redirect, request
from oauth2client import client
import json

def get_login_html(addr, port, cid, scope1, scope2):
    return template('login', addr=addr, port=port, cid=cid, scope1=scope1, scope2=scope2)

def get_auth_html(cid):
    return template('auth', cid=cid)

# print the key value pair as json format to the file
def print_to_file(key, value, filename='', mode='a'):
    if filename is '':
        with open('ece568app.out', mode) as outfile:
            json.dump({key: value}, outfile, indent=4)
            outfile.write('\n')
    else:
        with open(filename, mode) as outfile:
            json.dump({key: value}, outfile, indent=4)
            outfile.write('\n')

def output_helper(key, obj):
    if key is 'credentials':
        print_to_file('credentials', obj.to_json())
    elif key is 'profile':
        print_to_file('profile', obj, 'profile.out')

def get_client_object(addr, port, scope):
    flow = client.flow_from_clientsecrets(
        'client_secrets.json',
        scope=scope,
        redirect_uri=('http://'+addr+":"+port+"/drive.html")
        )
    return flow


