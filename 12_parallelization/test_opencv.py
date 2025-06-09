import cv2
import numpy as np
import time

img = np.random.randint(0, 256, (2160, 3840, 3), dtype=np.uint8)  # simulate 4K image

def test(label):
    start = time.time()
    for _ in range(10):
        cv2.GaussianBlur(img, (41, 41), 0)
    end = time.time()
    print(f"{label}: {end - start:.3f} seconds")

cv2.setNumThreads(1)
cv2.setUseOptimized(False)
test("Single-threaded")

cv2.setNumThreads(cv2.getNumberOfCPUs())
cv2.setUseOptimized(True)
test("Multi-threaded")

