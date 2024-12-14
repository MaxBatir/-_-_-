# - 1)Фунцкия с параметрами по умолчанию:

def print_params(a = 1, b = "Hello", c = True):
    print(a, b, c)
    print(a,b)
    print(a)
    print()
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# - 2)Распаковка мараметров:

values_list = [33, False, "magnetto"]
values_dict = {"a": "MARAT", "b": True, "c": 65}
print_params(*values_list)
print_params(**values_dict)

# - 3)Распаковка + отдельные параметры:

value_list2 = [777, False]
print_params(*value_list2, 42)
