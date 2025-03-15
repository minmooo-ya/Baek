C = int(input())

for _ in range(C):
    N = list(map(int,input().split()))
    count = N[0]
    score = N[1:]

    avg = sum(score) / count
    above_avg = sum(1 for score in score if score > avg)
    percentage = (above_avg / count) * 100  

    print(f"{percentage:.3f}%")