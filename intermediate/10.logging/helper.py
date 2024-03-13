import logging
# below I create my own internal logger (with the name of the module: 'helper')
logger = logging.getLogger(__name__)
logger.propagate = False    #if I don't want to have the propagation, I set it to 'False', now it won't propagate to the base logger.
                             #So now if we run the 'main.py' module, then nothing gets logged here.
logger.info('hello from helper')

