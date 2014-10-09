'''
flask-twython
 
Ejemplo simple y minimo para obtener los tokens de usuario OAUTH
 
'''
from flask import Flask, request, redirect
from twython import Twython

app = Flask(__name__)
#config
APP_KEY='APP_KEY'
APP_SECRET='APP_SECRET'
callback_url = 'http://YOUR-URLs/verify'
OAUTH_TOKEN =''
OAUTH_TOKEN_SECRET=''

@app.route("/")
def send_token():
	global OAUTH_TOKEN
	global OAUTH_TOKEN_SECRET
	twitter = Twython(APP_KEY, APP_SECRET)
	auth = twitter.get_authentication_tokens(callback_url)
	OAUTH_TOKEN = auth['oauth_token']
	OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
	redirect_url= auth['auth_url']

	return redirect(redirect_url)	

@app.route("/verify")
def get_verification():
	global OAUTH_TOKEN
	global OAUTH_TOKEN_SECRET
	twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	final_step = twitter.get_authorized_tokens(request.args['oauth_verifier'])
	OAUTH_TOKEN2 = final_step['oauth_token']
	OAUTH_TOKEN_SECRET2 = final_step['oauth_token_secret']
	return 'OK! OAUTH TOKEN:' + OAUTH_TOKEN2 +'\n OAUTH TOKEN SECRET: '+ OAUTH_TOKEN_SECRET2

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
