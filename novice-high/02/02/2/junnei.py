# 변수 선언 및 입력
n = int(input())

# 동적 배열 선언
v = list()

for _ in range(n):
    command = input()

    if command.startswith("push_back"):
        _, num = tuple(command.split())
        v.append(int(num))
    elif command.startswith("pop_back"):
        v.pop()
    elif command.startswith("size"):
        print(len(v))
    else:
        _, index = tuple(command.split())
        print(v[int(index) - 1])