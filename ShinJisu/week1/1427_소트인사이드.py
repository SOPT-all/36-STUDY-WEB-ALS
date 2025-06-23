# 백준 1427_소트인사이드
# 입력받은 숫자를 문자열로 처리하여 각 자릿수를 리스트의 요소로 변환
# sort() 메서드에 reverse=True 매개변수를 사용하여 내림차순 정렬
# 내림차순 정렬된 자릿수들을 다시 join() 메서드로 하나의 문자열로 결합
# 문자열로 된 숫자들도 비교 시 사전순으로 처리되므로, 숫자 크기에 따라 올바르게 정렬됨 !

n = input()

# 각 자리수를 리스트로 변환함
digits = list(n)

# 내림차순 정렬
# reverse=True 옵션으로 내림차순 정렬함
digits.sort(reverse=True)

# 정렬된 자리수들을 다시 하나의 문자열로 합침
result = ''.join(digits)

print(result)