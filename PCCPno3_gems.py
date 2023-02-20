"""
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
"""
    #해법 1-> 2중 포문이 돌고 O(n2) 형식으로 처리하는 법을 떠올려야 한다.
    #보석을 해싱한다. len(hs) = len(set(gems))일때가 가장 짧은 구간이다.
    #보석 종류의 개수만 알고 있으면 된다.
    #이렇게 하면 정확성은 통과하는데, 10만개면 효율성은 망한다.
    #그러면 어떻게 할 것인가가 포인트.
    #추가적으로 알아야 하는 것. 인덱스 번호에 따라서 0부터 6까지면 6-0+1 = 7이 len이 된다.
"""
        import collections
        def solution(gems):
            answer = [0,0]
            k =len(set(gems)) #이러면 보석의 종류개수를 정확히 안다.
            maxL = 100000
            for i in range(len(gems)): #진열대 1번 -> 인덱스 0번부터 전체 gems의 길이만큼
                sH = collections.defaultdict(int)
                for j in range(i, len(gems)): #진열대 1번부터 다시 돌아서 해싱할 녀석을 찾는다.
                    sH[gems[j]]+=1 #gem의 j번째 녀석의 gem 이름을 key로 하고 거기에 cnt한다.
                    if len(sH) == k:  #해쉬 전체에서 키가 들어온 값이 보석 전체 종류 개수와 같으면 다 들어온것.
                        if j-i+1 < maxL: #거기서 len의 길이가(살 구간의 길이) 가장 짧게 나온녀석이 maxL이 되는 것. 
                            maxL = j-i+1 #바로교체해주고 이녀석이 현재까지 가장 짧은 녀석이다. 
                            answer = [i+1, j+1] #답에 이걸 넣어주고
                        break #멈춘다. 더이상 i부터 찾는 내용 뒷편은 더 긴 길이가 되기때문에 멈추는 것. 
                              #다음 i+1로 넘어간다.

    이렇게 하면 정확성은 통과는 된다. 하지만 효율성은 통과할 수 없다.
    O(n2) -> O(n)으로 해야 해결할 수 있다. 
"""
    ''' 이런 경우 2pointers algorythm으로 해결해야 한다.
        #lt 부터 rt까지 싹쓸이 한다. 
        for rt in range(len(gems)):
            sH[gems[rt]]+=1
            while(len(sH) == 4)

        #여기서 포인터의 모습을 보자면
          lt     rt ->  rt ->  rt -> rt -> rt ->      rt    
        ["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]        
        #rt가 계속 움직인다. 

        #따라서 데이터의 형태를 보자면
        sh["DIA"]+=1 ->
            sh={'DIA':3,'RUBY':2,'EMERALD':1,'SAPPHIRE':1} 
            # 이런식으로 CNT가 올라가면서 sh의 키 값이 4개 일때 만족되고
            # 이때 lt는 0, rt = 6이 된다. 6-0+1 해서 구간은 7개일때. 종료된다.
            # 우리가 찾는것은 while문을 만족하는 가장 짧은 구간이다.
        result = [1,7]
        #이때 lt가 구간을 좁힌다. 
        #여기서 포인터의 모습을 보자면
                 lt                                    rt 
        ["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]      
        sh["DIA"]-=1
            sh={'DIA':2,'RUBY':2,'EMERALD':1,'SAPPHIRE':1} 
            #그래도 만족한다.  그래서 이 구간도 답이 될 수 있다.
        result = [2,7]

                         lt                              rt 
        ["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]      
        sh["RUBY"]-=1
            sh={'DIA':2,'RUBY':1,'EMERALD':1,'SAPPHIRE':1} 
        result = [3,7]

                               lt                        rt 
        ["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]      
        sh["RUBY"]-=1
            sh={'DIA':2,'RUBY':0,'EMERALD':1,'SAPPHIRE':1} 
            #ruby가 counting이 0이면 key를 delete 시켜야 한다.
            #이러면 while문이 참이 아니다. 그래서 답은 동일.
        result = [3,7]
        #이러면 여기서 rt를 증가시킨다. 
                               lt                               rt
        ["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]      
        sh["DIA"]+=1
            sh={'DIA':3,'EMERALD':1,'SAPPHIRE':1} 
            #그래도 3개라 while문이 참이 아니다.
            #그러면 result는 변하지 않는다.
        result = [3,7]
        #포인트는 lt는 키를 줄이면서 오고 rt는 증가시키면서 간다.
        #줄어들면 여기서 바로 멈춰서 끝내버리면 된다.
    '''

