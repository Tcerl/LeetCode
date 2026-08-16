def sum_all(*args):
    return sum(args)

def print_in(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_in(a=1, b=2, c=3, d=4))