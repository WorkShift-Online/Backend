# Этот файл не относится к проекту: он содержит конфигурацию WSGI сервера
from multiprocessing import cpu_count

bind = "127.0.0.1:8000"

workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

loglevel = 'debug'
accesslog = '/root/Logs/access_log.txt'
errorlog = '/root/Logs/error_log.txt'
