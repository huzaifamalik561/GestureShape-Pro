import cv2
import mediapipe as mp
import pyautogui
import random
import time
import math
import numpy as np

# Initialize variables
sy = 0
sx = 600

# Define a list of shapes
S = ["square", "circle", "triangle"]
random_shape = random.choice(S)
colors = [(0, 0, 255), (0, 255, 255), (0, 255, 0)]
random_color = random.choice(colors)

# Create a larger display window
window_width = 1280
window_height = 720

# Initialize the webcam capture
cap = cv2.VideoCapture(0)
cap.set(3, window_width)
cap.set(4, window_height)

# Initialize the hand detection model
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Initialize circle2 position
y2 = 0
x2 = random.randint(10, 680)
circle2_radius = 10
sx2, sy2 = 0, 0

# Initialize previous shape variables and score
prev_shape = None
prev_color = None
score = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x1 = int(landmark.x * frame_width)
                y1 = int(landmark.y * frame_height)
                if id == 8:  # Index finger tip
                    cv2.circle(img=frame, center=(x1, y1), radius=10, color=(0, 255, 255), thickness=-1)
                    pyautogui.moveTo(x1, y1)

                    # Check if shape is within the region of the shape
                    if random_shape == "circle":
                        cv2.circle(img=frame, center=(x2, y2), radius=70, color=random_color, thickness=-1)
                        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        circumference = 2 * math.pi * 70
                        if distance <= circumference / 6:
                            if random_color == (0, 0, 255):  # Red color
                                score += 5
                            elif random_color == (0, 255, 255):  # Yellow color
                                score += 2
                            elif random_color == (0, 255, 0):  # Green color
                                score -= 2
                            y2 = 0
                            x2 = random.randint(10, 680)
                            prev_shape = random_shape
                            prev_color = random_color
                            random_shape = random.choice(S)
                            random_color = random.choice(colors)
                            time.sleep(2)

                        y2 += 20
                        if y2 >= frame_height:
                            y2 = 0
                            x2 = random.randint(10, 680)
                            random_shape = random.choice(S)
                            random_color = random.choice(colors)

                    if random_shape == "square":
                        cv2.rectangle(img=frame, pt1=(sx, sy), pt2=(sx + 40, sy + 40), color=random_color,
                                      thickness=-1)
                        if abs(x1 - sx) <= 20 and abs(y1 - sy) <= 20:
                            if random_color == (0, 0, 255):  # Red color
                                score += 5
                            elif random_color == (0, 255, 255):  # Yellow color
                                score += 2
                            elif random_color == (0, 255, 0):  # Green color
                                score -= 2
                            sy = 0
                            sx = random.randint(10, 680)
                            prev_shape = random_shape
                            prev_color = random_color
                            random_shape = random.choice(S)
                            random_color = random.choice(colors)
                        if sy >= frame_height:
                            sy = 0
                            sx = random.randint(10, 680)
                            random_shape = random.choice(S)
                            random_color = random.choice(colors)
                        sy += 10

                    if random_shape == "triangle":
                        triangle_vertices = [(x2, y2), (x2 + 140, y2), (x2 + 70, y2 - 140)]
                        cv2.fillPoly(frame, [np.array(triangle_vertices)], random_color)

                        def point_in_triangle(pt, v1, v2, v3):
                            b1 = ((v2[1] - v3[1]) * (pt[0] - v3[0]) + (v3[0] - v2[0]) * (pt[1] - v3[1])) / \
                                 ((v2[1] - v3[1]) * (v1[0] - v3[0]) + (v3[0] - v2[0]) * (v1[1] - v3[1]))
                            b2 = ((v3[1] - v1[1]) * (pt[0] - v3[0]) + (v1[0] - v3[0]) * (pt[1] - v3[1])) / \
                                 ((v2[1] - v3[1]) * (v1[0] - v3[0]) + (v3[0] - v2[0]) * (v1[1] - v3[1]))
                            b3 = 1 - b1 - b2
                            return 0 <= b1 <= 1 and 0 <= b2 <= 1 and 0 <= b3 <= 1

                        if point_in_triangle((x1, y1), triangle_vertices[0], triangle_vertices[1], triangle_vertices[2]):
                            if random_color == (0, 0, 255):  # Red color
                                score += 5
                            elif random_color == (0, 255, 255):  # Yellow color
                                score += 2
                            elif random_color == (0, 255, 0):  # Green color
                                score -= 2
                            y2 = 0
                            x2 = random.randint(10, 680)
                            prev_shape = random_shape
                            prev_color = random_color
                            random_shape = random.choice(S)
                            random_color = random.choice(colors)
                            time.sleep(2)
                        y2 += 20
                        if y2 >= frame_height:
                            y2 = 0
                            x2 = random.randint(10, 680)
                            random_shape = random.choice(S)
                            random_color = random.choice(colors)

    # Display the score on the top right corner of the frame
    score_text = f"Score: {score}"
    cv2.putText(frame, score_text, (frame_width - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Check if the score reaches 20
    if score >= 20:
        # Display "Winner" message
        winner_text = "Winner! Congrats!"
        cv2.putText(frame, winner_text, (frame_width // 2 - 100, frame_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 0), 2)
        score = 20  # Limit the score to 20

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
