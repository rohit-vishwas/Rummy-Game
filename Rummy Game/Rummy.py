import pygame, sys, random
from pygame.locals import *
from random import *
import math
import bisect
class Character:
    def __init__(self,img,name):
        self.img = img
        self.click = False
        self.name= name
card=[]
joker=[]
def formDeck():
    global number, suit, card
    for i in number:
        for j in suit:
            card+=[j+i]
    card*=2
    for m in range(4):
        card+=["Joker"]
    return card
suit=["C","D","H","S"]
end=0
number=["1","2","3","4","5","6","7","8","9","9X","J","Q","R"]

def makeList(l):
    a=[]
    for k in range(len(l)):
        a+=[l[k].name]
    return a
def sortcards(l):
    global joker
    u= makeList(l)
    u.sort()
    ma=[[] for j in range(5)]
    print(u)    
    for i in range(len(u)):
        if u[i] not in joker:
            if u[i][0] =="S":
                eat= add([u[i]],ma[3])
                ma[3]= eat
            if u[i][0] =="H":
                eat= add([u[i]],ma[2])
                ma[2]= eat
            if u[i][0] =="D":
                eat= add([u[i]],ma[1])
                ma[1]= eat
            if u[i][0] =="C":
                eat= add([u[i]],ma[0])
                ma[0]= eat
        else:
                eat= add([u[i]],ma[4])
                ma[4]= eat
    return ma
di={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"9X":10,"oker":0,"Q":12,"J":11,"R":13}
deck=[]
d={"C":0,"D":1,"H":2,"S":3}
def checkSequence(l):
    y=[]
    i=-1
    while(i<4):
        i+=1
        lis=l[i]
        le=len(lis)
        co=1
        q=[0]
        j= -1
        while (j< (le-2)):
            j+=1
            if di[lis[j][1:]] != di[lis[j+1][1:]]-1:
                q.append(co)
                co=1
                co +=1
            else:
                co +=1
        q.append(co)
        y.append(max(q))
    return max(y),y
deck=[]
def add(a,b):
    return a+b
def TakeCard(l,faceup,facedown):
    global joker,d
    if faceup in joker:
        pygame.draw.rect(DISPLAYSURF,(0,255,0),(870,270,90,180),4)
        l[-1].append(faceup)
        pygame.time.delay(100)
        return 
    else:
        x=l[d[faceup[0]]]
        ind=bisect.bisect(x,faceup)
        if ind!=len(x) and ind != 0 and faceup not in x:
            if di[faceup[1:]]-di[x[ind-1][1:]]==1 or di[x[ind][1:]]-di[faceup[1:]]==1:
                pygame.draw.rect(DISPLAYSURF,(0,255,0),(870,270,90,180),4)
                l[faceupos].insert(ind,faceup)
                pygame.time.delay(100)
                del showcard[0]                
            else:
                pygame.draw.rect(DISPLAYSURF,(0,255,0),(870,270,90,180),4)
                facedownsuit=facedown[0]
                facedownpos=d[facedownsuit]
                bisect.insort(l[facedownpos],facedown)
                pygame.time.delay(100)
                del hidecard[0]
        else:
            if facedown not in joker:
                pygame.draw.rect(DISPLAYSURF,(0,255,0),(870,270,90,180),4)
                facedownsuit=facedown[0]
                facedownpos=d[facedownsuit]
                bisect.insort(l[facedownpos],facedown)
                del hidecard[0]
                pygame.time.delay(100)
            else:
                pygame.draw.rect(DISPLAYSURF,(0,255,0),(870,270,90,180),4)
                l[-1].append(facedown)
                pygame.time.delay(100)
card= formDeck()
jokervalue=card[-5]
for k in range(5):
    shuffle(card)
for k in range (len(card)):
    hide= Character(pygame.image.load(card[k]+".png"),card[k])
    hide.img= pygame.transform.scale(hide.img,(90,180))
    deck += [hide]

del card[-5]
joker=["Joker","Joker","Joker"]
if jokervalue !="Joker":
    joker+=[i+jokervalue[1:] for i in suit]*2 + ["Joker"]
joker.remove(jokervalue)

