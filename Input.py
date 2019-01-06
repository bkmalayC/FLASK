from BookModel import Book

B = Book()
B.add_book('Malay1' , 23 , 9990)
'''
B.add_book('Malay2' , 23 , 7892)
B.add_book('Malay3' , 23 , 7893)
B.add_book('Malay4' , 23 , 7894)
'''

print(B.get_all_books())


print(5*'*')
c = Book()
c.add_book('Nilay' , 23 , 9991)
l = [book for book in c.get_all_books()]
print(l)
print(id(B) , id(c))