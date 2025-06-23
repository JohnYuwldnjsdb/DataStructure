N = int(input())
a = []

for i in range(N):
    b = input()
    a.append(b)

for i in range(len(a[0])):
    c = a[0][i]
    f = True
    for j in range(1, len(a)):
        if a[j][i] != c:
            print("?",end="")
            f = False
            break
    if f:
        print(c, end="")