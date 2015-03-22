.PHONY: update_virtualenv remove_db create_db create_demo_data rebuild_full rebuild_quick install

update_virtualenv:
	pip install -r requirements.txt

remove_db:
	python manage.py reset_db --router=default --noinput

create_db:
	python manage.py syncdb --noinput
	python manage.py migrate users
	python manage.py migrate

create_demo_data:
	python manage.py create_test_data


rebuild_full: update_virtualenv remove_db create_db create_demo_data

rebuild: remove_pyc remove_orig remove_db create_db create_demo_data

install: rebuild_full
