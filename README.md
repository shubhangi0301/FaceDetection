# Face Detection using OpenCV

This repository contains a Python script for real-time face detection using OpenCV. The script detects faces in a webcam feed and draws rectangles around them.

## Requirements

- Python 3.x
- OpenCV library (`pip install opencv-python`)
  
## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/shubhangi0301/face-detection.git
   ```


3. Navigate to the directory containing the script:

   ```bash
   cd face-detection
   ```

5. Run the script:

   ```bash
   python facedetector.py
   ```

7. The script will open a window displaying the webcam feed with rectangles drawn around detected faces. Press the `Esc` key to exit the program.

## Troubleshooting

- If you encounter any issues with the script, ensure that you have installed the necessary dependencies and that your webcam is properly connected.
- If the cascade classifier fails to load, check the path to the XML file specified in the script.
