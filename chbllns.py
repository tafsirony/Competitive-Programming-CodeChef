for i in range(int(input())):
    r, g, b = [int(x) for x in input().split()]
    k = int(input())
    ans = 0

    if k == 1:
        print(1)
        continue
    print(min(r, k - 1) + min(g, k - 1) + min(b, k - 1) + 1)
        
