from PIL import Image


im = Image.open(
    'C:\\Users\\antan\\Desktop\\5th Semester\\Data mining\\Data\\ibtd\\Mask\\0000.bmp')
# pix = im.load()  # Get the width and hight of the image for iterating over
w, h = im.size
print("(", w, ",", h, ")")
print(im.size)
pix_val = list(im.getdata())
#print(pix[2, 45])

# pix[x,y] = value  # Set the RGBA Value of the image (tuple)
# im.save('alive_parrot.png')

file = open("0000co.txt", "w+")
# file.write()


#pix = im.load()
for x in range(120):
    for y in range(94):
        pix = im.load()
        cmask = pix[x, y]
        f = open("0000.txt", "w+")
        if cmask[0] == 255 and cmask[1] == 255 and cmask[2] == 255:
            #print(x," ",y)
            file.write(str(x) + "," + str(y) + ' white\n')
            aim = Image.open(
                "C:\\Users\\antan\\Desktop\\5th Semester\\Data mining\\Data\\ibtd\\0000.jpg")
            pic = aim.load()
            cact = pic[x, y]

            f.write(str(cact[0]) + " " + str(cact[1]) +" " + str(cact[2]) + " " + '2\n')
        else:
            f.write(str(cact[0]) + " " + str(cact[1]) +" " + str(cact[2]) + " " + '1\n')

f.close()
file.close()

