# python 2.7

def merge_the_tools(string, k):
    list_of_letters = list(string)
    for element in split_list(list_of_letters, k):
        print(''.join(element))
 
def split_list(slist,n):
    res = []
    start = 0
    for stop in list(range(len(slist)+n)[n::n]):
        res.append(slist[start:stop])
        start = stop
    res = [remove_duplicates(x) for x in res]
    return res

def remove_duplicates(alist):
    res = []
    for a in alist:
        if a not in res:
            res.append(a)
    return res



if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    