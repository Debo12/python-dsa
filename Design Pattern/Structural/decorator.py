import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time-start_time} to execute")
        return result
    return wrapper

@log_execution_time
def cook_recipe(name):
    time.sleep(2)
    print(f"cooked {name}")

cook_recipe('Noodles')