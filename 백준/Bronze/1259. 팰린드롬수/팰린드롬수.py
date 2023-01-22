while True:
    s = input()
    if s == "0":
        break
    
    for i in range(int(len(s) / 2)):
        if s[i] == s[-(i+1)]:
            continue
        else:
            print("no")
            break
    else:
        print("yes")