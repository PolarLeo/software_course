// mse.c
#include <stdint.h>

double mse_uint8(uint8_t* img1, uint8_t* img2, int size) {
    double mse = 0.0;
    for (int i = 0; i < size; ++i) {
        int diff = img1[i] - img2[i];
        mse += diff * diff;
    }
    return mse / size;
}

