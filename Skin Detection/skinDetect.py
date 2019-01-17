from PIL import Image

value = [[[0.0 for x in range(256)]for y in range(256)] for z in range(256)]

def main():
	
	file = open("imageData.txt", "r+")
	readMaskFiles(file)
	file.close()

	fl = open("imageData.txt", "r")
	calculateRatio(fl)
	fl.close()

	makeMask()


def readMaskFiles(file):
    prefixM = "C:\\Users\\antan\\Desktop\\5th Semester\\Data mining\\Data\\ibtd\\Mask\\"
    prefixR = "C:\\Users\\antan\\Desktop\\5th Semester\\Data mining\\Data\\ibtd\\"

    for i in range(0, 555):
        n = '{num:04d}'.format(num=i)
        pathMask = prefixM + str(n) + ".bmp"
        pathReal = prefixR + str(n) + ".jpg"

        imgM = Image.open(pathMask)
        width, height = imgM.size
        mask_pic = imgM.load()

        imgR = Image.open(pathReal)
        real_pic = imgR.load()

        print(width, " ", height)
        print(width * height)

        for x in range(width):
            for y in range(height):
                skinValue = '1'
                cmask = mask_pic[x, y]

                if cmask[0] >= 235 and cmask[1] >= 235 and cmask[2] >= 235:
                    skinValue = '2'
                    creal = real_pic[x, y]

                file.write(str(creal[0]) + " " + str(creal[1]) +" " + str(creal[2]) + " " + skinValue + '\n')

def calculateRatio(file):
	skin = [[[0 for x in range(256)]for y in range(256)] for z in range(256)]
	nonSkin = [[[0 for x in range(256)]for y in range(256)] for z in range(256)]

	fullData = file.readlines()

	for line in fullData:
		line = line.split()
		x = int(line[0])
		y = int(line[1])
		z = int(line[2])

		if line[3]=='1':
			skin[x][y][z] += 1
		else:
			nonSkin[x][y][z] += 1

	file1 = open('pixelRatioFinal.txt', 'w+')
	#fl = open('RatioForThreshold.txt', 'w+')

	for x in range(256):
		for y in range(256):
			for z in range(256):
				ratio = 0.0
				if nonSkin[x][y][z] != 0:
					ratio = float(skin[x][y][z] / nonSkin[x][y][z])
				else:
					ratio = 1.0
				#file1.write(str(skin[x][y][z])+ " "+ str(nonSkin[x][y][z])+ "\n")
				file1.write(str(x)+ " "+ str(y)+ " "+ str(z)+ " "+ str(ratio)+ "\n")
				global value
				value[x][y][z] = ratio
				'''
				if ratio >= 0.0 and ratio <= 1.0:
					fl.write(str(skin[x][y][z])+ " "+ str(nonSkin[x][y][z])+ "\n")
					fl.write(str(x)+ " "+ str(y)+ " "+ str(z)+ " "+ str(ratio)+ "\n")
				'''

	file1.close()
	#fl.close()


def makeMask():
	# To run the full functionality, you can use the 'value' list to compare with threshold.
	# I only ran this makeMask() function, commenting readMaskFile() & calculateRatio() function.
	# Threshold value I,ve taken is 0.30
	rat = [[[0 for x in range(256)]for y in range(256)] for z in range(256)]

	file1 = open('pixelRatioFinal.txt', 'r')
	fullData = file1.readlines()
	for line in fullData:
		aa = line.split()
		line = line.split(' ')
		x = int(line[0])
		y = int(line[1])
		z = int(line[2])
		val = float(line[3])
		rat[x][y][z] = val




	#im = Image.open("C:\\Users\\antan\\Desktop\\5th Semester\\watson.jpg")
	im1 = Image.open("C:\\Users\\antan\\Desktop\\5th Semester\\Web Tech\\ant.jpg")
	#pix = im.load()
	pix = im1.load()
	width, height = im1.size
	for x in range(width):
	    for y in range(height):
	        p = pix[x,y] 
	        if rat[p[0]] [p[1]] [p[2]] <= 0.30:
	        	pix[x,y] = (255, 255, 255)

	#im.save("watson.bmp", "BMP")
	im1.save("ant.bmp", "BMP")




if __name__ == '__main__':
    main()

