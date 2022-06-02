# global variables

add_library('minim')    # add minim audio library
import random   # adds random number
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
    global wall,score,paddle
    size (1000,1000)
    frameRate(120)
    minim=Minim(this)
    score = minim.loadFile("Pong Score.mp3")
    paddle = minim.loadFile("Pong Paddle.mp3")
    wall = minim.loadFile("Pong Wall.mp3")
    retro = createFont("retro.ttf", 150)
    textFont(retro)
frame, max_frame = 0, 52

def draw():
    global x,y,playerx,playery,mode,score1,score2, key_status,ball_speed_up,ball_speed_down,ball_speed_up2,ball_speed_down2,playery2,new_game,frame

    background(204,204,0)

    # when mode is 0 geerate the menu screen
    if mode == 0:
        new_game = True
        menu()
       
    # if mode is 1 generate game rules        
    elif mode == 1:
        global score1,score2
        strokeWeight(6)
        background(255)
        fill(255)
        rect(350,25,300,50)
        fill(0)
        textSize(35)
        text("Rules of Pong",420,60)
        text("1. Pong is a two-dimensional sports game that simulates table tennis.",50,110)
        text("2. The player controles an in-game paddle by moving it vertically ",50,140)
        text("across the left or right side of the screen.",85,170)
        text("3. They can compete against the other player controlling the ",50,200)
        text("second paddle on the opposing side.",80,230)
        text("4. Players use the paddes to hit a ball back and forth.",50,260)
        text("5. The goal is for each player to reach nine points before the other opponent.",50,290)
        text("6. Points are earned when one payer fails to return the ball to he other.",50, 320)
        textSize(25)

        text("Up and Down is the paddle contoles for player 2.",550,800)
        text("W and S is the paddle contoles for player 1.",50,800)

        fill(255)
        rect(800,850,150,100)
        textSize(40)

        fill(0)
        text("Return",830,910)

        Image = loadImage("Arrowkeys.png")
        Image2 = loadImage("keys.jpg")

        image(Image,550,350)

        image(Image2,0,350)

        # adds text that blinks
        global timer, n
        if timer == True:
            fill(0)
            text('Press Enter To Begin',300,910)
            for i in range(1,200):
                n += 0.001
                print(n)
                if n >= 2.5:
                    n = 0
                    timer = False
               
        if timer == False:
            fill(255)
            text('Press Enter To Begin',300,910)

            for i in range(1,200):
                n += 0.001
                print(n)
                if n >= 2.5:
                    n = 0
                    timer = True
       
    # if mode is 2, when new game starts ball direction changes
    if mode == 2:
        if new_game == True:
            ball_direction()
            new_game = False
        game()
       
    # when mode is 3 print player 1 congradulations
    elif mode == 3:
        player1_win()
       
    # when mode is 4 print player 2 congradulations        
    elif mode == 4:
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
   
    # if enter is pessed mode is 1
    if mode == 0 and(key == ENTER):
        mode = 1
   
    # if enter is pressed after the first mode is 2 and game will start  
    elif mode == 1 and(key == ENTER):
        mode = 2

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

    if x >= 100 and x <= 110:
        if y >= playery+40 and y <= playery+60:
            paddle.play()
            paddle.rewind()
            xspeed = xspeed
            yspeed = 0
           

    if x >= 100 and x <= 110:
        if y >= playery+60 and y <= playery+100:
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
        
        mode = 3
    elif score2 == 9:
        new_game = True
        mode = 4
       
