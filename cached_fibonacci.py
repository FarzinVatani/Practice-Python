import time


class Tools:
    def __init__(self):
        self.hash_table = dict()
        self.args = None
        self.kwargs = None
        self.hash_key = []
        self.log_stack = []

    def appendLogStack(self, log):
        self.log_stack.append(log)
        return self

    def appendHashKeyStack(self):
        temp_args = self.args or ""
        temp_kwargs = self.kwargs or ""

        self.hash_key.append(f"{temp_args}{temp_kwargs}")
        return self

    def updateState(self, **kwargs):
        for key in kwargs:
            self.appendLogStack(f"KEY: {key} = {kwargs[key]}")
            setattr(self, key, kwargs[key])

        return self

    def updateHashTable(self):
        last_hash_key = self.hash_key[-1]

        if last_hash_key in self.hash_table:
            self.appendLogStack("Already Cached in Hash Table")
            return self

        self.hash_table[last_hash_key] = self.cached_function(
            *self.args, **self.kwargs)
        log = f"""
        UPDATE:
            self.hash_table[{last_hash_key}] = {self.hash_table[last_hash_key]}
        """
        self.appendLogStack(log)
        return self

    def cacheFunc(self, cached_function):
        self.cached_function = cached_function

        def wrapper(*args, **kwargs):
            self.updateState(
                args=args,
                kwargs=kwargs).appendHashKeyStack().updateHashTable()

            return self.hash_table[self.hash_key.pop()]

        return wrapper



@Tools().cacheFunc
def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start = time.time()

    result = fib(int(input("enter: ")))
    print(result)
    print(f"time: {time.time() - start}")
