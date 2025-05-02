import pgzrun
TITLE="The quizzzzzzzzzz"
HEIGHT=600
WIDTH=800
score=0
gameisgone=False
qlist=[]
qnum=0
totalq=0
timer=10
movingwordsrect=Rect(0,0,WIDTH,70)
questionrect=Rect(10,100,670,150)
answerrect1=Rect(10,290,335,115)
answerrect2=Rect(350,290,335,115)
answerrect3=Rect(10,415,335,115)
answerrect4=Rect(350,415,335,115)
answerrect=[answerrect1,answerrect2,answerrect3,answerrect4]
timerrect=Rect(690,100,100,150)
skiprect=Rect(690,300,100,260)

def draw():
    screen.fill((50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    screen.draw.filled_rect(questionrect,(41,2,25))
    screen.draw.filled_rect(answerrect1,(107,4,45))
    screen.draw.filled_rect(answerrect2,(107,4,45))
    screen.draw.filled_rect(answerrect3,(107,4,45))
    screen.draw.filled_rect(answerrect4,(107,4,45))
    screen.draw.filled_rect(timerrect,(50,0,48))
    screen.draw.filled_rect(skiprect,(50,0,48))
    message=f"Hiiii welcome to the quiz (you have done {qnum} out of {totalq} questions)"
    screen.draw.textbox(message,movingwordsrect,color=(250,250,250))
    screen.draw.textbox(str(timer),timerrect,color=(250,250,250))
    screen.draw.textbox("Skip",skiprect,color=(250,250,250),angle=-90)
    screen.draw.textbox(q[0],questionrect,color=(250,250,250))
    forbelow=1
    for i in answerrect:
        screen.draw.textbox(q[forbelow].strip(),i,color=(250,250,250))
        forbelow+=1    

def update():
    movingwordsrect.x-=3
    if movingwordsrect.right<=0:
        movingwordsrect.left=800

def on_mouse_down(pos):
    box=1
    for i in answerrect:
        if i.collidepoint(pos):
            if box is int(q[5]):
                correctans()
            else:
                gameover()
        box+=1

def correctans():
    global timer,q,score,qlist
    score+=1
    if qlist:
        q=listseparate()
        timer=10
    else:
        gameover()

def gameover():
    global q,timer,gameisgone,score
    boo=f"You have lost - you managed to answer {score} questions correct."
    q=[boo,"-","-","-","-",78]
    timer=0
    gameisgone=True

def loadnlist():
    global qlist,totalq
    with open("questions.txt","r") as file:
        for i in file:
            qlist.append(i)
            totalq+=1

def listseparate():
    global qnum
    qnum+=1
    return qlist.pop(0).split("|")
loadnlist()
q=listseparate()

clock.schedhule_interval(update_time_left,1)
pgzrun.go()