# 반복문으로 1부터 20까지 합 구하기

# while 문 안에서 브레이크 만나면
# 반복횟수가 끝나지 않았어도 while 문 중단
sum=0
i=1

while i <= 20:
    sum = sum + i
    if sum > 100:
        print('마지막 sum', sum)
        print('마지막 i', i)
        break
    i+=1