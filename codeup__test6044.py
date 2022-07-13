#정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.

a, b=input().split()
a=int(a)
b=int(b)
#a,b=map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print('%.2f'%(a/b))

