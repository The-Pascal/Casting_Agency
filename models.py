
from sqlalchemy import Column, String,Date, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import os

database_name = "casting"
database_path = "postgres://{}:{}@{}/{}".format("duke", "Time@1234","localhost:5432",database_name)
db = SQLAlchemy()

'''
setup_db(app)
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
Define Actor class here

'''
class Actor(db.Model):  
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  movie_id = Column(Integer, db.ForeignKey('movies.id'), nullable=False)

  def __init__(self, name, age, gender , movie_id):
    self.name = name
    self.age = age
    self.gender = gender
    self.movie_id = movie_id

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
      'movie_id':self.movie_id
    }


'''
Define Movie class here 

'''
class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release = Column(Date)
  actors = db.relationship('Actor', backref='movies')

  def __init__(self, title, release):
    self.title = title
    self.release = release

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release,
      'actors': self.actors
    }
