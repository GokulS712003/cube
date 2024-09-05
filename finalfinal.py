
from tkinter import *
from PIL import ImageTk,Image,ImageSequence
import time
from itertools import count
import numpy as np
print("noepad")
root = Tk()
mylabelmoves=Label()
mylabelmoves.pack(fill=X,side="bottom")
l=Label(root,text="Solving Rubix Cube",font=("courier",40),bg="black",fg="white")
l.pack(fill=X,side=TOP)
l2=Label(root,bg="GOLD")
l2.pack(fill=BOTH)
global V,Rr,Br,position,final,solutionlabel,solmoves,ig
solmoves=[]
ig=0

temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
final=['B','B','B','B','B','B','B','B','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W']

finalcheck=['B','B','B','B','B','B','B','B','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W']

Rr=0
Br=0
Or=0
Gr=0
Wr=0
Yr=0
V=""
position=[]

#importing labells
blue_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\blue.png"))
red_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\red.png"))
orange_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\orange.png"))
grey_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\grey.png"))
green_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\green.png"))
yellow_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\yellow.png"))
white_labell=ImageTk.PhotoImage(Image.open("D:\\allcases\\white.png"))

#moves import should be done first
#R




#MAIN PROGRAM

def RED():
    global V,Rr,position
    print(V)
    if(len(V)<=52):
        position.append('R')
        V=V+'R'
        Rr=Rr+1
        
        
        if(Rr==8):
            red['state']= DISABLED
        if(len(V)==1 and Rr<=8):
            rc1.place(x=100,y=330)
            g11.place(x=100009,y=330)
        if(len(V)==2 and Rr<=8):
            rc2.place(x=170,y=330)
            g12.place(x=10000,y=400)
        if(len(V)==3 and Rr<=8):
            rc3.place(x=240,y=330)
            g13.place(x=1233200,y=470)
        if(len(V)==4 and Rr<=8):
            rc4.place(x=100,y=400)
            g14.place(x=17242240,y=330)
           
        if(len(V)==5 and Rr<=8):
            rc6.place(x=240,y=400)
            g16.place(x=172320,y=470)
        if(len(V)==6 and Rr<=8):
            rc7.place(x=100,y=470)
            g17.place(x=2234240,y=330)
        if(len(V)==7 and Rr<=8):
            rc8.place(x=170,y=470)
            g18.place(x=24120,y=400)
            print(position)
        if(len(V)==8 and Rr<=8):
            rc9.place(x=240,y=470)
            g19.place(x=22240,y=470)
        if(len(V)==9 and Rr<=8):
            rc21.place(x=360,y=330)
            g21.place(x=312260,y=330)
        if(len(V)==10 and Rr<=8):
            rc22.place(x=430,y=330)
            g22.place(x=30060,y=400)
        if(len(V)==11 and Rr<=8):
            rc23.place(x=500,y=330)
            g23.place(x=36990,y=470)
        if(len(V)==12 and Rr<=8):
            rc24.place(x=360,y=400)
            g24.place(x=43000,y=330)
        if(len(V)==13 and Rr<=8):
            rc26.place(x=500,y=400)
            g26.place(x=430000,y=470)
        if(len(V)==14 and Rr<=8):
            rc27.place(x=360,y=470)
            g27.place(x=50990,y=3030)
        if(len(V)==15 and Rr<=8):
            rc28.place(x=430,y=470)
            g28.place(x=50000,y=400)
        if(len(V)==16 and Rr<=8):
            rc29.place(x=500,y=470)
            g29.place(x=59000,y=470)
        if(len(V)==17 and Rr<=8):
            rc31.place(x=620,y=330)
            g31.place(x=69920,y=330)
        if(len(V)==18 and Rr<=8):
            rc32.place(x=690,y=330)
            g32.place(x=629990,y=400)
        if(len(V)==19 and Rr<=8):
            rc33.place(x=760,y=330)
            g33.place(x=62000,y=470)
        if(len(V)==20 and Rr<=8):
            rc34.place(x=620,y=400)
            g34.place(x=612290,y=330)
        if(len(V)==21 and Rr<=8):
            rc36.place(x=760,y=400)
            g36.place(x=6900000,y=470)
        if(len(V)==22 and Rr<=8):
            rc37.place(x=620,y=470)
            g37.place(x=761120,y=330)
        if(len(V)==23 and Rr<=8):
            rc38.place(x=690,y=470)
            g38.place(x=70060,y=400)
        if(len(V)==24 and Rr<=8):
            rc39.place(x=760,y=470)
            g39.place(x=76000,y=470)
        if(len(V)==25 and Rr<=8):
            rc41.place(x=880,y=330)
            g41.place(x=88000,y=110)
        if(len(V)==26 and Rr<=8):
            rc42.place(x=950,y=330)
            g42.place(x=88000,y=180)
        if(len(V)==27 and Rr<=8):
            rc43.place(x=1020,y=330)
            g43.place(x=80080,y=250)
        if(len(V)==28 and Rr<=8):
            rc44.place(x=880,y=400)
            g44.place(x=95990,y=110)
        if(len(V)==29 and Rr<=8):
            rc46.place(x=1020,y=400)
            g46.place(x=95990,y=250)
        if(len(V)==30 and Rr<=8):
            rc47.place(x=880,y=470)
            g47.place(x=102000,y=110)
        if(len(V)==31 and Rr<=8):
            rc48.place(x=950,y=470)
            g48.place(x=199020,y=180)
        if(len(V)==32 and Rr<=8):
            rc49.place(x=1020,y=470)
            g49.place(x=1021230,y=250)
        if(len(V)==33 and Rr<=8):
            rc51.place(x=1140,y=330)
            g51.place(x=1112340,y=330)
        if(len(V)==34 and Rr<=8):
            rc52.place(x=1210,y=330)
            g52.place(x=1123140,y=400)
        if(len(V)==35 and Rr<=8):
            rc53.place(x=1280,y=330)
            g53.place(x=1123440,y=470)
        if(len(V)==36 and Rr<=8):
            rc54.place(x=1140,y=400)
            g54.place(x=1299910,y=330)
        if(len(V)==37 and Rr<=8):
            rc56.place(x=1280,y=400)
            g56.place(x=12137730,y=470)
        if(len(V)==38 and Rr<=8):
            rc57.place(x=1140,y=470)
            g57.place(x=1299980,y=330)
        if(len(V)==39 and Rr<=8):
            rc58.place(x=1210,y=470)
            g58.place(x=1299980,y=400)
        if(len(V)==40 and Rr<=8):
            rc59.place(x=1280,y=470)
            g59.place(x=129980,y=470)
        if(len(V)==41 and Rr<=8):
            rc61.place(x=880,y=110)
            g61.place(x=889990,y=110)
        if(len(V)==42 and Rr<=8):
            rc62.place(x=950,y=110)
            g62.place(x=95099,y=110)
        if(len(V)==43 and Rr<=8):
            rc63.place(x=1020,y=110)
            g63.place(x=1029990,y=110)
        if(len(V)==44 and Rr<=8):
            rc64.place(x=880,y=180)
            g64.place(x=88990,y=180)
        if(len(V)==45 and Rr<=8):
            rc66.place(x=1020,y=180)
            g66.place(x=102000,y=180)
        if(len(V)==46 and Rr<=8):
            rc67.place(x=880,y=250)
            g67.place(x=88000,y=250)
        if(len(V)==47 and Rr<=8):
            rc68.place(x=950,y=250)
            g68.place(x=95000,y=250)
        if(len(V)==48 and Rr<=8):
            rc69.place(x=1020,y=250)
            g69.place(x=1020000,y=250)
            SOLUTION()
def BLUE():
    global V,Br,position
   
    if(len(V)<=52):
        position.append('B')
        V=V+'B'
        Br=Br+1
        print(V)
        if(Br==8):
            blue['state']= DISABLED
        if(len(V)==1 and Br<=8):
            bc1.place(x=100,y=330)
            g11.place(x=100009,y=330)
        if(len(V)==2 and Br<=8):
            bc2.place(x=170,y=330)
            g12.place(x=10000,y=400)
        if(len(V)==3 and Br<=8):
            bc3.place(x=240,y=330)
            g13.place(x=1233200,y=470)
        if(len(V)==4 and Br<=8):
            bc4.place(x=100,y=400)
            g14.place(x=17242240,y=330)
           
        if(len(V)==5 and Br<=8):
            bc6.place(x=240,y=400)
            g16.place(x=172320,y=470)
        if(len(V)==6 and Br<=8):
            bc7.place(x=100,y=470)
            g17.place(x=2234240,y=330)
        if(len(V)==7 and Br<=8):
            bc8.place(x=170,y=470)
            g18.place(x=24120,y=400)
        if(len(V)==8 and Br<=8):
            bc9.place(x=240,y=470)
            g19.place(x=22240,y=470)
        if(len(V)==9 and Br<=8):
            bc21.place(x=360,y=330)
            g21.place(x=312260,y=330)
        if(len(V)==10 and Br<=8):
            bc22.place(x=430,y=330)
            g22.place(x=30060,y=400)
        if(len(V)==11 and Br<=8):
            bc23.place(x=500,y=330)
            g23.place(x=36990,y=470)
        if(len(V)==12 and Br<=8):
            bc24.place(x=360,y=400)
            g24.place(x=43000,y=330)
        if(len(V)==13 and Br<=8):
            bc26.place(x=500,y=400)
            g26.place(x=430000,y=470)
        if(len(V)==14 and Br<=8):
            bc27.place(x=360,y=470)
            g27.place(x=50990,y=3030)
        if(len(V)==15 and Br<=8):
            bc28.place(x=430,y=470)
            g28.place(x=50000,y=400)
        if(len(V)==16 and Br<=8):
            bc29.place(x=500,y=470)
            g29.place(x=59000,y=470)
        if(len(V)==17 and Br<=8):
            bc31.place(x=620,y=330)
            g31.place(x=69920,y=330)
        if(len(V)==18 and Br<=8):
            bc32.place(x=690,y=330)
            g32.place(x=629990,y=400)
        if(len(V)==19 and Br<=8):
            bc33.place(x=760,y=330)
            g33.place(x=62000,y=470)
        if(len(V)==20 and Br<=8):
            bc34.place(x=620,y=400)
            g34.place(x=612290,y=330)
        if(len(V)==21 and Br<=8):
            bc36.place(x=760,y=400)
            g36.place(x=6900000,y=470)
        if(len(V)==22 and Br<=8):
            bc37.place(x=620,y=470)
            g37.place(x=761120,y=330)
        if(len(V)==23 and Br<=8):
            bc38.place(x=690,y=470)
            g38.place(x=70060,y=400)
        if(len(V)==24 and Br<=8):
            bc39.place(x=760,y=470)
            g39.place(x=76000,y=470)
        if(len(V)==25 and Br<=8):
            bc41.place(x=880,y=330)
            g41.place(x=88000,y=110)
        if(len(V)==26 and Br<=8):
            bc42.place(x=950,y=330)
            g42.place(x=88000,y=180)
        if(len(V)==27 and Br<=8):
            bc43.place(x=1020,y=330)
            g43.place(x=80080,y=250)
        if(len(V)==28 and Br<=8):
            bc44.place(x=880,y=400)
            g44.place(x=95990,y=110)
        if(len(V)==29 and Br<=8):
            bc46.place(x=1020,y=400)
            g46.place(x=95990,y=250)
        if(len(V)==30 and Br<=8):
            bc47.place(x=880,y=470)
            g47.place(x=102000,y=110)
        if(len(V)==31 and Br<=8):
            bc48.place(x=950,y=470)
            g48.place(x=199020,y=180)
        if(len(V)==32 and Br<=8):
            bc49.place(x=1020,y=470)
            g49.place(x=1021230,y=250)
        if(len(V)==33 and Br<=8):
            bc51.place(x=1140,y=330)
            g51.place(x=1112340,y=330)
        if(len(V)==34 and Br<=8):
            bc52.place(x=1210,y=330)
            g52.place(x=1123140,y=400)
        if(len(V)==35 and Br<=8):
            bc53.place(x=1280,y=330)
            g53.place(x=1123440,y=470)
        if(len(V)==36 and Br<=8):
            bc54.place(x=1140,y=400)
            g54.place(x=1299910,y=330)
        if(len(V)==37 and Br<=8):
            bc56.place(x=1280,y=400)
            g56.place(x=12137730,y=470)
        if(len(V)==38 and Br<=8):
            bc57.place(x=1140,y=470)
            g57.place(x=1299980,y=330)
        if(len(V)==39 and Br<=8):
            bc58.place(x=1210,y=470)
            g58.place(x=1299980,y=400)
        if(len(V)==40 and Br<=8):
            bc59.place(x=1280,y=470)
            g59.place(x=129980,y=470)
        if(len(V)==41 and Br<=8):
            bc61.place(x=880,y=110)
            g61.place(x=889990,y=110)
        if(len(V)==42 and Br<=8):
            bc62.place(x=950,y=110)
            g62.place(x=95099,y=110)
        if(len(V)==43 and Br<=8):
            bc63.place(x=1020,y=110)
            g63.place(x=1029990,y=110)
        if(len(V)==44 and Br<=8):
            bc64.place(x=880,y=180)
            g64.place(x=88990,y=180)
        if(len(V)==45 and Br<=8):
            bc66.place(x=1020,y=180)
            g66.place(x=102000,y=180)
        if(len(V)==46 and Br<=8):
            bc67.place(x=880,y=250)
            g67.place(x=88000,y=250)
        if(len(V)==47 and Br<=8):
            bc68.place(x=950,y=250)
            g68.place(x=95000,y=250)
        if(len(V)==48 and Br<=8):
            bc69.place(x=1020,y=250)
            g69.place(x=1020000,y=250)
            SOLUTION()


