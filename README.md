**Virtual Mouse Game**
This is a Python application that turns your hand movements into a virtual mouse control game using OpenCV, MediaPipe, and PyAutoGUI.

**Overview**
This application uses the computer's webcam to track hand movements, specifically the position of your index finger, and maps it to control various shapes on the screen. The objective of the game is to interact with these shapes and earn points based on the color and position of the shapes.

**Features**
Real-time hand tracking using the MediaPipe library.
Three types of shapes: square, circle, and triangle.
Shapes appear randomly on the screen with different colors.
The index finger tip acts as a cursor to interact with the shapes.
Score tracking: Points are awarded or deducted based on interactions.
Winning condition: The game ends when the player reaches a score of 20 points.
**Requirements**
Python 3.x
OpenCV
MediaPipe
PyAutoGUI
NumPy
Installation
Make sure you have Python 3.x installed.

Install the required Python packages using pip:
pip install opencv-python mediapipe pyautogui numpy
Clone this repository to your local machine:

git clone https://github.com/yourusername/virtual-mouse-game.git
Navigate to the project directory:

cd virtual-mouse-game
Run the application:

python main.py
**#How to Play**
Run the application following the installation instructions.

Use your webcam to track your hand movements.

Move your index finger to control the cursor.

Interact with the shapes on the screen:

Circle: Move the cursor inside the circle to earn points.
Square: Move the cursor inside the square to earn points.
Triangle: Move the cursor inside the triangle to earn points.
Points are awarded based on the color of the shape:

Red: +5 points
Yellow: +2 points
Green: -2 points
The game ends when you reach a score of 20 points, and a "Winner" message is displayed.

**Customization**
You can customize the game by modifying the following variables in the code:

S: List of available shapes (square, circle, triangle).
colors: List of available colors (RGB tuples).
window_width and window_height: Adjust the display window size.

**Acknowledgments**
This project was inspired by computer vision and gesture control concepts.
It utilizes the MediaPipe library for hand tracking.
PyAutoGUI is used for cursor control.
