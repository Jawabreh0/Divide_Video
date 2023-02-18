import cv2

# Open the video file
video = cv2.VideoCapture('/home/jawabreh/Desktop/HumaneX '
                         'Project/Products/FaceRecognition/FR_Dataset/Team_Videos_Dataset/Ahmad_Video_Dataset'
                         '/Ahmad_Vid1.MOV')

# Get the total number of frames and calculate the interval between frames to capture
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
frame_interval = round(total_frames / 100)

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
                "/home/jawabreh/Desktop/HumaneX Project/Products/FaceRecognition/FR_Dataset/Team_Faces_Dataset"
                "/Ahmad_Face_Dataset/{}.jpg".format(image_count), image)

# Release the video object
video.release()
