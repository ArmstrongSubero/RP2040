print("Average of 10 numbers")
sum = 0

for n in range(10):
    print("Enter number", n + 1, ":", end='')
    m = float(input())
    sum = sum + m

average = sum / 10
print("Average= ", average)
