def sqfoot(x, y):
    """takes height(ft) and width(ft)  both as int or float of floor and returns square footage"""
    return(x*y)

def circum(radius):
    """takes circle radius and (int or float) and returns circumference"""
    from math import pi
    return(2*radius*pi)





def doMath(string):
    """ Does Basic math in PEMDAS order .  String must have all elements seperated by a space.  ie doMath('2 - 3 * 2 / 2')"""
    s=string.split()
    while len(s) >=3:
        for i in range(0, len(s)):
            if s[i] == "*" or s[i] == "/":
                if s[i] == "*":
                    x = float(s[i-1])*float(s[i+1])
                    if len(s) == 3:
                        s = [str(x)]
                        break
                    elif i == 0:
                        s = [str(x)]+s[i+2:] #[1][+][2][*][3][+][1]
                        break
                    elif i == len(s):
                        s = s[0:i-1]+[str(x)]
                        break
                    else:
                        s = s[0:i-1]+[str(x)]+s[i+2:]
                        break
                if s[i] == "/":
                    x = float(s[i-1])/float(s[i+1])
                    if len(s) == 3:
                        s = [str(x)]
                        break
                    elif i == 0:
                        s = [str(x)]+s[i+2:]
                        break
                    elif i == len(s):
                        s = s[0:i-1]+[str(x)]
                        break
                    else:
                        s = s[0:i-1]+[str(x)]+s[i+2:]
                        break
        for i in range(0, len(s)):
            if s[i] == "+" or s[i] == "-":
                if s[i] == "+":
                    x = float(s[i-1]) + float(s[i+1])
                    if len(s) == 3:
                        s = [str(x)]
                        break
                    elif i == 0:
                        s = [str(x)]+s[i+2:]
                        break
                    elif i == len(s):
                        s = s[0:i-1]+[str(x)]
                        break
                    else:
                        s = s[0:i-1]+[str(x)]+s[i+2:]
                        break
                if s[i] == "-":
                    x = float(s[i-1])-float(s[i+1])
                    if len(s) == 3:
                        s = [str(x)]
                        break
                    elif i == 0:
                        s = [str(x)]+s[i+2:]
                        break
                    elif i == len(s):
                        s = s[0:i-1]+[str(x)]
                        break
                    else:
                        s = s[0:i-1]+[str(x)]+s[i+2:]
                        break
    return(float(s[0]))
