# Import OpenCV
import cv2

# Save captured video in webcam
webcam = cv2.VideoCapture()
  
# Always running until break
while(True):
      
    # Capture each frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # On pressing ESC, break
    if cv2.waitKey(0) == 27:
        break
  
# After the loop release the cap object
webcam.release()
# Destroy all windows
cv2.destroyAllWindows()