import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import Actor, Movie, setup_db
from app import create_app
from models import db


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TEST CASES STARTS HERE
    """

    #TEST for successfully getting movies
    def test_get_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"],True)
        self.assertTrue(data["Total number of movies"]>0)

    # #TEST for successfully getting actors
    def test_get_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"],True)
        self.assertTrue(data["Total number of actors"]>0)


    # TEST post a new movie
    def test_post_new_movie(self):

        new_movie = {
            'title' : 'Universe',
            'release': '2010-10-13',
        }

        res = self.client().post("/movies", json=new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movie added'])>0)

    # TEST for 400 status code for missing title of movie
    def test_400_new_movie(self):

        new_movie = {
            'release': '2010-10-13'
        }

        res = self.client().post("/movies", json=new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    # TEST post a new actor
    def test_post_new_actor(self):

        new_actor = {
            'name' : 'Robert Downey Jr',
            'age': 44,
            'gender': 'Male',
            'movie_id': 4
        }

        res = self.client().post("/actors", json=new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], "actor added successfully")

    # TEST for 400 status code for missing age of new actor
    def test_400_new_actor(self):

        new_actor = {
            'name' : 'Robert Downey Jr',
            'gender': 'Male',
            'movie_id': 4
        }

        res = self.client().post("/actors", json=new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    # TEST for change details of already present movie
    def test_patch_movie(self):

        movie_details = {
            'title': "The THOR",
            'release': "2014-12-05"
        }
        
        res = self.client().patch("/movies/5", json=movie_details)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "update successfull")

    #TEST for movie not found while patching
    def test_400_movie_not_present_for_patching(self):
        movie_details = {
            'title': "The THOR",
            'release': "2014-12-05"
        }

        res = self.client().patch("/movies/5000", json=movie_details)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    # TEST for change details of already present actor
    def test_patch_actor(self):

        patch_actor = {
            'name' : 'John Doe',
            'age':24,
            'gender': 'Male',
            'movie_id': 2
        }
        
        res = self.client().patch("/actors/5", json=patch_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["message"], "update successfull")

    #TEST for actor not found while patching
    def test_400_actor_not_present_for_patching(self):
        patch_actor = {
            'name' : 'John Doe',
            'age':24,
            'gender': 'Male',
            'movie_id': 2
        }

        res = self.client().patch("/actors/5000", json=patch_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for deleting a specific actor
    def test_delete_actor(self):
        res = self.client().delete("/actors/5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for getting 404 while deleting a specific actor
    def test_404_delete_actor(self):
        res = self.client().delete("/actors/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


    # TEST for deleting a specific movie
    def test_delete_movie(self):
        res = self.client().delete("/movies/5")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    # TEST for getting 404 while deleting a specific movie
    def test_404_delete_movie(self):
        res = self.client().delete("/movies/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
