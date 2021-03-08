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
def proxy():
    response=get(f'{SITE_NAME}trending/movie/week?{API_KEY}')
    app.logger.info(len(response.json()['results']))
    return response.json()
app.run(debug=True)