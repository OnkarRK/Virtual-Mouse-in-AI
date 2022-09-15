import cv2
import mediapipe as mp 
import pyautogui


cap = cv2.VideoCapture(0)#operate the camera
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils#get landmark location of hand
screen_width,screen_height = pyautogui.size()
index_y = 0


while True:
    success, frame = cap.read()#read the camera
    frame = cv2.flip(frame,1)#flip the frame lefthand side 2 righthand side
    frame_height,frame_width,_ = frame.shape#get frame height & width
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
   
   
    if hands:
       
        for hand in hands:
          drawing_utils.draw_landmarks(frame,hand) #landmark location on hand
          landmarks = hand.landmark
         
         
          for id,landmark in enumerate(landmarks):
              x = int(landmark.x*frame_width)
              y = int(landmark.y*frame_height)
               
              if id ==8:#for index finger
                  cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))#to drawe the circle on index finger
                  index_x = screen_width/frame_width*x#to move outside the frame on allover screen on horizontally
                  index_y = screen_width/frame_height*y#to move outside the frame on allover screen on vertically
                  pyautogui.moveTo(index_x,index_y)
              
              
              if id ==12:#for middle finger
                  cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))#to drawe the circle on index finger
                  middle_x = screen_width/frame_width*x#to move outside the frame on allover screen on horizontally
                  middle_y = screen_width/frame_height*y#to move outside the frame on allover screen on vertically
                  print('outside',abs(index_y - middle_y))
                  if abs(index_y - middle_y) < 30:#when diff is less than then click
                       pyautogui.click()#to click the ponit
                       pyautogui.click()
                       pyautogui.sleep(1)
                     
    cv2.imshow('virtual mouse',frame)#display the output
    if cv2.waitKey(1)==ord('v'):
      break