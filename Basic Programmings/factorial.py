from functools import lru_cache
from datetime import datetime

@lru_cache
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

start = datetime.now()
print(factorial(50))
end = datetime.now()
duration = end - start
print(f"Time taken: {duration.total_seconds():.4f} seconds")