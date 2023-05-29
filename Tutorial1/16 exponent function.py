# exponent e.g. 2 ^ 3 = (2 to the power of 3)
print(2**3)
print(4**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(abs(pow_num)):
        result = result * base_num
    if pow_num >= 0:
        return result
    else:
        return 1/result

print(raise_to_power(5, 2))
print(raise_to_power(-5, 3))
print(raise_to_power(5, 0))
print(raise_to_power(5, -2))
