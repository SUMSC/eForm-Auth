bind = '127.0.0.1:8001'     # bind host:port
workers = 2
timeout = 10
keepalive = 3
daemon = True
user = 'amber'
worker_class = 'gevent'     # run in gevent mode
proc_name = 'gunicorn.proc'
pidfile = '/home/amber/eForm-Backend/logs/eForm-Auth-0.pid'
#loglevel = 'info'
#access_logfile = '/home/amber/eForm-Backend/logs/eForm-Auth-0.log'
#error_logfile = '/home/amber/eForm-Backend/logs/eForm-Auth-0.error.log'

