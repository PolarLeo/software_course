# generate two random frames
import random
import numpy as np
import cv2
import time


# well this is funny, I tried to recreate what I did in my code earlier, where I replaced
# the slow numpy operation with a fast OpenCV operation, but it seems that the OpenCV
# operation is actually slower than the numpy operation, but I dont think that is true in my actual code
# its probably because I didnt actually reproduce the exact same operation
# and since I dont have the old cod anymore, I dont know what it was
def generate_random_frame(width, height):
    """Generate a random frame with given width and height."""
    return np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)


def main():

    # slow old variant
    # profile it
    start_time1 = time.time()

    for i in range(1000):
        frame1 = generate_random_frame(640, 480)
        frame2 = generate_random_frame(640, 480)
        mse_slow = ((frame1 - frame2) ** 2).mean()
    end_time1 = time.time()
    print(f"Slow variant took {end_time1 - start_time1:.4f} seconds")

    # fast new variant
    start_time2 = time.time()
    for i in range(1000):
        frame1 = generate_random_frame(640, 480)
        frame2 = generate_random_frame(640, 480)
        mse_fast = np.mean(cv2.absdiff(frame1, frame2) ** 2)
    end_time2 = time.time()
    print(f"Fast variant took {end_time2 - start_time2:.4f} seconds")
    # calculate the speedup
    speedup = (end_time1 - start_time1) / (end_time2 - start_time2)
    print(f"Speedup: {speedup:.2f}x")


if __name__ == "__main__":
    main()
