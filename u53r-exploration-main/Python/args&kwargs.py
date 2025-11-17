



#1. args
def sample_function(*args):
    for arg in args:
        print(arg)

sample_function(1, 2, 3, 'hello')
# Output:
# 1
# 2
# 3
# hello







#2. kwargs
def sample_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

sample_function(name='Ramil', age=20)
# Output:
# name = Ramil
# age = 20
