"""
Swipe detection class.
"""
import cv2
import mediapipe as mp

# pylint disable=too-many-instance-attributes


class SwipeDetection():
    """
    Class containing functions for swipe detection.

    Attributes:
        Hands: the object the camera actually tracks
        mp_drawing:
        mp_hands:
        mode:
        max_hands
        min_detection_con:
        min_track_con:
        results:
    """

    def __init__(self, mode=False, max_hands=2, min_detectioncon=.6,
                 min_trackcon=.5):

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.mode = mode
        self.max_hands = max_hands
        self.min_detection_con = min_detectioncon
        self.min_track_con = min_trackcon
        self.results = None
        self.hands = self.mp_hands.Hands(model_complexity=0,
                                         min_detection_confidence=.6,
                                         min_tracking_confidence=.5)
        # self.hands = self.mp_hands.Hands(self.mode, self.max_hands,
        #                                  self.min_detection_con,
        #                                  self.min_track_con)
        # For webcam input:
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def move_to_pos(self, cheems_move):
        """
        returns movement vector based on the move
        cheems uses goes left for attack, right for defend,
        and up for magic

        Args:
            cheems_move: takes in "attack", "defend", or "magic"

        returns [0, 0] for other strings
        """
        vector = [0, 0]
        if cheems_move == "attack":
            vector = [-1, 0]  # left
        elif cheems_move == "defend":
            vector = [1, 0]  # right
        elif cheems_move == "magic":
            vector = [0, -1]  # up

        return vector

    def determine_move(self):
        """
        opening and starting open cv to track hands
        tracking hand position overtime and compares
        overall movement

        returns a string of move based on hand direction
        """
        # with self.mp_hands.Hands(
        #         model_complexity=0,
        #         min_detection_confidence=0.6,
        #         min_tracking_confidence=0.5) as hands:
        i = 0
        overall_list = []  # trying to create a list containing past and
        # present positions
        while self.cap.isOpened():  # while video is being captured
            success, image = self.cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as
            # not writeable topass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            points = results.multi_hand_landmarks
            # print(points)  # prints None if no hand, list of dictionaries
            # if hand seen, all 21 points tracked
            if results.multi_hand_landmarks:  # if hand is in frame
                for hand_landmarks in points:  # goes through landmarks
                    # in points
                    lmlist = []
                    if points:
                        myhand = points[0]  # point at base of palm
                        # myhand.landmark = each point being tracked?
                        # 21 points per hand, elem = x and y coords per point
                        i += 1
                        # goes through 21 points
                        for pointnumb, elem in enumerate(myhand.landmark):
                            height, width, _ = image.shape
                            centerx, centery = int(
                                elem.x*width), int(elem.y*height)
                            lmlist.append([pointnumb, centerx, centery])
                    # list of of lists of 3 coords, doesn't save previous coords
                    overall_list.append(lmlist)
                self.mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style())
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if i > 2:  # top right is 0,0
                if overall_list[-1][0][1] - overall_list[0][0][1] > 150:
                    self.cap.release()
                    return "attack"  # left
                if overall_list[-1][0][1] - overall_list[0][0][1] < -150:
                    self.cap.release()
                    return "defend"  # right
                if overall_list[-1][0][2] - overall_list[0][0][2] < -150:
                    self.cap.release()
                    return "magic"  # up
                if overall_list[-1][0][2] - overall_list[0][0][2] > 200:
                    return "end"  # down
            if cv2.waitKey(5) & 0xFF == 27:
                break

    def quit(self):
        """
        Function to close all OpenCV windows.
        """
        self.cap.release()
        cv2.destroyAllWindows()