def GREEN():
    global V,Gr,position
    
    if(len(V)<=52):
        position.append('G')
        V=V+'G'
        Gr=Gr+1
        print(V)
        if(Gr==8):
            green['state']= DISABLED
        if(len(V)==1 and Gr<=8):
            gc1.place(x=100,y=330)
            g11.place(x=100009,y=330)
        if(len(V)==2 and Gr<=8):
            gc2.place(x=170,y=330)
            g12.place(x=10000,y=400)
        if(len(V)==3 and Gr<=8):
            gc3.place(x=240,y=330)
            g13.place(x=1233200,y=470)
        if(len(V)==4 and Gr<=8):
            gc4.place(x=100,y=400)
            g14.place(x=17242240,y=330)
           
        if(len(V)==5 and Gr<=8):
            gc6.place(x=240,y=400)
            g16.place(x=172320,y=470)
        if(len(V)==6 and Gr<=8):
            gc7.place(x=100,y=470)
            g17.place(x=2234240,y=330)
        if(len(V)==7 and Gr<=8):
            gc8.place(x=170,y=470)
            g18.place(x=24120,y=400)
        if(len(V)==8 and Gr<=8):
            gc9.place(x=240,y=470)
            g19.place(x=22240,y=470)
        if(len(V)==9 and Gr<=8):
            gc21.place(x=360,y=330)
            g21.place(x=312260,y=330)
        if(len(V)==10 and Gr<=8):
            gc22.place(x=430,y=330)
            g22.place(x=30060,y=400)
        if(len(V)==11 and Gr<=8):
            gc23.place(x=500,y=330)
            g23.place(x=36990,y=470)
        if(len(V)==12 and Gr<=8):
            gc24.place(x=360,y=400)
            g24.place(x=43000,y=330)
        if(len(V)==13 and Gr<=8):
            gc26.place(x=500,y=400)
            g26.place(x=430000,y=470)
        if(len(V)==14 and Gr<=8):
            gc27.place(x=360,y=470)
            g27.place(x=50990,y=3030)
        if(len(V)==15 and Gr<=8):
            gc28.place(x=430,y=470)
            g28.place(x=50000,y=400)
        if(len(V)==16 and Gr<=8):
            gc29.place(x=500,y=470)
            g29.place(x=59000,y=470)
        if(len(V)==17 and Gr<=8):
            gc31.place(x=620,y=330)
            g31.place(x=69920,y=330)
        if(len(V)==18 and Gr<=8):
            gc32.place(x=690,y=330)
            g32.place(x=629990,y=400)
        if(len(V)==19 and Gr<=8):
            gc33.place(x=760,y=330)
            g33.place(x=62000,y=470)
        if(len(V)==20 and Gr<=8):
            gc34.place(x=620,y=400)
            g34.place(x=612290,y=330)
        if(len(V)==21 and Gr<=8):
            gc36.place(x=760,y=400)
            g36.place(x=6900000,y=470)
        if(len(V)==22 and Gr<=8):
            gc37.place(x=620,y=470)
            g37.place(x=761120,y=330)
        if(len(V)==23 and Gr<=8):
            gc38.place(x=690,y=470)
            g38.place(x=70060,y=400)
        if(len(V)==24 and Gr<=8):
            gc39.place(x=760,y=470)
            g39.place(x=76000,y=470)
        if(len(V)==25 and Gr<=8):
            gc41.place(x=880,y=330)
            g41.place(x=88000,y=110)
        if(len(V)==26 and Gr<=8):
            gc42.place(x=950,y=330)
            g42.place(x=88000,y=180)
        if(len(V)==27 and Gr<=8):
            gc43.place(x=1020,y=330)
            g43.place(x=80080,y=250)
        if(len(V)==28 and Gr<=8):
            gc44.place(x=880,y=400)
            g44.place(x=95990,y=110)
        if(len(V)==29 and Gr<=8):
            gc46.place(x=1020,y=400)
            g46.place(x=95990,y=250)
        if(len(V)==30 and Gr<=8):
            gc47.place(x=880,y=470)
            g47.place(x=102000,y=110)
        if(len(V)==31 and Gr<=8):
            gc48.place(x=950,y=470)
            g48.place(x=199020,y=180)
        if(len(V)==32 and Gr<=8):
            gc49.place(x=1020,y=470)
            g49.place(x=1021230,y=250)
        if(len(V)==33 and Gr<=8):
            gc51.place(x=1140,y=330)
            g51.place(x=1112340,y=330)
        if(len(V)==34 and Gr<=8):
            gc52.place(x=1210,y=330)
            g52.place(x=1123140,y=400)
        if(len(V)==35 and Gr<=8):
            gc53.place(x=1280,y=330)
            g53.place(x=1123440,y=470)
        if(len(V)==36 and Gr<=8):
            gc54.place(x=1140,y=400)
            g54.place(x=1299910,y=330)
        if(len(V)==37 and Gr<=8):
            gc56.place(x=1280,y=400)
            g56.place(x=12137730,y=470)
        if(len(V)==38 and Gr<=8):
            gc57.place(x=1140,y=470)
            g57.place(x=1299980,y=330)
        if(len(V)==39 and Gr<=8):
            gc58.place(x=1210,y=470)
            g58.place(x=1299980,y=400)
        if(len(V)==40 and Gr<=8):
            gc59.place(x=1280,y=470)
            g59.place(x=129980,y=470)
        if(len(V)==41 and Gr<=8):
            gc61.place(x=880,y=110)
            g61.place(x=889990,y=110)
        if(len(V)==42 and Gr<=8):
            gc62.place(x=950,y=110)
            g62.place(x=95099,y=110)
        if(len(V)==43 and Gr<=8):
            gc63.place(x=1020,y=110)
            g63.place(x=1029990,y=110)
        if(len(V)==44 and Gr<=8):
            gc64.place(x=880,y=180)
            g64.place(x=88990,y=180)
        if(len(V)==45 and Gr<=8):
            gc66.place(x=1020,y=180)
            g66.place(x=102000,y=180)
        if(len(V)==46 and Gr<=8):
            gc67.place(x=880,y=250)
            g67.place(x=88000,y=250)
        if(len(V)==47 and Gr<=8):
            gc68.place(x=950,y=250)
            g68.place(x=95000,y=250)
        if(len(V)==48 and Gr<=8):
            gc69.place(x=1020,y=250)
            g69.place(x=1020000,y=250)
            SOLUTION()

def WHITE():
    global V,Wr,position
   
    if(len(V)<=52):
        position.append('W')
        V=V+'W'
        Wr=Wr+1
        print(V)
        if(Wr==8):
            white['state']= DISABLED
        if(len(V)==1 and Wr<=8):
            wc1.place(x=100,y=330)
            g11.place(x=100009,y=330)
        if(len(V)==2 and Wr<=8):
            wc2.place(x=170,y=330)
            g12.place(x=10000,y=400)
        if(len(V)==3 and Wr<=8):
            wc3.place(x=240,y=330)
            g13.place(x=1233200,y=470)
        if(len(V)==4 and Wr<=8):
            wc4.place(x=100,y=400)
            g14.place(x=17242240,y=330)
            
        if(len(V)==5 and Wr<=8):
            wc6.place(x=240,y=400)
            g16.place(x=172320,y=470)
        if(len(V)==6 and Wr<=8):
            wc7.place(x=100,y=470)
            g17.place(x=2234240,y=330)
        if(len(V)==7 and Wr<=8):
            wc8.place(x=170,y=470)
            g18.place(x=24120,y=400)
        if(len(V)==8 and Wr<=8):
            wc9.place(x=240,y=470)
            g19.place(x=22240,y=470)
        if(len(V)==9 and Wr<=8):
            wc21.place(x=360,y=330)
            g21.place(x=312260,y=330)
        if(len(V)==10 and Wr<=8):
            wc22.place(x=430,y=330)
            g22.place(x=30060,y=400)
        if(len(V)==11 and Wr<=8):
            wc23.place(x=500,y=330)
            g23.place(x=36990,y=470)
        if(len(V)==12 and Wr<=8):
            wc24.place(x=360,y=400)
            g24.place(x=43000,y=330)
        if(len(V)==13 and Wr<=8):
            wc26.place(x=500,y=400)
            g26.place(x=430000,y=470)
        if(len(V)==14 and Wr<=8):
            wc27.place(x=360,y=470)
            g27.place(x=50990,y=3030)
        if(len(V)==15 and Wr<=8):
            wc28.place(x=430,y=470)
            g28.place(x=50000,y=400)
        if(len(V)==16 and Wr<=8):
            wc29.place(x=500,y=470)
            g29.place(x=59000,y=470)
        if(len(V)==17 and Wr<=8):
            wc31.place(x=620,y=330)
            g31.place(x=69920,y=330)
        if(len(V)==18 and Wr<=8):
            wc32.place(x=690,y=330)
            g32.place(x=629990,y=400)
        if(len(V)==19 and Wr<=8):
            wc33.place(x=760,y=330)
            g33.place(x=62000,y=470)
        if(len(V)==20 and Wr<=8):
            wc34.place(x=620,y=400)
            g34.place(x=612290,y=330)
        if(len(V)==21 and Wr<=8):
            wc36.place(x=760,y=400)
            g36.place(x=6900000,y=470)
        if(len(V)==22 and Wr<=8):
            wc37.place(x=620,y=470)
            g37.place(x=761120,y=330)
        if(len(V)==23 and Wr<=8):
            wc38.place(x=690,y=470)
            g38.place(x=70060,y=400)
        if(len(V)==24 and Wr<=8):
            wc39.place(x=760,y=470)
            g39.place(x=76000,y=470)
        if(len(V)==25 and Wr<=8):
            wc41.place(x=880,y=330)
            g41.place(x=88000,y=110)
        if(len(V)==26 and Wr<=8):
            wc42.place(x=950,y=330)
            g42.place(x=88000,y=180)
        if(len(V)==27 and Wr<=8):
            wc43.place(x=1020,y=330)
            g43.place(x=80080,y=250)
        if(len(V)==28 and Wr<=8):
            wc44.place(x=880,y=400)
            g44.place(x=95990,y=110)
        if(len(V)==29 and Wr<=8):
            wc46.place(x=1020,y=400)
            g46.place(x=95990,y=250)
        if(len(V)==30 and Wr<=8):
            wc47.place(x=880,y=470)
            g47.place(x=102000,y=110)
        if(len(V)==31 and Wr<=8):
            wc48.place(x=950,y=470)
            g48.place(x=199020,y=180)
        if(len(V)==32 and Wr<=8):
            wc49.place(x=1020,y=470)
            g49.place(x=1021230,y=250)
        if(len(V)==33 and Wr<=8):
            wc51.place(x=1140,y=330)
            g51.place(x=1112340,y=330)
        if(len(V)==34 and Wr<=8):
            wc52.place(x=1210,y=330)
            g52.place(x=1123140,y=400)
        if(len(V)==35 and Wr<=8):
            wc53.place(x=1280,y=330)
            g53.place(x=1123440,y=470)
        if(len(V)==36 and Wr<=8):
            wc54.place(x=1140,y=400)
            g54.place(x=1299910,y=330)
        if(len(V)==37 and Wr<=8):
            wc56.place(x=1280,y=400)
            g56.place(x=12137730,y=470)
        if(len(V)==38 and Wr<=8):
            wc57.place(x=1140,y=470)
            g57.place(x=1299980,y=330)
        if(len(V)==39 and Wr<=8):
            wc58.place(x=1210,y=470)
            g58.place(x=1299980,y=400)
        if(len(V)==40 and Wr<=8):
            wc59.place(x=1280,y=470)
            g59.place(x=129980,y=470)
        if(len(V)==41 and Wr<=8):
            wc61.place(x=880,y=110)
            g61.place(x=889990,y=110)
        if(len(V)==42 and Wr<=8):
            wc62.place(x=950,y=110)
            g62.place(x=95099,y=110)
        if(len(V)==43 and Wr<=8):
            wc63.place(x=1020,y=110)
            g63.place(x=1029990,y=110)
        if(len(V)==44 and Wr<=8):
            wc64.place(x=880,y=180)
            g64.place(x=88990,y=180)
        if(len(V)==45 and Wr<=8):
            wc66.place(x=1020,y=180)
            g66.place(x=102000,y=180)
        if(len(V)==46 and Wr<=8):
            wc67.place(x=880,y=250)
            g67.place(x=88000,y=250)
        if(len(V)==47 and Wr<=8):
            wc68.place(x=950,y=250)
            g68.place(x=95000,y=250)
        if(len(V)==48 and Wr<=8):
            wc69.place(x=1020,y=250)
            g69.place(x=1020000,y=250)
            SOLUTION()

def ORANGE():
    global V,Or,position
    
    if(len(V)<=52):
        position.append('O')
        V=V+'O'
        Or=Or+1
        print(V)
        if(Or==8):
            orange['state']= DISABLED
        if(len(V)==1 and Or<=8):
            oc1.place(x=100,y=330)
            g11.place(x=100009,y=330)
        if(len(V)==2 and Or<=8):
            oc2.place(x=170,y=330)
            g12.place(x=10000,y=400)
        if(len(V)==3 and Or<=8):
            oc3.place(x=240,y=330)
            g13.place(x=1233200,y=470)
        if(len(V)==4 and Or<=8):
            oc4.place(x=100,y=400)
            g14.place(x=17242240,y=330)
           
        if(len(V)==5 and Or<=8):
            oc6.place(x=240,y=400)
            g16.place(x=172320,y=470)
        if(len(V)==6 and Or<=8):
            oc7.place(x=100,y=470)
            g17.place(x=2234240,y=330)
        if(len(V)==7 and Or<=8):
            oc8.place(x=170,y=470)
            g18.place(x=24120,y=400)
        if(len(V)==8 and Or<=8):
            oc9.place(x=240,y=470)
            g19.place(x=22240,y=470)
        if(len(V)==9 and Or<=8):
            oc21.place(x=360,y=330)
            g21.place(x=312260,y=330)
        if(len(V)==10 and Or<=8):
            oc22.place(x=430,y=330)
            g22.place(x=30060,y=400)
        if(len(V)==11 and Or<=8):
            oc23.place(x=500,y=330)
            g23.place(x=36990,y=470)
        if(len(V)==12 and Or<=8):
            oc24.place(x=360,y=400)
            g24.place(x=43000,y=330)
        if(len(V)==13 and Or<=8):
            oc26.place(x=500,y=400)
            g26.place(x=430000,y=470)
        if(len(V)==14 and Or<=8):
            oc27.place(x=360,y=470)
            g27.place(x=50990,y=3030)
        if(len(V)==15 and Or<=8):
            oc28.place(x=430,y=470)
            g28.place(x=50000,y=400)
        if(len(V)==16 and Or<=8):
            oc29.place(x=500,y=470)
            g29.place(x=59000,y=470)
        if(len(V)==17 and Or<=8):
            oc31.place(x=620,y=330)
            g31.place(x=69920,y=330)
        if(len(V)==18 and Or<=8):
            oc32.place(x=690,y=330)
            g32.place(x=629990,y=400)
        if(len(V)==19 and Or<=8):
            oc33.place(x=760,y=330)
            g33.place(x=62000,y=470)
        if(len(V)==20 and Or<=8):
            oc34.place(x=620,y=400)
            g34.place(x=612290,y=330)
        if(len(V)==21 and Or<=8):
            oc36.place(x=760,y=400)
            g36.place(x=6900000,y=470)
        if(len(V)==22 and Or<=8):
            oc37.place(x=620,y=470)
            g37.place(x=761120,y=330)
        if(len(V)==23 and Or<=8):
            oc38.place(x=690,y=470)
            g38.place(x=70060,y=400)
        if(len(V)==24 and Or<=8):
            oc39.place(x=760,y=470)
            g39.place(x=76000,y=470)
        if(len(V)==25 and Or<=8):
            oc41.place(x=880,y=330)
            g41.place(x=88000,y=110)
        if(len(V)==26 and Or<=8):
            oc42.place(x=950,y=330)
            g42.place(x=88000,y=180)
        if(len(V)==27 and Or<=8):
            oc43.place(x=1020,y=330)
            g43.place(x=80080,y=250)
        if(len(V)==28 and Or<=8):
            oc44.place(x=880,y=400)
            g44.place(x=95990,y=110)
        if(len(V)==29 and Or<=8):
            oc46.place(x=1020,y=400)
            g46.place(x=95990,y=250)
        if(len(V)==30 and Or<=8):
            oc47.place(x=880,y=470)
            g47.place(x=102000,y=110)
        if(len(V)==31 and Or<=8):
            oc48.place(x=950,y=470)
            g48.place(x=199020,y=180)
        if(len(V)==32 and Or<=8):
            oc49.place(x=1020,y=470)
            g49.place(x=1021230,y=250)
        if(len(V)==33 and Or<=8):
            oc51.place(x=1140,y=330)
            g51.place(x=1112340,y=330)
        if(len(V)==34 and Or<=8):
            oc52.place(x=1210,y=330)
            g52.place(x=1123140,y=400)
        if(len(V)==35 and Or<=8):
            oc53.place(x=1280,y=330)
            g53.place(x=1123440,y=470)
        if(len(V)==36 and Or<=8):
            oc54.place(x=1140,y=400)
            g54.place(x=1299910,y=330)
        if(len(V)==37 and Or<=8):
            oc56.place(x=1280,y=400)
            g56.place(x=12137730,y=470)
        if(len(V)==38 and Or<=8):
            oc57.place(x=1140,y=470)
            g57.place(x=1299980,y=330)
        if(len(V)==39 and Or<=8):
            oc58.place(x=1210,y=470)
            g58.place(x=1299980,y=400)
        if(len(V)==40 and Or<=8):
            oc59.place(x=1280,y=470)
            g59.place(x=129980,y=470)
        if(len(V)==41 and Or<=8):
            oc61.place(x=880,y=110)
            g61.place(x=889990,y=110)
        if(len(V)==42 and Or<=8):
            oc62.place(x=950,y=110)
            g62.place(x=95099,y=110)
        if(len(V)==43 and Or<=8):
            oc63.place(x=1020,y=110)
            g63.place(x=1029990,y=110)
        if(len(V)==44 and Or<=8):
            oc64.place(x=880,y=180)
            g64.place(x=88990,y=180)
        if(len(V)==45 and Or<=8):
            oc66.place(x=1020,y=180)
            g66.place(x=102000,y=180)
        if(len(V)==46 and Or<=8):
            oc67.place(x=880,y=250)
            g67.place(x=88000,y=250)
        if(len(V)==47 and Or<=8):
            oc68.place(x=950,y=250)
            g68.place(x=95000,y=250)
        if(len(V)==48 and Or<=8):
            oc69.place(x=1020,y=250)
            g69.place(x=1020000,y=250)
            SOLUTION()

