release: sh -c 'python manage.py migrate && python manage.py loaddata initial_faq.json'
web: python manage.py migrate && gunicorn project_django.wsgi