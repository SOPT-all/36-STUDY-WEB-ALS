# 백준 11729_하노이 탑 이동 순서
# 재귀 알고리즘을 활용한 하노이 타워 문제 해결 방법
# 원판 n개를 A에서 C로 옮기는 과정에서 B를 보조 기둥으로 활용

n = int(input())

def hanoi(n, start, mid, end):
    # 종료 조건: 원판이 1개일 때는 바로 옮기면 됨
    if n == 1:
        print(start, end)
        return
    
    # 1. n-1개의 원판을 start에서 mid로 이동 (end를 보조로 사용)
    hanoi(n-1, start, end, mid)
    
    # 2. 가장 큰 원판을 start에서 end로 이동
    print(start, end)
    
    # 3. n-1개의 원판을 mid에서 end로 이동 (start를 보조로 사용)
    hanoi(n-1, mid, start, end)

# 이동 횟수 출력
print(2**n - 1)

# 하노이 타워 이동 과정 출력
hanoi(n, 1, 2, 3)