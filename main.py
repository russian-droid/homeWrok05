#from www.python-course.eu
#from www.python-course.eu

#Write a function which calculates the position of the n-th occurence
#of a string sub in another string s. If sub doesn't occur in s, -1 shall be returned.

def findnth(s, sub, n): #s=string, sub=element n= n-th occurance (ex: 3rd occurance)
    num = 0
    start = -1
    while num < n:
        start = s.find(sub, start+1)
        if start == -1: 
            break
        num += 1
    
    return start
#
s = "abc xyz abc jkjkjk abc lkjkjlkj abc jlj"
print(findnth(s,"abc", 3))