""" #무슨 느낌인진 알겠는데, 잘 모르겠다.
    gemCount = len(set(gems))
    gemHash = collections.defaultdict(int)

    for i in range (0,len(gems)):
        gemHash[gems[i]] = 0
        while(len(gemHash) == gemCount):
            gemHash[gems[i]]+= 1        
            print(gemHash)
"""
    '''
    import collections
    def solution(gems):
        answer = [0,0] #구간을 저장하는 애니까 0,0으로 해놓는다.
        sH = collections.defaultdict(int) #int 넣으면 기본적으로 0으로 초기화 된다.
        k = len(set(gems)) #중복을 제외한 보석종류의 가지수
        lt = 0 
        maxL = 100000 #구간 길이의 가장 작은 값을 찾아야 하니까 max값을 잡았따.
        for rt in range(len(gems)): #rt가 0부터 끝까지 도는거다. rt가 증가하면서 해싱하는거다.
            sH[gems[rt]]+=1
            while(len(sH) == k): #rt값이 증가해서 세팅된 경우, lt값을 증가시켜서 구간 내 재확인을 하는거다.
                if rt-lt+1 < maxL: #rt-lt+1 = 구간의 길이 인데 일단 저장을 한번해준다.
                    #cf. 구간의 길이가 작을때만 바꾼다. 같은 상황이 생기면 안바꾼다. 
                    #예를 들어 앞도 구간이 5고 뒤고 5인경우에는 바꾸지 않는다.
                    #인덱스 번호가 작은 쪽을 선택한다고 했다. 진열대 번호가 큰걸로 바꿔야 하는 경우에 같다를 해야한다. 
                    maxL = rt-lt+1 #가장 구간이 큰 값에 현재 값을 저장.
                    answer = [lt+1,rt+1] #answer로 들어가는 내용은 인덱스니까 +1
                sH[gems[lt]]-=1 #이제 lt가 한번씩 움직인다. lt가 움직였으니 그 자리 있던 값은 빼주고
                if sH[gems[lt]] == 0: #그게 0이 되면 아예 삭제를 시켜서 key값을 지운다.
                    del sH[gems[lt]]  #이걸 삭제해야 while문이 조건에 맞춰 멈춘다.
                lt+=1 #그리고 lt는 증가한다. 언제까지? key 값이 전체 보석종류수와 동일할 때까지.
        #for문 안에 while 있는데 이것도 이중for문 아닌가? 조건에 따라 멈춘다는 걸 생각했을 때 n2보다는 무조건 적게 돈다.
        #for문안에 있는 while문은 몇번 도는가? 프로그램이 종료될때까지 총 n번밖에 도는 것이다. n번씩이 아니라. *N이 아니라 +N이다. 
        #실질적으로 lt = 0부터 시작해서 보석의 개수만큼도 안돌게 되어있다. 최적화다.
        #O(N2)이 아니라 O(2N) 이기 때문에 시간복잡도는 O(N)이나 마찬가지다.           
    '''
#최종 풀이 내용
import collections

def solution(gems):
    #return 해줄 answer가 시작 번호와 끝번호를 구하기에 0,0으로 초기화해준다.
    answer = [0,0]
    #먼저 중복을 제거한 보석 전체의 개수를 구한다.
    gemCount = len(set(gems))
    #접근 할때 보석의 이름으로 hash를 잡고, 그것이 몇번 중복되었는지 count할 object를 만든다.
    # defaultdict로 만들면 초기화 값은 0이다.
    gemHash = collections.defaultdict(int)

    #pointer가 2개 돌꺼다. 바깥쪽에 기준 포인터를 잡아준다.
    leftPointer = 0
    #최소 구간을 찾아야 하기때문에 전제 구간의 최대 수를 잡아준다. gems의 최대 배열크기.
    maxRange = 100000
    
    #포인터가 2개 도는 for문을 만들고 while을 통해 조건을 설정한다.
    #오른쪽 포인터가 증가하는 것으로 설정. 범위는 0부터 gems의 max range다.
    for rightPointer in range (len(gems)):
        gemHash[gems[rightPointer]] += 1
        while(len(gemHash) == gemCount):
            buyRange = rightPointer - leftPointer + 1
            if buyRange < maxRange:
                maxRange = buyRange;
                answer = [leftPointer + 1 , rightPointer +1]
            gemHash[gems[leftPointer]] -=1
            if gemHash[gems[leftPointer]] == 0:
                del gemHash[gems[leftPointer]]
            leftPointer += 1
    
    return answer
