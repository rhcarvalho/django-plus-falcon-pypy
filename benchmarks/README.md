Benchmarks
==========

The app was served first from a virtualenv using CPython 2.7.9, and later by another virtualenv with PyPy 2.5.0.
Commands run:

    ab -n 20000 -c 200 -r http://127.0.0.1:8000/json > *-django.txt
    ab -n 20000 -c 200 -r http://127.0.0.1:8000/falcon/json > *-falcon.txt

I've also run this against the Docker container with PyPy 2.5.0:

    ab -n 20000 -c 200 -r http://192.168.59.103:8000/json > pypy-docker-django.txt
    ab -n 20000 -c 200 -r http://192.168.59.103:8000/falcon/json > pypy-docker-falcon.txt
