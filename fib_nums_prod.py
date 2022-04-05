fib_list = [0, 1]
n = 120
for i in range(1, n):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list.append(fib2)
fib_list_prod = list(map(lambda x, y: x*y, fib_list, fib_list[1:]))


def productFib(prod):
    if prod in fib_list_prod:
        index = fib_list_prod.index(prod)
        return [fib_list[index], fib_list[index+1], True]
    else:
        diff_list = list(map(lambda x, y: x - y, [prod]*len(fib_list_prod), fib_list_prod))
        max_neg_elem = max(diff_list, key=lambda x: x<0)
        index = diff_list.index(max_neg_elem)
        return [fib_list[index], fib_list[index+1], False]
