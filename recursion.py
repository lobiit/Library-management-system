i = 1
for i in range(0, 10):
    i += 1
    print(i)


def fn(a):
    if a > 20:
        return
    print(a)
    fn(a + 1)
    print(f"End of call where a = {a}")
    return

fn(1)
