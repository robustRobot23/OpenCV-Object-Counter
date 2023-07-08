import cv2

def printValues(contours):
    for contour in contours:
        print(contour)


def findMax(contour):
    xMax = 0
    xMin = 1e9
    yMax = 0
    yMin = 1e9
    for contourSubSet in contour:
        for coordinates in contourSubSet:
            if coordinates[0] > xMax:
                xMax = coordinates[0]
            if coordinates[0] < xMin:
                xMin = coordinates[0]
            if coordinates[1] > yMax:
                yMax = coordinates[1]
            if coordinates[1] < yMin:
                yMin = coordinates[1]
    print(f"Max X Value: {xMax}, Min X Value: {xMin}")
    print(f"Max Y Value: {yMax}, Min Y Value: {yMin}")


threshold_area = 100
min_threshold_perimeter = 5e2
max_threshold_perimeter = 1e6
max_num_vertices = 200

def isContourThick(contour):
    xMax = 0
    xMin = 1e9
    yMax = 0
    yMin = 1e9
    for contourSubSet in contour:
        for coordinates in contourSubSet:
            if coordinates[0] > xMax:
                xMax = coordinates[0]
            if coordinates[0] < xMin:
                xMin = coordinates[0]
            if coordinates[1] > yMax:
                yMax = coordinates[1]
            if coordinates[1] < yMin:
                yMin = coordinates[1]

    delta_y = abs(yMax - yMin)
    if delta_y > 50:
        return True
        
def checkContour(contour):
    area = cv2.contourArea(contour)
    
    perimeter = cv2.arcLength(contour, True)
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Get the number of vertices of the polygon
    num_vertices = len(approx)
    thick = isContourThick(contour)
    if area > threshold_area and perimeter > min_threshold_perimeter and perimeter < max_threshold_perimeter and num_vertices <= max_num_vertices and thick:
        return contour
    
    return None



