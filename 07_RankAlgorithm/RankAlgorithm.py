#[?] 주어진(지정한 범위) 데이터의 순위(등수)를 구하는 로직

# 순위 알고리즘(Rank Algorithm): 점수 데이터에 대한 순위 구하기 
def main():
    #[1] Input
    scores = [ 90, 87, 100, 95, 80 ] # 등수: 3, 4, 1, 2, 5 
    N = len(scores)
    rankings = [1] * N # 모두 1로 초기화
    # [1, 1, 1, 1, 1] 이렇게 뜬다.
    # 1로 초기화 시킨 그릇이 5개라는 소리.
    print(rankings)
    #[2] Process: RANK
    #하나하나 돌아가면서 비교한다. 그래서 2중 for문 사용
    for i in range(N):
    #rankings[i] = 1 # 1등으로 초기화, 순위 배열을 매 회전마다 1등으로 초기화
        #이거 없어도 돌아간다. 이미 초기화 되어있음.
        for j in range(N):
            if scores[i] < scores[j]: # 현재(i)와 나머지들(j) 비교
                rankings[i] += 1 # RANK: 나보다 큰 점수가 나오면 순위 1증가

    #ranking의 핵심은 나보다 큰 수가 나올때마다 점수를 하나씩 증가시킨다는 점에 있다.

    #[3] Output
    for i in range(N):
        print(f"{scores[i]:3}점: {rankings[i]}등")
        #:3으로 출력되는 칸을 3칸으로 줘서 가지런히 정렬.
if __name__ == "__main__":
    main()
