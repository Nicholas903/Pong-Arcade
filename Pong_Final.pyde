# global variables

add_library('minim')    # add minim audio library
import random   # adds random number
import time 
timer = True
n = 0
x = 507
y = 500

xspeed = 3
yspeed = 3

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

speed_list = [1,-1,0]



# ################################################

def setup():
    global wall,score,paddle, new_game
    size (1000,1000)
    frameRate(120)
    minim=Minim(this)
    score = minim.loadFile("Pong Score.mp3")
    paddle = minim.loadFile("Pong Paddle.mp3")
    wall = minim.loadFile("Pong Wall.mp3")



  
    
def draw():
    global x,y,playerx,playery,mode,score1,score2, key_status,ball_speed_up,ball_speed_down,ball_speed_up2,ball_speed_down2,playery2,new_game
    
    background(0)
    # if mode is 2, when new game starts ball direction changes
    if mode == 0:
        if new_game == True:
            ball_direction()
            new_game = False
            
        game()
            
       
        
    # when mode is 3 print player 1 congradulations 
    elif mode == 1:
        player1_win()
        
    # when mode is 4 print player 2 congradulations         
    elif mode == 2:
        player2_win()
    # player movement for paddle  
    # player 1 controles          
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
            
    # Player 2 controles         
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
    global mode
    
   
def keyReleased():
    global key_status
    key_status[key] = False
    key_status[keyCode] = False

    

    
    
#game board and interacives
def game():
    global playerx,playery,mode,score1,score2,ball,x,y
    noStroke()
    background(0)
    detect_hit()

    design()
    player1score()
    player2score()
    ellipse(x,y,20,20)
    rect(100, playery, 10, 100)
    rect(900, playery2, 10, 100)
    x += xspeed
    y += yspeed

# detects if the ball has collided with the wall or if it hts the players paddle
def detect_hit():
    global x,y,xspeed,yspeed,playery,score1,score2,mode,playery2,score,wall,paddle,ball
    win()

    if y >= height-15:
        wall.play()
        yspeed = yspeed * -1.01
        wall.rewind()
    elif y <= 15:
        wall.play()
        yspeed = yspeed * -1.01
        wall.rewind()

    if x >= 900 and x <= 910:
        if y <= playery2+100 and y >= playery2-40:
            paddle.play()
            xspeed = -5
            yspeed = -5
            paddle.rewind()

    if x >= 900 and x <= 910:
        if y >= playery2+40 and y <= playery2+60:
            paddle.play()
            paddle.rewind()
            xspeed = xspeed
            yspeed = 0
   

                    
    if x >= 900 and x <= 910:
        if y >= playery2+60 and y <= playery2+110:
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

    if x >= 100 and x <= 110:
        if y >= playery+40 and y <= playery+60:
            paddle.play()
            paddle.rewind()
            xspeed = xspeed
            yspeed = 0
            

    if x >= 100 and x <= 110:
        if y >= playery+60 and y <= playery+110:
            paddle.play()
            yspeed = 5
            xspeed = 5
            paddle.rewind()

# when someone scores a point
def win():
    global score1, score2,x,y,yspeed,xspeed,mode,new_game,playery,playery2
    if x >= width-15 :
        score.play()
        score1 = score1 + 1
        new_game = True
        yspeed = 5
        x = 507
        y = 500
        score.rewind()
        return

        
    elif x <= 15:
        score.play()
        score2 = score2 + 1
        new_game = True
        yspeed = 5
        x = 507
        y = 500
        score.rewind()
        return

    if score1 == 9:
        new_game = True
        mode = 1
    elif score2 == 9:
        new_game = True
        mode = 2
        
# congradulations for player 1 and return to menu         
def player1_win():
    global x,y,xspeed,yspeed,ball_speed_down,ball_speed_up2,ball_speed_down2,timer,n

    background(0)
    
    ball_speed_up = 0
    ball_speed_down = 0
    ball_speed_up2 = 0
    ball_speed_down2 = 0

   

    fill(255)
    textSize(55)
    text("Cogratulations player 1!",200,700)
    text("Better luck next time player 2.",150,750)
    text("Game over!",350,300)
        
                
# congradulations for player 1 and return to menu         
def player2_win():
    global x,y,xspeed,yspeed,ball_speed_down,ball_speed_up2,ball_speed_down2,timer,n

    background(0)
   
    ball_speed_up = 0
    ball_speed_down = 0
    ball_speed_up2 = 0
    ball_speed_down2 = 0


    fill(255)
    textSize(55)
    text("Cogratulations player 2!",200,700)
    text("Better luck next time player 1.",150,750)
    text("Game over!",350,300)

        
                
# adds the middle design for the game                
def design():
    for i in range(20):
        rect(500,50*i,15,30)

# player 1 score               
def player1score():
    fill(255)
    textSize(300)
    text(score1,250,250)
    
# player 2 score
def player2score():
    fill(255)
    textSize(300)
    text(score2,575,250)

# the direction the ball will start in when a game starts
def ball_direction():
    global x,y,ball,xspeed,yspeed
    xspeed = 3
    yspeed = 3
    xspeed_factor = random.randint(0,1)
    yspeed_factor = random.randint(0,2)
    
    xspeed *= speed_list[xspeed_factor]
    yspeed *= speed_list[yspeed_factor]
    
