import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_migrate import Migrate

from models import setup_db, Movie, Actor, db
from auth import requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    Set up CORS. Allow '*' for origins.
    '''
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    '''
    Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    '''
    functions used to query
    '''
    def func_to_query(to_be_queried):
        return to_be_queried.query.all()

    '''
    function to format a request
    '''
    def func_to_format(to_be_formatted):
        formatted = [term.format() for term in to_be_formatted]
        return formatted

    '''
    function to get json from request
    '''
    def get_json(get_this):
        return request.json.get(get_this)

    '''
    Get all actors from database
    '''
    @app.route('/actors', methods=['GET'])  # working fine
    @requires_auth('get:actors')
    def get_all_actors_from_db():
        all_actors = func_to_query(Actor)

        all_actors_final = func_to_format(all_actors)

        return jsonify({
            'All Actors': all_actors_final,
            'Total number of actors': len(all_actors_final),
            'success': True
        })

    '''
    Get all movies from database
    '''
    @app.route('/movies', methods=['GET'])  # working fine
    @requires_auth('get:movies')
    def get_all_movies_to_show():
        all_movies = func_to_query(Movie)

        all_movies = func_to_format(all_movies)

        for movie in all_movies:
            movie['actors'] = func_to_format(movie['actors'])

        return jsonify({
            'movies': all_movies,
            'Total number of movies': len(all_movies),
            'success': True
        })

    '''
    Post a new movie
    '''
    @app.route('/movies', methods=['POST'])  # working fine
    @requires_auth('post:movies')
    def add_movie():
        title = get_json('title')
        release = get_json('release')

        if not (title and release):
            return abort(400)

        movie_to_add = Movie(title, release)
        movie_to_add.insert()

        return jsonify({
            'success': True,
            'message': 'movie added successfully',
            'movie added': movie_to_add.format()
        })

    '''
    Post a new actor
    '''
    @app.route('/actors', methods=['POST'])  # working fine
    @requires_auth('post:actors')
    def add_actor():
        name = get_json('name')
        age = get_json('age')
        gender = get_json('gender')
        movie_id = get_json('movie_id')

        if not (name and age and gender):
            return abort(400)

        actor_to_add = Actor(name, age, gender, movie_id)
        actor_to_add.insert()

        return jsonify({
            'success': True,
            'message': "actor added successfully",
            'actor added': actor_to_add.format()
        })

    '''
    Change a movie details
    '''
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])  # working fine
    @requires_auth('patch:movies')
    def change_movie_details(movie_id):
        movie = Movie.query.get(movie_id)

        if not movie:
            abort(400)

        title = get_json('title')
        release = get_json('release')

        movie.title = title
        movie.release = release

        changed_movie = Movie(title, release)

        movie.update()

        return jsonify({
            "success": True,
            "message": "update successfull",
            "movie changed to ": changed_movie.format()
        })

    '''
    Change an actor details
    '''
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])  # working fine
    @requires_auth('patch:actors')
    def change_actor_details(actor_id):
        actor = Actor.query.get(actor_id)

        if not actor:
            abort(400)

        name = get_json('name')
        age = get_json('age')
        gender = get_json('gender')
        movie_id = get_json('movie_id')

        actor.name = name
        actor.age = age
        actor.gender = gender
        actor.movie_id = movie_id

        changed_actor = Actor(name, age, gender, movie_id)

        actor.update()

        return jsonify({
            "success": True,
            "message": "update successfull",
            "actor changed to ": changed_actor.format()
        })

    '''
    Delete a movie
    '''
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])  # working fine
    @requires_auth('delete:movies')
    def delete_specific_movie(movie_id):

        movie = Movie.query.get(movie_id)

        if movie is None:
            return abort(404)
        else:
            movie.delete()
            return jsonify({
                'success': True,
                'deleted': movie_id
            })

    '''
    Delete a actor
    '''
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])  # working fine
    @requires_auth('delete:actors')
    def delete_specific_actor(actor_id):

        actor = Actor.query.get(actor_id)

        if actor is None:
            return abort(404)
        else:
            actor.delete()
            return jsonify({
                'success': True,
                'deleted': actor_id
            })

    '''
    Search a actor
    '''
    @app.route('/search/actors', methods=['POST'])  # working fine
    @requires_auth('search:actors')
    def search_question():

        actor_name_to_search = request.json.get('searchTerm', '')

        if (actor_name_to_search == ''):
            abort(422)

        actorFound = Actor.query.filter(
            Actor.name == actor_name_to_search).all()

        if not actorFound:
            abort(404)

        return jsonify({
            'success': True,
            'message': 'Actors are found',
        })

    '''
    Search a movie
    '''
    @app.route('/search/movies', methods=['POST'])  # working fine
    @requires_auth('search:movies')
    @requires_auth()
    def search_movie():

        movie_name_to_search = request.json.get('searchTerm', '')

        if (movie_name_to_search == ''):
            abort(422)

        movieFound = Movie.query.filter(
            Movie.title == movie_name_to_search).all()

        if not movieFound:
            abort(404)

        return jsonify({
            'success': True,
            'message': 'Movies are found',
        })

    '''
    Error handlers for expected errors
    '''

    # Error handler for 404-Not found
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404

    # Error handler for 422-Unprocessable Entity
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    # Error handler for 400-bad request
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    # Error handler for 500-Internal Server Error
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
        }), 500

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
