python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --no-input
python manage.py runserver 0.0.0.0:8000
# gunicorn --workers=2 --bind=0.0.0.0:8000 CMS.wsgi:application