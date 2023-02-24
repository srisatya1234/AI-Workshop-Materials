from utils.storageutils import MySQLManager
from .base import BaseSearcher
from utils.storageutils import CONFIG


class LibraryBookSearcher(BaseSearcher):
    
    def __init__(self, title, author, search_type='title'):
        self.title = title
        self.author = author
        self.search_type = search_type
    
    def _search_by_title(self):
        title = self.title
        if title is None:
            return 'book not found'
        query = '' # update your query to extract availbility of the book
        # if not available who borrowed it
        res = {} # {"status": 1, "borrower": "someobody" }
        try:
            res = MySQLManager.execute_query(query, None, **CONFIG['database']['gnitsstudents'])
            # format the output
        except Exception as error:
            print(error)
        return res
    
    def _search_by_author(self):
        author = self.author
        if author is None:
            return 'book not found'
        query = '' # update your query to extract availbility of the book
        # if not available who borrowed it
        res = {} 
        try:
            res = MySQLManager.execute_query(query, None, **CONFIG['database']['gnitsstudents'])
            # format the output
        except Exception as error:
            print(error)
        # {"status": 1, "borrower": "someobody" }
        # {"status": 0, "borrower": "" }
        return res
    
    def search(self):
        required_output = {}
        if self.search_type == 'title':
            required_output = self._search_by_title()
        else:
            required_output =  self._search_by_author()
        return required_output
