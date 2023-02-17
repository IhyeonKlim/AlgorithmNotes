
import collections

def solution(id_list, report, k):
  #입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.
  #각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
  #신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
  #한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
  #k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
  #유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
  #다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

  #제한사항
    #2 ≤ id_list의 길이 ≤ 1,000
    #1 ≤ id_list의 원소 길이 ≤ 10
    #id_list의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
    #id_list에는 같은 아이디가 중복해서 들어있지 않습니다.
    #1 ≤ report의 길이 ≤ 200,000
    #3 ≤ report의 원소 길이 ≤ 21
    #report의 원소는 "이용자id 신고한id"형태의 문자열입니다.
    #예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
    #id는 알파벳 소문자로만 이루어져 있습니다.
    #이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
    #자기 자신을 신고하는 경우는 없습니다.
    #1 ≤ k ≤ 200, k는 자연수입니다.
    #return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

    answer = []
    #report에 들어온 데이터가 중복되므로 set으로 리스트를 만들어준다.
    report = list(set(report))

    #신고한 유저에게 정지 사실을 메일로 발송해야한다. 그러면 신고한 유저가 누굴 신고했는지 담을 곳이 필요하다. 
    #데이터를 담을 2개의 딕셔너리를 만든다. key value를 통해 꺼낼 수 있도록.
    #hash ->key + value 탐색에 검색속도를 O(1)을 제공한다.
    
    #set 구조니까 set으로 만든다. 
    report_hashset = collections.defaultdict(set)

    #신고당한 사람은 k번 이상 신고 당할시 정지되어야 한다. 
    #int 구조니까 int로 만든다.
    baned_count = collections.defaultdict(int)
    
    #먼저 리포트를 정리한다. 나의 아이디 : {신고한 유저1, 유저2} 가 될것이다. 
    for x in report:
        reporter, banedUser = x.split(" ")
        report_hashset[reporter].add(banedUser)
        #신고 당한사람은 몇회 신고 당했는지 누적시킨다.
        baned_count[banedUser]+=1

    #전체 아이디리스트에서 각 id별로 메일을 몇통 받는지 센다.
    for name in id_list:
        mail=0
        #각 아이디 별로 신고한 사람 찾기 내가 신고한 유저가 몇번 신고받았는지 체크.
        for user in report_hashset[name]:
            #신고당한 녀석의 id로 조회해서 누적횟수가 k보다 많은지 조회
            if baned_count[user] >=k:
                mail+=1
        answer.append(mail)    
    return answer
