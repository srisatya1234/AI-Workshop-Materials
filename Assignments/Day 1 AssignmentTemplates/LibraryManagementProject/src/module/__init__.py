from .librarybooksearch import LibraryBookSearcher
from .librarybookupdate import LibraryBookUpdater


def search(city=None, email=None, starting_letter=None, search_type='city'):
    search_init = LibraryBookSearcher(city, email, starting_letter, search_type)
    output = search_init.search()
    return output


def update(id, borrower, status):
    update_init = LibraryBookUpdater(id, borrower, status)
    output = update_init.update()
    return output
