# Personal website

Source code for my website at http://pegman.space

Written in python3 and responder. With sass for css preprocessing.

I run the tests and deploy pipeline on a jenkins instance running on an orange pi.

## To run
```
python -m pip install pipenv
pipenv shell
pipenv install --dev
pipenv run assets
python -m website_201
```