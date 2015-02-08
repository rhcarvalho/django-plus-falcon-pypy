Django + Falcon on PyPy
-----------------------

This project demos how to combine a Django and a Falcon WSGI app into a hybrid WSGI app with custom dispatching.
Yeah, it is meant just for me to play with Docker, PyPy and Falcon.


Usage
-----

You will need Docker and Fig installed. Then you just need to run:

    fig up

And visit [http://localhost:8000](http://localhost:8000) or [http://$(boot2docker ip):8000](http://192.168.59.103:8000) to see your hybrid app running.

If you don't want to use Fig, you can use the Docker client directly:

    docker build -t pypy-falcon-hello .
    docker run --rm -it -p 8000:8000 --name falcon pypy-falcon-hello


URLs
----

    /           :: Hello from Django
    /falcon     :: Hello from Falcon
    /falcon/404 :: Request info as seen by Falcon
    /admin      :: Django admin interface (user: admin, password: admin)
    /random     :: Hello from a random subapp

For benchmarking:

    /json        :: {"hello":"world"}
    /falcon/json :: {"hello":"world"}
