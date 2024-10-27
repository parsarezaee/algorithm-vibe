##  return the largest string x such that x divides both str1 and str2.
import math



str1 = "ABCABC"
str2 = "ABC"

if str1 + str2 != str2 + str1:
    print("")
gcd_length = math.gcd(len(str1), len(str2))
print(str1[:gcd_length])