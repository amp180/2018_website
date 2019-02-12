# Personal website

Source code for my website at http://pegman.space

Written in HTML and Sass. Served using uvicorn and responder. With sass for css preprocessing.

I run the tests and ansible deploy pipeline in a jenkins instance running on an orange pi.

The ansible playbook also configures my email server and a few self-hosted web services I use.

## To run
```
python -m pip install pipenv
pipenv shell
pipenv install --dev
pipenv run assets
python -m website_2018
```
