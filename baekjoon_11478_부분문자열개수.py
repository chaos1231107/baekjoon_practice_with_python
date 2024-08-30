s = input()
substring = set()
i = 0

while i < len(s):
    for j in range(i+1, len(s)+1):
        str = s[i:j]
        if str not in substring:
            substring.add(str)
    i += 1
print(len(substring))