# A simple program to remove all duplicates in a list/array

list = [10,15,20,16,19,19,10,30,40]
# List with duplicates

def rmDup(duplist):
    noduplist = []
    for i in duplist:
        if i not in noduplist:
            noduplist.append(i)
    return noduplist

print(rmDup(list))
