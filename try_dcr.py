from app.agent_logger import AgentLogger

def log(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            logger.log(value)
            return value
        return wrapper
    return decorator
 
logger = AgentLogger() 
@log(logger = logger)
def hello():
    return 'hello'
    

hello()
