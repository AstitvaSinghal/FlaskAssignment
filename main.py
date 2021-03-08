from flask import Flask,request
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

@app.route('/search_movie')
def search_movie():
    search_query=request.args.get('search_query')
    response=get(f'{SITE_NAME}search/movie?{API_KEY}&query={search_query}&language=en-US&page=1&include_adult=false')
    response=response.json()
    results=[]
    for i in range(0,len(response['results'])):
        try:
            id=response['results'][i]['id']
        except:
            id="N/A"
        try:
            title=response['results'][i]['title']
        except:
            title="N/A"
        try:
            overview=response['results'][i]['overview']
        except:
            overview="N/A"
        try:
            poster_path=response['results'][i]['poster_path']
        except:
            poster_path="N/A"
        try:
            release_date=response['results'][i]['release_date']
        except:
            release_date="N/A"
        try:
            vote_average=response['results'][i]['vote_average']
        except:
            vote_average="N/A"
        try:
            vote_count=response['results'][i]['vote_count']
        except:
            vote_count="N/A"
        try:
            genre_ids=response['results'][i]['genre_ids']
        except:
            genre_ids="N/A"
        results.append({"id":id,
                        "title":title,
                        "overview":overview,
                        "poster_path":poster_path,
                        "release_date":release_date,
                        "vote_average":vote_average,
                        "vote_count":vote_count,
                        "genre_ids":genre_ids})
    return {"results":results}

@app.route('/search_tv')
def search_tv():
    search_query=request.args.get('search_query')
    response=get(f'{SITE_NAME}search/tv?{API_KEY}&language=en-US&page=1&query={search_query}&include_adult=false')
    response=response.json()
    results=[]
    for i in range(0,len(response['results'])):
        try:
            id=response['results'][i]['id']
        except:
            id="N/A"
        try:
            name=response['results'][i]['name']
        except:
            name="N/A"
        try:
            overview=response['results'][i]['overview']
        except:
            overview="N/A"
        try:
            poster_path=response['results'][i]['poster_path']
        except:
            poster_path="N/A"
        try:
            first_air_date=response['results'][i]['first_air_date']
        except:
            first_air_date="N/A"
        try:
            vote_average=response['results'][i]['vote_average']
        except:
            vote_average="N/A"
        try:
            vote_count=response['results'][i]['vote_count']
        except:
            vote_count="N/A"
        try:
            genre_ids=response['results'][i]['genre_ids']
        except:
            genre_ids="N/A"
        results.append({"id":id,
                        "name":name,
                        "overview":overview,
                        "poster_path":poster_path,
                        "first_air_date":first_air_date,
                        "vote_average":vote_average,
                        "vote_count":vote_count,
                        "genre_ids":genre_ids})
    return {"results":results}

@app.route('/search_multi')
def search_multi():
    search_query=request.args.get('search_query')
    response=get(f'{SITE_NAME}search/multi?{API_KEY}&language=en-US&page=1&query={search_query}&include_adult=false')
    response=response.json()
    results=[]
    for i in range(0,len(response['results'])):
            
        try:
            id=response['results'][i]['id']
        except:
            id="N/A"
        try:
            overview=response['results'][i]['overview']
        except:
            overview="N/A"
        try:
            poster_path=response['results'][i]['poster_path']
        except:
            poster_path="N/A"
        try:
            vote_average=response['results'][i]['vote_average']
        except:
            vote_average="N/A"
        try:
            vote_count=response['results'][i]['vote_count']
        except:
            vote_count="N/A"
        try:
            genre_ids=response['results'][i]['genre_ids']
        except:
            genre_ids="N/A"
        if response['results'][i]['media_type']=="tv":
            try:
                name=response['results'][i]['name']
            except:
                name="N/A"
            try:
                first_air_date=response['results'][i]['first_air_date']
            except:
                first_air_date="N/A"
            results.append({"id":id,
                            "name":name,
                            "overview":overview,
                            "poster_path":poster_path,
                            "first_air_date":first_air_date,
                            "vote_average":vote_average,
                            "vote_count":vote_count,
                            "genre_ids":genre_ids})
        elif response['results'][i]['media_type']=="movie":
            try:
                title=response['results'][i]['title']
            except:
                title="N/A"
            try:
                release_date=response['results'][i]['release_date']
            except:
                release_date="N/A"
            results.append({"id":id,
                            "title":title,
                            "overview":overview,
                            "poster_path":poster_path,
                            "release_date":release_date,
                            "vote_average":vote_average,
                            "vote_count":vote_count,
                            "genre_ids":genre_ids})
    return {"results":results}

@app.route('/movie')
def movie_details():
    movie_id=request.args.get('movie_id')
    response=get(f'{SITE_NAME}movie/{movie_id}?{API_KEY}&language=en-US')
    response=response.json()
    try:
        id=response['id']
    except:
        id="N/A"
    try:
        title=response['title']
    except:
        title="N/A"
    try:
        runtime=response['runtime']
    except:
        runtime="N/A"
    try:
        release_date=response['release_date']
    except:
        release_date="N/A"
    try:
        spoken_languages=response['spoken_languages']
    except:
        spoken_languages="N/A"
    try:
        vote_average=response['vote_average']
    except:
        vote_average="N/A"
    try:
        vote_count=response['vote_count']
    except:
        vote_count="N/A"
    try:
        poster_path=response['poster_path']
    except:
        poster_path="N/A"
    try:
        genres=response['genres']
    except:
        genres="N/A"
    try:
        backdrop_path=response['backdrop_path']
    except:
        backdrop_path="N/A"
    results={"id":id,
                    "title":title,
                    "runtime":runtime,
                    "release_date":release_date,
                    "spoken_languages":spoken_languages,
                    "vote_average":vote_average,
                    "vote_count":vote_count,
                    "poster_path":poster_path,
                    "backdrop_path":backdrop_path,
                    "genres":genres}
    return results


app.run(debug=True)