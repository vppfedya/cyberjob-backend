release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn config.wsgi
web: python manage.py migrate && gunicorn config.wsgi --log-file -