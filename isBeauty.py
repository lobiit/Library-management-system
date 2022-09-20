def is_sub_string(a: str, z: str) -> bool:
    i = j = 0
    while i < len(a) and j < len(z):
        if a[i] == z[i]:
            i += 1
        j += 1

    return i == len(a)


print(is_sub_string('ace', 'abcde'))
