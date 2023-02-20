import collections

def solution(gems):
    answer = []
    #정확성과 효율성 테스트 각각 점수가 있다고 함.
    #조건 1. 진열대의 모든 물건을 싹쓸이.
    #단, 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아 구매.
    #진열대는 배열형태 1~8까지. 그 안에 중복이 있음.
    #3,4,6,7,로 구매하면 5번이 빠지기때문에 맞지 않음.
    #이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return하라.
    
    #answer는 시작 진열대 번호, 끝 진열대 번호를 차례대로 배열에 담아서 return 하면 되고
    #만약 가장 짧은 구간이 여러개라면 시작 진열대 번호가 가장 작은 구간을 return한다.
    #배열의 크기는 1이상 10만 이하.
    
    
    
    #풀이 전 과정 생각.
    #1. gems에 모든 종류가 어떤 것들이 있는지 알아내야하고.
    #2. 만들어진 set 내에 모든 count가 0이 아니어야 함. -> 그러면 전 개체가 담김.
    #3. gems의 인덱스 번호를 담아야 하는 것.
    #4. 예시에 따라. 인덱스 번호는 1부터 시작한다.
    gemSetList = list(set(gems))
    board = collections.defaultdict(list)
    map = {};
    print(gemSetList)
    for gem in gems:
        map[gem] += 1
        board.append(map[gem])            
    print(board)
    ## 여기까지 가 한계.
        
    return answer
