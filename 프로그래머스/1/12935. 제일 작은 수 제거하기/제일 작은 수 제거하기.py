def solution(mylist):
    if len(mylist) == 1:
        return [-1]
    mylist.remove(min(mylist))
    return mylist
