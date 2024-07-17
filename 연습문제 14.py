# 학점 변환기 함수. 점수 구간에 해당하는 학점이 아래아 같이 정의 됭 있다.
# 사용자로 부터 score를 입력 받아 학점으로 환산하여 반환하는 함수를 작성하여라.
def find_score(score):
    result = ""
    if score < 20 :
        result = 'E'
    elif score < 40 :
        result = 'D'
    elif score < 60 :
        result = 'C'
    elif score < 80 :
        result = 'B'
    else :
        result = 'A'

    return result

sc = int(input("점수를 입력하세요.:"))
res = score(sc)
