# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:49:58 2022

@author: Gustavo
"""

import mysql.connector
import tkinter as tt
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Label
import pygame
import cv2
import random 

class juego():
    def __init__(self):
        global x
        global ven
        global y
        global z
        global c
        
        c=0
        z=["lugar-1.jpg","lugar-2.jpg","lugar-3.jpg","lugar-4.jpg","lugar-5.jpg"]
        y=["arma-1.jpg","arma-2.jpg","arma-3.jpg","arma-4.jpg","arma-5.jpg"]
        x=random.randint(0,4)
        ven=tt.Tk()
        ven.title("Clue") 
        ven.config(bg="white")     
        ven.geometry("500x500")
        
        intro =  Label(text= "Ayudanos a descubrir un asesinato digno de televisa"
                    ).place(x=100,y=350)
        
        b1=ttk.Button(
            ven,
            text="Sospechosos",
            command=lambda: juego.sus(self)
            ).place(x=100,y=250)
        b2=ttk.Button(
            ven, 
            text="Armas", 
            command=lambda: juego.armas(self)
            ).place(x=300,y=250)
        
        b3=ttk.Button(
            ven,
            text="Lugares",
            command=lambda: juego.lug(self)
            ).place(x=200,y=250)
        b4=ttk.Button(
            ven, 
            text="Culpar", 
            command=lambda: juego.si(self)
            ).place(x=200,y=450)
        
        ven.mainloop()
    
    def sus(self):
        b1=ttk.Button(
            ven,
            text="    Lyn May    ",
            command=lambda: juego.lyn(self)
            ).grid(row=1)
        b2=ttk.Button(
            ven, 
            text="Maribel Guardia", 
            command=lambda: juego.mar(self)
            ).grid(row=2)
        b3=ttk.Button(
            ven,
            text="    Niurka     ",
            command=lambda: juego.niurka(self)
            ).grid(row=3)
        b4=ttk.Button(
            ven, 
            text="  Laura Bozzo  ", 
            command=lambda: juego.laura(self)
            ).grid(row=4)
        b5=ttk.Button(
            ven,
            text="    Luna Gil   ",
            command=lambda: juego.luna(self)
            ).grid(row=5)

    
    def lug(self):
        b1=ttk.Button(
            ven,
            text="Salon de baile",
            command=lambda: juego.luga(self)
            ).grid(row=3)
        b2=ttk.Button(
            ven, 
            text="Piscina", 
            command=lambda: juego.luga1(self)
            ).grid(row=5)
        b3=ttk.Button(
            ven,
            text="Baño",
            command=lambda: juego.luga2(self)
            ).grid(row=2)
        b4=ttk.Button(
            ven, 
            text="Gimnsio", 
            command=lambda: juego.luga3(self)
            ).grid(row=1)
        b5=ttk.Button(
            ven,
            text=" Sala",
            command=lambda: juego.luga4(self)
            ).grid(row=4)
        
    
    def armas(self):
        b1=ttk.Button(
            ven,
            text="Inyeccion de botox",
            command=lambda: juego.resar(self)
            ).grid(row=3)
        b2=ttk.Button(
            ven, 
            text="Juguete", 
            command=lambda: juego.resar1(self)
            ).grid(row=4)
        b3=ttk.Button(
            ven,
            text=" Zapatillas de baile",
            command=lambda: juego.resar2(self)
            ).grid(row=2)
        b4=ttk.Button(
            ven, 
            text="Microfono", 
            command=lambda: juego.resar3(self)
            ).grid(row=5)
        b5=ttk.Button(
            ven,
            text="Sosten",
            command=lambda: juego.resar4(self)
            ).grid(row=1)

    def lyn(self):
        global x
        global c
        y=["lynmay-1.jpg","lynmay-2.jpg","lynmay-3.jpg","lynmay-4.mp4",""]
     
        if x!=4 and x!=3:
            im=cv2.imread(y[x],cv2.IMREAD_COLOR)
            cv2.imshow("Sospechosa: Lyn May",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif x==3:
            cap = cv2.VideoCapture('lynmay-4.mp4')

            while cap.isOpened():
                ret, frame = cap.read()

                cv2.imshow('frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Lyn May")
            l.grid(row=2, column=6)
        
    def mar(self):
        global x
        global c
        y=["maribel-1.png","","maribel-3.jpg","maribel-4.jpg","maribel-5.jpg"]
        
        if x!=1:
            
            im=cv2.imread(y[x],cv2.IMREAD_COLOR)
            cv2.imshow("Sospechosa: Maribel Guardia",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        else:

            c=c+3
            l = Label(text="No hay evidencias de Maribel Guardia")
            l.grid(row=2, column=6)

    def niurka(self):
        global x
        global c
        y=["","niurka-2.jpg","niurka-3.jpg","niurka-4.mp4","niurka-5.jpg"]
        
        if x!=0 and x!=3:
            
            im=cv2.imread(y[x],cv2.IMREAD_COLOR)
            cv2.imshow("Sospechosa: Niurka",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif x==3:
            cap = cv2.VideoCapture('niurka-4.mp4')

            while cap.isOpened():
                ret, frame = cap.read()

                cv2.imshow('frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        
        else:
            c=c+3
            l = Label(text="No hay evidencias de Niurka")
            l.grid(row=2, column=6)

    def laura(self):
        global x
        global c
        y=["laura-1.mp4","laura-2.jpg","","laura-4.jpg","laura-5.jpg"]
        
        if x!=2 and x!=0:
            
            im=cv2.imread(y[x],cv2.IMREAD_COLOR)
            cv2.imshow("Sospechosa: Laura Bozzo",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif x==0:
            cap = cv2.VideoCapture('laura-1.mp4')

            while cap.isOpened():
                ret, frame = cap.read()

                cv2.imshow('frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        else:

            c=c+3
            l = Label(text="No hay evidencias de Laura Bozzo")
            l.grid(row=2, column=6)

    def luna(self):
        global x
        global c
        y=["luna-1.png","luna-2.png","luna-3.png","","luna-5.mp4"]
        
        if x!=3 and x!=4:
            
            im=cv2.imread(y[x],cv2.IMREAD_COLOR)
            cv2.imshow("Sospechosa: Luna Gil",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif x==4:
            cap = cv2.VideoCapture('luna-5.mp4')

            while cap.isOpened():
                ret, frame = cap.read()

                cv2.imshow('frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Luna Gil")
            l.grid(row=2, column=6)
        
    def resar(self):
        global x
        global y
        global c
        a=0
        if x!=a:
            
            im=cv2.imread(y[a],cv2.IMREAD_COLOR)
            cv2.imshow("Arma: Inyeccion de botox",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Inyeccion de botox")
            l.grid(row=3, column=6)
        
    def resar1(self):
        global x
        global y
        global c
        a=1
        if x!=a:
            
            im=cv2.imread(y[a],cv2.IMREAD_COLOR)
            cv2.imshow("Arma: Juguete",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Juguete")
            l.grid(row=3, column=6)

    def resar2(self):
        global x
        global y
        global c
        a=2
        if x!=a:
            
            im=cv2.imread(y[a],cv2.IMREAD_COLOR)
            cv2.imshow("Arma: Zapatillas de baile",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Zapatillas de baile")
            l.grid(row=3, column=6)
        
    def resar3(self):
        global x
        global y
        global c
        a=3
        if x!=a:
            
            im=cv2.imread(y[a],cv2.IMREAD_COLOR)
            cv2.imshow("Arma: Microfono",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Microfono")
            l.grid(row=3, column=6)        
        
    def resar4(self):
        global x
        global y
        global c
        a=4
        if x!=a:
            
            im=cv2.imread(y[a],cv2.IMREAD_COLOR)
            cv2.imshow("Arma: Sosten",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Sosten")
            l.grid(row=3, column=6)    
            
    def luga(self):
        global x
        global z
        global c
        a=0
        if x!=a:
            
            im=cv2.imread(z[a],cv2.IMREAD_COLOR)
            cv2.imshow("Lugar: Salon de baile",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Salon de baile")
            l.grid(row=4, column=6)
        
    def luga1(self):
        global x
        global y
        global c
        
        a=1
        if x!=a:
            
            im=cv2.imread(z[a],cv2.IMREAD_COLOR)
            cv2.imshow("Lugar: Piscina",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Piscina")
            l.grid(row=4, column=6)

    def luga2(self):
        global x
        global z
        global c
        
        a=2
        if x!=a:
            
            im=cv2.imread(z[a],cv2.IMREAD_COLOR)
            cv2.imshow("Lugar: Baño",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Baño")
            l.grid(row=4, column=6)
        
    def luga3(self):
        global x
        global y
        global c
        
        a=3
        if x!=a:
            
            im=cv2.imread(z[a],cv2.IMREAD_COLOR)
            cv2.imshow("Lugar: Gimnasio",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Gimnasio")
            l.grid(row=4, column=6)        
        
    def luga4(self):
        global x
        global y
        global c
        
        a=4
        if x!=a:
            
            im=cv2.imread(z[a],cv2.IMREAD_COLOR)
            cv2.imshow("Lugar: Sala",im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            c=c+3
            l = Label(text="No hay evidencias de Sala")
            l.grid(row=4, column=6)   
            
    
    def si(self):
        global c
        
        if c==9:
            l = Label(text="¡Felicidades! Encontraste al asesino")
            l.place(x=100, y=400) 
        else:
            l = Label(text="No tienes la evidencia aun")
            l.place(x=100, y=400)        


    
a= juego()