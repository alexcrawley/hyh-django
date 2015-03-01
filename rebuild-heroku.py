heroku pg:reset --app hyh-django jade
heroku run --app hyh-django python manage.py syncdb
heroku run --app hyh-django python manage.py create_test_event_data
