import cv2
import math

def select_ball(contours, min_radius):
    if not contours:
        return None

    best = None
    best_area = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area < 200:
            continue

        perimeter = cv2.arcLength(c, True)
        if perimeter == 0:
            continue

        circularity = 4 * math.pi * area / (perimeter * perimeter)
        if circularity < 0.7:
            continue

        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius < min_radius:
            continue

        if area > best_area:
            best_area = area
            best = (int(x), int(y), int(radius))

    return best
