"""
Simple python wrapper around the Readernaut.com API.

Readernaut API information
(http://groups.google.com/group/readernaut-api/web/restful-api-overview)
"""

import urllib
import urllib2
from xml.etree import ElementTree as ET


API_URL = "http://readernaut.com/api/v1/xml/%s/%s"


def open_books_xml(username, category='', data=None):
    """Returns a Readernaut users books as xml (result of a urllib2.urlopen).

    Arguments:
        username - Readernaut username
        category - category to retrieve books from, leave blank for all books
        data     - optional request data to be appended with urlencode

    Readernaut API Information
    (http://groups.google.com/group/readernaut-api/web/restful-api-overview)
    """
    url = API_URL % (urllib.quote(username), 'books/%s' % urllib.quote(category))
    return urllib2.urlopen(url, urllib.urlencode(data or {}))


def open_notes_xml(username, data=None):
    """Returns a Readernaut users notes as xml (result of a urllib2.urlopen).

    Arguments:
        username - Readernaut username
        data     - optional request data to be appended with urlencode
    """
    url = API_URL % (urllib.quote(username), 'notes')
    return urllib2.urlopen(url, urllib.urlencode(data or {}))


def open_contacts_xml(username, data=None):
    """Returns a Readernaut users contacts as xml (result of a urllib2.urlopen).

    Arguments:
        username - Readernaut username
        data     - optional request data to be appended with urlencode
    """
    url = API_URL % (urllib.quote(username), 'contacts')
    return urllib2.urlopen(url, urllib.urlencode(data or {}))


def parse_books(xml):
    """Returns a list of books contained in a Readernaut book list.

    Arguments:
        xml - xml for a Readernaut book list
    """
    books = []
    for book in ET.parse(xml).getiterator('book_edition'):
        books.append({
            'title': book.find('title').text,
            'authors': [author.text for author in book.find('authors')],
            'permalink': book.find('permalink').text,
            'isbn': book.find('isbn').text,
            'covers': {
                'small': book.find('covers/cover_small').text,
                'medium': book.find('covers/cover_medium').text,
                'large': book.find('covers/cover_large').text,
            }
        })
    return books


def get_books(*args, **kwargs):
    """Wraps parse_books and open_books_xml."""
    xml = open_books_xml(*args, **kwargs)
    books = parse_books(xml)
    xml.close()
    return books


if __name__ == '__main__':
    import doctest
    doctest.testmod()
