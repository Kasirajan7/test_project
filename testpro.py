print("Note: Place the image file in the working directory")
import os
from PIL import Image
while True:
    #Creating the new directory
    #if directory already exists ask for another directory
    newpath = input("Input the path where the folder want to be created: ") 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        imageFile="test.png"
        str1="mipmap"
        newpath=newpath+"/"+str1
        #opening the imagefile
        im1=Image.open(imageFile)
        width=24
        height=24
        #resizing the image in bicubic format
        im2=im1.resize((width*2,height*2), Image.BICUBIC)
        im3=im1.resize((width*3,height*3), Image.BICUBIC)
        im4=im1.resize((width*4,height*4), Image.BICUBIC)
        im5=im1.resize((width*6,height*6), Image.BICUBIC)
        im6=im1.resize((width*8,height*8), Image.BICUBIC)

        #Creating directory within another directory and saving the resized image
        
        newpath1=newpath+"/"+str1+"-mdpi"
        os.makedirs(newpath1)
        im2.save(os.path.join(newpath1,"test")+".png")
        newpath1=newpath+"/"+str1+"-hdpi"
        os.makedirs(newpath1)
        im3.save(os.path.join(newpath1,"test")+".png")
        newpath1=newpath+"/"+str1+"-xhdpi"
        os.makedirs(newpath1)
        im4.save(os.path.join(newpath1,"test")+".png")
        newpath1=newpath+"/"+str1+"-xxhdpi"
        os.makedirs(newpath1)
        im5.save(os.path.join(newpath1,"test")+".png")
        newpath1=newpath+"/"+str1+"-xxxhdpi"
        os.makedirs(newpath1)
        im6.save(os.path.join(newpath1,"test")+".png")
        print("Image resized Successfully")
        break
    else:
        print("Path Already exists")
        
