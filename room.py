input = input("Input:")
input = list(input)
dict = {}
for el in input:
    if el not in dict:
        dict[el] = 1
    else:
        dict[el] += 1
print(dict)