def YELLOW():
    global V,Yr,position

    if(len(V)<=52):
        position.append('Y')
        V=V+'Y'
        Yr=Yr+1
        print(V)
        if(Yr==8):
            yellow['state']= DISABLED
        if(len(V)==1 and Yr<=8):
            yc1.place(x=100,y=330)
            g11.place(x=100009,y=330)
        if(len(V)==2 and Yr<=8):
            yc2.place(x=170,y=330)
            g12.place(x=10000,y=400)
        if(len(V)==3 and Yr<=8):
            yc3.place(x=240,y=330)
            g13.place(x=1233200,y=470)
        if(len(V)==4 and Yr<=8):
            yc4.place(x=100,y=400)
            g14.place(x=17242240,y=330)
          
        if(len(V)==5 and Yr<=8):
            yc6.place(x=240,y=400)
            g16.place(x=172320,y=470)
        if(len(V)==6 and Yr<=8):
            yc7.place(x=100,y=470)
            g17.place(x=2234240,y=330)
        if(len(V)==7 and Yr<=8):
            yc8.place(x=170,y=470)
            g18.place(x=24120,y=400)
        if(len(V)==8 and Yr<=8):
            yc9.place(x=240,y=470)
            g19.place(x=22240,y=470)
        if(len(V)==9 and Yr<=8):
            yc21.place(x=360,y=330)
            g21.place(x=312260,y=330)
        if(len(V)==10 and Yr<=8):
            yc22.place(x=430,y=330)
            g22.place(x=30060,y=400)
        if(len(V)==11 and Yr<=8):
            yc23.place(x=500,y=330)
            g23.place(x=36990,y=470)
        if(len(V)==12 and Yr<=8):
            yc24.place(x=360,y=400)
            g24.place(x=43000,y=330)
        if(len(V)==13 and Yr<=8):
            yc26.place(x=500,y=400)
            g26.place(x=430000,y=470)
        if(len(V)==14 and Yr<=8):
            yc27.place(x=360,y=470)
            g27.place(x=5090,y=3030)
        if(len(V)==15 and Yr<=8):
            yc28.place(x=430,y=470)
            g28.place(x=50000,y=400)
        if(len(V)==16 and Yr<=8):
            yc29.place(x=500,y=470)
            g29.place(x=59000,y=470)
        if(len(V)==17 and Yr<=8):
            yc31.place(x=620,y=330)
            g31.place(x=69920,y=330)
        if(len(V)==18 and Yr<=8):
            yc32.place(x=690,y=330)
            g32.place(x=629990,y=400)
        if(len(V)==19 and Yr<=8):
            yc33.place(x=760,y=330)
            g33.place(x=62000,y=470)
        if(len(V)==20 and Yr<=8):
            yc34.place(x=620,y=400)
            g34.place(x=612290,y=330)
        if(len(V)==21 and Yr<=8):
            yc36.place(x=760,y=400)
            g36.place(x=6900000,y=470)
        if(len(V)==22 and Yr<=8):
            yc37.place(x=620,y=470)
            g37.place(x=761120,y=330)
        if(len(V)==23 and Yr<=8):
            yc38.place(x=690,y=470)
            g38.place(x=70060,y=400)
        if(len(V)==24 and Yr<=8):
            yc39.place(x=760,y=470)
            g39.place(x=76000,y=470)
        if(len(V)==25 and Yr<=8):
            yc41.place(x=880,y=330)
            g41.place(x=88000,y=110)
        if(len(V)==26 and Yr<=8):
            yc42.place(x=950,y=330)
            g42.place(x=88000,y=180)
        if(len(V)==27 and Yr<=8):
            yc43.place(x=1020,y=330)
            g43.place(x=80080,y=250)
        if(len(V)==28 and Yr<=8):
            yc44.place(x=880,y=400)
            g44.place(x=95990,y=110)
        if(len(V)==29 and Yr<=8):
            yc46.place(x=1020,y=400)
            g46.place(x=95990,y=250)
        if(len(V)==30 and Yr<=8):
            yc47.place(x=880,y=470)
            g47.place(x=102000,y=110)
        if(len(V)==31 and Yr<=8):
            yc48.place(x=950,y=470)
            g48.place(x=199020,y=180)
        if(len(V)==32 and Yr<=8):
            yc49.place(x=1020,y=470)
            g49.place(x=1021230,y=250)
        if(len(V)==33 and Yr<=8):
            yc51.place(x=1140,y=330)
            g51.place(x=1112340,y=330)
        if(len(V)==34 and Yr<=8):
            yc52.place(x=1210,y=330)
            g52.place(x=1123140,y=400)
        if(len(V)==35 and Yr<=8):
            yc53.place(x=1280,y=330)
            g53.place(x=1123440,y=470)
        if(len(V)==36 and Yr<=8):
            yc54.place(x=1140,y=400)
            g54.place(x=1299910,y=330)
        if(len(V)==37 and Yr<=8):
            yc56.place(x=1280,y=400)
            g56.place(x=12137730,y=470)
        if(len(V)==38 and Yr<=8):
            yc57.place(x=1140,y=470)
            g57.place(x=1299980,y=330)
        if(len(V)==39 and Yr<=8):
            yc58.place(x=1210,y=470)
            g58.place(x=1299980,y=400)
        if(len(V)==40 and Yr<=8):
            yc59.place(x=1280,y=470)
            g59.place(x=129980,y=470)
        if(len(V)==41 and Yr<=8):
            yc61.place(x=880,y=110)
            g61.place(x=889990,y=110)
        if(len(V)==42 and Yr<=8):
            yc62.place(x=950,y=110)
            g62.place(x=95099,y=110)
        if(len(V)==43 and Yr<=8):
            yc63.place(x=1020,y=110)
            g63.place(x=1029990,y=110)
        if(len(V)==44 and Yr<=8):
            yc64.place(x=880,y=180)
            g64.place(x=88990,y=180)
        if(len(V)==45 and Yr<=8):
            yc66.place(x=1020,y=180)
            g66.place(x=102000,y=180)
        if(len(V)==46 and Yr<=8):
            yc67.place(x=880,y=250)
            g67.place(x=88000,y=250)
        if(len(V)==47 and Yr<=8):
            yc68.place(x=950,y=250)
            g68.place(x=95000,y=250)
        if(len(V)==48 and Yr<=8):
            yc69.place(x=1020,y=250)
            g69.place(x=1020000,y=250)
            SOLUTION()
def right():
    global position,final,solmoves
    
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print("r")
    solmoves.append("r")
    


    
    
    


    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[42]
    temp[3]=position[3]
    temp[4]=position[44]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[47]
    temp[8]=position[13]
    temp[9]=position[11]
    temp[10]=position[8]
    temp[11]=position[14]
    temp[12]=position[9]
    temp[13]=position[15]
    temp[14]=position[12]
    temp[15]=position[10]
    temp[16]=position[39]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[36]
    temp[20]=position[20]
    temp[21]=position[34]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[2]
    temp[35]=position[35]
    temp[36]=position[4]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[7]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[21]
    temp[43]=position[43]
    temp[44]=position[19]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[16]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    
        
    

    
    

    
    
    
    
    
    print(position)

    return position

def right1():
    global position,final,solutionlabel,solmoves
    solmoves.append("r1")

    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print("r1")
    

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[34]
    temp[3]=position[3]
    temp[4]=position[36]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[39]
    temp[8]=position[10]
    temp[9]=position[12]
    temp[10]=position[15]
    temp[11]=position[9]
    temp[12]=position[14]
    temp[13]=position[8]
    temp[14]=position[11]
    temp[15]=position[13]
    temp[16]=position[47]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[44]
    temp[20]=position[20]
    temp[21]=position[42]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[21]
    temp[35]=position[35]
    temp[36]=position[19]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[16]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[2]
    temp[43]=position[43]
    temp[44]=position[4]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[7]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    
    print(position)

    

   
       
    
    return position


def l():
    global position,final,solutionlabel,solmoves
    solmoves.append("l")

    

    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print("l")
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[40]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[43]
    temp[4]=position[4]
    temp[5]=position[45]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[37]
    temp[19]=position[19]
    temp[20]=position[35]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[32]
    temp[24]=position[26]
    temp[25]=position[28]
    temp[26]=position[31]
    temp[27]=position[25]
    temp[28]=position[30]
    temp[29]=position[24]
    temp[30]=position[27]
    temp[31]=position[29]
    temp[32]=position[0]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[3]
    temp[36]=position[36]
    temp[37]=position[5]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[23]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[20]
    temp[44]=position[44]
    temp[45]=position[18]
    temp[46]=position[46]
    temp[47]=position[47]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)
    
   
    
    
    

   
    
       
    
    return position
def l1():
    
    global position,final,solutionlabel,solmoves
    solmoves.append("l1")
    print("l1")
 
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[32]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[35]
    temp[4]=position[4]
    temp[5]=position[37]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[45]
    temp[19]=position[19]
    temp[20]=position[43]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[40]
    temp[24]=position[29]
    temp[25]=position[27]
    temp[26]=position[24]
    temp[27]=position[30]
    temp[28]=position[25]
    temp[29]=position[31]
    temp[30]=position[28]
    temp[31]=position[26]
    temp[32]=position[23]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[20]
    temp[36]=position[36]
    temp[37]=position[18]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[0]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[3]
    temp[44]=position[44]
    temp[45]=position[5]
    temp[46]=position[46]
    temp[47]=position[47]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)

  
       
    
    return position
def u():
    global position,final,solutionlabel,solmoves
    solmoves.append("u")
    print("u")
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[8]
    temp[1]=position[9]
    temp[2]=position[10]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[16]
    temp[9]=position[17]
    temp[10]=position[18]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[24]
    temp[17]=position[25]
    temp[18]=position[26]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[0]
    temp[25]=position[1]
    temp[26]=position[2]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[37]
    temp[33]=position[35]
    temp[34]=position[32]
    temp[35]=position[38]
    temp[36]=position[33]
    temp[37]=position[39]
    temp[38]=position[36]
    temp[39]=position[34]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position) 
       
    
    return position
def u1():
    global position,final,solutionlabel,solmoves
    solmoves.append("u1")
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print("u1")
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[24]
    temp[1]=position[25]
    temp[2]=position[26]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[0]
    temp[9]=position[1]
    temp[10]=position[2]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[8]
    temp[17]=position[9]
    temp[18]=position[10]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[16]
    temp[25]=position[17]
    temp[26]=position[18]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[34]
    temp[33]=position[36]
    temp[34]=position[39]
    temp[35]=position[33]
    temp[36]=position[38]
    temp[37]=position[32]
    temp[38]=position[35]
    temp[39]=position[37]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)
       
    
    return position

def d():
    global position,final,solutionlabel,solmoves
    solmoves.append("d")
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    
    print("d")
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[13]
    temp[6]=position[14]
    temp[7]=position[15]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[21]
    temp[14]=position[22]
    temp[15]=position[23]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[29]
    temp[22]=position[30]
    temp[23]=position[31]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[5]
    temp[30]=position[6]
    temp[31]=position[7]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[42]
    temp[41]=position[44]
    temp[42]=position[47]
    temp[43]=position[41]
    temp[44]=position[46]
    temp[45]=position[40]
    temp[46]=position[43]
    temp[47]=position[45]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position) 
   
    
    return position

def d1():
    global position,final,solutionlabel,solmoves
    solmoves.append("d1")
    print("d1")
    
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[29]
    temp[6]=position[30]
    temp[7]=position[31]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[5]
    temp[14]=position[6]
    temp[15]=position[7]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[13]
    temp[22]=position[14]
    temp[23]=position[15]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[21]
    temp[30]=position[22]
    temp[31]=position[23]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[45]
    temp[41]=position[43]
    temp[42]=position[40]
    temp[43]=position[46]
    temp[44]=position[41]
    temp[45]=position[47]
    temp[46]=position[44]
    temp[47]=position[42]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
  
    print(position)
       
    
    return position

def f():
    global position,final,solutionlabel,solmoves
    solmoves.append("f")
    print("f")
    
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[5]
    temp[1]=position[3]
    temp[2]=position[0]
    temp[3]=position[6]
    temp[4]=position[1]
    temp[5]=position[7]
    temp[6]=position[4]
    temp[7]=position[2]
    temp[8]=position[37]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[38]
    temp[12]=position[12]
    temp[13]=position[39]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[40]
    temp[27]=position[27]
    temp[28]=position[41]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[42]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[31]
    temp[38]=position[28]
    temp[39]=position[26]
    temp[40]=position[13]
    temp[41]=position[11]
    temp[42]=position[8]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)
    
    return position

def f1():
    global position,final,solutionlabel,solmoves
    solmoves.append("f1")
    print("f1")
    
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[2]
    temp[1]=position[4]
    temp[2]=position[7]
    temp[3]=position[1]
    temp[4]=position[6]
    temp[5]=position[0]
    temp[6]=position[3]
    temp[7]=position[5]
    temp[8]=position[42]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[41]
    temp[12]=position[12]
    temp[13]=position[40]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[39]
    temp[27]=position[27]
    temp[28]=position[38]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[37]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[8]
    temp[38]=position[11]
    temp[39]=position[13]
    temp[40]=position[26]
    temp[41]=position[28]
    temp[42]=position[31]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)
    
              
    
    return position

def ba():
    global position,final,solutionlabel,solmoves
    solmoves.append("ba")
    print("ba")
    
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[32]
    temp[11]=position[11]
    temp[12]=position[33]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[34]
    temp[16]=position[18]
    temp[17]=position[20]
    temp[18]=position[23]
    temp[19]=position[17]
    temp[20]=position[22]
    temp[21]=position[16]
    temp[22]=position[19]
    temp[23]=position[21]
    temp[24]=position[45]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[46]
    temp[28]=position[28]
    temp[29]=position[47]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[29]
    temp[33]=position[27]
    temp[34]=position[24]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[15]
    temp[46]=position[12]
    temp[47]=position[10]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    position=temp
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)
    
   
       
    
    return position
def ba1():
    global position,final,solutionlabel,solmoves
    solmoves.append("ba1")
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    
    print("ba1")
    
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[10]
    temp[11]=position[11]
    temp[12]=position[12]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[15]
    temp[16]=position[16]
    temp[17]=position[17]
    temp[18]=position[18]
    temp[19]=position[19]
    temp[20]=position[20]
    temp[21]=position[21]
    temp[22]=position[22]
    temp[23]=position[23]
    temp[24]=position[24]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[27]
    temp[28]=position[28]
    temp[29]=position[29]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[32]
    temp[33]=position[33]
    temp[34]=position[34]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[45]
    temp[46]=position[46]
    temp[47]=position[47]
    temp[0]=position[0]
    temp[1]=position[1]
    temp[2]=position[2]
    temp[3]=position[3]
    temp[4]=position[4]
    temp[5]=position[5]
    temp[6]=position[6]
    temp[7]=position[7]
    temp[8]=position[8]
    temp[9]=position[9]
    temp[10]=position[47]
    temp[11]=position[11]
    temp[12]=position[46]
    temp[13]=position[13]
    temp[14]=position[14]
    temp[15]=position[45]
    temp[16]=position[21]
    temp[17]=position[19]
    temp[18]=position[16]
    temp[19]=position[22]
    temp[20]=position[17]
    temp[21]=position[23]
    temp[22]=position[20]
    temp[23]=position[18]
    temp[24]=position[34]
    temp[25]=position[25]
    temp[26]=position[26]
    temp[27]=position[33]
    temp[28]=position[28]
    temp[29]=position[32]
    temp[30]=position[30]
    temp[31]=position[31]
    temp[32]=position[10]
    temp[33]=position[12]
    temp[34]=position[15]
    temp[35]=position[35]
    temp[36]=position[36]
    temp[37]=position[37]
    temp[38]=position[38]
    temp[39]=position[39]
    temp[40]=position[40]
    temp[41]=position[41]
    temp[42]=position[42]
    temp[43]=position[43]
    temp[44]=position[44]
    temp[45]=position[24]
    temp[46]=position[27]
    temp[47]=position[29]
    position[0]=temp[0]
    position[1]=temp[1]
    position[2]=temp[2]
    position[3]=temp[3]
    position[4]=temp[4]
    position[5]=temp[5]
    position[6]=temp[6]
    position[7]=temp[7]
    position[8]=temp[8]
    position[9]=temp[9]
    position[10]=temp[10]
    position[11]=temp[11]
    position[12]=temp[12]
    position[13]=temp[13]
    position[14]=temp[14]
    position[15]=temp[15]
    position[16]=temp[16]
    position[17]=temp[17]
    position[18]=temp[18]
    position[19]=temp[19]
    position[20]=temp[20]
    position[21]=temp[21]
    position[22]=temp[22]
    position[23]=temp[23]
    position[24]=temp[24]
    position[25]=temp[25]
    position[26]=temp[26]
    position[27]=temp[27]
    position[28]=temp[28]
    position[29]=temp[29]
    position[30]=temp[30]
    position[31]=temp[31]
    position[32]=temp[32]
    position[33]=temp[33]
    position[34]=temp[34]
    position[35]=temp[35]
    position[36]=temp[36]
    position[37]=temp[37]
    position[38]=temp[38]
    position[39]=temp[39]
    position[40]=temp[40]
    position[41]=temp[41]
    position[42]=temp[42]
    position[43]=temp[43]
    position[44]=temp[44]
    position[45]=temp[45]
    position[46]=temp[46]
    position[47]=temp[47]
    temp=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
    print(position)
    
    

    return position
