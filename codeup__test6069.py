# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

a = str(input())

if a is str('A'):
    print('best!!!')
elif a is str('B') :
    print('good!!')
elif a is str('C'):
    print('run!')
elif a is str('D'):
    print('slowly~')
else :
    print('what?')