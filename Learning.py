def reverse(x: int) -> int:
        a = 0
        if x>0:
            while x:
                a = 10*a + x%10
                x = x//10
            return a
        elif x<0:
            x = -x
            while x:
                a = 10*a + x%10
                x = x//10
            return -a
        else:
            return a


print(reverse(-123))