MaxChainLength = 1
MaxChainNum = 1

for Number in range(1, 1000000):
    StartingNumber = Number
    ChainLength = 1
    #print(Number)
    while(Number != 1):
        if Number % 2 == 0:
            Number = Number / 2
            ChainLength += 1
        else:
            Number = 3 * Number + 1
            ChainLength += 1

    if ChainLength > MaxChainLength:
        MaxChainLength = ChainLength
        MaxChainNum = StartingNumber

print(MaxChainLength)
print(MaxChainNum)
