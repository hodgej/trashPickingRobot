import cv2
import numpy as np
import tracker as trck


#tracker object
tracker = trck.EuclideanDistTracker()

#Video Settings
videoOut = True
device = cv2.VideoCapture(0)
on = True

def run():
    ret, frame = device.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define what constitutes blue
    lowerRange = np.array([90, 90, 90])
    uppderRange = np.array([130, 255, 255])

    #mask blue objects
    mask = cv2.inRange(hsv, lowerRange, uppderRange)
    
    #bitwise and with video feed
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #get contours of blue objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    detections = []
    for cnt in contours:
        #calculate areas and remove small elements
        area = cv2.contourArea(cnt)

        if area > 200:
            cv2.drawContours(result, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            print(x)
            cv2.rectangle(result, (x,y), (x+w, y+h), (0,255,0), 3 )
            detections.append([x,y,w,h])


    #object tracking #

    box_ids = tracker.update(detections)

    for b_id in box_ids:
        x,y,w,h, id = b_id

        cv2.putText(result, str(id), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

    if videoOut:
        imgW = len(result)
        imgH = len(result[0])
        print(result.shape)
        cenX = int(imgW/2)
        cenY = int(imgH/2)
        cv2.circle(result, (cenX, cenY), 3, (255,255,255), 3, )
        cv2.imshow("Masked", mask)
        cv2.imshow("Thing", result)
    
    if cv2.waitKey(1) == 27:
        on = False

    return tracker.center_points
    

while on == True:
    run()


device.release()
cv2.destroyAllWindows()