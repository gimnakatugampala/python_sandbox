# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core modules
import datetime
from datetime import date
import time

# today = datetime.date.today()
today = date.today()
timestamp = time.time()

print(today)
print(timestamp)

# Pip Modules
from camelcase import CamelCase

c = CamelCase()
print(c.hump('Hello there world'))

# Import Customer Validator
import validitor
from validitor import validate_email

email = 'test@test.com'
if validate_email(email):
    print('Email is Valid')
else:
    print('Email is in valid')