#[?] 무작위 데이터를 순서대로 [오름차순(ASC)|내림차순(DESC)] 정렬 
#선택정렬은 인덱스 번호에 +1 따라 회차다.
#자료구조의 개수 n개에서 n-1만큼 무조건 회차가 돈다.
#cf. 정보처리기사, 선택정렬 알고리즘에서 2회차로 알맞는것은?
#자료 [9,4,5,11,8]

#1회차 [4,9,5,11,8]
#2회차 [4,5,9,11,8]
#3회차 [4,5,8,11,9]
#4회차 [4,5,8,9,11] 5-1번 돌았다.



# 정렬 알고리즘(Sort Algorithm): 가장 [작은|큰] 데이터를 왼쪽으로 순서대로 이동
def main():

    #[1] Input: Data Structure(Array, List, Stack, Queue, Tree, DB, ...)
    #인풋은 자료구조 영역이다.
    data = [ 3, 2, 1, 5, 4 ] # 정렬되지 않은 데이터 
    N = len(data) # 의사코드(슈도코드) 형태로 알고리즘을 표현하기 위함
    # print(data) 

    #[2] Process: Selection Sort(선택 정렬) 알고리즘
    #의사코드 영역 = 알고리즘.
    #for문 2개 if문 하나, + 스왑 알고리즘. 
    for i in range(0, N - 1): # i = 0 to N - 1 마지막은 안돌린다. 왜? n-1이니까.
        for j in range(i + 1, N): # j = i + 1 to N 
            #i랑 비교해야하니까 i를 제외하고라는 뜻이다. 
            if data[i] > data[j]: # 부등호 방향: 오름차순(>), 내림차순(<)
                #스왑 코드의 기본, temp라는거 만들어서 넣었다가 바꾼다.
                #스왑 알고리즘이라고 해도 된다.
                temp = data[i]
                data[i] = data[j]
                data[j] = temp # SWAP
                #temp = data[i]; data[i] = data[j]; data[j] = temp
                #파이썬이지만 세미콜론으로 바꿔줄 수 있다.
        # print(data)

    #[3] Output: UI(Console, Desktop, Web, Mobile, ...)
    #화면송출.
    for i in range(N):
        print(data[i]) # print(data)

if __name__ == "__main__":
    main()
