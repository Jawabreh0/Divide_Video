# Video Frames Splitter
This is a simple Python script that can be used to convert an AI training video into a collection of JPEG images. The script utilizes the OpenCV library to extract frames from the video and save them as images.


## Usage

1. Edit the script to set the input and output paths.
```python
video_path = '/path/to/input/video.mp4'
output_dir = '/path/to/output/directory'
```

2. Run the script from the command line using Python.
```bash
python Divide_Video.py
```

3. The script will convert the video into a series of JPEG images and save them in the output directory

## Parameters
* video_path: the path to the input video file.
* output_dir: the path to the output directory where the JPEG images will be saved.
* frame_interval: the number of frames to skip before capturing a new frame. This value can be adjusted to capture more or fewer images from the video.

## Dependencies
* OpenCV (cv2) library
* Python 3.x
