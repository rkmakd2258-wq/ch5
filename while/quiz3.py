lis = [100,77,-5,10]
# i가 0부터 3이 될때까지 총 4번 반복수행

i=0
while i<4:
    #77을 만나면 반복문 종료
    if lis[i] == 77:
        i+=1
        break
    print(lis[i])
    i+=1
