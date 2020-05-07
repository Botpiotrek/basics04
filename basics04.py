def brr(list_b):
    print(list_b)
    global list_a
    list_a = [1, 2, 3, 4, 5, 6, 7]


list_a = [1, 2, 3, 4, 5, 6, 7]
list_a = list_a[::2]
brr(list_a)
list_a = list_a[1::2]
brr(list_a)
list_a.reverse()
brr(list_a)
list_a = list_a[-2::-2]
brr(list_a)
list_a = list_a[0::6]
brr(list_a)
list_a = list_a[-1::-3]
brr(list_a)
list_a = []
brr(list_a)
list_a = list_a[4:7]
brr(list_a)


"""
[1, 3, 5, 7]
[2, 4, 6]
[7, 6, 5, 4, 3, 2, 1]
[6, 4, 2]
[1, 7]
[7, 4, 1]
[] # pusta lista
[5, 6, 7]
"""