a = set()
b = set()
list_a = []
list_b = []
a_len, b_len = map(int, input().split())

a.update(map(int,input().split()))
b.update(map(int, input().split()))

print(len(a ^ b))