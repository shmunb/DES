import conversion_lib as con

lst = list(range(1, 65))

result = tuple(lst[con.IP_scheme] for i in range(64))