#정수 1개를 입력받아 2배 곱해 출력해보자.

n=int(input())
print(n<<1)

#컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
#2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
#지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

#n = 10
#print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
#print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
#print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
#print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.