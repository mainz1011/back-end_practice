import logging

'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
import helper
#this creates a hierarchy of loggers: it starts at the root logger, and all the new loggers get added to this hierarchy. And they propagate msgs up to the base logger.
#results:  03/04/2024 18:31:20 - helper - INFO - hello from helper
'''


# set different log handlers
'''
logger = logging.getLogger(__name__)
#create my handler
 #now I want to have a handler log to this stream. And I also want a file handler to log to the file
stream_h = logging.StreamHandler()    #this's a built-in class
file_h = logging.FileHandler('file.log')

 #and for each handler, you wanna set the level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
 #now first, we set the formatter to our handler
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
 #at the end, we add our handler to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)
 #now if we use this logger
logger.warning('watch out, it\'s a warning')
logger.error('watch out, it\'s an error')
#results:  __main__ - WARNING - watch out, it's a warning
           __main__ - ERROR - watch out, it's an error
'''


'''
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('watch out, it\'s a debug msg')
#results:  2024-03-04 20:59:30,277 - simpleExample - DEBUG - watch out, it's a debug msg
'''


# Capturing stack traces in your log
'''
try:
    a = [1, 2, 3]
    val = a[4]     #this will raise an index error
except IndexError as e:    #we can catch this error with 'IndexError as e'
    logging.error(e, exc_info=True)     #results:  ERROR:root:list index out of range
                    #'exc_info=True' can log the stack trace, see the '- errors shown' below
 
- errors shown: 
ERROR:root:list index out of range
Traceback (most recent call last):
  File "...main.py", line 53, in <module>
    val = a[4]     #this will raise an index error
          ~^^^
IndexError: list index out of range
'''

#if you don't know which kind of error it would be, then 'import traceback'
'''
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())
'''
'''
- errors shown: 
ERROR:root:The error is Traceback (most recent call last):
  File "...main.py", line 72, in <module>
    val = a[4]
          ~^^^
IndexError: list index out of range
'''


# Rotating file handlers
 #if there's a large application with lots of log msgs, and you wanna keep track of the emost recent events,
  #then you can use a rotating file handler that keeps the file small.
'''
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB, and keep 5 backup logs app.log.1, app.log.2, etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Welcome to learn!')
#results(now in our folder, we have 5 app.log files)
'''

#if your app will be running for a long time, then you can use a timed rotating file handler
import time
from logging.handlers import TimedRotatingFileHandler    #this will create a rotating log based on how much time has passed
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0/w1/w2... (Mon/Tue/Wed...). Below it's set that a file is created every 5 seconds
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("Check out how it works!")
    time.sleep(5)
#results(now in our folder, a timed_test.log file is created every 5 seconds, and a total of 5 such files are created)

