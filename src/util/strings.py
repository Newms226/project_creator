

def require_string(obj, log=None):
    if isinstance(obj, str):
        if log is not None:
            log.debug('String test passed.')
            log.debug(f'RETURNED {obj}')
        return obj

    # else
    if log is not None:
        log.info(f'String test failed on {obj}')
        log.debug(f'RETURNED {str(obj)}')

    return str(obj)
