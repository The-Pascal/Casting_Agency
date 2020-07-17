# CASTING AGENCY
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. A user needs to have appropriate permissions to get, post, patch or delete movies or actors in the database.

The app has casting assistants who can get all details of movies or actors, but not change anything.
However, the casting director have the permission to see all details of movies or actors and also change any details or add more actors or delete any actor.
But executive producer has all the permissions to change, add, update or delete any movie or actor via correct endpoints.

The permission tokens are added under 'JWT Tokens' section of readme.

All the endpoints and their implementations are added under 'Endpoints' section of readme. However to use them, you have to use postman or curl, since the app doesn't have any frontend yet.

The app is hosted on heroku and the url for the same is as follows-
**Application URL - https://casting-agency-12345.herokuapp.com/**

### JWT Tokens:

- Casting Assistant
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkVnBmeHE5RS0xS1paSlNTQVU5QiJ9.eyJpc3MiOiJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDU2ODA5NDE5Njc3NjM2NjUzMTYiLCJhdWQiOlsibXlhcHAiLCJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0OTYyNzE4LCJleHAiOjE1OTUwNDkxMTgsImF6cCI6IkpaTUMzNzBXYmNnNVphUW9LU0l4a1FPeW9iTVcwRVVvIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwic2VhcmNoOmFjdG9ycyIsInNlYXJjaDptb3ZpZXMiXX0.MuRbpTp6rXMdJgIbMtUMYv7zZUn2-785XQG2UqYQzz7mhsxMXgmJDECx66xK5AbSQuuVC_03NwYKvPjYwkOqvz5ggvDKRtzQNi8bylsLIXg1xI6Y1NJkAibTbaLyHBUuuC_jlcVdlDezFc4-ZCxNWlZGEqY64CAsFU3NxCXGMI14G-Uc4xLmgIqW2G7gLOiRq5-mJMcOMPq1IyKEslqS0JaXY4h-mbXZFoR7EWmdldxVjIIf7aTGnDx4ayBeZNdgPh3uTVHToBoyJWolQ9RDtDSEsuEEZt7TqNpp3XHKjbswB6DZbRptN6xeTfZ8OPc6e81B9AWkJbacGqQqaIu_EA

- Casting Director
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkVnBmeHE5RS0xS1paSlNTQVU5QiJ9.eyJpc3MiOiJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDU2MzkxNzEyMjUxMDQ4MjgyMzMiLCJhdWQiOlsibXlhcHAiLCJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0OTYyNzgxLCJleHAiOjE1OTUwNDkxODEsImF6cCI6IkpaTUMzNzBXYmNnNVphUW9LU0l4a1FPeW9iTVcwRVVvIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwic2VhcmNoOmFjdG9ycyIsInNlYXJjaDptb3ZpZXMiXX0.E3MHvC2HpYtrwBulxQbYFUs47x5xbFLIpxe6HBcUqwriBErn2LfqsLvqoRONoKgs-DbK8vftvXpYntNTNRJzflQPfiphgP3LgopNU0zg2r96YRAvYQM3GhKsYa2Lw6ix2MxPQH5NY4DjHVYy8qqKpXjcknfYolBqGbuiaqgIiEeisicTprqGSDf-GCZopcenvo_qZoCTBweqwSKOaWjoOLYJ5vF6jtPCc-TRUXmMwI_VezWyu-H8e0afNRMSKqRORJtS10tofcxY1uIvuBSEm5ChE2EFr93IWvglh6fx0U7evEa3dZM0TlBbmPtx-HWSECzTCxRr78lOwKevjtZXfA


- Executive Producer
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkVnBmeHE5RS0xS1paSlNTQVU5QiJ9.eyJpc3MiOiJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE1Mzg4MDU0Nzc3MzQ4ODAyMDEiLCJhdWQiOlsibXlhcHAiLCJodHRwczovL2Rldi1xOGI5c210aC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTk0OTYyODM3LCJleHAiOjE1OTUwNDkyMzcsImF6cCI6IkpaTUMzNzBXYmNnNVphUW9LU0l4a1FPeW9iTVcwRVVvIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIiwic2VhcmNoOmFjdG9ycyIsInNlYXJjaDptb3ZpZXMiXX0.orSa4uybbWvQ2m4TO7wFZ0gaaovySi9D7RxyPWMRjAArzHRc8gtavGpq1Qmoc2_bjAtb8kN7yMRErXzPVqqfjIz7EEYm-Gxv3j3X94dnTcvRvyvcUXg3DZoUpTkvxzM1Au6cSeey0T_hHdY65INPwWu8L09-4gsNtqTiCMBZRpa-3fw-d3mm2KsraDHRfT_vECHTjrpoJT-sWqKMuF-eObKFWcFcV4qDMn6czCHsCAFxHHC7WGdZUDqggQzJzluBS4g_KWAHvRm-etYESM02PNtubIrxALLweuvmSE4aWcBXUEG-7NsJdijij96iKEGdgWng7C0zIqAXgq2-knnj2w

### Installing Dependencies

#### Python

Install Python3.7 using official python docs.

