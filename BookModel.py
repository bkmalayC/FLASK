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

    @staticmethod
    def add_book(_name , _price , _isbn):
        new_book = Book(name = _name , price = _price , isbn = _isbn)
        db.session.add(new_book)
        db.session.commit()

    def get_book_by_isbn(self , _isbn) :
        return Book.query.filter_by(isbn = _isbn).first()


    @staticmethod
    def delete_book(isbn):
        # if(Book.query.filter_by(isbn = isbn).all()) != None:
            book = Book.query.filter_by(isbn = isbn).delete()
            db.session.commit()
            return book
        #else:
            #return None

    def modify_books(self , _isbn):
        pass

    @staticmethod
    def replace_book(isbn , new_book):

        books = Book.query.filter_by(isbn = isbn).all()
        for book in books :
            if 'name' in new_book.keys()  :
                book.name = new_book['name']
            if 'price' in new_book.keys() :
                book.price = new_book['price']
        db.session.commit()

    def __repr__(self):
        book_object = {
            'name'  : self.name,
            'price' : self.price,
            'isbn'  : self.isbn
        }
        return json.dumps(book_object)





