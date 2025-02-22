import cv2
import numpy as np
import mediapipe as mp
import random
import time

# Initialize MediaPipe for hand tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Ball properties (starting from center-right)
ball_x, ball_y = 450, 50  # Ball starts from the center-right
ball_speed = 10  # Ball speed

# Ball lengths (Short, Good, Full)
ball_lengths = {"Short": 250, "Good": 350, "Full": 450}
current_length = random.choice(list(ball_lengths.values()))  # Random ball length

# Initialize bat position
prev_x, prev_y = 0, 0

# Initialize shot type & score
shot_type = "Waiting for shot..."  
color = (255, 255, 255)
score = 0  # Start with zero score
total_balls = 100  # Total balls to be played
balls_played = 0  # Balls played counter

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for better interaction
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hand (bat)
    result = hands.process(rgb_frame)
    
    bat_x, bat_y = None, None  # Reset bat coordinates
    bat_contact = False  # Reset bat-ball collision flag

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index finger tip (bat position)
            bat_x = int(hand_landmarks.landmark[8].x * frame.shape[1])
            bat_y = int(hand_landmarks.landmark[8].y * frame.shape[0])

            # Show detected hand position
            cv2.putText(frame, f"Bat: {bat_x}, {bat_y}", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Calculate bat speed
            speed = np.sqrt((bat_x - prev_x) ** 2 + (bat_y - prev_y) ** 2) if bat_x and bat_y else 0

            # Check for bat-ball collision
            if bat_x and abs(bat_x - ball_x) < 40 and abs(bat_y - ball_y) < 40:
                bat_contact = True

            # Shot classification
            if bat_contact:
                if speed > 40:
                    shot_type = "Power Shot (SIX)"
                    color = (0, 0, 255)
                    score += 6  # Increase score by 6
                elif 20 < speed <= 40:
                    shot_type = "Drive (Four)"
                    color = (0, 255, 255)
                    score += 4  # Increase score by 4
                else:
                    shot_type = "Defensive Shot"
                    color = (255, 255, 255)
                    score += 1  # Increase score by 1

                # PAUSE for 2 seconds on valid shots
                cv2.putText(frame, shot_type, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                cv2.putText(frame, f"Score: {score}", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cricket Batting Simulation", frame)
                cv2.waitKey(2000)  # Pause for 2 seconds before resuming
            else:
                shot_type = "Missed Shot"
                color = (0, 165, 255)

            prev_x, prev_y = bat_x, bat_y  # Update previous position

    else:
        # If no hand is detected, display waiting message
        shot_type = "No Hand Detected"
        color = (0, 0, 255)

    # Ball movement (coming from center-right)
    if ball_y < current_length:
        ball_y += ball_speed
    else:
        ball_y = 50  # Reset ball position
        ball_x = 450  # Always from the center-right
        current_length = random.choice(list(ball_lengths.values()))  # New ball length
        balls_played += 1  # Increase ball count

    # Draw bowler (Fixed on center-right)
    cv2.circle(frame, (450, 30), 20, (0, 255, 0), -1)  # Head
    cv2.line(frame, (450, 50), (450, 110), (0, 255, 0), 5)  # Body
    cv2.line(frame, (450, 70), (470, 90), (0, 255, 0), 5)  # Arm (throwing)

    # Draw ball
    cv2.circle(frame, (ball_x, ball_y), 10, (255, 0, 0), -1)

    # Display shot type, score, and remaining balls
    cv2.putText(frame, shot_type, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.putText(frame, f"Score: {score}", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Balls Left: {total_balls - balls_played}", (500, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show frame
    cv2.imshow("Cricket Batting Simulation", frame)

    # End game after 10 balls
    if balls_played >= total_balls:
        cv2.putText(frame, "Game Over!", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.putText(frame, f"Total Score: {score}", (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.imshow("Cricket Batting Simulation", frame)
        cv2.waitKey(3000)  # Pause for 3 seconds
        break

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
