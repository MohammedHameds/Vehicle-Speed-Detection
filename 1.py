import cv2
import time

car_cascade = cv2.CascadeClassifier("cars.xml")
cap = cv2.VideoCapture("video.mp4")

car_num = 1
ax1 = 70
ay = 90
ax2 = 230
bx1 = 15
by = 125
bx2 = 225 

def speed_cal(time):
    try :
        speed = (10/1000) * (time / 3600)
        return speed
    except ZeroDivisionError :
        print('Can\'t divide by zero !!')
        

while cap.isOpened() :
    ret,frame = cap.read()
    blurred = cv2.blur(frame,(15,15))    
    gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,2)
         
    cv2.line(frame,(ax1,ay),(ax2,ay),(255,0,0),2)
    cv2.line(frame,(bx1,by),(bx2,by),(255,0,0),2)

    for car in cars :
        (x,y,w,h) = car
        xx = (int((x+x+w)/2))
        yy = (int((y+y+h)/2))
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.circle(frame,(xx,yy),2,(0,255,0),-1)
                
        while int(ay) >= int((y+y+h)/2) and  int(ay) <= int((y+y+h)/2) +1  :
            cv2.line(frame,(ax1,ay),(ax2,ay),(0,255,0),2)
            start_time = time.time()
            break
        
        while int(ay) <= (int((y+h)/2)) :
              cv2.line(frame,(bx1,by),(bx2,by),(0,0,255),2)
              speed = speed_cal(time.time() - start_time)
              print('Car num' + str(car_num) + " with speed " + str(speed) + ' KM/H')
              car_num += 1
              break
            # else :

        
    cv2.imshow('Frame' , frame)
    if cv2.waitKey(50) == ord('q'):
            break

    
cv2.destroyAllWindows()
cap.release()   
