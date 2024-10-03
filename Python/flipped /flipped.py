def flippingBits(n):

    flipped = ~n
    
    result = flipped & 0xFFFFFFFF
    
    return result


q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    result = flippingBits(n)
    print(result)
