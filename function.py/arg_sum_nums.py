def sum_num(*args):
    result = 0
    for n in args:
        result += n
    return result
print(sum_num(10,20,30))
print(sum_num(10,20,30,40,50))