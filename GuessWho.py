# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:30:18 2022

@author: Gustavo
"""

import mysql.connector
import tkinter as tt
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Label
import pygame


class queen():
    def __init__(self):
        global dato
        global season
        global ven
        global b1
        global b2
        global x
        global y
        global l
        global ide
        global yy
        global g
        global destruir 
        global result 
        
        result="simon"
        destruir=0
        g=0
        ide=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        x=0
        y=-1
        yy=0
        dato=["from season ",
              "the winner?",
              "the Snatch Game winner?",
              "the first eliminated queen?",
              "miss Congeniality?",
              "an All Stars queen?",
              "black?",
              "white?",
              "hispanic?",
              "asian or mid-eastern?",
              " a size queen?",
              "a weird queen?",
              "a comedy queen?",
              "a look queen?",
              "a good singer?",
              "encontrada"
              ]
        
        season=["10?","11?","12?","13?","9?","8?","7?","6?","5?","4?","3?","2?","1?"]
        
        ven=tt.Tk()
        ven.title("RuPual´s Drag Race: Guess Who?") 
        ven.config(bg="white")
        ven.geometry("600x625")
        image1 = Image.open("Rupaul.jpg")
        test = ImageTk.PhotoImage(image1)
        ld = tt.Label(image=test)
        ld.image = test
        ld.place(x=-180,y=-45)
        
        image2 = Image.open("dialogo.png")
        test2 = ImageTk.PhotoImage(image2)
        lda = tt.Label(image=test2, bg="white")
        lda.image = test2
        lda.place(x=-15,y=0)
        
        pygame.mixer.init()
        sound = pygame.mixer.Sound("Monologue_Long.mp3")
        sound.play()

        b1=ttk.Button(
            ven,
            text="Yes",
            command=lambda: queen.postivo(self)
            ).place(x=100,y=450)
        b2=ttk.Button(
            ven, 
            text="No", 
            command=lambda: queen.negativo(self)
            ).place(x=320,y=450)
        
        l = Label(ven, text="Are you ready to play? ")
        l.place(x=70,y=80)

        ven.mainloop()
    
    def postivo(self):
        global x
        global y
        global yy
        global ide
        global l
        global g
        global destruir
        
        if destruir == 1:
            ven.destroy()
        
        if yy== 0 and y==0:
            ide[y]=10
        if yy== 1 and y==0:
            ide[y]=11
        elif yy== 2 and y==0:
            ide[y]=12
        elif yy== 3 and y==0:
            ide[y]=13
        
        if yy== 4 and y==0:
            ide[y]=9
        if yy== 5 and y==0:
            ide[y]=8
        
        elif yy== 6 and y==0:
            ide[y]=7
        if yy== 7 and y==0:
            ide[y]=6
        if yy== 8 and y==0:
            ide[y]=5
        elif yy== 9 and y==0:
            ide[y]=4
        elif yy== 10 and y==0:
            ide[y]=3
        elif yy== 11 and y==0:
            ide[y]=2
        elif yy== 12 and y==0:
            ide[y]=1
            
        x=1
        if y>0 and y<15:
            ide[y]=1
            
        if ide[1] == 1:
            y=14
            g=1
            queen.busca(self)
        if ide[2] == 1:
            y=14
            g=1
            queen.busca(self)
        if ide[3] == 1:
            y=14
            g=1
            queen.busca(self)
        if ide[4] == 1:
            y=14
            g=1
            queen.busca(self)
        
        if (ide[6]==1 or ide[7]==1 or ide[8]==1 or ide[9]==1) and y<10:
            y=9
            
        y=y+1
        
        if y == 15 and g==0:
            queen.busca(self)
        print(ide)
        print(y)
        queen.lista(self)
    
    def busca(self):
    
    
        global destruir
        

        mydb = mysql.connector.connect(
          host="localhost",
          user="gavato",
          passwd="recovery1234gus" ,
          database="Dragas"
        )

        c = mydb.cursor()

        if ide[1]==1:
            c.execute("SELECT nom FROM reinas WHERE winner=1 AND temp="+ str(ide[0]) )
        if ide[2]==1:
            c.execute("SELECT nom FROM reinas WHERE sg_winner=1 AND temp="+ str(ide[0]) )
        if ide[3]==1:
            c.execute("SELECT nom FROM reinas WHERE fe=1 AND temp="+ str(ide[0]) )
        if ide[4]==1:
            c.execute("SELECT nom FROM reinas WHERE miss_c=1 AND temp="+ str(ide[0]) )        
        if ide[4]==0 and ide[1]==0 and ide[2]==0 and ide[3]==0 :
            c.execute("SELECT nom FROM reinas WHERE all_stars="+ str(ide[5])
                      +" AND b="+ str(ide[6])
                      +" AND w="+ str(ide[7])
                      +" AND h="+ str(ide[8])
                      +" AND a="+ str(ide[9])
                      +" AND size="+ str(ide[10])
                      +" AND weird="+ str(ide[11])
                      +" AND comedy="+ str(ide[12])
                      +" AND look="+ str(ide[13])
                      +" AND sing="+ str(ide[14])
                      +" AND temp="+ str(ide[0]))
        
        dato[-1]=str(c.fetchall())
        
        destruir=1

    def nombre(self):
        global result
        global texta
        global l
       
        l["text"] ="Write the name of the new queen"
        texta = tt.StringVar()
        textbox = ttk.Entry(ven, textvariable=texta)
        textbox.place(x=70,y=100)
        b3=ttk.Button(
            ven, 
            text="ok", 
            command=lambda: queen.nuevo(self,texta)
            ).place(x=70,y=130)

        
    def negativo(self):
        global x
        global y
        global yy
        global l
        global destruir 
        
        if destruir == 1:
            queen.nombre(self)

        x=0
        yy=yy+1
        if ide[0] != 0:
            y=y+1
        print(ide)
        if y == 15:
            queen.busca(self)
        if y <= 15:
            queen.lista(self)
    
    def lista(self):
        global x
        global y
        global l
        if yy < 14 and y == 0:
            l["text"] ="Is your queen "+ dato[y] + season[yy]
        else:
            l["text"] ="Is your queen "+ dato[y]
           
    def nuevo(self, texta):
        global result
        global l
       
        l["text"] ="Your queen has been added"
        
        result=texta.get()
        print(result)
        mydb = mysql.connector.connect(
          host="localhost",
          user="gavato",
          passwd="recovery1234gus" ,
          database="Dragas"
        )

        c = mydb.cursor()
        
        c.execute("INSERT INTO reinas (nom, temp, winner, sg_winner, fe, miss_c, all_stars, b, w, h, a, size, weird, comedy, look, sing) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (result, ide[0],ide[1], ide[2],ide[3], ide[4], ide[5],ide[6],ide[7],ide[8],ide[9],ide[10],ide[11],ide[12],ide[13],ide[14]))

        mydb.commit()
        
        
            
q= queen()
