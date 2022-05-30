add_library('minim')    # add minim audio library
import random 

x = 507
y = 500

xspeed = 5
yspeed = 5
playery = 450
playery2 = 450
score1 = 0
score2 = 0
mode = 0 
new_game = True
ball = 0

ball_speed_up = 20
ball_speed_down = 20
ball_speed_up2 = 20
ball_speed_down2 = 20

def setup():
    global wall,score,paddle
    size (1000,1000)
    frameRate(120)
    minim=Minim(this)
    score = minim.loadFile("Pong Score.mp3")
    paddle = minim.loadFile("Pong Paddle.mp3")
    wall = minim.loadFile("Pong Wall.mp3")




  
    
def draw():
    global x,y,playerx,playery,mode,score1,score2, key_status,ball_speed_up,ball_speed_down,ball_speed_up2,ball_speed_down2,playery2,new_game
    
    background(0)
    if mode == 0:
        if new_game == True:
            ball_path()
            new_game = False
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
    
def ball_path():
    global x,y,ball
    ball = random.randrange(1,2)
    
    
def game():
    global playerx,playery,mode,score1,score2,ball

    background(0)
    detect_hit()

    design()
    player1score()
    player2score()
    ellipse(x,y,20,20)
    rect(100, playery, 10, 100)
    rect(900, playery2, 10, 100)

    

def detect_hit():
    global x,y,xspeed,yspeed,playery,score1,score2,mode,playery2,score,wall,paddle
    win()
    ball_direction()

    if y >= height-15:
        wall.play()
        yspeed = yspeed * -1.01
        wall.rewind()
    elif y <= 15:
        wall.play()
        yspeed = yspeed * -1.01
        wall.rewind()

    print(x,y)
    if x >= 900 and x <= 910:
        if y <= playery2+100 and y >= playery2-40:
            paddle.play()
            xspeed = -5
            yspeed = -5
            paddle.rewind()

    if x >= 900 and x <= 910:
        if y >= playery2+40 and y <= playery2+60:
            paddle.play()
            xspeed = -5
            yspeed = 0
            paddle.rewind()

                    
    if x >= 900 and x <= 910:
        if y >= playery2+60 and y <= playery2+100:
            paddle.play()
            yspeed = 5
            xspeed = -5
            paddle.rewind()


            
    if x >= 100 and x <= 110 :
        if y <= playery+100 and y >= playery-40:
            paddle.play()
            xspeed = 5
            yspeed = -5
            paddle.rewind()

    if x >= 100 and x <= 110 :
        if y >= playery+40 and y <= playery+60:
            paddle.play()
            xspeed = 5
            yspeed = 0
            paddle.rewind()

    if x >= 100 and x <= 110:
        if y >= playery+60 and y <= playery+100:
            paddle.play()
            yspeed = 5
            xspeed = 5
            paddle.rewind()

def win():
    global score1, score2,x,y,yspeed,xspeed,mode,new_game,playery,playery2
    if x >= width-15 :
        score.play()
        score1 = score1 + 1
        new_game = True
        x = 507
        y = 500
        
        score.rewind()
        return

        
    elif x <= 15:
        score.play()
        score2 = score2 + 1
        new_game = True
        x = 507
        y = 500
        score.rewind()
        return

    if score1 == 9:
        mode = 1
    elif score2 == 9:
        mode = 1
def game_over():
    global x,y,xspeed,yspeed,ball_speed_down,ball_speed_up2,ball_speed_down2

    background(0,0,0,100)
    xspeed = 0
    yspeed = 0 
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

def ball_direction():
    global x,y,ball
    
    if ball == 1:
        x += xspeed
        y += yspeed
    elif ball == 2:
        x += -xspeed
        y += yspeed
    elif ball == 3:
        x += xspeed
        y += -yspeed
    elif ball == 4:
        x += -xspeed
        y += -yspeed
    elif ball == 5:
        x += -xspeed
        y = 500
    elif ball == 6:
        x += xspeed
        y = 500
    
