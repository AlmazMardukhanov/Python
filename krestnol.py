import tkinter
from tkinter import *
pole1=[]
x=0
player='X'
game_run = True



class GAME():

    def pole():
        global row
        global col
        for row in range(3):
            line=[]
            for col in range(3):
                button=Button(root,text=(row,col),width=4,height=2,font=('Verdana',20,'bold'),bg='aqua',command=lambda col=col,row=row:KNOPKI.click1(row,col))
                button.grid(row=row,column=col,sticky='nsew')

                line.append(button)
            pole1.append(line)
        new_game=Button(root,text='Начать новую игру',font=('verdana',20,'bold'),bg='aquamarine',command=KNOPKI.newgame)
        new_game.grid(column=0,columnspan=3,sticky='nsew')


    def check(player):
        for n in range(3):
            GAME.check_line(pole1[n][0],pole1[n][1],pole1[n][2],player)
            GAME.check_line(pole1[0][n], pole1[1][n], pole1[2][n],player)
        GAME.check_line(pole1[0][0],pole1[1][1], pole1[2][2],player)
        GAME.check_line(pole1[2][0], pole1[1][1], pole1[0][2],player)

    def check_line(a1, a2, a3,player):
        if a1['text'] == player and a2['text'] == player and a3['text'] == player:
            a1['background'] = a2['background'] = a3['background'] = 'green'
            global game_run
            game_run = False

class KNOPKI():

    def ch_player():
        global player
        if player == '0':
            player = 'X'
        else:
            player = '0'

    def newgame():
        global game_run
        game_run = True
        for row in range(3):
            for col in range(3):
                pole1[row][col]['text'] = ' '
                pole1[row][col]['background']='aqua'





    def click1(row,col):

        if pole1[row][col]['text']==' ' and game_run==True:
                pole1[row][col]['text']=player


                GAME.check(player)
                KNOPKI.ch_player()


        if pole1[row][col]['text'] == ' ' and game_run==True :
            pole1[row][col]['text'] = player


            GAME.check(player)
            KNOPKI.ch_player()








root=Tk()
root.geometry('+500+200')
root.title('Крестики-нолики')

GAME.pole()
root.mainloop()