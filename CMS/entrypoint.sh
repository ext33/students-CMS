python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind=0.0.0.0:8000 CMS.wsgi:application