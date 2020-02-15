#!/usr/bin/env python

import os
import plaid
from flask import Flask
from flask import render_template


app = Flask(__name__)


PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_PUBLIC_KEY = os.getenv('PLAID_PUBLIC_KEY')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')
PLAID_PRODUCTS = os.getenv('PLAID_PRODUCTS', 'transactions')
PLAID_COUNTRY_CODES = os.getenv('PLAID_COUNTRY_CODES', 'US,CA,GB,FR,ES')
#PLAID_OAUTH_REDIRECT_URI = os.getenv('PLAID_OAUTH_REDIRECT_URI', '');

client = plaid.Client(
    client_id = PLAID_CLIENT_ID, 
    secret=PLAID_SECRET,
    public_key=PLAID_PUBLIC_KEY, 
    environment=PLAID_ENV,
    api_version='2019-05-29')

@app.route('/hello_world')
def hello_world():
    DATA = {'name':'man',
            'hobbies':['gaming', 'coding', 'gyming']}

    return render_template(
        'hello_world.ejs',
        plaid_environment=PLAID_ENV,
        data=DATA,
    )


if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))