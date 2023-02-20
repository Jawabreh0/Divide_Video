import cv2

# Open the video file
video = cv2.VideoCapture('./ok.MOV')

total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))


desired_frames = 500
frame_interval = max(total_frames // desired_frames, 1)  


frame_count = 0
image_count = 0
success = True

# Loop through the video frames
while success and image_count < desired_frames:
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

    if not success and image_count < desired_frames:
        video.set(cv2.CAP_PROP_POS_FRAMES, total_frames-1)
        _, image = video.read()

        while image_count < desired_frames:
            image_count += 1
            cv2.imwrite(
                "./ok/{}.jpg".format(image_count), image)

    if not success and image_count == desired_frames:
        break

video.release()
