

import cv2

image= cv2.imread("C:/Users/khadijeh.valipour/Desktop/ai/assigment37/mnist.jpg")
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)

cv2.imshow("",image)
cv2.waitKey()

count=0
number=0

for i in range (0,1000,20) :
    for j in range (0,2000,20) :
        num= image[i:i+20 , j:j+20]
        path = "outpot" + str(number) + "/number" + str(number) + "_" + str(count) + ".png"
        count+=1
        cv2.imwrite(path,number)

    if count == 500 :
        number += 1
        count=0