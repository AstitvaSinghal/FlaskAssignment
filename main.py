from flask import Flask
from requests import get

app = Flask(__name__,static_url_path='/static')
# https://api.themoviedb.org/3/trending/movie/week?api_key=43bbbb54f13dcbf603430aa378bc0051
SITE_NAME = 'https://api.themoviedb.org/3/'
API_KEY='api_key=43bbbb54f13dcbf603430aa378bc0051'

@app.route('/')
def serveHomePage():
    return app.send_static_file('index.html')

@app.route('/trending')
def trending():
    response=get(f'{SITE_NAME}trending/movie/week?{API_KEY}')
    response=response.json()
    results=[]
    for i in range(0,5):
        try:
            title=response['results'][i]['title']
        except:
            title="N/A"
        try:
            backdrop_path=response['results'][i]['backdrop_path']
        except:
            backdrop_path="N/A"
        try:
            release_date=response['results'][i]['release_date']
        except:
            release_date="N/A"
        results.append({"title":title,"backdrop_path":backdrop_path,"release_date":release_date})
    return {"results":results}

@app.route('/airing_today')
def airing_today():
    response=get(f'{SITE_NAME}tv/airing_today?{API_KEY}')
    response=response.json()
    # return response
    results=[]
    for i in range(0,5):
        try:
            name=response['results'][i]['name']
        except:
            name="N/A"
        try:
            backdrop_path=response['results'][i]['backdrop_path']
        except:
            backdrop_path="N/A"
        try:
            first_air_date=response['results'][i]['first_air_date']
        except:
            first_air_date="N/A"
        results.append({"name":name,"backdrop_path":backdrop_path,"first_air_date":first_air_date})
    return {"results":results}

app.run(debug=True)