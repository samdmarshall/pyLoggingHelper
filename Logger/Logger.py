import logging

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object):
    __metaclass__ = Singleton
    _internal_logger = None

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def write():
        if Logger._internal_logger == None:
            Logger._internal_logger = logging.getLogger('com.pewpewthespells.py.logging_helper')
            Logger._internal_logger.setLevel(logging.INFO)

            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # create formatter
            formatter = logging.Formatter('[%(levelname)s]: %(message)s')

            # add formatter to ch
            ch.setFormatter(formatter)

            # add ch to logger
            Logger._internal_logger.addHandler(ch)
        return Logger._internal_logger
