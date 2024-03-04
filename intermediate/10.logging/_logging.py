#Python comes with a powerful built-in logging module.
 #Different log levels, different config options, how to log in different modules, how to use different log handlers,
  #how to capture stack traces in your log, how to use rotating file handler.
import logging
'''
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
#results (by default):  WARNING:root:This is a warning message
                        ERROR:root:This is an error message
                        CRITICAL:root:This is a critical message
'''
#here '%s' is string format
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



# log 'handler' objects are responsible for dispatching the appropriate log msg to the handler's specific destination.
 #for example, you can use different handlers to send log msgs to this standard output stream / files via HTTP/email.



# config methods: apart from basic config, we can use the file config or dict config methods.
                                                    #similar to the file config, the dict config is just a different syntax to use https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema



# Capturing stack traces in your log (useful when troubleshooting)