def ThrowCard(l):
    for i in range(len(suit)):
        c,x=[], l[i]
        if x==[]:
            continue
        rk=0
        for j in range(len(x)-1):
            ap= di[x[j+1][1:]]
            bj= di[x[j][1:]]
            c.append(ap - bj)
        y=0
        if c.count(0)!=0:
            indo=c.index(0)
            return (l[i].pop(indo))
        
        elif c==[]:
            return (l[i].pop(0))
        else:
            maxc=max(c)
            for y in range(4):
                y=y+1
            if maxc>2:
                indmax=([math.inf]+c+[math.inf]).index(maxc)
                if c[indmax-1]>c[indmax+1]:
                    abn=l[i][(indmax-1)]
                    del l[i][indmx-1]
                    return (abn)
                else:
                    abn=l[i][(indmax)]
                    del l[i][indmx]
                    return (abn)
def checkfirstlife(l):
    m,n=checkSequence(l)
    if m>=3:
        return True,m,n
    return False,m,n
AI_pic= Character(pygame.image.load(r"AIpic.png"),"AIpic")
AI_pic.img= pygame.transform.scale(AI_pic.img,(120,150))
jokerpic= Character(pygame.image.load(jokervalue+".png"),jokervalue)
jokerpic.img= pygame.transform.scale(jokerpic.img,(90,180))
show= Character(pygame.image.load(r"show.png"),"show")
show.img= pygame.transform.scale(show.img,(60,40))
def checksecondlife(l):
    x,y,z=checkfirstlife(l)
    t=[]
    z1=z.copy()
    z1.sort()
    r=z1[len(z1)-2]
    if x==True:
        if (y>=7 or (y>=4 and r>=3) or (y==3 and r>=4)) or (((y==6) or (y>=4 and r==2) or (y==3 and r==3)) and len(l[-1])!=0):
            return True
        lenl1=len(l[-1])
        if lenl1!=[]:
            if y>=4 and r==1:
                for i in range (4):
                    if i==z.index(4):
                        return False
                    for j in range (len(l[i])-1):
                        ap= di[l[i][j+1][1:]]
                        bj= di[l[i][j][1:]]
                        if ap-bj == 2:
                            return True
        return False
    return False

