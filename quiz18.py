import pgzrun
TITLE="The quizzzzzzzzzz"
HEIGHT=600
WIDTH=800
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

def update():
    movingwordsrect.x-=3
    if movingwordsrect.right<=0:
        movingwordsrect.left=800

def loadnlist():
    global qlist,totalq
    with open("questions.txt","r") as file:
        for i in file:
            qlist.append(i)
            totalq+=1

loadnlist()
print(qlist)

pgzrun.go()