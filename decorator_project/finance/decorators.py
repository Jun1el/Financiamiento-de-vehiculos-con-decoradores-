import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("userlog.log"),
    logging.StreamHandler()
])
def log_execution(func):
    """Decorador para registrar las ejecuciones."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando {func.__name__}")
        print(f"[LOG] Argumentos: {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Resultado: {result}")
        return result
    return wrapper


def trace_execution(func):
    """Decorador para rastrear parámetros y resultados."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE] {func.__name__} llamado con:")
        print(f" - Args: {args}")
        print(f" - Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"[TRACE] Resultado de {func.__name__}: {result}")
        return result
    return wrapper


def log_user_interaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"User interaction with function '{func.__name__}'")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' completed")
        return result
    return wrapper
