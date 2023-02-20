from utils.storageutils import MySQLManager
from .base import BaseSearcher
from utils.storageutils import CONFIG
from time import time


class LibraryBookupdater(BaseSearcher):
    
    def __init__(self, id, status, borrower, search_type='title'):
        self.id = id
        self.status = status
        self.borrower = borrower
        self.date = time.now()
    
    def _update_status(self):
        # self.id, self.status, self.borrower, self.date
        query = '' # use MySQLManager.update() query to update a particular row
        # if not available who borrowed it
        res = {} 
        try:
            res = MySQLManager.execute_query(query, None, **CONFIG['database']['gnitsstudents'])
            # format the output
            # res = {"status": "sucessfull" }
        except Exception as error:
            print(error)
            # res = {"status": "failed" }
        return res
    
    def update(self):
        required_output = self._update_status()
        return required_output
