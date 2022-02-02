import time

class tools:
    def __init__(self):
        self.hash_table = dict()
        self.args = None
        self.kwargs = None
        self.hash_key = []


    def updateHashKeyStack(self):
        temp_args = self.args or ''
        temp_kwargs = self.kwargs or ''

        self.hash_key.append(f"{temp_args}{temp_kwargs}")

    
    def updateState(self, **kwargs):
        for key in kwargs:
            print(f"KEY: {key} = {kwargs[key]}")
            setattr(self, key, kwargs[key])


    def updateHashTable(self):
        last_hash_key = self.hash_key[-1]

        if last_hash_key in self.hash_table:
            return "Already Cached in Hash Table"

        self.hash_table[last_hash_key] = self.cached_function(*self.args, **self.kwargs) 
        
        return f"UPDATE: self.hash_table[{last_hash_key}] = {self.hash_table[last_hash_key]}"


    def cacheFunc(self, cached_function):
        self.cached_function = cached_function
        def wrapper(*args, **kwargs):
            self.updateState(args=args, kwargs=kwargs)
            self.updateHashKeyStack()
            print(self.updateHashTable())
            print(args)
            print("**********")

            return self.hash_table[self.hash_key.pop()]

        return wrapper


cached = tools()

@cached.cacheFunc
def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1)+fib(n-2)


start = time.time()

result = fib(int(input("enter: ")))
print(result)
print(f"time: {time.time() - start}")

