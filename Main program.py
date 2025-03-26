from GetAmmount import GetAmmount, NamesandSubs
import math as m
import random as r


def numclasses(x,y):
    if x == "Fn":
        return(m.ceil(y/22))
    elif x == "Dt":
        return(m.ceil(y/24))
    elif x == "Ad" or x == "Be":
        return(m.ceil(y/28))
    else:
        return(m.ceil(y/32))

csvfile = "Masterv2.csv"
classtypes = {}    
numclass = {}
typeslst = ["10a","10b","10c"]
r.shuffle(typeslst)
counter = 0
peoplelst = NamesandSubs(csvfile)
subjectlst = GetAmmount(csvfile)
peopleandlesson = {}
for x,y in subjectlst.items():
    numclass.update({x:numclasses(x,y)})
for y,x in numclass.items():
    if x != 0:
        placeholderlst = []
        for n in range(x):
            placeholderlst.append(typeslst[counter])
            counter += 1
            if counter == 3:
                counter = 0
        classtypes.update({ y:placeholderlst})

sortedclasstypes = dict(sorted(classtypes.items(), key=lambda item: item[1]))
for classes,types in sortedclasstypes.items():
    x = 0
    n = 0
    for k,y in peoplelst.items():
        for v in y:
            if v == classes:
                current = [peopleandlesson.get(k)]
                current.append([classes,types[x]])
                if current[0] == None:
                    current.pop(0)
                peopleandlesson.update({k:current})
                n = n + 1
                if k == "Fn" and n == 22:
                    n = 0
                    x = 1
                elif k == "Dt" and n == 24:
                    n = 0
                    x = 1
                elif (k == "Ad" or k == "Be") and n == 28:
                    n = 0
                    x = 1
                elif n == 32:
                    n = 0
                    x = 1
            l = list(peopleandlesson.items())
            r.shuffle(l)
            peopleandlesson = dict(l)

                
                    
                    
for c,b in peopleandlesson.items():
    print(c,"    ",b)
                    
            
       
        
