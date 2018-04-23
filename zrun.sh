python3 manage.py runserver 0.0.0.0:8000 &
python3 -m celery -A oj worker -l warning &
