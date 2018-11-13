

def require_string(obj, log=None):
    if isinstance(obj, str):
        if log is not None:
            log.debug(f'String test passed on {obj}')
        return obj

    # else
    log.info(f'String test failed on {obj} returning {str(obj)}')
    return str(obj)
