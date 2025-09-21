import turtle as t
import random as rd

t.bgcolor('#e83bff')

snake = t.Turtle()
snake.shape('square')
snake.color("#5E06A5")
snake.speed(0)
snake.penup()
snake.hideturtle()

folha = t.Turtle()
folha_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('folha',folha_shape)
folha.shape('folha')
folha.color('green')
folha.penup()
folha.hideturtle()
folha.speed()

inicio_do_jogo = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def fora_da_janela():
    parede_a_esquerda = -t.window_width()/2
    parede_a_direita = t.window_width()/2
    parede_superior = t.window_height()/2
    parede_inferior = -t.window_height()/2
    (x,y) = snake.pos()
    fora_do_limite = x < parede_a_esquerda or  x > parede_a_direita or  y < parede_inferior or y > parede_superior
    return fora_do_limite

def fim_de_jogo():
    snake.color('#e83bff')
    folha.color('#e83bff')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def placar_na_tela(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def lugar_folha():
    folha.hideturtle()
    folha.setx(rd.randint(-200,200))
    folha.sety(rd.randint(-200,200))
    folha.showturtle()

def inicio_de_jogo():
    global inicio_do_jogo
    if inicio_do_jogo:
        return
    inicio_do_jogo = True


    text_turtle.clear()
    t.clear()
    t.bgcolor('#e83bff')
    snake.hideturtle()
    folha.hideturtle()

    score = 0
    snake_speed = 1.5
    snake_length = 3

    snake.shapesize(1,snake_length,1)
    snake.color("#5E06A5")
    snake.setheading(0)
    snake.goto(0,0)
    snake.showturtle()

    folha.color('green')
    placar_na_tela(score)
    lugar_folha()

    while True:
        snake.forward(snake_speed)
        if snake.distance(folha)<20:
            lugar_folha()
            snake_length = snake_length + 1
            snake.shapesize(1,snake_length,1)
            snake_speed = snake_speed + 0.5
            score = score + 10
            placar_na_tela(score)

        if fora_da_janela():
            fim_de_jogo()
            inicio_do_jogo = False   
            return

def mover_para_cima():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def mover_para_baixo():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def mover_para_esquerda():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def mover_para_direita():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)

t.onkey(inicio_de_jogo,'space')
t.onkey(mover_para_cima,'Up')
t.onkey(mover_para_direita,'Right')
t.onkey(mover_para_baixo,'Down')
t.onkey(mover_para_esquerda,'Left')
t.listen()
t.mainloop()

