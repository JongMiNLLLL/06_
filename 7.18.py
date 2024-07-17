# print("hello world")

# 연습문제 구구단 3단을 출력
for i in range(1,10) :
# 3*3=9와같이 나타내기
    number = 3*i
    print("3 *", i , "=" , 3*i)

for i in range(1,10):
    for k in range(11,20) :
        print(i,k)
# 이중 반복문

m = [[1,2,3], [4,5,6], [7,8,9]]
for i in m:
    for k in i:
        print(k)