def SOLUTION():
    
    global positon,final
    final=['B','B','B','B','B','B','B','B','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W']
    print (position)
    while(position!=final):
        
        if(position[6]=='R' and position[41]=='W'):
            f(),d(),f1(),d1()
            print (position)
        if(position[30]=='R' and position[43]=='W'):
            l(),d(),d(),l1(),d(),d()
        if(position[22]=='R' and position[46]=='W'):
            ba(),d1(),ba1(),d()
        
        #white in base and blue in side:
        if(position[30]=='B' and position[43]=='W'):
             l(),d(),l1(),d1()

                
        if(position[22]=='B' and position[46]=='W'):
            ba(),d(),d(),ba1(),d(),d()
        if(position[14]=='B' and position[44]=='W'):
            right(),d1(),right1(),d()
        #white in base and green in side:
        if(position[6]=='G' and position[41]=='W'):
            f(),d(),d(),f1(),d(),d()
        if(position[30]=='G' and position[43]=='W'):
            l(),d1(),l1(),d()
        if(position[14]=='G' and position[44]=='W'):
            right(),d(),right1(),d()
               #white in base orange in sides:
        if(position[6]=='O' and position[41]=='W'):
            f(),d1(),f1(),d()
        if(position[14]=='O' and position[44]=='W'):
            right(),d(),d(),right1(),d(),d()
                
        if(position[46]=='O' and position[22]=='W'):
            ba(),d(),ba1(),d1()
        if(position[4]=='W' and position[11]=='B'):
            d1(), right1(), d()
        if(position[12]=='W' and position[19]=='B'):
            d(), d(), ba(), d(), d()
        if(position[20]=='W' and position[27]=='B'):
            d(), l(), d1()
        if(position[28]=='W' and position[3]=='B'):
            f1()
        if(position[4]=='W' and position[11]=='R'):
            right1()
        if(position[12]=='W' and position[19]=='R'):
            d1(), ba(), d()
        if(position[20]=='W' and position[27]=='R'):
            d(), d(), l(), d(), d()
        if(position[28]=='W' and position[3]=='R'):
            d(), f1(), d1()
        if(position[4]=='W' and position[11]=='G'):
            d(), right1(), d1()
        if(position[12]=='W' and position[19]=='G'):
            ba(), 
        if(position[20]=='W' and position[27]=='G'):
            d1(), l(), d()
        if(position[28]=='W' and position[3]=='G'):
            d(), d(), f1(), d(), d()
        if(position[4]=='W' and position[11]=='O'):
            d(), d(), right1(), d(), d()
        if(position[12]=='W' and position[19]=='O'):
            d(), ba(), d1()
        if(position[20]=='W' and position[27]=='O'):
            l()
        if(position[28]=='W' and position[3]=='O'):
            d1(), f1(), d()
        #White left in second layer
        if(position[3]=='W' and position[28]=='B'):
            d(), l1(), d1()
        if(position[27]=='W' and position[20]=='B'):
            d(), d(), ba1(), d(), d()
        if(position[19]=='W' and position[12]=='B'):
            d1(), right(), d()
        if(position[11]=='W' and position[4]=='B'):
            f()
        if(position[3]=='W' and position[28]=='R'):
            d1(), d1(), l1(), d(), d()
        if(position[27]=='W' and position[20]=='R'):
            d1(), ba1(), d()
        if(position[19]=='W' and position[12]=='R'):
            right()
        if(position[11]=='W' and position[4]=='R'):
           d(), f(), d1()
        if(position[3]=='W' and position[28]=='G'):
           d1(), l1(), d()
        if(position[27]=='W' and position[20]=='G'):
           ba1()
        if(position[19]=='W' and position[12]=='G'):
           d(), right(), d1()
        if(position[11]=='W' and position[4]=='G'):
           d(), d(), f(), d(), d()
        if(position[3]=='W' and position[28]=='O'):
            l1()
        if(position[27]=='W' and position[20]=='O'):
            d(), ba1(), d1()
        if(position[19]=='W' and position[12]=='O'):
            d(), d(), right(), d(), d()
        if(position[11]=='W' and position[4]=='O'):
            d1(), f(), d()
        if(position[1]=='W' and position[38]=='B'):
            u1(), right1(), f(), right()
        if(position[25]=='W' and position[35]=='B'):
            l1(), f1(), l()
        if(position[17]=='W' and position[33]=='B'):
            u(),right1(),f(),right()
        if(position[9]=='W' and position[36]=='B'):
            right1(), f(), right()
        if(position[1]=='W' and position[38]=='R'):
            f(), right1(), f1()
        if(position[25]=='W' and position[35]=='R'):
            u1(), f(), right1(), f1()
        if(position[17]=='W' and position[33]=='R'):
            u(), u(), f(), right1(), f1()
        if(position[9]=='W' and position[36]=='R'):
            u(),f(),right1(),f1()
           
        if(position[1]=='W' and position[38]=='G'):
            f(), d(), right1(), d1(), f1()
        if(position[25]=='W' and position[35]=='G'):
            u1(), d1(), f1(), l1(), f(), d()
        if(position[17]=='W' and position[33]=='G'):
            u(), right(), ba(), right1()
        if(position[9]=='W' and position[36]=='G'):
            right(), ba(), right1()
        if(position[1]=='W' and position[38]=='O'):
            f1(), l1(), f()
        if(position[25]=='W' and position[35]=='O'):
            u1(), f1(), l1(), f()
        if(position[17]=='W' and position[33]=='O'):
            u(), u(), f1(), l1(), f()
        if(position[9]=='W' and position[36]=='O'):
            u(), f1(), l1(), f()
        if(position[38]=='W' and position[1]=='B'):
            f(), f()
        if(position[35]=='W' and position[25]=='B'):
            u1(), f(), f()
        if(position[33]=='W' and position[17]=='B'):
            u(), u(), f(), f()
        if(position[36]=='W' and position[9]=='B'):
            u(), f(), f()
        if(position[38]=='W' and position[1]=='O'):
            u(), l(), l()
        if(position[35]=='W' and position[25]=='O'):
            l(), l()
        if(position[33]=='W' and position[17]=='O'):
            u1(), l(), l()
        if(position[36]=='W' and position[9]=='O'):
            u(), u(), l(), l()
        if(position[38]=='W' and position[1]=='G'):
            u(), u(), ba(), ba()
        if(position[35]=='W' and position[25]=='G'):
            u(), ba(), ba()
        if(position[33]=='W' and position[17]=='G'):
            ba(), ba()
        if(position[36]=='W' and position[9]=='G'):
            u1(), ba(), ba()
        if(position[38]=='W' and position[1]=='R'):
            u1(), right(), right()
        if(position[35]=='W' and position[25]=='R'):
            u(), u(), right(), right()
        if(position[33]=='W' and position[17]=='R'):
            u(), right(), right()
        if(position[36]=='W' and position[9]=='R'):
            right(), right()

       #First Layer now plus over    
        if(position[2]=='W' and position[39]=='B' and position[8]=='R'):
            u(), right(), u1(), right1()
        if(position[0]=='R' and position[26]=='W' and position[37]=='B'):
            right(), u1(), right1()
        if(position[24]=='R' and position[32]=='B' and position[18]=='W'):
            u1(), right(), u1(), right1()
        if(position[10]=='W' and position[34]=='B' and position[16]=='R'):
            u(), u(), right(), u1(), right1()
        if(position[2]=='W' and position[39]=='O' and position[8]=='B'):
            u(), d1(), right(), u1, right1(), d()
        if(position[26]=='W' and position[37]=='O' and position[0]=='B'):
            d1(), right(), u1(), right1(), d()
        if(position[18]=='W' and position[24]=='B' and position[32]=='O'):
            u1(), d1(), right(), u1(), right1(), d()
        if(position[10]=='W' and position[34]=='O' and position[16]=='B'):
            u(), u(), d1(), right(), u1(), right1(), d()
        if(position[0]=='B' and position[26]=='W' and position[37]=='o'):
            d1(),right(),u1(),right1(),d()
            
        if(position[2]=='W' and position[39]=='R' and position[8]=='G'):
            u(),d(),right(),u1(),right1(),d1()
        if(position[26]=='W' and position[0]=='G' and position[37]=='R'):
            d(),right(),u1(),right1(),d1()
        if(position[18]=='W' and position[24]=='G' and position[32]=='R'):
            d(),u1(),right(),u1(),right1(),d1()
        if(position[10]=='W' and position[34]=='R' and position[16]=='G'):
            u(),u(),d(),right(),u1(),right1(),d1()
        if(position[2]=='W' and position[39]=='G' and position[8]=='O'):
            u(),d(),d(),right(),u1(),right1(),d(),d()
        if(position[26]=='W' and position[37]=='G' and position[0]=='O'):
            d(),d(),right(),u1(),right1(),d(),d()
        if(position[18]=='W' and position[24]=='O' and position[32]=='G'):
            u(),l1(),u1(),l()
        if(position[10]=='W' and position[34]=='G' and position[16]=='O'):
            l1(),u1(),l()
        if(position[2]=='B' and position[39]=='R' and position[8]=='W'):
            right(),u(),right1()
        if(position[0]=='W' and position[26]=='B' and position[37]=='R'):
            u1(),right(),u(),right1()
        if(position[32]=='R' and position[24]=='W' and position[18]=='B'):
            u(),u(),right(),u(),right1()
        if(position[34]=='R' and position[10]=='B' and position[16]=='W'):
            u(),right(),u(),right1()
        if(position[2]=='O' and position[39]=='B' and position[8]=='W'):
            d1(),right(),u(),right1(),d()
        if(position[0]=='W' and position[26]=='O' and position[37]=='B'):
            u1(),d1(),right(),u(),right1(),d()
        if(position[24]=='W' and position[32]=='B' and position[18]=='O'):
            u(),u(),d1(),right(),u(),right1(),d()
        if(position[10]=='O' and position[34]=='B' and position[16]=='W'):
            u(),d1(),right(),u(),right1(),d()
        if(position[2]=='G' and position[39]=='O' and position[8]=='W'):
            d(),d(),right(),u(),right1(),d(),d()
        if(position[0]=='W' and position[37]=='O' and position[26]=='G'):
            d(),d(),u1(),right(),u(),right1(),d(),d()
        if(position[24]=='W' and position[32]=='O' and position[18]=='G'):
            l1(),u(),l()
        if(position[34]=='O' and position[10]=='G' and position[16]=='W'):
            d(),d(),u(),right(),u(),right1(),d(),d()
        if(position[2]=='R' and position[39]=='G' and position[8]=='W'):
            d(),right(),u(),right1(),d1()
        if(position[0]=='W' and position[37]=='G' and position[26]=='R'):
            right1(),u(),u(),right()
        if(position[32]=='G' and position[24]=='W' and position[18]=='R'):
            right1(),u(),right()
        if(position[10]=='R' and position[34]=='G' and position[16]=='W'):
            u1(),right1(),u(),right()
        if(position[39]=='W' and position[2]=='R' and position[8]=='B'):
            right(),u(),u(),right1(),u1(),right(),u(),right1()
        if(position[0]=='B' and position[26]=='R' and position[37]=='W'):
            u1(),right(),u(),u(),right1(),u1(),right(),u(),right1()
        if(position[32]=='W' and position[24]=='B' and position[18]=='R'):
            u(),u(),right(),u(),u(),right1(),u1(),right(),u(),right1()
        if(position[34]=='W' and position[10]=='R' and position[16]=='B'):
            u(),right(),u(),u(),right1(),u1(),right(),u(),right1()
        if(position[39]=='W' and position[2]=='B' and position[8]=='O'):
            d1(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d()
        if(position[0]=='O' and position[26]=='B' and position[37]=='w'):
            U1(),d1(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d()
        if(position[32]=='W' and position[24]=='O' and position[18]=='B'):
            u(),u(),d1(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d()
        if(position[34]=='W' and position[10]=='B' and position[16]=='O'):
            u(),d1(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d()
        if(position[39]=='W' and position[2]=='O' and position[8]=='G'):
            d(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d(),d()
        if(position[0]=='G' and position[37]=='W' and position[26]=='O'):
            u1(),d(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d(),d()
        if(position[32]=='W' and position[24]=='G' and position[18]=='R'):
            u(),u(),d(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d(),d()
        if(position[34]=='W' and position[10]=='O' and position[16]=='G'):
            u(),d(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d(),d()
        if(position[39]=='W' and position[2]=='G' and position[8]=='R'):
            d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d1()
        if(position[0]=='R' and position[37]=='W' and position[26]=='G'):
            u1(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d1()
        if(position[32]=='W' and position[24]=='R' and position[18]=='G'):
            u(),u(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d1()
        if(position[34]=='W' and position[10]=='G' and position[16]=='R'):
            u(),d(),right(),u(),u(),right1(),u1(),right(),u(),right1(),d1()
        if(position[7]=='W' and position[13]=='B' and position[42]=='R'):
            right(),u(),right1(),u1(),right(),u(),u(),right1(),u1(),right(),u(),right1()
        if(position[5]=='B' and position[31]=='W' and position[40]=='R'):
            l(),u1(),l1(),u(),right(),u1(),right1()
        if(position[23]=='W' and position[29]=='B' and position[45]=='R'):
            l1(),u1(),l(),u1(),right(),u1(),right1()
        if(position[15]=='W' and position[47]=='R' and position[21]=='B'):
            right1(),u(),u(),right(),right(),u1(),right1()
#orange blue
        if(position[7]=='W' and position[13]=='O' and position[41]=='B'):
            right(),u(),right1(),l1(),f1(),l(),f(),l1(),f1(),l(),f(),u1(),l(),u(),l1()
        if(position[31]=='W' and position[5]=='O' and position[40]=='B'):
            l(),u1(),l1(),u(),u(),f(),u1(),f1()
        if(position[23]=='W' and position[29]=='O' and position[45]=='B'):
            l1(),u1(),l(),f(),u1(),f1()
        if(position[15]=='W' and position[47]=='B' and position[21]=='O'):
            right1(),u1(),right(),f(),u1(),f1()
        if(position[7]=='W' and position[13]=='G' and position[42]=='O'):
            f1(),u1(),f(),l1(),u1(),l()
        if(position[5]=='G' and position[40]=='O' and position[31]=='W'):
            l(),u1(),l1(),u1(),l1(),u1(),l()
        if(position[23]=='W' and position[29]=='G' and position[45]=='O'):
            l1(),u1(),l(),u(),l1(),u1(),l()
        if(position[15]=='W' and position[47]=='O' and position[21]=='G'):
            right1(),l1(),u1(),l(),right()
            #redgreen
        if(position[7]=='W' and position[13]=='R' and position[42]=='G'):
            right(),u1(),right1(),ba1(),u1(),ba()
        if(position[5]=='R' and position[40]=='G' and position[31]=='W'):
            l(),u1(),l1(),ba1(),u1(),ba()
        if(position[23]=='W' and position[29]=='R' and position[45]=='G'):
            l1(),u1(),l(),u(),u(),ba1(),u(),ba()
        if(position[15]=='W' and position[47]=='G' and position[21]=='R'):
            right1(),u(),u(),right(),u1(),ba1(),u1(),ba()
        if(position[13]=='W' and position[7]=='R' and position[42]=='B'):
            right(),u(),right1(),u1(),right(),u(),right1()
        if(position[5]=='W' and position[31]=='R' and position[40]=='B'):
            f(),u(),u(),f1(),f1(),u(),f()
        if(position[29]=='W' and position[45]=='B' and position[23]=='R'):
            l1(),u(),l(),f1(),u(),f()
        if(position[21]=='W' and position[15]=='R' and position[47]=='B'):
            ba1(),f1(),u(),f(),ba()
        if(position[13]=='W' and position[7]=='O' and position[42]=='G'):
            right(),u(),right1(),ba(),u(),ba1()
        if(position[5]=='W' and position[40]=='G' and position[31]=='O'):
            f(),ba(),u(),f1(),ba1()
        if(position[29]=='W' and position[45]=='G' and position[23]=='O'):
            l1(),u(),u(),l(),u(),ba(),u(),ba1()
        if(position[15]=='O' and position[47]=='G' and position[21]=='W'):
            right1(),u(),right(),u(),u(),ba(),u(),ba1()
        if(position[7]=='G' and position[13]=='W' and position[42]=='R'):
            right(),u(),u(),right(),right(),u(),right1()
        if(position[5]=='W' and position[40]=='R' and position[31]=='G'):
            l(),u(),l1(),u(),right1(),u(),right()
        if(position[29]=='W' and position[45]=='R' and position[23]=='G'):
            l1(),right1(),u(),l(),right()
        if(position[15]=='G'and position[47]=='R') and position[21]=='W':
            ba1(),u(),ba(),u(),u(),right1(),u(),right()
        if(position[13]=='W' and position[7]=='B') and position[42]=='O':
            right(),l(),u(),right1(),l1()

        if(position[5]=='W' and position[40]=='O') and position[31]=='B':
            f(),u1(),u1(),f1(),u(),l(),u(),l1()

        if(position[29]=='W' and position[45]=='O') and position[23]=='B':
            l1(),u(),u(),l(),l(),u(),l1()

        if(position[21]=='W' and position[15]=='B') and position[47]=='O':
            right1(),u(),right(),u(),l(),u(),l1()

        if(position[5]=='R' and position[40]=='W') and position[31]=='B':
            d1(),right(),u(),right1(),d(),right(),u1(),right1()

        if(position[29]=='R' and position[23]=='B') and position[45]=='W':
            d(),d(),right(),u(),right1(),d(),d(),right(),u1(),right1()

        if(position[15]=='B' and position[47]=='W') and position[21]=='R':
            d(),right(),u(),right1(),d1(),right(),u1(),right1()

        if(position[7]=='O' and position[ 13 ]==' B ') and position[ 42 ]==' W ':
            right(),u(),right1(),d1(),right(),u1(),right1(),d()

        if(position[29]=='B' and position[23]=='O') and position[45]=='W':
            d1(),l(),u(),l1(),d(),l(),u(),l1()

        if(position[15]=='O' and position[21]=='B') and position[47]=='W':
            right1(),u(),u(),right(),u1(),l(),u(),l1()

        if(position[7]=='G' and position[13]=='O') and position[42]=='W':
            right(),u(),right1(),d(),d(),right(),u1(),right1(),d(),d()

        if(position[5]=='O' and position[40]=='W') and position[31]=='G':
            l(),u(),l1(),d1(),l(),u(),l1(),d()

        if(position[47]=='W' and position[15]=='G') and position[21]=='O':
            d1(),l1(),u(),l(),d(),l1(),u1(),l()

        if(position[7]=='R' and position[13]=='G') and position[42]=='W':
            right(),u(),right1(),u1(),ba1(),u1(),ba()

        if(position[13]=='G' and position[7]=='R') and position[42]=='W':
            l(),u1(),l1(),u(),u(),right1(),u(),right()

        if(position[29]=='G' and position[45]=='W') and position[23]=='R':
            l1(),u(),l(),u(),ba1(),u1(),ba()


        if(position[1]=='R' and position[38]=='B'):
            u(),u(),f1(),u(),f(),u(),right(),u1(),right1()


        if(position[35]=='B' and position[25]=='R'):
            u(),f1(),u(),f(),u(),right(),u1(),right1()
        if(position[33]=='B' and position[17]=='R'):
            f1(),u(),f(),u(),right(),u1(),right1()
        if(position[36]=='B' and position[9]=='R'):
            u1(),f1(),u(),f(),u(),right(),u1(),right1()
        if(position[1]=='B' and position[38]=='R'):
            u(),right(),u1(),right1(),f(),right1(),f1(),right()
        if(position[35]=='R' and position[25]=='B'):
            right(),u1(),right1(),f(),right1(),f1(),right()
        if(position[33]=='R' and position[17]=='B'):
            u1(),right(),u1(),right1(),f(),right1(),f1(),right()
        if(position[36]=='R' and position[9]=='B'):
            u(),u(),right(),u1(),right1(),f(),right1(),f1(),right()
        if(position[3]=='B' and position[28]=='R'):
            f(),l1(),u(),l(),f1(),l1(),u1(),l(),u(),f1(),right1(),u1(),right(),f()
        if(position[27]=='B' and position[20]=='R'):
            l1(),u1(),l(),u1(),ba(),u(),ba1(),u(),f1(),right1(),u1(),right(),f()
        if(position[12]=='R' and position[19]=='B'):
            right1(),u(),right(),u(),ba1(),u1(),ba(),u(),u(),right(),f(),u(),f1(),right1(),f(),u1(),f1()
        if(position[3]=='R' and position[28]=='B'):
            d(),l(),u1(),l1(),d1(),f(),right1(),f1(),right()
        if(position[27]=='R' and position[20]=='B'):
            d(),d(),l1(),u(),l(),d(),d(),u(),u(),right(),u1(),right1()
        if(position[12]=='B' and position[19]=='R'):
            d1(),right1(),u(),u(),right(),d(),u1(),f(),right1(),f1(),right()
        if(position[4]=='R' and position[11]=='B'):
            right(),u1(),right1(),u(),f1(),u(),u(),f(),u(),u(),f1(),u(),f()

        if(position[1]=='B' and position[38]=='O'):
            u1(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[35]=='O' and position[25]=='B'):
            u1(),u1(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[33]=='O' and position[17]=='B'):
            u(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[36]=='O' and position[9]=='B'):
            f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[1]=='O' and position[38]=='B'):
            u(),u(),f(),u1(),f1(),u1(),l(),u(),l1()

        if(position[33]=='B' and position[17]=='O'):
            f(),u1(),f1(),u1(),l(),u(),l1()

        if(position[35]=='B' and position[25]=='O'):
            u(),f(),u1(),f1(),u1(),l(),u(),l1()

        if(position[36]=='B' and position[9]=='O'):
            u1(),f(),u1(),f1(),u1(),l(),u(),l1()

        if(position[3]=='O' and position[28]=='B'):
            l(),u(),l1(),u1(),f(),u(),u(),f1(),u(),u(),f(),u1(),f1()

        if(position[ 27 ]==' O ' and position[ 20 ]==' B '):
            l1(),u1(),l(),u1(),ba(),u(),ba1(),u(),u(),f(),u1(),f1(),u1(),l(),u(),l1()

        if(position[19]=='O' and position[12]=='B'):
            right1(),u(),right(),u(),ba1(),u1(),ba(),u1(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[11]=='O' and position[4]=='B'):
            f1(),right1(),u1(),right(),f(),right1(),u(),right(),u1(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[27]=='B' and position[20]=='O'):
            l1(),u1(),l(),u1(),ba(),u(),ba1(),u1(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[19]=='B' and position[12]=='O'):
            right1(),u(),right(),u(),ba1(),u1(),ba(),u(),u(),f(),u1(),f1(),u1(),l(),u(),l1()

        if(position[11]=='B' and position[4]=='O'):
            right(),u1(),right1(),u1(),f1(),u(),f(),u(),f(),l1(),u(),l(),f1(),l1(),u1(),l()

        if(position[1]=='G' and position[38]=='O'):
            u1(),l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[35]=='O' and position[25]=='G'):
            u(),u(),l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[33]=='O' and position[17]=='G'):
            u(),l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[36]=='O' and position[9]=='G'):
            l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[38]=='G' and position[1]=='O'):
            ba(),u(),ba1(),u(),l1(),u1(),l()

        if(position[35]=='G ' and position[25]=='O'):
            u1(),l1(),ba1(),u(),ba(),l(),ba1(),u1(),ba()

        if(position[33]=='G' and position[17]=='O'):
            u(),u(),ba(),u(),ba1(),u(),l1(),u1(),l()

        if(position[36]=='G' and position[9]=='O'):
            u(),ba(),u(),ba1(),u(),l1(),u1(),l()

        if(position[3]=='O' and position[28]=='G'):
            l(),u(),l1(),u(),f(),u1(),f1(),u(),l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[12]=='G' and position[19]=='O'):
            right1(),u(),right(),u(),ba1(),u1(),ba(),u1(),l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[ 4 ]==' G ' and position[ 11 ]==' O '):
            d(),d(),right(),u(),right1(),d(),d(),u(),u(),l1(),u1(),l()

        if(position[3]=='G' and position[28]=='O'):
            l(),u(),l1(),u(),f(),u1(),f1(),u(),u(),l1(),ba1(),u(),ba(),l(),ba1(),u1(),ba()

        if(position[27]=='G' and position[20]=='O'):
            l1(),u1(),l(),u(),ba(),u(),u(),ba1(),u(),u(),ba(),u(),ba1()

        if(position[19]=='G' and position[12]=='O'):
            right1(),u(),right(),u(),ba1(),u1(),ba(),l1(),ba1(),u(),ba(),l(),ba1(),u1(),ba()

        if(position[11]=='G' and position[4]=='O'):
            right(),u1(),right1(),f(),right1(),f1(),right(),u(),l1(),u1(),l(),u1(),ba(),u(),ba1()

        if(position[1]=='R' and position[38]=='G'):
            right1(),ba(),u1(),ba1(),right(),ba(),u(),ba1()

        if(position[35]=='G' and position[25]=='R'):
            u1(),right1(),ba(),u1(),ba1(),right(),ba(),u(),ba1()

        if(position[33]=='G' and position[17]=='R'):
            u(),u(),right1(),ba(),u1(),ba1(),right(),ba(),u(),ba1()

        if(position[36]=='G' and position[9]=='R'):
            u(),right1(),ba(),u1(),ba1(),right(),ba(),u(),ba1()

        if(position[38]=='R' and position[1]=='G'):
            u(),right1(),u(),right(),u(),ba1(),u1(),ba()

        if(position[35]=='R' and position[25]=='G'):
            right1(),u(),right(),u(),ba1(),u1(),ba()

        if(position[33]=='R' and position[17]=='G'):
            u1(),right1(),u(),right(),u(),ba1(),u1(),ba()

        if(position[36]=='R' and position[9]=='G'):
            u(),u(),right1(),u(),right(),u(),ba1(),u1(),ba()

        if(position[3]=='G' and position[28]=='R'):
            d(),d(),l(),u1(),l1(),d(),d(),u(),u(),right1(),u(),right()

        if(position[27]=='G' and position[20]=='R'):
            d1(),l1(),u(),l(),d(),u(),ba1(),u1(),ba()

        if(position[11]=='G' and position[4]=='R'):
            d(),right(),u(),right1(),d1(),u1(),ba1(),u1(),ba()

        if(position[3]=='R' and position[28]=='G'):
            l(),u(),l1(),u(),f(),u1(),f1(),u1(),right1(),u(),right(),u(),ba1(),u1(),ba()

        if(position[27]=='R' and position[20]=='G'):
            l1(),u1(),l(),u1(),ba(),u(),ba1(),ba1(),u1(),ba(),u1(),right1(),u(),right()

        if(position[19]=='R' and position[12]=='G'):    
            right1(),u(),right(),u1(),ba1(),u(),u(),ba(),u(),u(),ba1(),u1(),ba()

        if(position[11]=='R' and position[4]=='G'):
            d(),right(),u1(),right1(),d1(),right1(),u(),u(),right(),u(),u(),right1(),u(),right()
#oll            
#oll
            #dot
        if((position[32]=='O' or position[32]=='R' or position[32]=='B' or position[32]=='G'or position[32]=='Y')and(position[33]=='O' or position[33]=='R' or position[33]=='B' or position[33]=='G')and(position[34]=='O' or position[34]=='R' or position[34]=='B' or position[34]=='G'or position[34]=='Y')and(position[35]=='O' or position[35]=='R' or position[35]=='B' or position[35]=='G')and(position[36]=='O' or position[36]=='G' or position[36]=='B' or position[36]=='R')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='O' or position[38]=='G' or position[38]=='B' or position[38]=='R')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='R' or position[9]=='B' or position[9]=='G'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            f(),right(),u(),right1(),u1(),f1()
            #rod NEEDs
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]=='O' or position[33]=='G' or position[33]=='B' or position[33]=='R')and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='Y')and(position[36]=='Y')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='O' or position[38]=='G' or position[38]=='B' or position[38]=='R')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            f(),right(),u(),right1(),u1(),f1()
            
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='O' or position[35]=='G' or position[35]=='B' or position[35]=='R')and(position[36]=='O' or position[36]=='G' or position[36]=='B' or position[36]=='R')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='Y')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or  position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or  position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),f(),right(),u(),right1(),u1(),f1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]=='O' or position[33]=='G' or position[33]=='B' or position[33]=='R')and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='O' or position[35]=='G' or position[35]=='B' or position[35]=='R')and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='Y')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            f(),right(),u(),right1(),u1(),f1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]=='O' or position[33]=='G' or position[33]=='B' or position[33]=='R')and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]=='O' or position[36]=='G' or position[36]=='B' or position[36]=='R')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or  position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u1(),f(),right(),u(),right1(),u1(),f1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]=='O' or position[36]=='G' or position[36]=='B' or position[36]=='R')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='O' or position[38]=='G' or position[38]=='B' or position[38]=='R')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),u(),f(),right(),u(),right1(),u1(),f1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]=='Y')and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='O' or position[35]=='G' or position[35]=='B' or position[35]=='R')and(position[36]=='Y')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='O' or position[38]=='G' or position[38]=='B' or position[38]=='R')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),f(),right(),u(),right1(),u1(),f1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='Y')and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]==('Y'))and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or  position[25]=='R' or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            right(),u(),right1(),u(),right(),u(),u(),right1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='Y')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]==('Y'))):
            u1(),right(),u(),right1(),u(),right(),u(),u(),right1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R' or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]==('Y'))and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='Y')):
            u(),u(),right(),u(),right1(),u(),right(),u(),u(),right1()

        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='Y')and(position[39]==('Y'))and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]==('Y'))and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]==('Y'))):
            u(),right(),u(),right1(),u(),right(),u(),u(),right1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u1(),right1(),u1(),right(),u1(),right1(),u(),u(),right1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            right1(),u1(),right(),u1(),right1(),u(),u(),right1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='Y')and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]==('Y'))and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),right1(),u1(),right(),u1(),right1(),u(),u(),right1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),u(),right1(),u1(),right(),u1(),right1(),u(),u(),right1()

            

        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]==('Y'))and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R' or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]==('Y'))and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            right(),u(),u(),right1(),u1(),right(),u(),right1(),u1(),right(),u1(),right1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]==('Y'))and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]== 'G' or position[18]=='B' or position[18]=='R' or position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]==('Y'))):
            u(),right(),u(),u(),right1(),u1(),right(),u(),right1(),u1(),right(),u1(),right1()
