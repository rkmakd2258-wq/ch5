# 반복문으로 "hello"를 5번 출력
i=0

while i<5:
    print('hello')
    i+=1

# 반복문으로 숫자 1부터 7까지 출력

i=1

while i<8:
    print(i)
    i+=1

# 반복문으로 1 3 5 7 9 홀수 5개를 출력

i=0

while i<5:
    print(i*2+1)
    i+=1

# 반복문을 사용해서 11부터 20까지 출력하세요

i=11

while i<21:
    print(i)
    i+=1

# 반복문을 사용해서 1부터 5까지 합을 구하세요

i=1
sum=0 #합을 저장할 변수

while i<6:
    # 더하는 수는 1부터 5까지 증가하는 수
    sum=sum+i
    i+=1
print('합계:', sum)



#1+2+3+4+5
#변수=더하는코드
#누적:자기자신+더하는 수
sum=0
sum=sum+1
sum=sum+2
sum=sum+3
sum=sum+4




# 반복문으로 리스트의 요소를 하나씩 출력하세요

nums = [10,20,30]

i=0

while i<3:
    print(nums[i])
    i+=1


# 1부터 20까지 더한 합 구하기
i=1
sum=0

while i<= 20:
    if sum>100:
        break
    sum=sum+i
    i+=1
print(sum)


#반복문으로 요소를 하나씩 출력하다가 77을 만나면 break를 사용해 반복문을 종료하세요

lis=[100,77,-5,10]

i=0
while i<4:
    if lis[i] == 77:
        break
    print(lis[i])
    i+=1


# 1부터 10까지 하나씩 출력하다가
# 3의 배수를 만나면 break를 사용해 반복문을 종료하세요

i=1

while i<11:
    if i%3 == 0:
        break
    print(i)
    i+=1


lis= ['aa', 'bbb', 'ccccc', 'dd']

# 반복문으로 요소를 하나씩 출력하다가 
# 문자열의 길이가 4를 넘으면 반복문을 종료하세요

i=0

while i<4:
    if len(lis[i]) > 4:
        break
    print(lis[i])
    i+=1


# 반복문으로 1부터 10까지 출력
# 짝수 건너뛰고 홀수만 출력

i=1

while i<11:
    if i%2 == 0:
        i+=1
        continue
    print(i)
    i+=1


# 리스트 생성
lis = [10,'a', True, 20, 'b']

# while문으로 리스트의 요소를 하나씩 출력하세요
# 단, 숫자를 만나면 continue를 사용해 건너뛰세요

print(type(10))
print(type('a'))
print(type(True))

i=0
while i<5:
    if type(lis[i]) == int: #타입 == int
        i+=1
        continue
    print(lis[i])
    i+=1


