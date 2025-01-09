def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 7)
print_params(3, 7, "ef")
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'строка',True]
values_dict = {'a' : 2, 'b' : 'слово', 'c' : True}
# print_params(*values_list, **values_dict)
# TypeError: print_params() got multiple values for argument 'a'

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

