
# 10250
times = int(input()) # 반복 횟수
a = 0
b = 0
for i in range(times):
    h, w, n = map(int, input().split()) # 층, 방 갯수, 도착한 순서 
    
    x = n % h # 맨 앞 숫자
    
    if x == 0: # x가 0이면 a에 h값 넣기
        a = h
    else:a = x # 아니면 a에 x값 넣기
    
    y = n // h # 맨 뒤 숫자
    
    if a == h: # a가 h값 과 같다면 b에 y값 넣기
        b = y
    else: b = y+1 # 아니면 y값에 +1 하고 넣기
    
    if b < 10: # b가 10이상이 아니면 앞에 0 붙이기
        print("%d0%d" % (a, b))
    else: print("%d%d"% (a, b))



# 2884
H, M = map(int, input().split()) # 시, 분

if M < 45: # 만약 M이 45보다 작으면 H-1, M + 60 - 45 하기
    M = M + 60 - 45
    if H == 0: # 만약 H가 0이면 H를 24로바꾸기
        H = 24
    H -= 1
else: M = M - 45 # 아니면 M에서 45빼기


print(H, M) # 출력


# 2747
F = [0] * 46 # F에 리스트 만들기
F[1] = 1 # F1을 1로 정하기
n = int(input()) # n번째 숫자 입력
for i in range(2, n+1): # 피보나치 수열 2 부터 n까지 반복하기
     F[i] = F[i-1] + F[i-2]
print(F[n]) # 출력

# 10872
a = 1
N = int(input()) # 팩토리얼 수 입력
for i in range(2, N+1): # 팩토리얼 1 부터 N까지 반복
    a = a * i
print(a)#출력

        
# 1085
x, y, w, h = map(int, input().split())# 현수가 있는곳(x, y), 오른쪽위 꼭짓점(w, h)입력
print(min(w-x, h-y, x, y)) # 이 수들 중에서 최솟값 구해서 출력

# 2523
n = int(input()) # 별찍기 횟수 입력
for i in range(-n+1,n): # 별찍기 -n+1에서 n까지 반복
    print('*' * (n - abs(i))) # n-에서 절댓값 i 를 빼고 별이랑 곱하기