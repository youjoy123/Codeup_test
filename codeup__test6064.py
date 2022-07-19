# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = int(a if(a<b) else b)
e = int(d if(d<c) else c)
print(int(e))