################################
            
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='Y')and(position[36]=='Y')and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]=='Y')and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]==('Y'))and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='Y')):
            right(),u(),u(),right(),right(),u1(),right(),right(),u1(),right(),right(),u(),u(),right()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='Y')):
            u1(),right(),u(),u(),right(),right(),u1(),right(),right(),u1(),right(),right(),u(),u(),right()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]==('Y'))and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]==('Y'))and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]==('Y'))and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),u(),right(),u(),u(),right(),right(),u1(),right(),right(),u1(),right(),right(),u(),u(),right()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R' or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R' or position[9]=='Y')and(position[10]==('Y'))and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),right(),u(),u(),right(),right(),u1(),right(),right(),u1(),right(),right(),u(),u(),right()
###########################
            
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R' or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]==('Y'))and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R' or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u1(),right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]==('Y'))and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R' or position[26]=='Y')):
            u(),u(),right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or 'Y')and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R' or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='Y')):
            u(),right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='Y')):
            right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u1(),right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]=='Y')and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R' or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]==('Y'))and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]==('Y'))and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),u(),right(),right(),d(),right(),u(),u(),right1(),d1(),right(),u(),u(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]==('Y'))and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R' or 'Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]==('Y'))and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or  position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),right(),ba1(),right1(),f(),right(),ba(),right1(),f1()

            
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y')and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]==('Y'))and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R' or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            right1(),f(),right(),ba(),right1(),f1(),right(),ba1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]==('Y'))and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u1(),right1(),f(),right(),ba(),right1(),f1(),right(),ba1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]=='O' or position[34]=='G' or position[34]=='B' or position[34]=='R'or position[34]=='Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]=='O' or position[37]=='G' or position[37]=='B' or position[37]=='R'or position[37]=='Y')and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='O' or position[8]=='G' or position[8]=='B' or position[8]=='R'or position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='G' or position[10]=='B' or position[10]=='R'or position[10]=='Y')and(position[16]=='Y')and(position[17]=='O' or position[17]=='G' or position[17]=='B' or position[17]=='R'or position[17]=='Y')and(position[18]=='O' or position[18]=='G' or position[18]=='B' or position[18]=='R'or position[18]=='Y')and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='Y'):
            u(),u(),right1(),f(),right(),ba(),right1(),f1(),right(),ba1()
        if((position[32]=='O' or position[32]=='G' or position[32]=='B' or position[32]=='R'or position[32]=='Y')and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]=='O' or position[39]=='G' or position[39]=='B' or position[39]=='R'or position[39]=='Y')and(position[0]=='O' or position[0]=='G' or position[0]=='B' or position[0]=='R'or position[0]=='Y')and(position[1]=='O' or position[1]=='G' or position[1]=='B' or position[1]=='R'or position[1]=='Y')and(position[2]=='O' or position[2]=='G' or position[2]=='B' or position[2]=='R'or position[2]=='Y')and(position[8]=='Y')and(position[9]=='O' or position[9]=='G' or position[9]=='B' or position[9]=='R'or position[9]=='Y')and(position[10]=='O' or position[10]=='B' or position[10]=='G' or position[10]=='R'or position[10]=='Y')and(position[16]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[17]=='O' or position[16]=='G' or position[16]=='B' or position[16]=='R'or position[16]=='Y')and(position[18]==('Y'))and(position[24]=='O' or position[24]=='G' or position[24]=='B' or position[24]=='R'or position[24]=='Y')and(position[25]=='O' or position[25]=='G' or position[25]=='B' or position[25]=='R'or position[25]=='Y')and(position[26]=='O' or position[26]=='G' or  position[26]=='B' or position[26]=='R'or position[26]=='Y')):
            u(),right1(),f(),right(),ba(),right1(),f1(),right(),ba1()
