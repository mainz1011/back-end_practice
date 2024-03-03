#Python comes with a powerful built-in logging module. Different log levels, different config options, how to log in different modules, how to use different log handlers, how to capture stack traces in your log, how to use rotating file handler.
import logging
''' #can log to 5 different log levels as show right below
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
#results (by default):  WARNING:root:This is a warning message
                        ERROR:root:This is an error message
                        CRITICAL:root:This is a critical message
'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
#results:  03/03/2024 22:10:39 - root - DEBUG - This is a debug message
          #03/03/2024 22:10:39 - root - INFO - This is an info message
          #03/03/2024 22:10:39 - root - WARNING - This is a warning message
          #03/03/2024 22:10:39 - root - ERROR - This is an error message
          #03/03/2024 22:10:39 - root - CRITICAL - This is a critical message


