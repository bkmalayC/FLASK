from flask import Flask , jsonify , request , Response , json
from BookModel import *
from lib import *
from settings import *

#app = Flask(__name__)

@app.route('/books')
def get_books():

    return jsonify({'books' : books})

@app.route('/books/<int:isbn>')
def get_books_byIsbn (isbn):
    return_value = {}
    for book in books:
        if isbn == book['isbn'] :
            return_value = {'name' : book['name'] , 'price' : 2*book['price']}

    return jsonify(return_value)

@app.route('/books/<int:isbn>' , methods = ['PUT'])
def replace_book(isbn) :

    request_data = request.get_json(force = True)
    current_isbn = isbn
    new_book = request_data
    new_book.update({'isbn' : isbn})

    for book in books:
        if book['isbn'] == isbn :
            books.remove(book)

    books.insert(0 , new_book)
    return Response("" , 204)

@app.route('/books' , methods = ['POST'])
def add_books():
    #return "Hello Malay"
    requestObj = request.get_json(force = True)
    #print(requestObj)
    if(validBookObject(requestObj)) :
        new_book = {
                     "name"  : requestObj['name'],
                     "price" : requestObj['price'],
                     "isbn"  : requestObj['isbn'],
                   }
        books.insert(0 , new_book )
        response = Response("" ,status = 501 , mimetype= 'json' )
        response.headers['Path'] = "/books/" + str(new_book['isbn'])
    else :
        invalidRequest = {
            "Error" : "Bad request -- Format is not good" ,
            "Help"  : "name :  XXX , price : YYY , isbn : ZZZ"
        }
        response = Response( json.dumps(invalidRequest), status = 999 , mimetype='application/json')

    return response

@app.route('/books/<int:isbn>' , methods = ['PATCH'])
def update_books(isbn) :

    request_data = request.get_json(force=True)
    print(request_data)
    current_isbn = isbn

    updated_book = {}
    if ('name' in request_data) :
        updated_book['name'] = request_data['name']

    if ('price' in request_data):
        updated_book['price'] = request_data['price']

    for book in books :
        if isbn == book['isbn'] :
            book.update(updated_book)

    return Response("", 204)


@app.route('/books/<int:isbn>' , methods = ['DELETE'])

def delete_book(isbn):
    deleted_book = []
    for book in books:
        if book['isbn'] == isbn :
            #print(book)
            deleted_book.append(book)
            books.remove(book)

    print(deleted_book)
    #print(json.dumps(deleted_book))
    errormsg = { 'error' : 'No book found to be deleted' , 'Cooments' : 'Check well'}
    x = {'name': 'book2', 'price': 450, 'isbn': 9553849872}

    if len(deleted_book) == 0 :
        return Response(json.dumps(errormsg) , status = 404)
    else :
        return Response(json.dumps(deleted_book) , status = 504)

    #return jsonify(deleted_book)



app.run(port = 5000)
