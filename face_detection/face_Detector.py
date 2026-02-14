import cv2
import os
import time
import sys
import numpy as np

# -------------------- Configuration -------------------- #
MODEL_DIR = "models"  # folder where model files are saved
SAVE_DIR = "saved_faces"  # folder to save detected faces
CONFIDENCE_THRESHOLD = 0.6  # minimum confidence to consider a detection

# Model files
PROTOTXT = os.path.join(MODEL_DIR, "deploy.prototxt")
MODEL = os.path.join(MODEL_DIR, "res10_300x300_ssd_iter_140000.caffemodel")


# -------------------- Helper Functions -------------------- #
def load_model(prototxt_path: str, model_path: str):
    """
    Load the Caffe SSD model from disk.
    """
    if not os.path.isfile(prototxt_path):
        print(f"[ERROR] Prototxt file not found at {prototxt_path}")
        sys.exit(1)
    if not os.path.isfile(model_path):
        print(f"[ERROR] Caffe model not found at {model_path}")
        sys.exit(1)

    print("[INFO] Loading model...")
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    return net


def initialize_camera(camera_index=0):
    """
    Initialize webcam video capture.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("[ERROR] Cannot open webcam.")
        sys.exit(1)
    return cap


def detect_faces(net, frame):
    """
    Perform face detection on a frame using the DNN model.
    Returns list of bounding boxes and confidences.
    """
    (h, w) = frame.shape[:2]
    # Prepare input blob
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 1.0,
        (300, 300), (104.0, 177.0, 123.0)
    )
    net.setInput(blob)
    detections = net.forward()
    faces = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > CONFIDENCE_THRESHOLD:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            # Ensure bounding boxes are within the frame
            startX, startY = max(0, startX), max(0, startY)
            endX, endY = min(w - 1, endX), min(h - 1, endY)
            faces.append((startX, startY, endX, endY, confidence))
    return faces


def save_faces(frame, faces):
    """
    Save detected faces to SAVE_DIR with unique filenames.
    """
    os.makedirs(SAVE_DIR, exist_ok=True)
    for idx, (startX, startY, endX, endY, confidence) in enumerate(faces):
        face_crop = frame[startY:endY, startX:endX]
        timestamp = int(time.time() * 1000)
        filename = os.path.join(SAVE_DIR, f"face_{timestamp}_{idx}.png")
        cv2.imwrite(filename, face_crop)


def draw_faces(frame, faces):
    """
    Draw bounding boxes and confidence on the frame.
    """
    for (startX, startY, endX, endY, confidence) in faces:
        text = f"{confidence*100:.1f}%"
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(frame, text, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)


# -------------------- Main Function -------------------- #
def main():
    # Load model
    net = load_model(PROTOTXT, MODEL)

    # Initialize webcam
    cap = initialize_camera()

    prev_time = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        # Detect faces
        faces = detect_faces(net, frame)

        # Draw faces and confidence
        draw_faces(frame, faces)

        # Save detected faces
        save_faces(frame, faces)

        # Display face count
        cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Calculate FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show frame
        cv2.imshow("Face Detection", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


# -------------------- Entry Point -------------------- #
if __name__ == "__main__":
    main()
