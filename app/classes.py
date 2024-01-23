import json
from flask import Flask, request

BOOK_ID = 0
BOOK_TITLE = 1
BOOK_AUTHOR = 2
AUTHOR_NAME = 0

app = Flask(__name__)

booksID = 0
books = [(booksID, 'A Hole in the Sky', 'A. Hopkins')]
authors = {"A. Hopkins": {0}}


@app.post('/addBooks')
def add_books():
    new_books = request.get_json()
    for new_book in new_books['newBooks']:
        global booksID
        global books
        global authors

        booksID += 1

        books.append((booksID, new_book['bookTitle'], new_book['AuthorName']))

        if new_book['AuthorName'] in authors.keys():
            authors[new_book['AuthorName']].add(booksID)
        else:
            authors[new_book['AuthorName']] = {booksID}

    return 'Added', 201


@app.get('/searchBookByAuthor/<string:author_name>')
def search_book_by_author(author_name):
    return {'books': [book[BOOK_TITLE] for book in books if book[BOOK_ID] in authors[author_name]]}


@app.get('/searchAuthorByBook/<string:book_title>')
def search_author_by_book(book_title):
    for book in books:
        if book[BOOK_TITLE] == book_title:
            return book[BOOK_AUTHOR]
    return 'Book not found', 300


@app.get('/library')
def library():
    json_library = {'library': []} # The library
    for author_name, author_booksID in authors.items():
        formatted_author_book = []
        author_books = [(book[BOOK_ID], book[BOOK_TITLE]) for book in books if book[BOOK_ID] in author_booksID] # author books
        for b in author_books:
            formatted_author_book.append({'bookID':b[BOOK_ID], 'bookTitle':b[BOOK_TITLE]})
        json_library['library'].append({author_name: formatted_author_book})  # Adding an author and its books
    return json_library


def main():
    library()


if __name__ == '__main__':
    main()
