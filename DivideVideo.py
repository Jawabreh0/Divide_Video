import cv2
import math

# Open the video file
video = cv2.VideoCapture('./Oguzhan_Vid1.MOV')

# Get the total number of frames and calculate the interval between frames to capture
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_interval = math.ceil(total_frames / 500)

# Initialize variables
frame_count = 0
image_count = 0
success = True

# Loop through the video frames
while success:
    # Read the next frame
    success, image = video.read()

    # Only process frames that were read successfully
    if success:
        # Increment the frame counter
        frame_count += 1

        # Only save frames at the desired intervals
        if frame_count % frame_interval == 0:
            # Increment the image counter
            image_count += 1

            # Save the image
            cv2.imwrite(
                "./ok/{}.jpg".format(image_count), image)

            if image_count == 500:
                break

    # Jugaaaaaaar
    if frame_count == total_frames and image_count < 500:
        video.set(cv2.CAP_PROP_POS_FRAMES, total_frames-1)
        _, image = video.read()

        while image_count < 500:
            image_count += 1
            cv2.imwrite(
                "./ok/{}.jpg".format(image_count), image)

video.release()