#oll finished
#pll
            #1
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]==position[1]==position[10])and (position[25]==position[26]==position[8]) and (position[24]==position[17]==position[2]) and (position[9]==position[16]==position[18])):
            right1(),f(),right1(),ba(),ba(),right(),f1(),right1(),ba(),ba(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and(position[0]==position[17]==position[18])and (position[24]==position[25]==position[2]) and (position[26]==position[9]==position[16]) and (position[1]==position[8]==position[10])):
            u1(),right1(),f(),right1(),ba(),ba(),right(),f1(),right1(),ba(),ba(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[8]==position[1])and (position[17]==position[16]==position[26]) and (position[25]==position[0]==position[2]) and (position[24]==position[9]==position[10])):
            u(),u(),right1(),f(),right1(),ba(),ba(),right(),f1(),right1(),ba(),ba(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[2]==position[16])and (position[8]==position[9]==position[18]) and (position[25]==position[0]==position[10]) and (position[24]==position[26]==position[17])):
            u(),right1(),f(),right1(),ba(),ba(),right(),f1(),right1(),ba(),ba(),right(),right()
            #2
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[18])and (position[25]==position[26]==position[16]) and (position[2]==position[9]==position[24]) and (position[8]==position[10]==position[17])):
            right(),right(),ba(),ba(),right(),f(),right1(),ba(),ba(),right(),f1(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[25]==position[24]==position[10])and (position[17]==position[18]==position[8]) and (position[26]==position[1]==position[16]) and (position[0]==position[2]==position[9])):
            u1(),right(),right(),ba(),ba(),right(),f(),right1(),ba(),ba(),right(),f1(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[25]==position[8])and (position[17]==position[16]==position[2]) and (position[1]==position[24]==position[26]) and (position[0]==position[9]==position[10])):
            u(),u(),right(),right(),ba(),ba(),right(),f(),right1(),ba(),ba(),right(),f1(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[16]==position[25])and (position[9]==position[8]==position[26]) and (position[24]==position[2]==position[1]) and (position[0]==position[17]==position[10])):
            u(),right(),right(),ba(),ba(),right(),f(),right1(),ba(),ba(),right(),f1(),right()
#3
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[24]==position[25]==position[26])and (position[1]==position[8]==position[18]) and (position[0]==position[10]==position[17]) and (position[2]==position[9]==position[16])):
            right1(),u1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),u(),right()
            
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[2])and (position[8]==position[25]==position[18]) and (position[9]==position[16]==position[26]) and (position[10]==position[24]==position[17])):
            u(),right1(),u1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),u(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[8]==position[9]==position[10])and (position[2]==position[24]==position[17]) and (position[0]==position[25]==position[18]) and (position[1]==position[26]==position[16])):
            u(),u(),right1(),u1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),u(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[16]==position[17]==position[18])and (position[24]==position[2]==position[9]) and (position[1]==position[26]==position[8]) and (position[0]==position[25]==position[10])):
            u1(),right1(),u1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),u(),right()
#4
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[25]==position[18]==position[8])and (position[24]==position[9]==position[26]) and (position[16]==position[2]==position[1]) and (position[0]==position[10]==position[17])):
            right(),right(),u(),right1(),u(),right1(),u1(),right(),u1(),right(),right(),u1(),d1(),right1(),u(),right(),d()
            
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[17])and (position[26]==position[1]==position[16]) and (position[8]==position[25]==position[18]) and (position[24]==position[9]==position[10])):
            
            u(),right(),right(),u(),right1(),u(),right1(),u1(),right(),u1(),right(),right(),u1(),d1(),right1(),u(),right(),d()

            
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[8]==position[10]==position[25])and (position[2]==position[8]==position[24]) and (position[26]==position[16]==position[1]) and (position[0]==position[17]==position[18])):
            u(),u(),right(),right(),u(),right1(),u(),right1(),u1(),right(),u1(),right(),right(),u1(),d1(),right1(),u(),right(),d()


        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[16]==position[18])and (position[0]==position[10]==position[17]) and (position[2]==position[9]==position[24]) and (position[25]==position[26]==position[8])):
            u1(),right(),right(),u(),right1(),u(),right1(),u1(),right(),u1(),right(),right(),u1(),d1(),right1(),u(),right(),d()


#5
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[24]==position[26]==position[17])and (position[25]==position[2]==position[16]) and (position[9]==position[10]==position[0]) and (position[1]==position[8]==position[18])):
            right1(),u1(),right(),u(),d(),right(),right(),u(),right1(),u(),right(),u1(),right(),u1(),right(),right(),d1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[2]==position[24])and (position[0]==position[25]==position[10]) and (position[26]==position[8]==position[17]) and (position[9]==position[16]==position[18])):
            u1(),right1(),u1(),right(),u(),d(),right(),right(),u(),right1(),u(),right(),u1(),right(),u1(),right(),right(),d1()
            
#edited
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[17]==position[18])and (position[1]==position[16]==position[26]) and (position[25]==position[8]==position[10]) and (position[2]==position[24]==position[9])):
            u(),u(),right1(),u1(),right(),u(),d(),right(),right(),u(),right1(),u(),right(),u1(),right(),u1(),right(),right(),d1()


        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[25])and (position[1]==position[10]==position[24]) and (position[8]==position[17]==position[18]) and (position[9]==position[16]==position[26])):
            u(),right1(),u1(),right(),u(),d(),right(),right(),u(),right1(),u(),right(),u1(),right(),u1(),right(),right(),d1()


#6
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[10]==position[25])and (position[1]==position[8]==position[18]) and (position[2]==position[16]==position[17]) and (position[9]==position[24]==position[26])):
            right(),right(),u1(),right(),u1(),right(),u(),right1(),u(),right(),right(),u(),d(),right(),u1(),right1(),d1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[10]==position[25])and (position[1]==position[16]==position[18]) and (position[24]==position[2]==position[17]) and (position[26]==position[8]==position[9])):
            u1(),right(),right(),u1(),right(),u1(),right(),u(),right1(),u(),right(),right(),u(),d(),right(),u1(),right1(),d1()
            

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[18])and (position[2]==position[24]==position[17]) and (position[8]==position[10]==position[25]) and (position[26]==position[9]==position[16])):
            u(),u(),right(),right(),u1(),right(),u1(),right(),u(),right1(),u(),right(),right(),u(),d(),right(),u1(),right1(),d1()


        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[17])and (position[1]==position[8]==position[18]) and (position[26]==position[9]==position[16]) and (position[10]==position[24]==position[25])):
            u(),right(),right(),u1(),right(),u1(),right(),u(),right1(),u(),right(),right(),u(),d(),right(),u1(),right1(),d1()


#7
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[10]==position[17])and (position[1]==position[26]==position[24]) and (position[25]==position[2]==position[16]) and (position[26]==position[17]==position[16])):
            right(),u(),right1(),u1(),d1(),right(),right(),u1(),right(),u1(),right1(),u(),right(),right()            

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[9])and (position[1]==position[10]==position[24]) and (position[25]==position[8]==position[18]) and (position[26]==position[16]==position[17])):
            u(),right(),u(),right1(),u1(),d1(),right(),right(),u1(),right(),u1(),right1(),u(),right(),right()            
            

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[9]==position[18])and (position[1]==position[16]==position[26]) and (position[24]==position[2]==position[25]) and (position[8]==position[10]==position[17])):
            u(),u(),right(),u(),right1(),u1(),d1(),right(),right(),u1(),right(),u1(),right1(),u(),right(),right()            


        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[25]==position[16]==position[18])and (position[26]==position[17]==position[8]) and (position[0]==position[1]==position[10]) and (position[2]==position[9]==position[24])):
            u1(),right(),u(),right1(),u1(),d1(),right(),right(),u1(),right(),u1(),right1(),u(),right(),right()            


#8
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[18])and (position[2]==position[24]==position[25]) and (position[26]==position[17]==position[16]) and (position[10]==position[9]==position[8])):
            l(),u(),right1(),u(),u(),l1(),u1(),right(),u(),l(),u(),right1(),u(),u(),l1(),u1(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[16]==position[17])and (position[24]==position[25]==position[2]) and (position[8]==position[9]==position[26]) and (position[0]==position[1]==position[10])):
            u(),l(),u(),right1(),u(),u(),l1(),u1(),right(),u(),l(),u(),right1(),u(),u(),l1(),u1(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[24]==position[26]==position[25])and (position[0]==position[1]==position[10]) and (position[16]==position[2]==position[17]) and (position[9]==position[18]==position[8])):
            u(),u(),l(),u(),right1(),u(),u(),l1(),u1(),right(),u(),l(),u(),right1(),u(),u(),l1(),u1(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[2])and (position[26]==position[17]==position[16]) and (position[18]==position[9]==position[8]) and (position[10]==position[25]==position[24])):
            u1(),l(),u(),right1(),u(),u(),l1(),u1(),right(),u(),l(),u(),right1(),u(),u(),l1(),u1(),right()

#9
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[2]==position[16])and (position[0]==position[9]==position[10]) and (position[8]==position[17]==position[18]) and (position[24]==position[25]==position[26])):
            right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[2])and (position[25]==position[16]==position[26]) and (position[8]==position[17]==position[18]) and (position[9]==position[10]==position[24])):
            u(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[8]==position[9]==position[10])and (position[1]==position[2]==position[24]) and (position[0]==position[17]==position[18]) and (position[16]==position[25]==position[26])):
            u(),u(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1()


        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[2]==position[24])and (position[9]==position[0]==position[10]) and (position[25]==position[26]==position[8]) and (position[16]==position[17]==position[18])):
            u1(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1()

#10
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[10])and (position[9]==position[2]==position[16]) and (position[24]==position[26]==position[17]) and (position[8]==position[18]==position[25])):
            right(),u1(),right1(),u1(),right(),u(),right(),d1(),right1(),u1(),right(),d(),right1(),u(),u(),right1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[25])and (position[1]==position[16]==position[26]) and (position[8]==position[9]==position[18]) and (position[10]==position[17]==position[24])):
            u(),right(),u1(),right1(),u1(),right(),u(),right(),d1(),right1(),u1(),right(),d(),right1(),u(),u(),right1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[10]==position[8])and (position[9]==position[2]==position[24]) and (position[26]==position[17]==position[16]) and (position[0]==position[25]==position[18])):
            u(),u(),right(),u1(),right1(),u1(),right(),u(),right(),d1(),right1(),u1(),right(),d(),right1(),u(),u(),right1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[24]==position[25])and (position[1]==position[8]==position[26]) and (position[9]==position[16]==position[1]) and (position[0]==position[10]==position[17])):
            u1(),right(),u1(),right1(),u1(),right(),u(),right(),d1(),right1(),u1(),right(),d(),right1(),u(),u(),right1()
                    

#11
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[10]==position[25])and (position[1]==position[24]==position[26]) and (position[9]==position[16]==position[2]) and (position[8]==position[17]==position[18])):
            right(),right(),f(),right(),u(),right(),u1(),right1(),f1(),right(),u(),u(),right1(),u(),u(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[9])and (position[1]==position[8]==position[18]) and (position[25]==position[26]==position[16]) and (position[10]==position[17]==position[24])):
            u(),right(),right(),f(),right(),u(),right(),u1(),right1(),f1(),right(),u(),u(),right1(),u(),u(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[2]==position[24])and (position[10]==position[8]==position[17]) and (position[9]==position[26]==position[16]) and (position[0]==position[25]==position[18])):
            u(),u(),right(),right(),f(),right(),u(),right(),u1(),right1(),f1(),right(),u(),u(),right1(),u(),u(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[9]==position[10])and (position[1]==position[8]==position[26]) and (position[24]==position[2]==position[17]) and (position[1]==position[26]==position[8])):
            u1,right(),right(),f(),right(),u(),right(),u1(),right1(),f1(),right(),u(),u(),right1(),u(),u(),right()

#12
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[10]==position[1])and (position[25]==position[2]==position[16]) and (position[8]==position[17]==position[18]) and (position[24]==position[9]==position[26])):
            right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),f1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[17])and (position[1]==position[10]==position[24]) and (position[25]==position[26]==position[16]) and (position[8]==position[9]==position[18])):
            u(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),f1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[1]==position[24]==position[2])and (position[9]==position[0]==position[18]) and (position[26]==position[17]==position[16]) and (position[25]==position[8]==position[10])):
            u(),u(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),f1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[9]==position[10])and (position[1]==position[16]==position[18]) and (position[24]==position[2]==position[25]) and (position[26]==position[17]==position[8])):
            u1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u1(),right(),u(),right1(),f1()

#13
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[18]==position[9])and (position[1]==position[8]==position[26]) and (position[2]==position[25]==position[16]) and (position[10]==position[24]==position[17])):
            right(),right(),u(),f1(),right1(),u(),right(),u1(),right1(),u(),right(),u1(),right1(),u(),right(),u1(),f(),u1(),right(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[0]==position[25])and (position[1]==position[24]==position[10]) and (position[9]==position[2]==position[16]) and (position[8]==position[17]==position[26])):
            u(),right(),right(),u(),f1(),right1(),u(),right(),u1(),right1(),u(),right(),u1(),right1(),u(),right(),u1(),f(),u1(),right(),right()