#### Virtual Environment (venv)

You can use virtual environment to keep all your python dependencies separate.
To setup virtual environment 
- Install virtual environment using
```
pip install virtualenv
```
- To create a virtual environment use
```
virtualenv name_of_virtualenv
```

#### PIP Dependencies from requirements.txt

You can install all required pip dependencies from requirements.txt using -

```
pip3 install -r requirements.txt
```

##### Other Dependencies Required

- Flask
- Flask-CORS
- SQLAlchemy

## Local Database setup

After creating the database, you can use the following commands to create required relations-
```
flask db init
flask db migrate
flask db upgrade
```


## Running the server

First export the required environment variables from setup.sh for that terminal using
```
source setup.sh
``` 

Then you can run the server from root directory using
```
python3 app.py
```

## Project Details:

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

#### Models:

There are two models in the projects for movies and actors respectively-

- Movies with attributes title and release date
- Actors with attributes name, age and gender

#### Roles:

- Casting Assistant
    "get:actors",
    "get:movies"
- Casting Director
    "delete:actors",
    "get:actors",
    "get:movies",
    "patch:actors",
    "patch:movies",
    "post:actors",
    "search:actors",
    "search:movies"
- Executive Producer
    "delete:actors",
    "delete:movies",
    "get:actors",
    "get:movies",
    "patch:actors",
    "patch:movies",
    "post:actors",
    "post:movies",
    "search:actors",
    "search:movies"



## API DOCUMENTATION

### Endpoints

For using these endpoints, you have to send a jwt token with each request and with appropriate permissions to access that particular endpoints. I have already added tokens in the 'JWT tokens' section of this readme.
Since the application don't have a frontend, you can use curl or postman to use these endpoints.

- GET '/movies' - used to get all movies
- GET "/actors" - used to get all actors
- POST "/movies" - used to add more movies
- POST "/actors" - used to add more actors
- PATCH "/movies/int:movie_id"  -   used to change details of specific movie
- PATCH "/actors/int:actor_id"  -   used to change details of specific actor
- DELETE "/movies/int:movie_id" - used to delete a specific movie
- DELETE "/actors/int:actor_id" - used to delete a specific actor

##### GET '/movies'

- Fetches a dictionary of movies with key:value pair of total number of movies.
- Request Arguments: None
- Permission: required
- Returns:
``` 
{
    "Total number of movies": 1,
    "movies": [
        {
            "actors": [2],
            "id": 1,
            "release_date": "Wed, 13 Oct 2010 00:00:00 GMT",
            "title": "Universe"
        },
    ],
    "success": true
}
```


##### GET "/actors"
- Fetches a dictionary of all actors with key:value pair of total number of actors
- Request Arguments: None
- Permission: required
- Returns:
```
{
    "All Actors": [
        {
            'name' : 'Robert Downey Jr',
            'age': 44,
            'gender': 'Male',
            'movie_id': 4
        }
    ],
    "Total number of actors": 0,
    "success": true
}
```

##### POST "/movies"
- Adds a new movie to the database
- Request Arguments: required
    - title : title of movie
    - release : releasing date of movie
- Permission: required
- Returns :
```
{
    "message": "movie added successfully",
    "movie added": {
        "actors": [],
        "id": 5,
        "release_date": "Mon, 10 Feb 2014 00:00:00 GMT",
        "title": "Godfather"
    },
    "success": true
}
```

##### POST "/actors"
- Adds a new actor to the database
- Request Arguments: required
    - name : name of actor
    - age : age of actor
    - gender : gender of actor
    - movie_id : movie to which actor is related
- Permission: required
- Returns :
```
{
    "actor added": {
        "age": 44,
        "gender": "Male",
        "id": 1,
        "movie_id": 2,
        "name": "Robert Downey Jr"
    },
    "message": "actor added successfully",
    "success": true
}
```

##### PATCH "/movies/int:movie_id"
- Used to change details of a specific movie
- Request Parameters: Present
    movie_id: movie ID needed to be changed
- Returns :
```
{
    "success": True,
    "message": "update successfull",
    "movie changed to ":{
        "actors": [],
        "id": 2,
        "release_date": "Mon, 24 Feb 2002 00:00:00 GMT",
        "title": "Son of Justice"
    }
}
```

##### PATCH "/actors/int:actor_id"
- Used to change details of a specific actor
- Request Parameters: Present
    actor_id: actor ID needed to be changed
- Returns :
```
{
    "actor changed to ":{
        "age": 32,
        "gender": "Male",
        "id": 12,
        "movie_id": 4,
        "name": "Alpha Dude"
    }
    "success": True,
    "message": "update successfull",
}
```

##### DELETE "/movies/int:movie_id"
- Delete a specific movie from database
- Request Arguments: Present
    movie_id: ID of the movie
- Response Body:
```
{
    'success': True,
    'deleted': 5
}
```

##### DELETE "/actors/int:actor_id"
- Delete a specific actor from database
- Request Arguments: Present
    actor_id: ID of the actor
- Response Body:
```
{
    'success': True,
    'deleted': 5
}
```

