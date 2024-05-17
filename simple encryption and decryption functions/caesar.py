def encode(str,n):
    result = ''
    for ch in str:
        if (ord(ch) > 64 and ord(ch) < 91) or (ord(ch) > 96 and ord(ch) < 123): # ord -> converts a char to its ascii value.
            result += chr(ord(ch) + n)
        else:
            result += ch
    return result


def decode(str,n):
    result = ''
    for ch in str:
        if (ord(ch) > 64 and ord(ch) < 91) or (ord(ch) > 96 and ord(ch) < 123):
            result += chr(ord(ch) - n)
        else:
            result += ch
    return result


# you can make it user friendly now.