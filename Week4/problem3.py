# https://www.acmicpc.net/problem/2309

height = [int(input()) for _ in range(9)]
total = sum(height)

found = False

for i in range(9):
    for j in range(i + 1, 9):
        if total - height[i] - height[j] == 100:
            # i, j 제외한 7명 출력
            for k in range(9):
                if k != i and k != j:
                    print(height[k])
            found = True
            break
    if found:
        break