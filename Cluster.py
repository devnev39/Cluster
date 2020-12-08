import random
import matplotlib.pyplot as plt
import math

REDI = 5
GENERATE = 50
RNGE = 50
TopList = []
class Home:
    def __init__(self,x,y,xy,id):
        self.id = id
        self.x = x
        self.y = y
        self.xy = xy
        self.clustered = False
        self.connected = []
        self.parrent = 0
        
    def __str__(self):
        return f'[{self.x},{self.y}]'

    def FindCluster(self,lst):
        TopList.append(self)
        lst.remove(self)
        for each in lst:
            dist = getDist(each,self)
            if(dist<=REDI):
                if(each.clustered==False):
                    self.connected.append(each)
                    each.clustered = True
                    each.parrent = self
                    TopList.append(each)

        for each in self.connected:
            each.FindCluster(lst)

    def Show(self):
        if(self.parrent):
            plt.plot([self.x,self.parrent.x],[self.y,self.parrent.y],'ro-')
            if(len(self.connected)):
                for each in self.connected:
                    each.Show()
        else:
            for each in self.connected:
                each.Show()                    
        
count = 0
def Clusterize(lst,lstHead,lstPrev):

    for each in lstHead:
        TopList.append(each)
        for a in lst:
            if(a!=each):
                dist = getDist(each,a)
                if(dist<=REDI):
                    each.connected.append(a)
                    a.clustered = True
                    lst.remove(a)
                    TopList.append(a)

            


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

lst_show = lst.copy()
lst[0].FindCluster(lst)
print('Found Cluster..')
plt.plot([a.x for a in lst_show],[a.y for a in lst_show],'go')
#plt.plot([a.x for a in TopList],[a.y for a in TopList],'ro-')
for x in TopList:
    x.Show()
plt.plot(lst_show[0].x,lst_show[0].y,'bo')

plt.show()  

