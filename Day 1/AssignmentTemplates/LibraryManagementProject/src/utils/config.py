import json
import pkgutil

CONFIG = json.loads(pkgutil.get_data('config', 'config.json'))

# data will appear once you run datagenerator.ipynb
booksdata = json.loads(pkgutil.get_data('data', 'booksdata.json'))
