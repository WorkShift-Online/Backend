# Этот файл не относится к проекту: он содержит конфигурацию WSGI сервера
from multiprocessing import cpu_count

bind = "127.0.0.1:8000"

workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

loglevel = 'debug'
accesslog = '/home/automator/workshift/Logs/access_log.txt'
errorlog = '/home/automator/workshift/Logs/error_log.txt'
