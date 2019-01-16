from PIL import Image


def main():
	file = open("imageData.txt", "r+")
	#readMaskFiles(file)
	calculateRatio(file)

'''
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

                if cmask[0] == 255 and cmask[1] == 255 and cmask[2] == 255:
                    skinValue = '2'
                    creal = real_pic[x, y]

                file.write(str(creal[0]) + " " + str(creal[1]) +" " + str(creal[2]) + " " + skinValue + '\n')
'''

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

	file1 = open('pixelRatio.txt', 'w+')

	for x in range(256):
		for y in range(256):
			for z in range(256):
				ratio = 0.0
				if nonSkin[x][y][z] != 0:
					ratio = float(skin[x][y][z] / nonSkin[x][y][z])
				else:
					ratio = 1.0
				file1.write(str(skin[x][y][z])+ " "+ str(nonSkin[x][y][z])+ "\n")
				file1.write(str(x)+ " "+ str(y)+ " "+ str(z)+ " "+ str(ratio)+ "\n")





if __name__ == '__main__':
    main()

