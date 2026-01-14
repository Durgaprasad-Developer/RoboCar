import numpy as np

# ORANGE BALL (indoor light – safe range)
LOWER_HSV = np.array([5, 120, 120])
UPPER_HSV = np.array([25, 255, 255])

MIN_RADIUS = 12

# tracking tolerance
MAX_MISSED_FRAMES = 5