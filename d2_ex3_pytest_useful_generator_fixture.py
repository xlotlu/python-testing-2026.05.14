# dat fiind un json cu o structura de date de acest tip:
[
    {'title': 'Jungle Book', 'author': 'Rudyard Kipling'},
    {'title': 'Amintiri din copilărie', 'author': 'Ion Creangă'},
    {'title': 'Harap Alb', 'author': 'Ion Creangă'},
]

# scrieți teste pentru funcția

import json

def get_books(fname, author=None):
    """
    reads all books from the json file `fname`
    and optionally filters them by the given author
    """
    with open(fname, encoding="utf-8") as f:
        books = json.load(f)

    if author is None:
        return books
    
    """
    filtered = []
    for book in books:
        if book['author'] == author:
            filtered.append(book)

    return filtered
    """
    # the same as above but with list comprehension:

    return [
        book
        for book in books
        if book['author'] == author
    ]

