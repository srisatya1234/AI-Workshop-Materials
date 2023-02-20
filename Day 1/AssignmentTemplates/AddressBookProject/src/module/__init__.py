from .adressbooksearch import AddressBookSearcher


def search(city=None, email=None, starting_letter=None, search_type='city'):
    search_init = AddressBookSearcher(city, email, starting_letter, search_type)
    output = search_init.search()
    return output
