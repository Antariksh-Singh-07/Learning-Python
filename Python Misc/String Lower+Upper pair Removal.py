"""Input: s = 'leEeetcode'
Output: 'leetcode'
Explanation: In the first step, either you choose i = 1 or i = 2, both will result 'leEeetcode' to be reduced to 'leetcode' """
a = 1
def GoodString(dhaga):
    global a
    lst,i = [i for i in dhaga],0
    indices = []
    if len(lst)<2:
        strg = dhaga
    else:
        try:
            while i<len(lst):
                if lst[i].lower() == lst[i+1].lower():
                    if (lst[i].islower() and lst[i+1].isupper()) or (lst[i+1].islower() and lst[i].isupper()):
                       lst.pop(i)
                       lst.pop(i)
                       continue
                i+=1
        except IndexError:
            pass
        strg = "".join(lst)
    if a == 1:
        a+=1
        print(GoodString(strg))
    return strg
dhaga = "LeEetcodeEeeEEE"
GoodString(dhaga)