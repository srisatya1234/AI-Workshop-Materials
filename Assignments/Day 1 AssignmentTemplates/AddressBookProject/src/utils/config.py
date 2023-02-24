import json
import pkgutil

CONFIG = json.loads(pkgutil.get_data('config', 'config.json'))

# data will appear once you run datagenerator.ipynb
addressdata = json.loads(pkgutil.get_data('data', 'addressdata.json'))
