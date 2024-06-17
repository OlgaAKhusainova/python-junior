my_list = [(2, 2), (6, 13), (55, 3), (4, 8)]
res_list = sorted(my_list, key = lambda c: c[1], reverse=True)
#[lambda x: x[1].sort()]