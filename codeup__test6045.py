#정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = map(int, input().split())
d=a+b+c
e=('%.2f'%((a+b+c)/3))
print(d, e)
