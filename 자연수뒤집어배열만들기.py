#오답
def solution(n):
    answer = []
    reversedArr = []
    n = str(n)
    for i in n:
        reversedArr.append(i)
    print(reversedArr)
    
    for i in range(len(reversedArr),0,-1):
        answer.append(i)
    return answer
  
#what the..?
def solution2(n):
  answer = list(map(int, reverse(str(n))))
  return answer


#what the 2
def solution3(n):
  n = str(n)
  answer = []
  
  for i in range(1, len(n)+1:
      a = int(n[-i])
      answer.append(a)
  return answer
#what the 3
   for i in n :
       answer.appned(int(i))
    answer = answer[::-1]
    return answer
