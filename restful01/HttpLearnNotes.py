"""
hold the server up by:
$ python manage.py runserver

check the toy list
$ curl -X GET localhost:8000/toys/
# for nicer print
$ curl -iX GET localhost:8000/toys/

if you have Httpie package installed, even better print:
$ http :8000/toys/
"""