heroku pg:reset --app hyh-django jade
git push heroku master
heroku run --app hyh-django python manage.py migrate
heroku run --app hyh-django python manage.py create_test_data