# congratulations for player 1 and return to menu        
def player1_win():
    global x,y,xspeed,yspeed,ball_speed_down,ball_speed_up2,ball_speed_down2,timer,n,frame

    background(0)
   
    ball_speed_up = 0
    ball_speed_down = 0
    ball_speed_up2 = 0
    ball_speed_down2 = 0

    fill(255)
    rect(400,400,200,150)
    fill(0)
    textSize(50)
    text("Menu",460,490)

    fill(255)
    textSize(55)
    text("Congradulations player 1!",250,700)
    text("Better luck next time player 2!",230,750)
   
    # adds text that blinks
    if timer == True:
        fill(255)
        textSize(50)
        text("Game over!",400,350)
        for i in range(1,200):
            n += 0.001
            print(n)
            if n >= 2.5:
                n = 0
                timer = False
               
    if timer == False:
        fill(0)
        textSize(50)
        text("Game over!",400,350)

        for i in range(1,200):
            n += 0.001
            print(n)
            if n >= 2.5:
                n = 0
                timer = True
    # adds congratulations animation          
    frame += 1
    if frame >= max_frame:
        frame = 0
    print("(" + str(frame) + ")")
    image(loadImage("(" + str(frame) + ").gif"), 245, 0, 500, 281)
            
# congratulations for player 2 and return to menu    
def player2_win():
    global x,y,xspeed,yspeed,ball_speed_down,ball_speed_up2,ball_speed_down2,timer,n,frame

    background(0)
   
    ball_speed_up = 0
    ball_speed_down = 0
    ball_speed_up2 = 0
    ball_speed_down2 = 0

    fill(255)
    rect(400,400,200,150)
    fill(0)
    textSize(50)
    text("Menu",460,490)

    fill(255)
    textSize(55)
    text("Congradulations player 2!",250,700)
    text("Better luck next time player 1!",230,750)
   
    # adds text that blinks
    if timer == True:
        fill(255)
        textSize(50)
        text("Game over!",400,350)
        for i in range(1,200):
            n += 0.001
            print(n)
            if n >= 2.5:
                n = 0
                timer = False
               
    if timer == False:
        fill(0)
        textSize(50)
        text("Game over!",400,350)

        for i in range(1,200):
            n += 0.001
            print(n)
            if n >= 2.5:
                n = 0
                timer = True
                
    # adds congratulations animation              
    frame += 1
    if frame >= max_frame:
        frame = 0
    print("(" + str(frame) + ")")
    image(loadImage("(" + str(frame) + ").gif"), 245, 0, 500, 281) 
               
# adds the middle design for the game                
def design():
    for i in range(20):
        rect(500,50*i,15,30)

# player 1 score              
def player1score():
    fill(255)
    textSize(300)
    text(score1,280,250)
   
# player 2 score
def player2score():
    fill(255)
    textSize(300)
    text(score2,630,250)

# the direction the ball will start in when a game starts
def ball_direction():
    global x,y,ball,xspeed,yspeed
    xspeed = 3
    yspeed = 3
   
    xspeed_factor = random.randint(0,1)
    yspeed_factor = random.randint(0,2)
   
    xspeed *= speed_list[xspeed_factor]
    yspeed *= speed_list[yspeed_factor]  

   
# main menu            
def menu():
    fill (0)
    rect(150,150,700,700)
    textSize(70)
    fill(255)
    text("Welcome to pong!",300,250)  
   
    global timer, n
    # adds text that blinks
    if timer == True:
        fill(255)
        text('Press Enter To Start',260,700)
        for i in range(1,200):
            n += 0.001
            print(n)
            if n >= 2.5:
                n = 0
                timer = False
               
    if timer == False:
        fill(0)
        text('Press Enter To Start',250,700)

        for i in range(1,200):
            n += 0.001
            print(n)
            if n >= 2.5:
                n = 0
                timer = True
               
# if someone clicks mouse            
def mousePressed():
    # checks clicks if it is in respective mode/menu
    global mode,score1,score2,grid,turn,x,y,playery,playery2
   
    # retuns to menu
    if mouseX < 950 and mouseX >800 and mouseY < 950 and mouseY > 850 and mode == 1:
        mode = 0
   
    # when game is over and a player has won return to menu button  
    elif mouseX < 600 and mouseX > 400 and mouseY < 550 and mouseY > 400 and mode == 3 or mode == 4:
        mode = 0  
        score1 = 0
        score2 = 0
        playery = 450
        playery2 = 450
