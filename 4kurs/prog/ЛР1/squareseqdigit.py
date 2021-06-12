def length(n):
  i = 0
  while n > 0:
    n = n // 10
    i += 1
  return i

def squareSequenceDigit(n):
    b = []
    i = 1
    while i ** 2 <= 100000:
        ch = i ** 2
        k = length(ch)
        j = 0
        for j in range(k):
            if ch > 9:
                k -= 1
                b.append(ch // (10 ** k))
                ch = ch % (10 ** k)
            else:
                b.append(ch % 10)
        i += 1
    result = b[n-1]
    return result
    
    
    
    
if __name__ == "__main__":
    squareSequenceDigit(1)
    squareSequenceDigit(2)
    squareSequenceDigit(7)
    squareSequenceDigit(12)
    squareSequenceDigit(17)
    squareSequenceDigit(27)
    
