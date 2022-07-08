from resources.user import UserApi
from resources.movie import MovieApi, MoviesApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movie/<id>')

    api.add_resource(UserApi, '/api/user')