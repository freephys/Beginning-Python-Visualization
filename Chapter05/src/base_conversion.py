# base conversion helper functions
def oct2dec(s):
    return str(int(s, 8))
def hex2dec(s):
    return str(int(s, 16))
def dec2oct(s):
    return oct(int(s))
def dec2hex(s):
    return hex(int(s))
def hex2oct(s):
    return dec2oct(hex2dec(s))
def oct2hex(s):
    return dec2hex(oct2dec(s))

# support for Python 2.5
def dec2bin(s):
    bin_list, num =[], int(s)
    if num < 0:       # we don't convert negative numbers
        raise ValueError, "value must be positive"
    if not num:   # special case, number is zero
        return '0'
    # regular case
    while num:
        bin_list.append('1' if (num & 1) else '0')
        num >>= 1
    return "".join(reversed(bin_list))

def oct2bin(s):
    return dec2bin(oct2dec(s))
def hex2bin(s):
    return dec2bin(hex2dec(s))
def bin2dec(s):
    return str(int(s, 2))
def bin2hex(s):
    return dec2hex(bin2dec(s))
def bin2oct(s):
    return dec2oct(bin2dec(s))
