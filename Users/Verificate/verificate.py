import os
import pathlib
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import requests

'''Variavles'''
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
GOOGLE_CLIENT_ID = "110285543009-ai5r02kufp2t7eoph99pkuv9kgu4dlph.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

'''google functions'''
#create url for login
def url_login():
    try:
        authorization_url, state = flow.authorization_url()
        return {'url':authorization_url,'state':state}
    except:
        return {'msj':'error'}

#verificate the credentials
def callback(url):
    try:
        flow.fetch_token(authorization_response=url)
        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)
        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID
        )
        return {'name':id_info.get('name'),'verif':id_info.get('email_verified'),'email':id_info.get('email')}
    except:
        return {'msj':'error'}