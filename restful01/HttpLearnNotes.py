"""
hold the server up by:
$ python manage.py runserver

check the toy list
$ curl -X GET localhost:8000/toys/
# for nicer print
$ curl -iX GET localhost:8000/toys/

if you have Httpie package installed, even better print:
$ http :8000/toys/

now we check detailed items
$ http :8000/toys/3  

now we post to add new toy
$  http POST :8000/toys/ name="PvZ 2 puzzle" description="plants vs zombies" \
    toy_category="Puzzle" was_included_in_home=false release_date="2017-10-08T01:01:00.777777Z"
"""