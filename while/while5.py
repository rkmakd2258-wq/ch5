# 반복문으로 1부터 10까지 출력하기
# 단, 숫자가 짝수일때만 출력하기

# while문 안에서 continue를 만나면 더이상 아래 코드를 실행하지 않고 다시 반복문으로 돌아간다

i = 1
while i < 11:
    if i%2 == 1:
        i+=1
        continue 
    print(i)
    i += 1