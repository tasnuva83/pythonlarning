def reverse_half(st):
    st1 = st[5::-1]
    st2 = st[6:]
    halfreverse = st1 + st2
    print(halfreverse)
    return halfreverse
reverse_half('bangladesh')