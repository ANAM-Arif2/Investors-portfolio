
from multiprocessing import cpu_count
import os
wdir = os.getcwd()
accesslog = '/var/log/custom_logs/firewall.cybergen.com-access.log'
errorlog = '/var/log/custom_logs/firewall.cybergen.com-error.log'
# Socket Path
bind = 'unix:/var/python/fastapi/firewall.cybergen.com/firewall.cybergen.com.sock'

# Worker Options
workers = 2 * cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'
# Logging Options
loglevel = 'debug'
accesslog = os.path.join(accesslog)
errorlog = os.path.join(errorlog)

timeout = 1800
keepalive = 1000
threads = 3
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
raw_env = ['TOKENIZERS_PARALLELISM=False']
capture_output = True
worker_tmp_dir = os.path.join(wdir, 'log')
reload = True
