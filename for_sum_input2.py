n = int(input("수를 입력하세요 : "))
sum = 0
for i in range(n+1):
    sum = sum + i
    print('1부터',n,'까지의 합은',sum)
    print('1부터 {}까지의 합은 {}'.format(n,sum))
    print('1부터 %d까지의 합은 %d'%(n,sum))
    i+=1
    