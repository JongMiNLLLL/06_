# 홀수/짝수 판별기 함수, 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수를 작성하시오.
# 반환되는 값은 '홀수' 또는 '짝수'이다.



def onetwo(text) :
    result = ""
    if text % 2 == 0:
        result = "짝수"
    else :
        result = "홀수"
    return result

res = onetwo(153164634321317)
print(res)