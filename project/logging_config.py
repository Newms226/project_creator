import logging
import datetime

LOGGING_DIR = '/Users/michael/prog/python/python3/project_creator/logs'

logging.basicConfig()

# LOGGERS
root_logger = logging.getLogger('root')
root_logger.propagate = False


# FORMATTERS
_basic_formatter = logging.Formatter(
    fmt='%(name)s:%(levelname)s: %(module)s.%(funcName)s().%('
        'lineno)d: '
        '%(message)s')

# HANDLERS
_file_handler = logging.FileHandler(LOGGING_DIR
                                        + '/{:%b%m_%y:%I%p_%M-%S}.log'
                                        .format(datetime.datetime.now()),
                                    mode='w')
_file_handler.setLevel('DEBUG')
_file_handler.setFormatter(_basic_formatter)

_console_handler = logging.StreamHandler()
_console_handler.setLevel('WARNING')
_console_handler.setFormatter(_basic_formatter)

# set handlers
root_logger.addHandler(_file_handler)
root_logger.addHandler(_console_handler)

root_logger.setLevel('DEBUG')