#14
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[24]==position[25])and (position[1]==position[26]==position[8]) and (position[9]==position[16]==position[18]) and (position[0]==position[10]==position[17])):
            right(),u(),right1(),u(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u(),u(),right(),u1(),right1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[16]==position[25])and (position[9]==position[8]==position[26]) and (position[24]==position[2]==position[1]) and (position[0]==position[17]==position[0])):
            right(),u(),right1(),u(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u(),u(),right(),u1(),right1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[16]==position[25])and (position[9]==position[8]==position[26]) and (position[24]==position[2]==position[1]) and (position[0]==position[17]==position[0])):
            right(),u(),right1(),u(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u(),u(),right(),u1(),right1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[16]==position[25])and (position[9]==position[8]==position[26]) and (position[24]==position[2]==position[1]) and (position[0]==position[17]==position[0])):
            right(),u(),right1(),u(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),right(),u1(),right1(),u(),u(),right(),u1(),right1()

#15
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[18])and (position[10]==position[24]==position[25]) and (position[9]==position[26]==position[8]) and (position[16]==position[2]==position[17])):
            right1(),u(),right(),u1(),right1(),f1(),u1(),f(),right(),u(),right1(),f(),right1(),f1(),right(),u1(),right()
#16
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[18])and (position[25]==position[26]==position[8]) and (position[9]==position[16]==position[2]) and (position[10]==position[24]==position[17])):
            right1(),u(),right1(),u1(),right(),d(),right1(),d1(),right1(),u(),d(),right(),right(),u1(),right(),right(),d1(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[18]==position[25])and (position[1]==position[2]==position[16]) and (position[26]==position[8]==position[9]) and (position[10]==position[17]==position[24])):
            u(),right1(),u(),right1(),u1(),right(),d(),right1(),d1(),right1(),u(),d(),right(),right(),u1(),right(),right(),d1(),right(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[18]==position[25])and (position[1]==position[8]==position[26]) and (position[16]==position[2]==position[17]) and (position[10]==position[24]==position[9])):
            u(),u(),right1(),u(),right1(),u1(),right(),d(),right1(),d1(),right1(),u(),d(),right(),right(),u1(),right(),right(),d1(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[17]==position[18])and (position[1]==position[8]==position[26]) and (position[9]==position[2]==position[16]) and (position[10]==position[24]==position[25])):
            u1(),right1(),u(),right1(),u1(),right(),d(),right1(),d1(),right1(),u(),d(),right(),right(),u1(),right(),right(),d1(),right(),right()

#17


        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[1]==position[18])and (position[2]==position[25]==position[16]) and (position[26]==position[8]==position[17]) and (position[24]==position[9]==position[10])):
            f(),right(),u1(),right1(),u1(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),f1()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[17]==position[18])and (position[1]==position[10]==position[24]) and (position[2]==position[25]==position[16]) and (position[8]==position[9]==position[26])):
            u(),f(),right(),u1(),right1(),u1(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),f1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[16]==position[17])and (position[1]==position[10]==position[24]) and (position[0]==position[9]==position[18]) and (position[8]==position[25]==position[26])):
            u(),u(),f(),right(),u1(),right1(),u1(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),f1()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[1]==position[16])and (position[0]==position[9]==position[18]) and (position[8]==position[26]==position[17]) and (position[24]==position[25]==position[10])):
            u1(),f(),right(),u1(),right1(),u1(),right(),u(),right1(),f1(),right(),u(),right1(),u1(),right1(),f(),right(),f1()

#18
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[9]==position[24]==position[26])and (position[10]==position[25]==position[8]) and (position[18]==position[16]==position[1]) and (position[0]==position[2]==position[17])):
            right(),right(),u(),u(),right1(),u(),u(),right(),right(),u(),u(),right(),right(),u(),u(),right1(),u(),u(),right(),right()




#19
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[1]==position[0])and (position[8]==position[10]==position[25]) and (position[9]==position[16]==position[18]) and (position[26]==position[24]==position[17])):
            right(),u(),right1(),u(),right1(),u1(),right(),right(),u1(),right1(),u(),right1(),u(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[2]==position[25])and (position[1]==position[18]==position[16]) and (position[10]==position[9]==position[8]) and (position[24]==position[26]==position[17])):
            u(),right(),u(),right1(),u(),right1(),u1(),right(),right(),u1(),right1(),u(),right1(),u(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[25]==position[0]==position[2])and (position[24]==position[9]==position[26]) and (position[1]==position[8]==position[10]) and (position[18]==position[17]==position[16])):
            u(),u(),right(),u(),right1(),u(),right1(),u1(),right(),right(),u1(),right1(),u(),right1(),u(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]==position[17]==position[2])and (position[1]==position[8]==position[10]) and (position[9]==position[18]==position[16]) and (position[24]==position[25]==position[26])):
            u1(),right(),u(),right1(),u(),right1(),u1(),right(),right(),u1(),right1(),u(),right1(),u(),right()

#20
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[1]==position[0])and (position[8]==position[10]==position[17]) and (position[9]==position[24]==position[26]) and (position[25]==position[18]==position[16])):
            right1(),u(),right1(),u1(),right1(),u1(),right1(),u(),right(),u(),right(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[16]==position[25])and (position[9]==position[8]==position[10]) and (position[24]==position[26]==position[1]) and (position[0]==position[17]==position[2])):
            u(),right1(),u(),right1(),u1(),right1(),u1(),right1(),u(),right(),u(),right(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[18]==position[17]==position[16])and (position[25]==position[10]==position[8]) and (position[0]==position[2]==position[9]) and (position[24]==position[26]==position[1])):
            u(),u(),right1(),u(),right1(),u1(),right1(),u1(),right1(),u(),right(),u(),right(),right()

        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[24]==position[26]==position[25])and (position[0]==position[2]==position[9]) and (position[1]==position[18]==position[16]) and (position[10]==position[17]==position[8])):
            u1(),right1(),u(),right1(),u1(),right1(),u1(),right1(),u(),right(),u(),right(),right()

#21
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[0]==position[9])and (position[1]==position[10]==position[8]) and (position[25]==position[16]==position[18]) and (position[24]==position[26]==position[17])):
            right(),u(),right1(),u(),right1(),u1(),right1(),u(),right(),u1(),right1(),u1(),right(),right(),u(),right()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[2]==position[0]==position[25])and (position[1]==position[24]==position[26]) and (position[10]==position[8]==position[17]) and (position[9]==position[16]==position[18])):
            u(),right(),u(),right1(),u(),right1(),u1(),right1(),u(),right(),u1(),right1(),u1(),right(),right(),u(),right()
#final cases
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]=='O' and position[1]=='O' and position[2]=='O' and position[8]=='B' and position[9]=='B' and position[10]=='B')): 
            u()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]=='G' and position[1]=='G' and position[2]=='G' and position[8]=='O' and position[9]=='O' and position[10]=='O')):
            u(),u()
        if((position[32]==('Y'))and(position[33]==('Y'))and(position[34]==('Y'))and(position[35]==('Y'))and(position[36]==('Y'))and(position[37]==('Y'))and(position[38]==('Y'))and(position[39]==('Y'))and (position[0]=='R' and position[1]=='R' and position[2]=='R' and position[8]=='G' and position[9]=='G' and position[10]=='G')):
            u1()

        finalcheck=['B','B','B','B','B','B','B','B','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W']
        j=0
        if(position==finalcheck):
            print("solved")
            print(solmoves)
            clock()
            

    

def clock():
    
    
    global solmoves,ig
    j=len(solmoves)
    for ig in range(j) :
        print (solmoves[ig])
        if solmoves[ig]=='R':
            mylabelmoves.config(text="R")
            mylabelmoves.after(1000)
        if solmoves[ig]=='R1':
            mylabelmoves.config(text="R")
            mylabelmoves.after(1000)
        if solmoves[ig]=='l':
            mylabelmoves.config(text="l")
            mylabelmoves.after(1000)
        if solmoves[ig]=='l1':
            mylabelmoves.config(text="l1")
            mylabelmoves.after(1000)
        if solmoves[ig]=='f':
            mylabelmoves.config(text="f")
            mylabelmoves.after(1000)
        if solmoves[ig]=='f1':
            mylabelmoves.config(text="f1")
            mylabelmoves.after(1000)
            
        if solmoves[ig]=='d':
            mylabelmoves.config(text="d")
            mylabelmoves.after(1000)
        if solmoves[ig]=='d1':
            mylabelmoves.config(text="d1")
            mylabelmoves.after(1000)
        if solmoves[ig]=='u':
            mylabelmoves.config(text="u")
            mylabelmoves.after(1000)
        if solmoves[ig]=='u1':
            mylabelmoves.config(text="u1")
            mylabelmoves.after(1000)
        if solmoves[ig]=='ba':
            mylabelmoves.config(text="ba")
            mylabelmoves.after(1000)
        if solmoves[ig]=='ba1':
            mylabelmoves.config(text="ba1")
            mylabelmoves.after(1000)

               
        
       





    
    

    
        

        
        
    
#default bases

#blue

g12=Label(root,image=grey_labell)
g12.place(x=170,y=330)

b1=Label(root,image=blue_labell)
b1.place(x=170,y=400)

g18=Label(root,image=grey_labell)
g18.place(x=170,y=470)

g13=Label(root,image=grey_labell)
g13.place(x=240,y=330)

g16=Label(root,image=grey_labell)
g16.place(x=240,y=400)

g19=Label(root,image=grey_labell)
g19.place(x=240,y=470)

g11=Label(root,image=grey_labell)
g11.place(x=100,y=330)

g14=Label(root,image=grey_labell)
g14.place(x=100,y=400)

g17=Label(root,image=grey_labell)
g17.place(x=100,y=470)


#yellow
y1=Label(root,image=yellow_labell)
y1.place(x=1210,y=400)

g54=Label(root,image=grey_labell)
g54.place(x=1140,y=400)
g56=Label(root,image=grey_labell)
g56.place(x=1280,y=400)

g57=Label(root,image=grey_labell)
g57.place(x=1140,y=470)

g58=Label(root,image=grey_labell)
g58.place(x=1210,y=470)

g59=Label(root,image=grey_labell)
g59.place(x=1280,y=470)

g51=Label(root,image=grey_labell)
g51.place(x=1140,y=330)

g52=Label(root,image=grey_labell)
g52.place(x=1210,y=330)
g53=Label(root,image=grey_labell)
g53.place(x=1280,y=330)



#red


g22=Label(root,image=grey_labell)
g22.place(x=430,y=330)

r1=Label(root,image=red_labell)
r1.place(x=430,y=400)

g28=Label(root,image=grey_labell)
g28.place(x=430,y=470)

g23=Label(root,image=grey_labell)
g23.place(x=500,y=330)

g26=Label(root,image=grey_labell)
g26.place(x=500,y=400)

g29=Label(root,image=grey_labell)
g29.place(x=500,y=470)

g21=Label(root,image=grey_labell)
g21.place(x=360,y=330)

g24=Label(root,image=grey_labell)
g24.place(x=360,y=400)

g27=Label(root,image=grey_labell)
g27.place(x=360,y=470)

#green

g32=Label(root,image=grey_labell)
g32.place(x=690,y=330)

g1=Label(root,image=green_labell)
g1.place(x=690,y=400)

g38=Label(root,image=grey_labell)
g38.place(x=690,y=470)

g33=Label(root,image=grey_labell)
g33.place(x=760,y=330)

g36=Label(root,image=grey_labell)
g36.place(x=760,y=400)

g39=Label(root,image=grey_labell)
g39.place(x=760,y=470)

g31=Label(root,image=grey_labell)
g31.place(x=620,y=330)

g34=Label(root,image=grey_labell)
g34.place(x=620,y=400)

g37=Label(root,image=grey_labell)
g37.place(x=620,y=470)

#orange
g42=Label(root,image=grey_labell)
g42.place(x=950,y=330)
g46=Label(root,image=grey_labell)
g46.place(x=1020,y=400)
g43=Label(root,image=grey_labell)
g43.place(x=1020,y=330)
o1=Label(root,image=orange_labell)
o1.place(x=950,y=400)


g41=Label(root,image=grey_labell)
g41.place(x=880,y=330)

g44=Label(root,image=grey_labell)
g44.place(x=880,y=400)

g47=Label(root,image=grey_labell)
g47.place(x=880,y=470)

g48=Label(root,image=grey_labell)
g48.place(x=950,y=470)
g49=Label(root,image=grey_labell)
g49.place(x=1020,y=470)

#white
g64=Label(root,image=grey_labell)
g64.place(x=880,y=180)
g62=Label(root,image=grey_labell)
g62.place(x=950,y=110)
g68=Label(root,image=grey_labell)
g68.place(x=950,y=250)
g66=Label(root,image=grey_labell)
g66.place(x=1020,y=180)
g67=Label(root,image=grey_labell)
g67.place(x=880,y=250)
g61=Label(root,image=grey_labell)
g61.place(x=880,y=110)
o1=Label(root,image=white_labell)
g63=Label(root,image=grey_labell)
g63.place(x=1020,y=110)
o1.place(x=950,y=180)
g69=Label(root,image=grey_labell)
g69.place(x=1020,y=250)




                   


           








#changing labels                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
rc1=Label(root,image=red_labell)
rc2=Label(root,image=red_labell)
rc3=Label(root,image=red_labell)
rc4=Label(root,image=red_labell)
rc5=Label(root,image=red_labell)
rc6=Label(root,image=red_labell)
rc7=Label(root,image=red_labell)
rc8=Label(root,image=red_labell)
rc9=Label(root,image=red_labell)
rc10=Label(root,image=red_labell)
rc11=Label(root,image=red_labell)
rc12=Label(root,image=red_labell)
rc13=Label(root,image=red_labell)
rc14=Label(root,image=red_labell)
rc15=Label(root,image=red_labell)
rc16=Label(root,image=red_labell)
rc17=Label(root,image=red_labell)
rc18=Label(root,image=red_labell)
rc19=Label(root,image=red_labell)
rc20=Label(root,image=red_labell)
rc21=Label(root,image=red_labell)
rc22=Label(root,image=red_labell)
rc23=Label(root,image=red_labell)
rc24=Label(root,image=red_labell)
rc25=Label(root,image=red_labell)
rc26=Label(root,image=red_labell)
rc27=Label(root,image=red_labell)
rc28=Label(root,image=red_labell)
rc29=Label(root,image=red_labell)
rc30=Label(root,image=red_labell)
rc31=Label(root,image=red_labell)
rc32=Label(root,image=red_labell)
rc33=Label(root,image=red_labell)
rc34=Label(root,image=red_labell)
rc35=Label(root,image=red_labell)
rc36=Label(root,image=red_labell)
rc37=Label(root,image=red_labell)
rc38=Label(root,image=red_labell)
rc39=Label(root,image=red_labell)
rc40=Label(root,image=red_labell)
rc41=Label(root,image=red_labell)
rc42=Label(root,image=red_labell)
rc43=Label(root,image=red_labell)
rc44=Label(root,image=red_labell)
rc45=Label(root,image=red_labell)
rc46=Label(root,image=red_labell)
rc47=Label(root,image=red_labell)
rc48=Label(root,image=red_labell)
rc49=Label(root,image=red_labell)
rc50=Label(root,image=red_labell)
rc51=Label(root,image=red_labell)
rc52=Label(root,image=red_labell)
rc53=Label(root,image=red_labell)
rc54=Label(root,image=red_labell)
rc55=Label(root,image=red_labell)
rc56=Label(root,image=red_labell)
rc57=Label(root,image=red_labell)
rc58=Label(root,image=red_labell)
rc59=Label(root,image=red_labell)

rc61=Label(root,image=red_labell)

rc62=Label(root,image=red_labell)

rc63=Label(root,image=red_labell)

rc64=Label(root,image=red_labell)

rc65=Label(root,image=red_labell)
rc66=Label(root,image=red_labell)
rc67=Label(root,image=red_labell)

