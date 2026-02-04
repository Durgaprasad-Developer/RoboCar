# backend/vision/ball_tracking/config.py
import numpy as np

# ORANGE BALL (indoor light – safe range)
LOWER_HSV = np.array([0, 100, 100])
UPPER_HSV = np.array([30, 255, 255])

MIN_RADIUS = 6

# tracking tolerance
MAX_MISSED_FRAMES = 5