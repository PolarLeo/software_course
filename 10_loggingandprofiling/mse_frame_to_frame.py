import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pandas as pd
import logging
import os

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("mse_frame_to_frame.log")],
)

# Path to the directory containing .mp4 files
video_dir = Path("../vids_cropped/").glob("*.mp4")
skip_frames = 10  # Number of frames to skip for MSE calculation
# limit to only videos at distance 0.1
# Loop through each .mp4 file
video_dir = Path("../vids_cropped/").glob(f"*{'20250604'}*.mp4")
for video_path in video_dir:
    print(f"Processing: {video_path}")
    # Add your video processing code here
    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        exit()

    # Open the video file
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    # init
    mse_list = []
    prev_frame = None
    frame_number = 0
    # Loop through each frame
    while True:
        ret, frame = cap.read()
        # Break the loop if no frame is returned (end of video)
        if not ret:
            print("End of video.")
            break

            # compare the frame with the previous frame with MSE
        if frame_number % skip_frames == 0 and prev_frame is not None:
            mse = np.mean(((cv2.absdiff(prev_frame, frame) ** 2)))
            # print(f"MSE: {mse}")
            # append to a list of MSEs
            mse_list.append(mse)
        # save previous frame
        prev_frame = frame
        frame_number += 1
    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Define a function to calculate the moving average
    def moving_average(data, window_size):
        kernel = np.ones(window_size) / window_size
        moving_std = np.array(
            [
                np.std(data[i : i + window_size])
                for i in range(len(data) - window_size + 1)
            ]
        )
        return np.convolve(data, kernel, mode="valid"), moving_std

    # Apply the moving average to the MSE list
    window_size = 30  # frames?
    fps = 60  # frames per second
    smoothed_mse, moving_std = moving_average(mse_list, window_size)

    # Plot the original MSE values
    plt.plot(mse_list, label="Original MSE", alpha=0.5)
    # plot the std
    plt.plot(
        range(window_size - 1, len(mse_list)),
        moving_std,
        label="Moving STD",
        alpha=0.5,
        color="orange",
    )
    # Plot the smoothed mse values
    plt.plot(
        range(window_size - 1, len(mse_list)),
        smoothed_mse,
        label="Smoothed MSE",
        color="red",
    )
    # plot where the average is larger than the std
    boolean_array = smoothed_mse > 3 * moving_std
    seconds_above_std = sum(boolean_array) * window_size / fps
    print("seconds above std: " + str(seconds_above_std))
    plt.plot(
        np.where(boolean_array)[0] + window_size - 1,
        smoothed_mse[boolean_array],
        "x",
        alpha=0.5,
        label="Above STD",
        color="green",
    )

    # Add labels and title
    plt.xlabel("Frame number")
    plt.ylabel("MSE")
    plt.title("MSE vs Frame number (with Moving Average)")
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.savefig("./png/" + video_path.stem + "_" + str(skip_frames) + "SKIPPED_mse.png")
    plt.clf()
    print(
        f"Saved plot for {video_path.stem} with {skip_frames} frames skipped to png/"
        + video_path.stem
        + "_"
        + str(skip_frames)
        + "SKIPPED_mse.png"
    )
    # Save mse data to a CSV file
    csv_file = "./csv/" + video_path.stem + "_" + str(skip_frames) + "SKIPPED_mse.csv"
    df = pd.DataFrame(
        {
            "Frame Number": [i * skip_frames for i in range(len(mse_list))],
            "MSE": mse_list,
            "seconds above std": seconds_above_std,
        }
    )
    df.to_csv(csv_file, index=False)
    print(
        f"Saved mse data for {video_path.stem} with {skip_frames} frames skipped to csv/"
        + video_path.stem
        + "_"
        + str(skip_frames)
        + "SKIPPED_mse.csv"
    )
