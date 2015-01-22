# bitcoin-exchange

[![Build Status](https://travis-ci.org/film42/bitcoin-exchange.svg?branch=master)](https://travis-ci.org/film42/bitcoin-exchange)

A web app to facilitate bitcoin exchange

#### Getting Started

1. Setup a virtualenv and install dependencies in `requirements.txt`. You can do this by running `pip install -r requirements.txt`.
2. Create your own `bitcoin_exchange/settings.py` based off of `bitcoin_exchange/settings.py.sample`.
3. Migrate the database `python manage.py migrate`.
3. Run `honcho start` to start the server on port 5000.
