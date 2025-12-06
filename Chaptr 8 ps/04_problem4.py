def sum(n):
    if(n==1 or n==0):
        return 1
    return n + sum(n-1)

num = int(input("Enter the number : "))
ans = sum(num)
print(ans)