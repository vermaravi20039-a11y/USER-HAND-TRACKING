#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mediapipe as mp

print(mp.__version__)
print(hasattr(mp, "solutions"))


# In[4]:


import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
canvas = None
px, py = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    if canvas is None:
        canvas = np.zeros_like(frame)

    result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

        x = int(hand.landmark[8].x * w)
        y = int(hand.landmark[8].y * h)

        if hand.landmark[8].y < hand.landmark[6].y:
            if px != 0 and py != 0:
                cv2.line(canvas, (px, py), (x, y), (0, 255, 0), 5)
            px, py = x, y
        else:
            px, py = 0, 0
    else:q
        px, py = 0, 0

    cv2.imshow("Finger Drawing", cv2.add(frame, canvas))
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        canvas[:] = 0
    elif key == ord('q'):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()


# In[ ]:




