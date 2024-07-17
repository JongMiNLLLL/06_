# 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구해라
# 이중 리스트
my_list = [[100,200], [400,800], [1000,1400]]
for list in my_list :
    var = 0
    for l in list :
        var = var + l
        print(l)
        var = var + l
    print()

