# generate two random frames
import random
import numpy as np
import cv2
import time
import ctypes


# so i used the profiling example from earlier, and i actually managed to speed up the MSE calculation by using C code.
# it only sped up a bit, but it's probably because the way i call the C code is not optimal.
# but it works, so i can use it in the future for other calculations.
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

    # fast new variant with c code?
    # Load C lib
    lib = ctypes.CDLL("./libmse.so")
    mse_c = lib.mse_uint8
    mse_c.argtypes = [
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.POINTER(ctypes.c_uint8),
        ctypes.c_int,
    ]
    mse_c.restype = ctypes.c_double
    start_time2 = time.time()
    for i in range(1000):
        frame1 = generate_random_frame(640, 480)
        frame2 = generate_random_frame(640, 480)
        assert frame1.shape == frame2.shape, "Frames must have the same shape"
        size = frame1.size
        ptr1 = frame1.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
        ptr2 = frame2.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))

        # Compute
        mse_fast = mse_c(ptr1, ptr2, size)
    end_time2 = time.time()
    print(f"Fast variant took {end_time2 - start_time2:.4f} seconds")
    # calculate the speedup
    speedup = (end_time1 - start_time1) / (end_time2 - start_time2)
    print(f"Speedup: {speedup:.2f}x")


if __name__ == "__main__":
    main()
