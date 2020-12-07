import random
import matplotlib.pyplot as plt
import math

REDI = 3
GENERATE = 50
class Home:
    def __init__(self,x,y,xy,id):
        self.id = id
        self.x = x
        self.y = y
        self.xy = xy
        self.clustered = False
        self.connected = []
        
    def __str__(self):
        return f'[{self.x},{self.y}]'


def Clusterize(lst,head):
    for x in lst:
        if(x!=head):
            gap = getDist(head,x)
            if(gap<REDI):
                if(x.clustered==False):
                    head.connected.append(x)
                    x.clustered = True
    





def getDist(h1,h2):
    return math.sqrt((h2.x-h1.x)**2 + (h2.y-h1.y)**2)

def getXY():
    xy= []
    x = []
    y= []
    lstXY = []
    lstX = []
    lstY = []
    
    for _ in range(GENERATE):
        lstX.append(random.randrange(1,30))
    
    for _ in range(GENERATE):
        lstY.append(random.randrange(1,30))

    for a in range(GENERATE):
        xy.append([lstX[a],lstY[a]])

    [lstXY.append(a) for a in xy if a not in lstXY]

    for a in lstXY:
        x.append(a[0])
        y.append(a[1])

    lstHome = []
    i = 1
    for x in lstXY:
        lstHome.append(Home(x[0],x[1],x,i))
        i+=1

    return lstHome


lst = getXY()

plt.plot(lst[0].x,lst[0].y,'bo')
plt.plot([a.x for a in lst],[a.y for a in lst],'ro')

plt.show()  

