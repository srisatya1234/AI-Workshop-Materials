from utils.storageutils import MySQLManager
from .base import BaseSearcher
from utils.storageutils import CONFIG


class AddressBookSearcher(BaseSearcher):
    
    def __init__(self, city, email, starting_letter, search_type='city'):
        self.city = city
        self.email = email
        self.starting_letter = starting_letter
        self.search_type = search_type
    
    def _search_by_city(self):
        city_name = self.city
        if city_name is None:
            return []
        query = '' # update your query to extract all names with given city
        res = [] # this should be list of names
        try:
            res = MySQLManager.execute_query(query, None, **CONFIG['database']['gnitsstudents'])
            # format the output
        except Exception as error:
            print(error)
        return res
    
    def _search_by_email(self):
        required_email =  self.email
        query = '' # update your query here
        res = [] # should be list of names
        # execute the query using MySQLManager
        return res
    
    def _search_by_starting_letter(self):
        serach_letter_in_name = self.starting_letter
        query = '' # update where name starts with
        res = [] # should be list of names
        # execute the query using MySQLManager
        return res
    
    def search(self):
        required_output = {}
        if self.search_type == 'starting_letter':
            required_output['names'] = self._search_by_starting_letter()
        elif self.search_type == 'email':
            required_output['names'] =  self._search_by_email()
        else:
            required_output['names'] =  self._search_by_city()
        return required_output
