import multiprocessing
import os.path
import sys


_docker = os.path.isfile("/.dockerenv")

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "tornado"

max_requests = 100000
max_requests_jitter = int(0.2 * max_requests)

if _docker:
    bind = "0.0.0.0:8000"
else:
    bind = "127.0.0.1:8000"
keepalive = 120
