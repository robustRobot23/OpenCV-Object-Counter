import numpy as np
import cv2 
from matplotlib import pyplot as plt
from math import ceil, floor

def allPixelsBlack(image, rows, columnIndex):
    for row in rows:
        if image[row][columnIndex] > 100:
            return False
    return True

def makeNewPixelsBlack(newImage, rowIndex, columnIndex):
    newImage[rowIndex-1][columnIndex] = 0
    newImage[rowIndex][columnIndex] = 0
    return newImage

def makeRowWhite(image, rowIndex):
    whiteRow = np.ones(len(image[0])) * 255
    image[rowIndex] = whiteRow
    return image

def curveFinder(image, width, height):
    # print(f"Image is {len(image)}x{len(image[0])}")
    height = 3
    if height % 2 != 0:
        bottomHeight = floor(height/2)
        topHeight = ceil(height/2) 
    else:
        bottomHeight = int(height /2)
        topHeight = bottomHeight + 1

    i = bottomHeight

    while i < len(image):
        for rows in image[i-bottomHeight: i+ topHeight]:
            for column in rows:
                if allPixelsBlack(rows):
                    continue 

        i+= height

def lineFinder(image):
    newImage = image.copy()
    numColumns = len(image[0])
    
    print(newImage[200][600])
    for possibleRow in range(0, len(newImage)):
        for possibleColumn in range(0, 620):
            try:
                newImage[possibleRow][possibleColumn] = 255
            except:
                print(f"possibleRow = {possibleRow}, possibleColumn = {possibleColumn}")

    print(newImage[200][600])
    # plt.imshow(newImage, cmap = 'gray')
    rowIndex = 0
    while rowIndex < len(image):
        for columnIndex in range(0, numColumns):
            if allPixelsBlack(image, [rowIndex-1, rowIndex], columnIndex):
                newImage = makeNewPixelsBlack(newImage, rowIndex, columnIndex)
            if image[rowIndex][columnIndex] < 10:
                newImage[rowIndex][columnIndex] = 255
                continue
        rowIndex += 1
  

    return newImage

def readImage():
    initialImage = cv2.imread('Flash\\flash4.jpg', cv2.IMREAD_GRAYSCALE)
    image = initialImage
    assert image is not None, "file could not be read, check with os.path.exists()"
    image = cv2.medianBlur(image,3)
    image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,6)
    image = cv2.medianBlur(image,3)
    image = cv2.medianBlur(image,3)
    image = cv2.medianBlur(image,3)
    image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,13,6)

    # curveFinder(image, 5, 3)
    newImage = lineFinder(image)
    plt.imshow(newImage, cmap = 'gray')

    

readImage()


# (cnt, hierarchy) = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# for hierarchalValue in hierarchy:
#     print(hierarchalValue)
# cv2.drawContours(image, cnt, -1, (255, 0, 0), 2)


# plt.imshow(image)



# laplacian = cv.Laplacian(img,cv.CV_64F)
# sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
# sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()