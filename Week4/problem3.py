# https://www.acmicpc.net/problem/2309

height = [int(input()) for _ in range(9)] # 9명의 난쟁이 키를 입력받음
total = sum(height) # 9명 난쟁이의 전체 키 합을 구함

found = False

for i in range(9):
    for j in range(i + 1, 9):  #  두번의 난쟁이 선택 for 문 루프를 돌림
        # 현재 선택한 두 명의 키를 전체 키 합에서 뺐을 때 그 결과가 100이라면
        # 이 두 명이 가짜 난쟁이이고, 나머지 7명이 진짜 난쟁이
        if total - height[i] - height[j] == 100: 
            # i, j 제외한 7명 출력
            for k in range(9):
                if k != i and k != j:
                    print(height[k])
            found = True
            break
    if found:
        break