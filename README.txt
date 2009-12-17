============
pyreadernaut
============

Simple python wrapper around the Readernaut.com API.

------------
Installation
------------

You can install by running the following command inside this directory.
    
    python setup.py install

You can also install using either ``easy_install`` or ``pip``.
    
    easy_install pyreadernaut
    
    pip install pyreadernaut

Or you can just place readernaut.py somewhere on your python path.

--------------
Usage Examples
--------------

This example gets a list of the books that 'oscarduignan' is reading.

    import readernaut
    
    book_list = readernaut.get_books('oscarduignan', 'reading')
    for book in book_list:
        print '%s by %s' % (book['title'], ', '.join(book['authors']))

The Readernaut API only returns the first 20 results, you can request the next
20 results by passing in a dict with the optional url data.

    book_list = readernaut.get_books('oscarduignan', 'reading', {'page': 2})

You can control the order of the results in the same way.

    book_list = readernaut.get_books('oscarduignan', 'reading', {'order': '-modified'})

The above should be enough for most users, but you will find there are a few more
functions which you may find useful if you look at the source code.

Readernaut API documentation
(http://groups.google.com/group/readernaut-api/web/restful-api-overview)

-------
Changes
-------

0.1 - initial release
0.2 - readernaut API differed from their documentation, adjusted README.txt
0.3 - query strings were not being appened to url correctly, fixed

