from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80) , nullable = False)
    price = db.Column(db.Float , nullable = False)
    isbn = db.Column(db.Integer)

    # APIs to access book objects

    def json(self):
        return {'name' : self.name , 'price' : self.price , 'isbn' : self.isbn}

    @staticmethod
    def get_all_books() :
        return [Book.json(book) for book in Book.query.all()]


    def add_book(self , _name , _price , _isbn):
        new_book = Book(name = _name , price = _price , isbn = _isbn)
        db.session.add(new_book)
        db.session.commit()

    def get_book_by_isbn(self , _isbn) :
        return Book.query.filter_by(isbn = _isbn).first()


    def delete_book(self , _isbn):
        book = Book.query.filter_by(_isbn).delete()
        db.session.commit()


    def modify_books(self , _isbn):
        pass

    def replace_book(self_isbn):
        pass

    def __repr__(self):
        book_object = {
            'name'  : self.name,
            'price' : self.price,
            'isbn'  : self.isbn
        }
        return json.dumps(book_object)


