x = 200
y = 100

xspeed = 5
yspeed = 5
playery = 450
playery2 = 450
score1 = 0
score2 = 0
mode = 0 
ball_speed_up = 20
ball_speed_down = 20
ball_speed_up2 = 50
ball_speed_down2 = 50

def setup():
    size (1000,1000)
    frameRate(120)
    


  
    
def draw():
    global x,y,playerx,playery,mode,score1,score2, key_status,ball_speed_up,ball_speed_down,ball_speed_up2,ball_speed_down2,playery2
    
    background(0)
    if mode == 0:
        game()
    elif mode == 1:
        game_over()
    if "w" in key_status.keys() and key_status["w"]:
        playery += -ball_speed_up
        ball_speed_down = 20
        if playery <= 0:
            ball_speed_up = 0
    if "s" in key_status.keys() and key_status["s"]:
        playery += ball_speed_down
        ball_speed_up = 20
        if playery >= 900:
            ball_speed_down = 0
    if UP in key_status.keys() and key_status[UP]:
        playery2 += -ball_speed_up2
        ball_speed_down2 = 20
        if playery2 <= 0:
            ball_speed_up2 = 0
    if DOWN in key_status.keys() and key_status[DOWN]:
        playery2 += ball_speed_down2
        ball_speed_up2 = 20
        if playery2 >= 900:
            ball_speed_down2 = 0
        
key_status = {}        
def keyPressed():
    global key_status
    key_status[key] = True
    key_status[keyCode] = True


def keyReleased():
    global key_status
    key_status[key] = False
    key_status[keyCode] = False
    
def game():
    global x,y,playerx,playery,mode,score1,score2
    background(0)
    design()
    player1score()
    player2score()
    ellipse(x,y,20,20)
    rect(100, playery, 10, 100)
    rect(900, playery2, 10, 100)
    x += xspeed
    y += yspeed
       
    detect_hit()

def detect_hit():
    global x,y,xspeed,yspeed,playery,score1,score2,mode,playery2

    
    win()
    if y >= height-15:
        yspeed = yspeed * -1.01
    elif y <= 15:
        yspeed = yspeed * -1.01
    

    if x >= 900 and x <= 900:
        if y <= playery2+100 and y >= playery2-40:
            xspeed = -5
            yspeed = -5
            
    if x >= 900 and x <= 900:
        if y >= playery2+40 and y <= playery2+60:
            xspeed = -5
            yspeed = 0
    
                    
    if x >= 900 and x <= 900:
        if y >= playery2+60 and y <= playery2+100:
            yspeed = 5
            xspeed = -5
      
            
    if x >= 100 and x <= 105 :
        if y <= playery+100 and y >= playery-40:
            xspeed = 5
            yspeed = -5
          
    if x >= 100 and x <= 105 :
        if y >= playery+40 and y <= playery+60:
            xspeed = 5
            yspeed = 0
            
    if x >= 100 and x <= 105:
        if y >= playery+60 and y <= playery+100:
            yspeed = 5
            xspeed = 5
    

def win():
    global score1, score2,x,y,yspeed,xspeed,mode
    if x >= width-15 :
        score1 = score1 + 1
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

    if score1 == 9:
        mode = 1
    elif score2 == 9:
        mode = 1
def game_over():
    global x,y,xspeed,yspeed,ball_speed_down,ball_speed_up2,ball_speed_down2

    background(0,0,0,100)
    xspeed = 0
    yspeed
    ball_speed_up = 0
    ball_speed_down = 0
    ball_speed_up2 = 0
    ball_speed_down2 = 0

def design():
    for i in range(20):
        rect(500,50*i,15,30)
        
def player1score():
    fill(255)
    textSize(300)
    text(score1,250,250)
    
# player Y score
def player2score():
    fill(255)
    textSize(300)
    text(score2,575,250)
    
'''def keyPressed():
    global speed, playery2,playery,ball_speed_up,ball_speed_down,ball_speed_up2,ball_speed_down2
    
  
    if ((key) and ((key == 'w') or (key == 'W')) and mode == 0):
        playery += -ball_speed_up
        ball_speed_down = 50
        if playery <= 0:
            ball_speed_up = 0
    
    elif ((key) and ((key == 's') or (key == 'S'))and mode == 0):
        playery += ball_speed_down
        ball_speed_up = 50
        if playery >= 900:
            ball_speed_down = 0



    if (keyCode == UP and mode == 0):
        playery2 += -ball_speed_up2
        ball_speed_down2 = 50
        if playery2 <= 0:
            ball_speed_up2 = 0
    
    elif (keyCode == DOWN and mode == 0):
        playery2 += ball_speed_down2
        ball_speed_up2 = 50
        if playery2 >= 900:
            ball_speed_down2 = 0'''

    


    

        
