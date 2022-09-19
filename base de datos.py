# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:47:29 2022

@author: Gustavo
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="gavato",
  passwd="recovery1234gus" ,
  database="Dragas"
)

c = mydb.cursor()

name='Vanessa Vanjie Mateo'
season=10
winner=0
sgwinner=0
fe=1
missc=0
allstars=0
b=0
w=0
h=1
a=0
size=0
weird=0
comedy=1
look=1
sing=0

c.execute("INSERT INTO reinas (nom, temp, winner, sg_winner, fe, miss_c, all_stars, b, w, h, a, size, weird, comedy, look, sing) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (name, season, winner, sgwinner,fe,missc,allstars,b,w,h,a,size,weird,comedy,look,sing))

mydb.commit()

c.execute("SELECT * FROM reinas")

rows = c.fetchall()

for eachRow in rows:
    print(eachRow)