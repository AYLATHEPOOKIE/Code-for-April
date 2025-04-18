import pgzrun
TITLE="The quizzzzzzzzzz"
HEIGHT=600
WIDTH=800
movingwordsrect=Rect(0,0,WIDTH,50)
questionrect=Rect(0,50,650,100)
answerrect1=Rect(345,390,335,215)
answerrect2=Rect(365,175,335,215)
answerrect3=Rect(10,175,335,215)
answerrect4=Rect(10,175,335,215)

def draw():
    screen.fill((50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    screen.draw.filled_rect(movingwordsrect,(50,0,35))
    
def update():
    pass

pgzrun.go()