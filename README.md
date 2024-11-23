# ObstacleDetectionSystem on MACOS M1
# 1. Framework for the Object Detection System
This document outlines the framework for your object detection system, summarizing the key components, the development process, and troubleshooting steps. It is derived from iterative improvements and solutions discussed during the development.
# 2. Project Structure
ObstacleDetectionSystem/

├── data/

│   ├── images/                (Input images for detection)

│   └── models/                (Pre-trained models)

├── venv/                      (Python virtual environment)

├── detect_object.py           (Main detection script)

└── README.md                  (Project documentation)

# 3. Development Process
Step 1: Setting Up the Environment
Install Python 3.11.
step 2:Set up a virtual environment
python3 -m venv venv
step3: source venv/bin/activate
Install dependencies:
pip install tensorflow opencv-python numpy

# 4. Key Features
Pre-trained SSD MobileNet Model: Leverages TensorFlow’s object detection API for fast and accurate detection.
Confidence Filtering: Includes a confidence threshold to filter low-probability detections.
Visualization: Draws bounding boxes and labels directly on the image using OpenCV.

# 5. Challenges & Solutions
Challenge 1: Model Compatibility
Issue: Errors with model loading or API arguments, such as combined_non_max_suppression keyword arguments.
Solution: Ensured TensorFlow version compatibility and simplified post-processing logic.
Challenge 2: Dependency Conflicts
Issue: Conflicts between numpy and tensorflow versions.
Solution: Manually installed compatible versions:
bash
pip install numpy==1.26.0
Challenge 3: FileNotFoundError
Issue: Missing or misnamed files during script execution.
Solution: Added checks to verify file existence before processing.

# 6. How to Run
 Activate the virtual environment:
source venv/bin/activate
Run the detection script:
python detect_object.py
View the processed image with detected objects.

# 7. Future Work
Add support for real-time video detection.
Implement non-maximum suppression to improve bounding box accuracy.
Extend support for custom-trained models.
