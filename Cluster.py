import random
import matplotlib.pyplot as plt
import math

REDI = 10.00
GENERATE = 60
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
def Clusterize(lst):
    index = 0
    while(index!=(len(lst)-1)):
        head = lst[index]
        head.connected.append(head)
        for x in lst:
            if(x!=head):
                dist = getDist(head,x)
                if(dist<=REDI or dist<=(REDI+0.2)):
                    head.connected.append(x)
        index += 1
    headcount = 0
    
    lst.sort(key=lambda x: len(x.connected))
    
    head = lst[len(lst)-1]  
    print(f'selected : {len(head.connected)}')          
   #plt.plot([a.x for a in head.connected],[a.y for a in head.connected],'bo-')
    figure , axes = plt.subplots()
    per = plt.Circle((head.x,head.y),REDI,fill=False)
    axes.set_aspect(1)
    axes.add_artist(per)
    return head.connected



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
head = Clusterize(lst)
plt.plot(lst[0].x,lst[0].y,'bo')
plt.plot([a.x for a in lst],[a.y for a in lst],'ro')

prev = head[0]
for each in head:
    if(each==prev):
        plt.plot(prev.x,prev.y,'bo-')
        continue
    plt.plot([prev.x,each.x],[prev.y,each.y],'b--')
    prev = each        

plt.show()  

