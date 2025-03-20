from GetAmmount import GetAmmount
import math as m


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
subjectlst = (GetAmmount("Masterv2.csv"))
for x,y in subjectlst.items():
    numclass.update({x:numclasses(x,y)})

for y,x in numclass.items():
    if x == 3:
        z = x - 3
        numclass.update({y:z})
        classtypes.update({ y:["10a","10b","10c"]})
    elif x > 3:
        z = x - 3
        numclass.update({y:z})
        classtypes.update({ y:["10a","10b","10c"]})



    

    
    
    
        
print(classtypes)
print(numclass) 
        
          
  
  
  
  
  
  
  
  
  
