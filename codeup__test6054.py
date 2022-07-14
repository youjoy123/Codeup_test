# 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력

a, b=map(int, input().split())
if (bool(a) and bool(b)) :
    print('True')
else :
    print('False')