import math

def solution(fees, records):
    #문제 설명 주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다. 아래는 하나의 예시를 나타냅니다.  
    #어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
    #00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
    #누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
    #누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
    #초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
    #주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다. 
    #차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
    #제한사항
      #차량번호는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열입니다.
      #내역은 길이 2 또는 3인 문자열로, IN 또는 OUT입니다. IN은 입차를, OUT은 출차를 의미합니다.
      #시각은 차량이 입차되거나 출차된 시각을 나타내며, HH:MM 형식의 길이 5인 문자열입니다.
        #HH:MM은 00:00부터 23:59까지 주어집니다.
        #잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.
      #records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
      #records는 하루 동안의 입/출차된 기록만 담고 있으며, 입차된 차량이 다음날 출차되는 경우는 입력으로 주어지지 않습니다.
      #마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.
      #아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.
        #주차장에 없는 차량이 출차되는 경우
        #주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우
    
    
    #fees [180, 5000, 10, 600]
    #records	['05:34 5961 IN', '06:00 0000 IN', '06:34 0000 OUT', '07:59 5961 OUT', '07:59 0148 IN', '18:59 0000 IN', '19:09 0148 OUT', '22:59 5961 IN', '23:00 5961 OUT']
    
    answer = []
    
    #애초에 차량 번호는 0~9까지 4자리로 된 정수라고 했음.
    #같은 차량번호는 존재하지 않는다고 가정.  
  
    #각 차량번호를 인덱스로 하는 0부터 9999칸짜리 배열 생성 이러면 0000부터 9999까지 차량번호가 생긴것이다.
    #cf. int(0000)은 0이고 int(0001)은 1이다. int()는 앞의 0을 지워주기때문에 반드시 해야한다.
    inTime = [0]*10000
    #cf2. len(inTime)-1 9999 -> lastIndex   
    #들어와 있는지 여부를 체크
    isIn = [0]*10000
    #요금 합산을 체크
    sumT = [0]*10000
    
    #데이터를 정제하는 과정부터 시작. 레코드의 데이터 형태는 '시간 공백 차량번호 공백 들어오고 나가고 구분'이다. 
    for record in records : 
        time, carNo, inOrOut = record.split()
        h, m = time.split(":")
        if inOrOut == "IN":
            inTime[int(carNo)] = int(h)*60 + int(m)
            isIn[int(carNo)] = 1
        else :
            # 요금은 주차 기록이 왔다리 갔다리 하기 때문에 계속 누적 합산해줘야 한다. 
            sumT[int(carNo)] += int(h)*60 + int(m) - inTime[int(carNo)]
            isIn[int(carNo)] = 0
    #나간기록이 없으면 23시 59분에 나간걸로 친다고 했다. 그걸 계산해서 넣어준다.
    for i in range(10000):
        if isIn[i] == 1:
            sumT[i] += (23*60 + 59) -inTime[i]
    #요금계산            
    for j in range(10000):
        if sumT[j] > 0:
            # ceil에 대하여. 기본시간을 계산한 시간은 요금으로 나누었을 때 무조건 올림 처리한다.
            # max에 대하여. 180분이라는 시간보다 적게 머무를 경우 기본요금만 받아야 하기때문에 0처리를 해야한다. 
            carcFee = max(math.ceil((sumT[j] - fees[0])/fees[2]),0)*fees[3] + fees[1]
            answer.append(carcFee)
            
    #1만번 도는게 비효율적이라고 생각하나. 일단은. 데이터의 양을 가늠할 수 없기에 최대한 신속하게 배열로...        
    return answer
