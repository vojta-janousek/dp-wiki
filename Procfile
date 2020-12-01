release: python djangoapp/manage.py migrate
web: python djangoapp/manage.py runserver 0.0.0.0:$PORT --noreload
worker: python djangoapp/manage.py rqworker default
