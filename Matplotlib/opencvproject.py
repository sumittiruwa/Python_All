"""
Hand Gesture Recognition Project
A complete hand detection and gesture recognition system using OpenCV and MediaPipe
Detects and classifies various hand gestures in real-time

Author: AI Assistant
Requirements: opencv-python, mediapipe, numpy
"""

import cv2
import mediapipe as mp
import numpy as np
from collections import deque
import math

class HandGestureRecognizer:
    def __init__(self):
        """Initialize MediaPipe Hand Detector and Gesture Classifier"""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # Gesture history for smoothing
        self.gesture_history = deque(maxlen=5)
        self.gesture_text = ""
        
        # Colors for visualization
        self.colors = {
            'hand': (0, 255, 0),      # Green
            'gesture': (0, 0, 255),   # Red
            'landmark': (255, 0, 0)   # Blue
        }

    def calculate_distance(self, point1, point2):
        """Calculate Euclidean distance between two points"""
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def is_finger_extended(self, landmarks, finger_tip, finger_pip):
        """Check if a finger is extended"""
        return landmarks[finger_tip].y < landmarks[finger_pip].y

    def recognize_gesture(self, hand_landmarks):
        """
        Recognize hand gestures based on landmarks
        Detects: Peace, Thumbs Up, OK, Fist, Point, Open Hand, Rock
        """
        landmarks = hand_landmarks.landmark
        
        # Get finger tip positions (normalized to image space)
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        
        # Get finger pip positions
        index_pip = landmarks[6]
        middle_pip = landmarks[10]
        ring_pip = landmarks[14]
        pinky_pip = landmarks[18]
        
        # Get palm center
        wrist = landmarks[0]
        
        # Check which fingers are extended
        index_extended = self.is_finger_extended(landmarks, 8, 6)
        middle_extended = self.is_finger_extended(landmarks, 12, 10)
        ring_extended = self.is_finger_extended(landmarks, 16, 14)
        pinky_extended = self.is_finger_extended(landmarks, 20, 18)
        thumb_extended = landmarks[4].y < landmarks[3].y
        
        # Count extended fingers
        extended_count = sum([index_extended, middle_extended, ring_extended, pinky_extended])
        
        # Gesture Recognition Logic
        
        # 1. PEACE SIGN - Index and middle extended, others closed
        if index_extended and middle_extended and not ring_extended and not pinky_extended:
            distance = self.calculate_distance(
                (index_tip.x, index_tip.y),
                (middle_tip.x, middle_tip.y)
            )
            if distance > 0.05:  # Fingers separated
                return "✌️ PEACE"
        
        # 2. THUMBS UP - Only thumb extended, hand facing sideways
        if thumb_extended and not index_extended and not middle_extended:
            if thumb_tip.y < landmarks[5].y:  # Thumb above palm
                return "👍 THUMBS UP"
        
        # 3. OK GESTURE - Thumb and index together, others extended
        if not index_extended and not middle_extended and ring_extended and pinky_extended:
            thumb_index_dist = self.calculate_distance(
                (thumb_tip.x, thumb_tip.y),
                (index_tip.x, index_tip.y)
            )
            if thumb_index_dist < 0.05:  # Thumb and index touching
                return "👌 OK"
        
        # 4. POINT/INDEX - Only index extended, others closed
        if index_extended and not middle_extended and not ring_extended and not pinky_extended:
            return "☝️ POINT"
        
        # 5. FIST - All fingers closed
        if not index_extended and not middle_extended and not ring_extended and not pinky_extended and not thumb_extended:
            return "✊ FIST"
        
        # 6. OPEN HAND - All fingers extended
        if index_extended and middle_extended and ring_extended and pinky_extended and thumb_extended:
            return "✋ OPEN HAND"
        
        # 7. ROCK - Index and pinky extended, middle and ring closed
        if index_extended and not middle_extended and not ring_extended and pinky_extended:
            return "🤘 ROCK"
        
        # 8. THREE - Index, middle, ring extended
        if index_extended and middle_extended and ring_extended and not pinky_extended:
            return "3️⃣ THREE"
        
        # 9. THUMBS DOWN - Thumb pointing down
        if thumb_extended and not index_extended and not middle_extended:
            if thumb_tip.y > landmarks[5].y:  # Thumb below palm
                return "👎 THUMBS DOWN"
        
        # Default
        return "Unknown"

    def smooth_gesture(self, gesture):
        """Smooth gesture recognition using history"""
        self.gesture_history.append(gesture)
        # Return most common gesture in history
        from collections import Counter
        if self.gesture_history:
            return Counter(self.gesture_history).most_common(1)[0][0]
        return gesture

    def draw_landmarks(self, image, hand_landmarks, handedness):
        """Draw hand landmarks and connections on image"""
        self.mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS,
            self.mp_drawing_styles.get_default_hand_landmarks_style(),
            self.mp_drawing_styles.get_default_hand_connections_style()
        )

    def process_frame(self, frame):
        """Process a frame and detect hand gestures"""
        # Flip frame horizontally for selfie view
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape
        
        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect hands
        results = self.hands.process(rgb_frame)
        
        gesture_results = []
        
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                # Draw landmarks
                self.draw_landmarks(frame, hand_landmarks, handedness)
                
                # Recognize gesture
                gesture = self.recognize_gesture(hand_landmarks)
                smoothed_gesture = self.smooth_gesture(gesture)
                
                # Get hand label (Left/Right)
                hand_label = handedness.classification[0].label
                
                gesture_results.append({
                    'hand': hand_label,
                    'gesture': smoothed_gesture,
                    'landmarks': hand_landmarks
                })
        
        return frame, gesture_results

    def draw_info(self, frame, gesture_results):
        """Draw gesture information on frame"""
        h, w, c = frame.shape
        
        # Add title
        cv2.putText(frame, "Hand Gesture Recognition", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Add instructions
        cv2.putText(frame, "Press 'Q' to quit | Press 'S' to save image", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
        
        # Display gesture information
        y_offset = 120
        if gesture_results:
            for idx, result in enumerate(gesture_results):
                text = f"{result['hand']} Hand: {result['gesture']}"
                cv2.putText(frame, text, (10, y_offset + idx * 40),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No hand detected", (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Add FPS counter
        cv2.putText(frame, "FPS: 30", (w - 150, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return frame

    def run(self):
        """Main execution function - Start webcam and detect gestures"""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open webcam")
            return
        
        # Set camera properties
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        cap.set(cv2.CAP_PROP_FPS, 30)
        
        print("=" * 60)
        print("Hand Gesture Recognition System")
        print("=" * 60)
        print("Detected Gestures:")
        print("  ✌️  PEACE      - Index and middle extended")
        print("  👍 THUMBS UP   - Thumb pointing up")
        print("  👎 THUMBS DOWN - Thumb pointing down")
        print("  👌 OK          - Thumb and index together")
        print("  ☝️  POINT       - Only index extended")
        print("  ✊ FIST        - All fingers closed")
        print("  ✋ OPEN HAND   - All fingers extended")
        print("  🤘 ROCK        - Index and pinky extended")
        print("  3️⃣  THREE       - Index, middle, ring extended")
        print("=" * 60)
        print("Controls:")
        print("  Press 'Q' to quit")
        print("  Press 'S' to save image")
        print("=" * 60)
        
        image_counter = 0
        
        try:
            while True:
                ret, frame = cap.read()
                
                if not ret:
                    print("Error: Could not read frame")
                    break
                
                # Process frame
                frame, gesture_results = self.process_frame(frame)
                
                # Draw information
                frame = self.draw_info(frame, gesture_results)
                
                # Display frame
                cv2.imshow("Hand Gesture Recognition", frame)
                
                # Handle keyboard input
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == ord('Q'):
                    print("\nExiting...")
                    break
                elif key == ord('s') or key == ord('S'):
                    filename = f"gesture_capture_{image_counter}.jpg"
                    cv2.imwrite(filename, frame)
                    print(f"Image saved: {filename}")
                    image_counter += 1
        
        except KeyboardInterrupt:
            print("\nInterrupted by user")
        
        finally:
            cap.release()
            cv2.destroyAllWindows()
            print("Camera released and windows closed")

    def process_image(self, image_path):
        """Process a single image file"""
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not load image from {image_path}")
            return
        
        frame, gesture_results = self.process_frame(image)
        frame = self.draw_info(frame, gesture_results)
        
        # Save result
        output_path = "gesture_result.jpg"
        cv2.imwrite(output_path, frame)
        print(f"Result saved to {output_path}")
        
        # Display
        cv2.imshow("Hand Gesture Recognition - Image", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    """Main entry point"""
    import sys
    
    recognizer = HandGestureRecognizer()
    
    if len(sys.argv) > 1:
        # Process image if provided
        recognizer.process_image(sys.argv[1])
    else:
        # Run webcam mode
        recognizer.run()


if __name__ == "__main__":
    main()