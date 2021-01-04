import time

'''
def log_():
    def decorator(func):
        def wrapper(*args, **kwargs):
            name, cmd, out, duration = func(*args, *kwargs)
            logger = args[0].logger
            logger.log(name.upper())
            logger.log('run pipe')
            logger.log(cmd)
            logger.log(out)
            logger.log('ok' if out == 0 else 'err')
            logger.log('duration = '+str(round(duration))+'s')
            logger.log('')
            return name, cmd, out, duration
        return wrapper
    return decorator
'''

def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        name, cmd, out = func(*args, *kwargs)
        duration = time.time() - start
        logger = args[0].logger
        logger.log(name.upper())
        logger.log(cmd)
        logger.log(out)
        logger.log('ok' if out == 0 else 'err')
        logger.log('duration = '+str(round(duration))+'s')
        if len(args) > 3:
            mydict = args[3]
            for k, v in mydict.items():
                logger.log(k + ' = ' + v)
        logger.log('')
        return name, cmd, out
    return wrapper
    
