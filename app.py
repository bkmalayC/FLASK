from flask import Flask , jsonify , request , Response , json
from BookModel import *
from lib import *
from settings import *
import jwt , datetime

@app.route('/login')
def get_token():
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
    token = jwt.encode({'exp' : expiration_date} , app.config['SECRET_KEY'] , algorithm = 'HS256')
    return token


@app.route('/books')
def get_books():
    token = request.args.get('token')
    try :
        jwt.decode(token , app.config['SECRET_KEY'])
    except :
        return jsonify({'Error' : 'Token not valid'} , 401)
    return json.dumps({'Books' : Book.get_all_books()})

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
    new_book = request_data
    Book.replace_book(isbn , new_book)
    return Response("" , 204)

@app.route('/books' , methods = ['POST'])
def add_books():
    #return "Hello Malay"
    requestObj = request.get_json(force = True)
    #print(requestObj)
    if(validBookObject(requestObj)) :
        Book.add_book(requestObj['name'] , requestObj['price'] , requestObj['isbn'] )
        response = Response("" ,status = 501 , mimetype= 'json' )
        response.headers['Path'] = "/books/" + str(requestObj['isbn'])
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
    deleted_book = Book.delete_book(isbn)
    print(deleted_book)
    errormsg = { 'error' : 'No book found to be deleted' , 'Cooments' : 'Check well'}

    if deleted_book > 0 :
        return Response("" , 204)
    else :
        return Response(json.dumps(errormsg) , status = 504)

    #return jsonify(deleted_book)

app.run(port = 5000)
