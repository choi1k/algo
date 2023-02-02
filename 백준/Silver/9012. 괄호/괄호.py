n = int(input())
flag = True

for _ in range(n):
    s = list(input())
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack == []:
                flag = False
                break
            stack.pop()

    if stack == [] and flag == True:
        print("YES")
    else:
        print("NO")
        flag = True