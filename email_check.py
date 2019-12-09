import re
regex =  re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")
def fun(s):
    if(re.match(regex,s)):
        return True
    else:
        return False 