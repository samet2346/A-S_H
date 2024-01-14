import turtle
import random
import time

window = turtle.Screen()
window.bgcolor("white")
window.screensize(600,600)
window.title("turtle game")

gametu = turtle.Turtle()
gametu.color("red")
gametu.shape("turtle")
gametu.shapesize(3,3)
gametu.penup()

skor = 0
saniye = 15


skor_goster = turtle.Turtle()
skor_goster.color("blue")
skor_goster.speed(0)
skor_goster.penup()
skor_goster.goto(0,320)
skor_goster.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

saniye_goster = turtle.Turtle()
saniye_goster.color("green")
saniye_goster.speed(0)
saniye_goster.penup()
saniye_goster.goto(0,270)
saniye_goster.write("saniye: {}".format(saniye),align="center",font=("courier", 24, "normal"))






def skor_guncelle():
    skor_goster.clear()
    skor_goster.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

def saniye_guncelle():
    global saniye
    saniye -=1
    saniye_goster.clear()
    saniye_goster.write("saniye: {}".format(saniye),align="center", font=("courier", 24, "normal"))






    if saniye == 0:
        oyun_bitti()

def oyun_bitti():
        skor_goster.goto(0, 0)
        skor_goster.write("Oyun bitti!\nSkorunuz: {}".format(skor), align="center", font=("Courier", 24, "normal"))
        window.bye()


def rastgele_konum():
    x = random.randint(-270,270)
    y = random.randint(-270,270)
    return x,y

def click_code(x, y):
    global skor
    distance = gametu.distance(x, y)
    if distance < 50 and gametu == window.turtles()[0]:  # Eğer tıklanan nokta kamplumbaga ile belirlenen bir mesafede ve sadece kamplumbagaysa
        skor += 1
        skor_guncelle()
        yeni_konum = rastgele_konum()
        gametu.goto(yeni_konum)




window.onscreenclick(click_code)

while saniye > 0:
    saniye_guncelle()
    time.sleep(1)

window.mainloop()