rc68=Label(root,image=red_labell)

rc69=Label(root,image=red_labell)





bc1=Label(root,image=blue_labell)
bc2=Label(root,image=blue_labell)
bc3=Label(root,image=blue_labell)
bc4=Label(root,image=blue_labell)
bc5=Label(root,image=blue_labell)
bc6=Label(root,image=blue_labell)
bc7=Label(root,image=blue_labell)
bc8=Label(root,image=blue_labell)
bc9=Label(root,image=blue_labell)
bc10=Label(root,image=blue_labell)
bc11=Label(root,image=blue_labell)
bc12=Label(root,image=blue_labell)
bc13=Label(root,image=blue_labell)
bc14=Label(root,image=blue_labell)
bc15=Label(root,image=blue_labell)
bc16=Label(root,image=blue_labell)
bc17=Label(root,image=blue_labell)
bc18=Label(root,image=blue_labell)
bc19=Label(root,image=blue_labell)
bc20=Label(root,image=blue_labell)
bc21=Label(root,image=blue_labell)
bc22=Label(root,image=blue_labell)
bc23=Label(root,image=blue_labell)
bc24=Label(root,image=blue_labell)
bc25=Label(root,image=blue_labell)
bc26=Label(root,image=blue_labell)
bc27=Label(root,image=blue_labell)
bc28=Label(root,image=blue_labell)
bc29=Label(root,image=blue_labell)
bc30=Label(root,image=blue_labell)
bc31=Label(root,image=blue_labell)
bc32=Label(root,image=blue_labell)
bc33=Label(root,image=blue_labell)
bc34=Label(root,image=blue_labell)
bc35=Label(root,image=blue_labell)
bc36=Label(root,image=blue_labell)
bc37=Label(root,image=blue_labell)
bc38=Label(root,image=blue_labell)
bc39=Label(root,image=blue_labell)
bc40=Label(root,image=blue_labell)

bc41=Label(root,image=blue_labell)
bc42=Label(root,image=blue_labell)
bc43=Label(root,image=blue_labell)
bc44=Label(root,image=blue_labell)
bc45=Label(root,image=blue_labell)
bc46=Label(root,image=blue_labell)
bc47=Label(root,image=blue_labell)
bc48=Label(root,image=blue_labell)
bc49=Label(root,image=blue_labell)
bc50=Label(root,image=blue_labell)
bc51=Label(root,image=blue_labell)
bc52=Label(root,image=blue_labell)
bc53=Label(root,image=blue_labell)
bc54=Label(root,image=blue_labell)
bc55=Label(root,image=blue_labell)
bc56=Label(root,image=blue_labell)
bc57=Label(root,image=blue_labell)
bc58=Label(root,image=blue_labell)
bc59=Label(root,image=blue_labell)
bc61=Label(root,image=blue_labell)
bc62=Label(root,image=blue_labell)
bc63=Label(root,image=blue_labell)
bc64=Label(root,image=blue_labell)
bc65=Label(root,image=blue_labell)
bc66=Label(root,image=blue_labell)
bc67=Label(root,image=blue_labell)
bc68=Label(root,image=blue_labell)
bc69=Label(root,image=blue_labell)





gc1=Label(root,image=green_labell)
gc2=Label(root,image=green_labell)
gc3=Label(root,image=green_labell)
gc4=Label(root,image=green_labell)
gc5=Label(root,image=green_labell)
gc6=Label(root,image=green_labell)
gc7=Label(root,image=green_labell)
gc8=Label(root,image=green_labell)
gc9=Label(root,image=green_labell)
gc10=Label(root,image=green_labell)
gc11=Label(root,image=green_labell)
gc12=Label(root,image=green_labell)
gc13=Label(root,image=green_labell)
gc14=Label(root,image=green_labell)
gc15=Label(root,image=green_labell)
gc16=Label(root,image=green_labell)
gc17=Label(root,image=green_labell)
gc18=Label(root,image=green_labell)
gc19=Label(root,image=green_labell)
gc20=Label(root,image=green_labell)
gc21=Label(root,image=green_labell)
gc22=Label(root,image=green_labell)
gc23=Label(root,image=green_labell)
gc24=Label(root,image=green_labell)
gc25=Label(root,image=green_labell)
gc26=Label(root,image=green_labell)
gc27=Label(root,image=green_labell)
gc28=Label(root,image=green_labell)
gc29=Label(root,image=green_labell)
gc30=Label(root,image=green_labell)
gc31=Label(root,image=green_labell)
gc32=Label(root,image=green_labell)
gc33=Label(root,image=green_labell)
gc34=Label(root,image=green_labell)
gc35=Label(root,image=green_labell)
gc36=Label(root,image=green_labell)
gc37=Label(root,image=green_labell)
gc38=Label(root,image=green_labell)
gc39=Label(root,image=green_labell)
gc40=Label(root,image=green_labell)
gc41=Label(root,image=green_labell)
gc42=Label(root,image=green_labell)
gc43=Label(root,image=green_labell)
gc44=Label(root,image=green_labell)
gc45=Label(root,image=green_labell)
gc46=Label(root,image=green_labell)
gc47=Label(root,image=green_labell)
gc48=Label(root,image=green_labell)
gc49=Label(root,image=green_labell)
gc50=Label(root,image=green_labell)
gc51=Label(root,image=green_labell)
gc52=Label(root,image=green_labell)
gc53=Label(root,image=green_labell)
gc54=Label(root,image=green_labell)
gc55=Label(root,image=green_labell)
gc56=Label(root,image=green_labell)
gc57=Label(root,image=green_labell)
gc58=Label(root,image=green_labell)
gc59=Label(root,image=green_labell)
gc60=Label(root,image=green_labell)
gc61=Label(root,image=green_labell)
gc62=Label(root,image=green_labell)
gc63=Label(root,image=green_labell)
gc64=Label(root,image=green_labell)
gc65=Label(root,image=green_labell)
gc66=Label(root,image=green_labell)
gc67=Label(root,image=green_labell)
gc68=Label(root,image=green_labell)
gc69=Label(root,image=green_labell)


oc1=Label(root,image=orange_labell)
oc2=Label(root,image=orange_labell)
oc3=Label(root,image=orange_labell)
oc4=Label(root,image=orange_labell)
oc5=Label(root,image=orange_labell)
oc6=Label(root,image=orange_labell)
oc7=Label(root,image=orange_labell)
oc8=Label(root,image=orange_labell)
oc9=Label(root,image=orange_labell)
oc10=Label(root,image=orange_labell)
oc11=Label(root,image=orange_labell)
oc12=Label(root,image=orange_labell)
oc13=Label(root,image=orange_labell)
oc14=Label(root,image=orange_labell)
oc15=Label(root,image=orange_labell)
oc16=Label(root,image=orange_labell)
oc17=Label(root,image=orange_labell)
oc18=Label(root,image=orange_labell)
oc19=Label(root,image=orange_labell)
oc20=Label(root,image=orange_labell)
oc21=Label(root,image=orange_labell)
oc22=Label(root,image=orange_labell)
oc23=Label(root,image=orange_labell)
oc24=Label(root,image=orange_labell)
oc25=Label(root,image=orange_labell)
oc26=Label(root,image=orange_labell)
oc27=Label(root,image=orange_labell)
oc28=Label(root,image=orange_labell)
oc29=Label(root,image=orange_labell)
oc30=Label(root,image=orange_labell)
oc31=Label(root,image=orange_labell)
oc32=Label(root,image=orange_labell)
oc33=Label(root,image=orange_labell)
oc34=Label(root,image=orange_labell)
oc35=Label(root,image=orange_labell)
oc36=Label(root,image=orange_labell)
oc37=Label(root,image=orange_labell)
oc38=Label(root,image=orange_labell)
oc39=Label(root,image=orange_labell)
oc40=Label(root,image=orange_labell)
oc41=Label(root,image=orange_labell)
oc42=Label(root,image=orange_labell)
oc43=Label(root,image=orange_labell)
oc44=Label(root,image=orange_labell)
oc45=Label(root,image=orange_labell)
oc46=Label(root,image=orange_labell)
oc47=Label(root,image=orange_labell)
oc48=Label(root,image=orange_labell)
oc49=Label(root,image=orange_labell)
oc50=Label(root,image=orange_labell)
oc51=Label(root,image=orange_labell)
oc52=Label(root,image=orange_labell)
oc53=Label(root,image=orange_labell)
oc54=Label(root,image=orange_labell)
oc55=Label(root,image=orange_labell)
oc56=Label(root,image=orange_labell)
oc57=Label(root,image=orange_labell)
oc58=Label(root,image=orange_labell)
oc59=Label(root,image=orange_labell)
oc61=Label(root,image=orange_labell)
oc62=Label(root,image=orange_labell)
oc63=Label(root,image=orange_labell)
oc64=Label(root,image=orange_labell)
oc65=Label(root,image=orange_labell)
oc66=Label(root,image=orange_labell)
oc67=Label(root,image=orange_labell)
oc68=Label(root,image=orange_labell)
oc69=Label(root,image=orange_labell)





yc1=Label(root,image=yellow_labell)
yc2=Label(root,image=yellow_labell)
yc3=Label(root,image=yellow_labell)
yc4=Label(root,image=yellow_labell)
yc5=Label(root,image=yellow_labell)
yc6=Label(root,image=yellow_labell)
yc7=Label(root,image=yellow_labell)
yc8=Label(root,image=yellow_labell)
yc9=Label(root,image=yellow_labell)
yc10=Label(root,image=yellow_labell)
yc11=Label(root,image=yellow_labell)
yc12=Label(root,image=yellow_labell)
yc13=Label(root,image=yellow_labell)
yc14=Label(root,image=yellow_labell)
yc15=Label(root,image=yellow_labell)
yc16=Label(root,image=yellow_labell)
yc17=Label(root,image=yellow_labell)
yc18=Label(root,image=yellow_labell)
yc19=Label(root,image=yellow_labell)
yc20=Label(root,image=yellow_labell)
yc21=Label(root,image=yellow_labell)
yc22=Label(root,image=yellow_labell)
yc23=Label(root,image=yellow_labell)
yc24=Label(root,image=yellow_labell)
yc25=Label(root,image=yellow_labell)
yc26=Label(root,image=yellow_labell)
yc27=Label(root,image=yellow_labell)
yc28=Label(root,image=yellow_labell)
yc29=Label(root,image=yellow_labell)
yc30=Label(root,image=yellow_labell)
yc31=Label(root,image=yellow_labell)
yc32=Label(root,image=yellow_labell)
yc33=Label(root,image=yellow_labell)
yc34=Label(root,image=yellow_labell)
yc35=Label(root,image=yellow_labell)
yc36=Label(root,image=yellow_labell)
yc37=Label(root,image=yellow_labell)
yc38=Label(root,image=yellow_labell)
yc39=Label(root,image=yellow_labell)
yc40=Label(root,image=yellow_labell)
yc41=Label(root,image=yellow_labell)
yc42=Label(root,image=yellow_labell)
yc43=Label(root,image=yellow_labell)
yc44=Label(root,image=yellow_labell)
yc45=Label(root,image=yellow_labell)
yc46=Label(root,image=yellow_labell)
yc47=Label(root,image=yellow_labell)
yc48=Label(root,image=yellow_labell)
yc49=Label(root,image=yellow_labell)
yc50=Label(root,image=yellow_labell)
yc51=Label(root,image=yellow_labell)
yc52=Label(root,image=yellow_labell)
yc53=Label(root,image=yellow_labell)
yc54=Label(root,image=yellow_labell)
yc55=Label(root,image=yellow_labell)
yc56=Label(root,image=yellow_labell)
yc57=Label(root,image=yellow_labell)
yc58=Label(root,image=yellow_labell)
yc59=Label(root,image=yellow_labell)
yc60=Label(root,image=yellow_labell)
yc61=Label(root,image=yellow_labell)
yc62=Label(root,image=yellow_labell)
yc63=Label(root,image=yellow_labell)
yc64=Label(root,image=yellow_labell)
yc65=Label(root,image=yellow_labell)
yc66=Label(root,image=yellow_labell)
yc67=Label(root,image=yellow_labell)
yc68=Label(root,image=yellow_labell)
yc69=Label(root,image=yellow_labell)



wc1=Label(root,image=white_labell)
wc2=Label(root,image=white_labell)
wc3=Label(root,image=white_labell)
wc4=Label(root,image=white_labell)
wc5=Label(root,image=white_labell)
wc6=Label(root,image=white_labell)
wc7=Label(root,image=white_labell)
wc8=Label(root,image=white_labell)
wc9=Label(root,image=white_labell)
wc10=Label(root,image=white_labell)
wc11=Label(root,image=white_labell)
wc12=Label(root,image=white_labell)
wc13=Label(root,image=white_labell)
wc14=Label(root,image=white_labell)
wc15=Label(root,image=white_labell)
wc16=Label(root,image=white_labell)
wc17=Label(root,image=white_labell)
wc18=Label(root,image=white_labell)
wc19=Label(root,image=white_labell)
wc20=Label(root,image=white_labell)
wc21=Label(root,image=white_labell)
wc22=Label(root,image=white_labell)
wc23=Label(root,image=white_labell)
wc24=Label(root,image=white_labell)
wc25=Label(root,image=white_labell)
wc26=Label(root,image=white_labell)
wc27=Label(root,image=white_labell)
wc28=Label(root,image=white_labell)
wc29=Label(root,image=white_labell)
wc30=Label(root,image=white_labell)
wc31=Label(root,image=white_labell)
wc32=Label(root,image=white_labell)
wc33=Label(root,image=white_labell)
wc34=Label(root,image=white_labell)
wc35=Label(root,image=white_labell)
wc36=Label(root,image=white_labell)
wc37=Label(root,image=white_labell)
wc38=Label(root,image=white_labell)
wc39=Label(root,image=white_labell)
wc40=Label(root,image=white_labell)
wc41=Label(root,image=white_labell)
wc42=Label(root,image=white_labell)
wc43=Label(root,image=white_labell)
wc44=Label(root,image=white_labell)
wc45=Label(root,image=white_labell)
wc46=Label(root,image=white_labell)
wc47=Label(root,image=white_labell)
wc48=Label(root,image=white_labell)
wc49=Label(root,image=white_labell)
wc50=Label(root,image=white_labell)
wc51=Label(root,image=white_labell)
wc52=Label(root,image=white_labell)
wc53=Label(root,image=white_labell)
wc54=Label(root,image=white_labell)
wc55=Label(root,image=white_labell)
wc56=Label(root,image=white_labell)
wc57=Label(root,image=white_labell)
wc58=Label(root,image=white_labell)
wc59=Label(root,image=white_labell)
wc60=Label(root,image=white_labell)
wc61=Label(root,image=white_labell)
wc62=Label(root,image=white_labell)
wc63=Label(root,image=white_labell)
wc64=Label(root,image=white_labell)
wc65=Label(root,image=white_labell)
wc66=Label(root,image=white_labell)
wc67=Label(root,image=white_labell)
wc68=Label(root,image=white_labell)
wc69=Label(root,image=white_labell)




#input buttons
my_img=ImageTk.PhotoImage(Image.open("D:\\allcases\\red.png"))
red=Button(root,image=my_img,command=RED)
red.place(x=350,y=670)
my_img2=ImageTk.PhotoImage(Image.open("D:\\allcases\\green.png"))
green=Button(root,image=my_img2,command=GREEN)
green.place(x=550,y=670)

my_img5=ImageTk.PhotoImage(Image.open("D:\\allcases\\blue.png"))
blue=Button(root,image=my_img5,command=BLUE)
blue.place(x=1150,y=670)
my_img4=ImageTk.PhotoImage(Image.open("D:\\allcases\\orange.png"))
orange=Button(root,image=my_img4,command=ORANGE)
orange.place(x=950,y=670)



my_img3=ImageTk.PhotoImage(Image.open("D:\\allcases\\yellow.png"))
yellow=Button(root,image=my_img3,command=YELLOW)
yellow.place(x=750,y=670)





my_img6=ImageTk.PhotoImage(Image.open("D:\\allcases\\white.png"))
white=Button(root,image=my_img6,command=WHITE)
white.place(x=1350,y=670)






















root.mainloop()
