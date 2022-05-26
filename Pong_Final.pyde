x = 200
y = 100

xspeed = 4
yspeed = 4


def setup():
    size (1000,1000)
    
def draw():
    global x,y,playerx,playery,mode,score1,score2
    
    background(0)

    game()
   
        
def game():
    global x,y,playerx,playery,mode,score1,score2
    background(0)
    design()
  
    ellipse(x,y,20,20)
    x += xspeed
    y += yspeed
       
    detect_hit()

def detect_hit():
    global x,y,speed,xspeed,yspeed,playery,score1,score2,mode,playery2

    
    win()
    if y >= height-15:
        yspeed = yspeed * -1.01
    elif y <= 15:
        yspeed = yspeed * -1.01
    

def win():
    global score1, score2,x,y,yspeed,xspeed
    if x >= width-15 :
        yspeed = yspeed
        xspeed = xspeed
        x = 200
        y = 100
        return

        
    elif x <= 15:
        score2 = score2 + 1
        yspeed = -yspeed
        xspeed = -xspeed
        x = 200
        y = 100
        return
        

def design():
    for i in range(20):
        rect(500,50*i,15,30)


    


    

        
