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

classtypes = {}    
numclass = {}
typeslst = ["10a","10b","10c"]
r.shuffle(typeslst)
counter = 0
peoplelst = NamesandSubs("Masterv2.csv")
subjectlst = GetAmmount("Masterv2.csv")
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


for classes,types in classtypes.items():
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
                    
                    
for c,b in peopleandlesson.items():
    print(c,"    ",b)
                    
            
       
        
