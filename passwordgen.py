import random
import string

def generate(length,numbers=True,specialcharacters=True):
    l=string.ascii_letters
    n=string.digits
    sc=string.punctuation
   
     
    c=l
    if numbers:
        c+=n
    if specialcharacters:
        c+=sc
    pwd=""
    yes=False
    has_n=False
    has_sc=False

    while not yes or len(pwd)<length:
        new=random.choice(c)
        pwd+=new
        
        if new in n:
            has_n=True
        if new in sc:
            has_sc=True

        yes=True

        if numbers:
            yes=has_n
            
        if specialcharacters:
            yes=yes and has_sc
           
    return pwd
length=int(input("enter minimum length"))
has_n=input("want number y/n").lower()=="y"
has_sc=input("want special character y/n").lower()=="y"
pwd=generate(length,has_n,has_sc)
print("password=",pwd)