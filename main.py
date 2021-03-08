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
        try:
            media_type=response['results'][i]['media_type']
        except:
            media_type="N/A"
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
                            "genre_ids":genre_ids,
                            "media_type":media_type
                            })
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
                            "genre_ids":genre_ids,
                            "media_type":media_type
                            })
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

@app.route('/movie/credits')
def movie_credits():
    movie_id=request.args.get('movie_id')
    response=get(f'{SITE_NAME}movie/{movie_id}/credits?{API_KEY}&language=en-US')
    response=response.json()
    # return response
    results=[]
    for i in range(0,min(8,len(response['cast']))):
        try:
            name=response['cast'][i]['name']
        except:
            name="N/A"
        try:
            profile_path=response['cast'][i]['profile_path']
        except:
            profile_path="N/A"
        try:
            character=response['cast'][i]['character']
        except:
            character="N/A"
        results.append({"name":name,
                        "profile_path":profile_path,
                        "character":character,
                        })
    return {"results":results}

@app.route('/movie/reviews')
def movie_reviews():
    movie_id=request.args.get('movie_id')
    response=get(f'{SITE_NAME}movie/{movie_id}/reviews?{API_KEY}&language=en-US')
    response=response.json()
    results=[]
    for i in range(0,min(5,len(response['results']))):
        try:
            username=response['results'][i]["author_details"]['username']
        except:
            username="N/A"
        try:
            content=response['results'][i]['content']
        except:
            content="N/A"
        try:
            rating="N/A" if response['results'][i]["author_details"]['rating']==null else response['results'][i]["author_details"]['rating']
        except:
            rating="N/A"
        try:
            created_at=response['results'][i]['created_at']
        except:
            created_at="N/A"
        results.append({"username":username,
                        "content":content,
                        "rating":rating,
                        "created_at":created_at
                        })
    return {"results":results}

@app.route('/tv')
def tv_details():
    tv_show_id=request.args.get('tv_show_id')
    response=get(f'{SITE_NAME}tv/{tv_show_id}?{API_KEY}&language=en-US')
    response=response.json()
    # return response
    try:
        backdrop_path=response['backdrop_path']
    except:
        backdrop_path="N/A"
    try:
        episode_run_time=response['episode_run_time']
    except:
        episode_run_time="N/A"
    try:
        first_air_date=response['first_air_date']
    except:
        first_air_date="N/A"
    try:
        genres=response['genres']
    except:
        genres="N/A"
    try:
        id=response['id']
    except:
        id="N/A"
    try:
        name=response['name']
    except:
        name="N/A"
    try:
        number_of_seasons=response['number_of_seasons']
    except:
        number_of_seasons="N/A"
    try:
        overview=response['overview']
    except:
        overview="N/A"
    try:
        poster_path=response['poster_path']
    except:
        poster_path="N/A"
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
    results={
            "backdrop_path":backdrop_path,
            "episode_run_time":episode_run_time,
            "first_air_date":first_air_date,
            "genres":genres,
            "id":id,
            "name":name,
            "number_of_seasons":number_of_seasons,
            "overview":overview,
            "poster_path":poster_path,
            "spoken_languages":spoken_languages,
            "vote_average":vote_average,
            "vote_count":vote_count,
            }
    return results

@app.route('/tv/credits')
def tv_credits():
    tv_show_id=request.args.get('tv_show_id')
    response=get(f'{SITE_NAME}tv/{tv_show_id}/credits?{API_KEY}&language=en-US')
    response=response.json()
    # return response
    results=[]
    for i in range(0,min(8,len(response['cast']))):
        try:
            name=response['cast'][i]['name']
        except:
            name="N/A"
        try:
            profile_path=response['cast'][i]['profile_path']
        except:
            profile_path="N/A"
        try:
            character=response['cast'][i]['character']
        except:
            character="N/A"
        results.append({"name":name,
                        "profile_path":profile_path,
                        "character":character,
                        })
    return {"results":results}

@app.route('/tv/reviews')
def tv_reviews():
    tv_show_id=request.args.get('tv_show_id')
    response=get(f'{SITE_NAME}tv/{tv_show_id}/reviews?{API_KEY}&language=en-US')
    response=response.json()
    results=[]
    for i in range(0,min(5,len(response['results']))):
        try:
            username=response['results'][i]["author_details"]['username']
        except:
            username="N/A"
        try:
            content=response['results'][i]['content']
        except:
            content="N/A"
        try:
            rating="N/A" if response['results'][i]["author_details"]['rating']==null else response['results'][i]["author_details"]['rating']
        except:
            rating="N/A"
        try:
            created_at=response['results'][i]['created_at']
        except:
            created_at="N/A"
        results.append({"username":username,
                        "content":content,
                        "rating":rating,
                        "created_at":created_at
                        })
    return {"results":results}

@app.route('/genre/movie/list')
def genre_movie():
    response=get(f'{SITE_NAME}genre/movie/list?{API_KEY}&language=en-US')
    response=response.json()
    return response

@app.route('/genre/tv/list')
def genre_tv():
    response=get(f'{SITE_NAME}genre/tv/list?{API_KEY}&language=en-US')
    response=response.json()
    return response

app.run(debug=True)