cardImg= deck[ : 13]
AI= deck[13:26]
hidecard = deck[26:]
AI=sortcards(AI)
print(AI)
pygame.init()
DISPLAYSURF=pygame.display.set_mode((1430,800))
pygame.display.set_caption("Indian Rummy")
showcard= [deck[0]]
backcard= Character(pygame.image.load(r"backcard.jpg"),"backcard")
backcard.img= pygame.transform.scale(backcard.img,(150,180))
pos=[(20,600),(120,600),(220,600),(320,600),(420,600),(520,600),(620,600),(720,600),(820,600),(920,600),(1020,600),(1120,600),(1220,600),(1320,600)]
pol1=[(20,100),(120,100),(220,100),(320,100),(420,100),(520,100),(620,100),(720,100),(820,100),(920,100),(1020,100),(1120,100),(1220,100),(1320,100)]
pol=pos.copy()
rohit= True
while rohit:
    if len(showcard)>0:
        DISPLAYSURF.blit(showcard[0].img,(870,270))
    DISPLAYSURF.blit(backcard.img,(550,250))
    DISPLAYSURF.blit(AI_pic.img,(700,0))
    DISPLAYSURF.blit(jokerpic.img,(50,250))
    DISPLAYSURF.blit(show.img,(1200,350))
    for event in pygame.event.get():
        if event.type  == pygame.MOUSEBUTTONDOWN:
            if len(cardImg)==13 and showcard[0].img.get_rect(topleft=(870,270)).collidepoint(event.pos):
                cardImg=cardImg+[showcard[0]]
                del (showcard[0])
            elif len(cardImg)==13 and backcard.img.get_rect(topleft=(550,250)).collidepoint(event.pos):
                cardImg=cardImg+[hidecard[0]]
                del (hidecard[0])
            if show.img.get_rect(topleft=(1200,350)).collidepoint(event.pos):
                rohit= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cardImg[0].img.get_rect(topleft=pol[0]).collidepoint(event.pos):
                cardImg[0].click=True
            elif cardImg[1].img.get_rect(topleft=pol[1]).collidepoint(event.pos):
                cardImg[1].click=True
            elif cardImg[2].img.get_rect(topleft=pol[2]).collidepoint(event.pos):
                cardImg[2].click=True
            elif cardImg[3].img.get_rect(topleft=pol[3]).collidepoint(event.pos):
                cardImg[3].click=True
            elif cardImg[4].img.get_rect(topleft=pol[4]).collidepoint(event.pos):
                cardImg[4].click=True
            elif cardImg[5].img.get_rect(topleft=pol[5]).collidepoint(event.pos):
                cardImg[5].click=True
            elif cardImg[6].img.get_rect(topleft=pol[6]).collidepoint(event.pos):
                cardImg[6].click=True
            elif cardImg[7].img.get_rect(topleft=pol[7]).collidepoint(event.pos):
                cardImg[7].click=True
            elif cardImg[8].img.get_rect(topleft=pol[8]).collidepoint(event.pos):
                cardImg[8].click=True
            elif cardImg[9].img.get_rect(topleft=pol[9]).collidepoint(event.pos):
                cardImg[9].click=True
            elif cardImg[10].img.get_rect(topleft=pol[10]).collidepoint(event.pos):
                cardImg[10].click=True
            elif cardImg[11].img.get_rect(topleft=pol[11]).collidepoint(event.pos):
                cardImg[11].click=True
            elif cardImg[12].img.get_rect(topleft=pol[12]).collidepoint(event.pos):
                cardImg[12].click=True
            elif len(cardImg)==14 and cardImg[13].img.get_rect(topleft=pol[13]).collidepoint(event.pos):
                cardImg[13].click=True
        elif event.type == pygame.MOUSEBUTTONUP:
            for k in range(len(cardImg)):
                t= (pol[k][0]-40)//100
                if k!=t and 600<(pol[k][1])<780:
                    wada=cardImg[k]
                    if t>k:
                        for y in range(int(k),int(t)):
                            cardImg[y]=cardImg[y+1]
                        cardImg[int(t)]=wada
                    else:
                        for y in range(int(k),int(t),-1):
                            cardImg[y]=cardImg[y-1]
                        cardImg[int(t+1)]=wada
                if len(cardImg)== 14 and 870<(pol[k][0]+45)<960 and 270<(pol[k][1]+90)<450:
                    showcard=[cardImg[k]]+ showcard
                    pygame.display.update()
                    del (cardImg[k])
                    pygame.time.delay(100)
                    print(AI,showcard[0].name,hidecard[0].name)
                    TakeCard(AI,showcard[0].name,hidecard[0].name)
                    print(AI)
                    pygame.display.update()
                    new= ThrowCard(AI)
                    new= Character(pygame.image.load(new +".png"),new)
                    new.img= pygame.transform.scale(new.img,(90,180))
                    showcard= [new]+ showcard
                    print(AI)
                    
                    if checksecondlife(AI)== True:
                        rohit=False
                    
            pol=pos.copy()
            cardImg[0].click=cardImg[1].click=cardImg[2].click=cardImg[3].click=cardImg[4].click=cardImg[5].click=cardImg[12].click = False
            cardImg[6].click=cardImg[7].click=cardImg[8].click=cardImg[9].click=cardImg[10].click=cardImg[11].click= False
            if len(cardImg)==14:
                cardImg[13].click =False
        elif event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    DISPLAYSURF.fill((0,0,0))
    pygame.draw.rect(DISPLAYSURF,(0,255,0),(870,270,90,180),2)
    DISPLAYSURF.blit(cardImg[0].img,pol[0])
    DISPLAYSURF.blit(cardImg[1].img,pol[1])
    DISPLAYSURF.blit(cardImg[2].img,pol[2])
    DISPLAYSURF.blit(cardImg[3].img,pol[3])
    DISPLAYSURF.blit(cardImg[4].img,pol[4])
    DISPLAYSURF.blit(cardImg[5].img,pol[5])
    DISPLAYSURF.blit(cardImg[6].img,pol[6])
    DISPLAYSURF.blit(cardImg[7].img,pol[7])
    DISPLAYSURF.blit(cardImg[8].img,pol[8])
    DISPLAYSURF.blit(cardImg[9].img,pol[9])
    DISPLAYSURF.blit(cardImg[10].img,pol[10])
    DISPLAYSURF.blit(cardImg[11].img,pol[11])
    DISPLAYSURF.blit(cardImg[12].img,pol[12])
    if len(cardImg)==14:
        DISPLAYSURF.blit(cardImg[13].img,pol[13])
    if len(showcard) > 0:
        DISPLAYSURF.blit(showcard[0].img,(870,270))
    DISPLAYSURF.blit(backcard.img,(550,250))
    DISPLAYSURF.blit(AI_pic.img,(700,0))
    DISPLAYSURF.blit(jokerpic.img,(50,250))
    DISPLAYSURF.blit(show.img,(1200,350))
    if cardImg[0].click:
        x,y=pygame.mouse.get_pos()
        pol[0]=(x-45,y-90)
    elif cardImg[1].click:
        x,y=pygame.mouse.get_pos()
        pol[1]=(x-45,y-90)
    elif cardImg[2].click:
        x,y=pygame.mouse.get_pos()
        pol[2]=(x-45,y-90)
    elif cardImg[3].click:
        x,y=pygame.mouse.get_pos()
        pol[3]=(x-45,y-90)
    elif cardImg[4].click:
        x,y=pygame.mouse.get_pos()
        pol[4]=(x-45,y-90)
    elif cardImg[5].click:
        x,y=pygame.mouse.get_pos()
        pol[5]=(x-45,y-90)
    elif cardImg[6].click:
        x,y=pygame.mouse.get_pos()
        pol[6]=(x-45,y-90)
    elif cardImg[7].click:
        x,y=pygame.mouse.get_pos()
        pol[7]=(x-45,y-90)
    elif cardImg[8].click:
        x,y=pygame.mouse.get_pos()
        pol[8]=(x-45,y-90)
    elif cardImg[9].click:
        x,y=pygame.mouse.get_pos()
        pol[9]=(x-45,y-90)
    elif cardImg[10].click:
        x,y=pygame.mouse.get_pos()
        pol[10]=(x-45,y-90)
    elif cardImg[11].click:
        x,y=pygame.mouse.get_pos()
        pol[11]=(x-45,y-90)
    elif cardImg[12].click:
        x,y=pygame.mouse.get_pos()
        pol[12]=(x-45,y-90)
    elif len(cardImg)==14 and cardImg[13].click:
        x,y=pygame.mouse.get_pos()
        pol[13]=(x-45,y-90)
    pygame.display.update()
