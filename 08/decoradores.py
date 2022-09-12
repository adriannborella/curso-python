import time


def time_it(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took: {(end-start)*1000} mil sec")
        return result

    return wrapper


@time_it
def calc_square(num):
    result = []
    for num in num:
        result.append(num * num)
    return result


@time_it
def calc_cude(num):
    result = []
    for num in num:
        result.append(num * num * num)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_square = calc_cude(array)
