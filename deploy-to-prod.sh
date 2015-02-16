#!/usr/bin/env bash
git push heroku master
heroku run --app hyh-django python manage.py migrate
