import tensorflow as tf
import cv2
import numpy as np

# Load the pre-trained model (replace with your model path)
model_path = "data/models/ssd_mobilenet_v1_coco_2018_01_28/saved_model"
model = tf.saved_model.load(model_path)

# Get the inference function
infer = model.signatures['serving_default']

# Load the image
image_path = "data/images/test_image_2.jpeg"
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# Print the image shape
print("Image Shape: ", image.shape)

# Convert image to RGB (OpenCV loads it in BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to a tensor and add batch dimension
input_tensor = tf.convert_to_tensor(image_rgb)
input_tensor = input_tensor[tf.newaxis, ...]

# Run inference (detection)
output = infer(input_tensor)

# Print output to verify detection results
print("Detection Boxes: ", output['detection_boxes'])
print("Detection Classes: ", output['detection_classes'])
print("Detection Scores: ", output['detection_scores'])

# Set a threshold for drawing boxes
MIN_SCORE_THRESHOLD = 0.3

# Draw boxes around detected objects (optional)
for i in range(len(output['detection_boxes'][0])):  # Iterate through the boxes
    if output['detection_scores'][0][i] > MIN_SCORE_THRESHOLD:  # Filter by score
        detection = output['detection_boxes'][0][i]

        # Get coordinates for the bounding boxes
        (ymin, xmin, ymax, xmax) = detection.numpy()

        # Convert coordinates to pixel values (if needed)
        height, width, _ = image.shape
        ymin = int(ymin * height)
        xmin = int(xmin * width)
        ymax = int(ymax * height)
        xmax = int(xmax * width)

        # Draw the bounding box
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

# Display the image with detections
cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
