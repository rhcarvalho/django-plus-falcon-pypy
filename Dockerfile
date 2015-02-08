FROM pypy:2-onbuild

EXPOSE 8000
RUN ["pypy", "manage.py", "migrate"]
RUN ["pypy", "manage.py", "collectstatic", "--noinput", "-l"]
CMD ["./run"]
