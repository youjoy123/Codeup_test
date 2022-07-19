# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

while True : #While True 문으로 무한루프를 생성한 뒤 if 조건문으로 a가 0일 때만 break 해주도록 만들어줍니다.
    n=int(input())
    if (n==0):
        break
    else :
        print(n)