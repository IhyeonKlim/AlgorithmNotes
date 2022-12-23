# n명의 점수 중에서 80점 이상인 점수의 합계.

# 합계 알고리즘은 주어진 범위에 주어진 조건에 해당하는 자료들의 합계.

#다음 3개를 준비하고 시작하는 버릇.

#[?]
#[1] Input :
#[2] Process:
#[3] outPut :


#[1] Input : n명의 점수
scores = [100, 75, 50, 37, 90, 95]
sum = 0 #합계가 저장될 그릇이다.

N = len(scores) #의사코드(슈도 코드?)

#[2] Process: 합계 알고리즘 sumAlgorithm 영역 : 주어진 범위에 주어진 조건(필터링)을 따져야 한다.
for i in range(0, N): # 주어진 범위
    if scores[i] >= 80: #주어진 조건
        sum = sum + scores[i] #Sum


#[3] outPut :

print(f"{N}명의 점수 중 80점 이상의 합계: {sum}")

#vsCode 디버깅 연습 f9 f5 f11 f5

# [?] 1부터 20까지 정수 중 홀수의 합을 구하는 프로그램

#등차수열 : arithmetic sequence : 연속으로 두 수의 차이가 일정한 수열

#[1] input
sum =0

#[2] process

for i in range(1,20): #주어진 범위
    if i % 2 != 0: #주어진 조건 : 필터링
        sum = sum + i
        print(i, end=',')
#        print(i, end='\t') 탭으로 띄움.

#[3] output
print(f'\n1부터 20까지의 홀수의 합 : {sum}')


#[?] 1부터 1,000까지의 정수 중 13의 배수의 개수 (건수, 개수)
# 개수 알고리즘 (count algorithm) : 주어진 범위에 주어진 조건에 해당하는 자료들의 개수

#[1] Input :
count = 0 #개수를 저장할 변수는 0으로 초기화
#[2] Process: 개수 알고리즘 영역 : 주어진 범위에 주어진 조건(필터링)
for i in range(1,1000): #주어진 범위
    if i % 13 == 0: #주어진 조건 : 13의 배수면 개수 증가
        count += 1 #COUNT
#[3] outPut :
print(f'1부터 1,000까지의 정수 중 13의 배수의 개수 : {count}')


#[?]
# 평균 알고리즘 (average algorithm : 주어진 범위에 주어진 조건에 해당하는 자료들의 평균

#[1] Input :
data = [90, 65, 79, 50, 96]
sum =0
count =0
N = len(data) #의사코드(슈도코드)


#[2] Process : AVG = sum / count

for i in range(0,N):
    if data[i] >= 80 and data[i] <= 95:
        sum += data[i] # sum
        count += 1 #count
avg = 0
if sum != 0 or count !=0:
    avg = sum / count

#[3] outPut :

print(f'80점 이상 95점 이하인 자료의 평균 : {avg:.2f}')

import sys
#[?] 주어진 데이터 중에서 가장 큰 값
#최댓값 알고리즘 주어진 범위, 조건의 자료들 중 가장 큰 값.
def main():
#[0] init : 초기화 영역
    max = -sys.maxsize -1 #숫자형식의 데이터 중 가장 작은 수로 초기화.
#[1] Input :
    numbers = [-2, -5, -3, -7, -1] #MAX : -1
    N = len(numbers)
#[2] Process:
    for i in range(0,N):
        if numbers[i] > max:
            max = numbers[i] # MAX

#[3] outPut :
    print(f'최댓값 : {max}')

if __name__ == "__main__":
    main()