vishwas=[]
game=[]
for m in range(len(AI)):
    if AI[m]==[]:
        continue
    else:
        for n in range(len(AI[m])):
            vishwas+= [AI[m][n]]
for k in range (len(vishwas)):
    hide= Character(pygame.image.load(vishwas[k]+".png"),vishwas[k])
    hide.img= pygame.transform.scale(hide.img,(90,180))
    game += [hide]
DISPLAYSURF.fill((0,0,0))
DISPLAYSURF.blit(cardImg[0].img,pol[0])
DISPLAYSURF.blit(cardImg[1].img,pol[1])
DISPLAYSURF.blit(cardImg[2].img,pol[2])
DISPLAYSURF.blit(cardImg[3].img,pol[3])
DISPLAYSURF.blit(cardImg[4].img,pol[4])
DISPLAYSURF.blit(cardImg[5].img,pol[5])
DISPLAYSURF.blit(cardImg[6].img,pol[6])
DISPLAYSURF.blit(cardImg[7].img,pol[7])
DISPLAYSURF.blit(cardImg[8].img,pol[8])
DISPLAYSURF.blit(cardImg[9].img,pol[9])
DISPLAYSURF.blit(cardImg[10].img,pol[10])
DISPLAYSURF.blit(cardImg[11].img,pol[11])
DISPLAYSURF.blit(cardImg[12].img,pol[12])

DISPLAYSURF.blit(game[0].img,pol1[0])
DISPLAYSURF.blit(game[1].img,pol1[1])
DISPLAYSURF.blit(game[2].img,pol1[2])
DISPLAYSURF.blit(game[3].img,pol1[3])
DISPLAYSURF.blit(game[4].img,pol1[4])
DISPLAYSURF.blit(game[5].img,pol1[5])
DISPLAYSURF.blit(game[6].img,pol1[6])
DISPLAYSURF.blit(game[7].img,pol1[7])
DISPLAYSURF.blit(game[8].img,pol1[8])
DISPLAYSURF.blit(game[9].img,pol1[9])
DISPLAYSURF.blit(game[10].img,pol1[10])
DISPLAYSURF.blit(game[11].img,pol1[11])
DISPLAYSURF.blit(game[12].img,pol1[12])
pygame.display.update()            

