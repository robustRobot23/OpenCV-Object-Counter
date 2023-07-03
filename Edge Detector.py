# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import contourAnalysis as ca

image = cv2.imread('Flash\\flash4.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# plt.imshow(gray, cmap='gray')
blur = cv2.GaussianBlur(gray, (11, 11), 0)
canny = cv2.Canny(blur, 0, 150, 3)
# plt.imshow(canny, cmap='gray')
# canny1 = cv2.Canny(blur, 90, 300)
# canny2 = cv2.Canny(blur, 50, 200)
# canny3 = cv2.Canny(blur, 80, 250)
# canny4 = cv2.Canny(blur, 100, 230)

# threshold = cv2.adaptiveThreshold(gray ,100 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
# plt.imshow(threshold, cmap='gray')
dilated = cv2.dilate(canny, (1, 1), iterations=1)
# plt.imshow(dilated, cmap='gray')

(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)





filtered_cnt = []

for contour in cnt:
    
        

    # filtered_cnt.append(contour)
    appendContour = ca.checkContour(contour)
    if appendContour is not None:
        filtered_cnt.append(appendContour)

        # if len(filtered_cnt) == 8:
            # ca.printValues(contour)
            # ca.findMax(contour)
        
            # cv2.drawContours(rgb, contour, -1, (0, 255, 0), 2)
            # cv2.drawMarker(rgb, [600, 1300], 0, markerType = 1)


# Split touching contours apart using contour approximation
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# for i, contour in enumerate(filtered_cnt):
#     # Approximate the contour with a simpler polygon
#     epsilon = 0.01 * cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, epsilon, True)

#     # Draw the contour
#     cv2.drawContours(rgb, [approx], -1, (0, 255, 0), 2)


cv2.drawContours(rgb, filtered_cnt, -1, (0, 255, 0), 2)

print("Edges in the image : ", len(filtered_cnt))

# for contour in filtered_cnt:
#     # Approximate the contour with a simpler polygon
#     epsilon = 0.01 * cv2.arcLength(contour, True)
#     approx = cv2.approxPolyDP(contour, epsilon, True)

#     # Get the number of vertices of the polygon
#     num_vertices = len(approx)

#     # Determine the type of contour based on the number of vertices
#     if num_vertices == 3:
#         contour_type = "Triangle"
#     elif num_vertices == 4:
#         contour_type = "Rectangle or Square"
#     elif num_vertices == 5:
#         contour_type = "Pentagon"
#     else:
#         contour_type = "Other"

#     # Print the type of contour
#     # print("Contour type:", contour_type)
#     print("Number of vertices: ", num_vertices)

# plt.figure(figsize=(16, 16))
# plt.subplot(2, 2, 1)
# plt.imshow(canny1)
# plt.title("Canny1")
# plt.axis("off")

# plt.subplot(2, 2, 2)
# plt.imshow(canny2)
# plt.title("Canny2")
# plt.axis("off")

# plt.subplot(2, 2, 3)
# plt.imshow(canny3)
# plt.title("Canny3")
# plt.axis("off")

# plt.subplot(2, 2, 4)
# plt.imshow(canny4)
# plt.title("Canny4")
# plt.axis("off")


plt.imshow(rgb)
plt.show()