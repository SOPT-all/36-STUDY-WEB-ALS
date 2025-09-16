# 백준 15649_N과 M (1)
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고르는 순열 문제
# visited 배열로 사용한 숫자를 체크하고, 백트래킹으로 모든 경우의 수 탐색
# 길이가 M이 되면 출력하고, 재귀 호출 후 visited 상태를 원상복구 !!

N, M = map(int, input().split())
visited = [False] * (N + 1)  # 1부터 N까지 사용 여부 체크
path = []  # 현재까지 선택한 수열

def backtrack():
    # 길이가 M이 되면 출력
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    # 1부터 N까지 모든 수를 시도
    for i in range(1, N + 1):
        if not visited[i]:  # 아직 사용하지 않은 수라면
            visited[i] = True  # 사용 표시
            path.append(i)     # 경로에 추가
            backtrack()        # 다음 선택으로 재귀
            path.pop()         # 백트래킹: 선택 취소
            visited[i] = False # 백트래킹: 사용 표시 취소

backtrack()