# https://www.acmicpc.net/problem/1541

# 뺄셈을 기준으로 1차적으로 문자열을 분리한다
exp = input().split('-')  

# 첫 번째 덩어리 다 더하고, 덧셈은 다시 +로 분리해서 더해줌
initial = sum(map(int, exp[0].split('+')))  

result = initial  

for part in exp[1:]:  
    # - 뒤에 있는 덩어리들에 대해 반복함

    numbers = map(int, part.split('+'))  
    # +로 나눠서 각각의 숫자로 나눔

    # 덩어리 전체를 한 번에 빼준다.
    result -= sum(numbers)  

print(result)  