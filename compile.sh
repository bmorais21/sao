#!/bin/bash

python manage.py makemigrations
python manage.py migrations
python manage.py makemessages -l 'en'
python manage.py compilemessages
