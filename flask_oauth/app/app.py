from requests_oauthlib import OAuth1Session
from flask import Flask, jsonify, request, redirect,render_template
import urllib.parse as parse
from dotenv import load_dotenv
import os

load_dotenv()

# App Info
api_key = os.environ["TW_CLI_KEY"]
api_secret = os.environ["TW_SCR_KEY"]
# Twitter Endpoint
twitter_base_url = 'https://api.twitter.com'
authorization_endpoint = twitter_base_url + '/oauth/authenticate'
request_token_endpoint = twitter_base_url + '/oauth/request_token'
token_endpoint = twitter_base_url + '/oauth/access_token'
credentials=twitter_base_url + '/1.1/account/verify_credentials.json'

app = Flask(__name__)
app.json.ensure_ascii=False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/login")
def login():
    # 1.リクエストトークンを取得する。
    # (Step 1: Obtaining a request token:https://developer.twitter.com/en/docs/authentication/guides/log-in-with-twitter)
    twitter = OAuth1Session(api_key, api_secret)
    #oauth_callback = request.args.get('oauth_callback')
    oauth_callback="http://0.0.0.0:5005/callback"
    res = twitter.post(request_token_endpoint, params={
        'oauth_callback': oauth_callback})
    request_token = dict(parse.parse_qsl(res.content.decode("utf-8")))
    oauth_token = request_token['oauth_token']
    oauth_token_secret=request_token['oauth_token_secret']
    # 2.リクエストトークンを指定してTwitterへ認可リクエスト(Authorization Request)を行う。
    # (Step 2: Redirecting the user:https://developer.twitter.com/en/docs/authentication/guides/log-in-with-twitter#tab2)
    return redirect(authorization_endpoint+'?{}'.format(parse.urlencode({
        'oauth_token': oauth_token
    })))


@app.route("/callback")
def callback():
    # 3.ユーザー認証/同意を行い、認可レスポンスを受け取る。
    oauth_verifier = request.args.get('oauth_verifier')
    oauth_token = request.args.get('oauth_token')

    # 4.認可レスポンスを使ってトークンリクエストを行う。
    # (Step 3: Converting the request token to an access token:https://developer.twitter.com/en/docs/authentication/guides/log-in-with-twitter#tab3)
    twitter = OAuth1Session(
        api_key,
        api_secret,
        oauth_token
    )

    res=twitter.post(token_endpoint,params={'oauth_verifier': oauth_verifier})

    access_token = dict(parse.parse_qsl(res.content.decode("utf-8")))

    twitter = OAuth1Session(api_key, api_secret, access_token['oauth_token'], access_token['oauth_token_secret'])
    response = twitter.get('https://api.twitter.com/1.1/account/verify_credentials.json')
    user_info = response.json()

    # ユーザー名とアイコンのURLを取得
    username = user_info['screen_name']
    icon_url = user_info['profile_image_url_https']
    name=user_info['name']

    return jsonify({'username':username,'icon_url':icon_url,'name':name})
    #return jsonify(access_token)


if __name__ == "__main__":
    app.run(debug=True)

