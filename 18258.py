import sys
input = sys.stdin.readline

N = int(input())

qu = []

for i in range(N):
    state = input().rstrip()

    if state == "pop":
        if qu == []:
            print('-1')
        else:
            print(qu[0])
            qu.remove(qu[0])
    elif state == "size":
        print(len(qu))

    elif state == "empty":
        if qu == []:
            print("1")
        else:
            print("0")

    elif state == "front":
        if qu == []:
            print("-1")
        else:
            print(qu[0])

    elif state == "back":
        if qu == []:
            print("-1")
        else:
            print(qu[-1])

    else:
        temp = list(state.split())
        qu.append(temp[1])