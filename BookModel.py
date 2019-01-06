from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename = 'books'
    id = db.Column(db.Integer, primary_key=True)




books = [
    {'name' : 'book100' , 'price' : 350 , 'isbn' : 8553849872} ,
    {'name' : 'book200' , 'price' : 450 , 'isbn' : 9553849872}

     ]