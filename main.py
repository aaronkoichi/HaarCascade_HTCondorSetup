import cv2
import sys
import os

def mosaic_area(image, x, y, w, h, factor=10):
    """
    Applies a mosaic effect to a specific region of interest (ROI).
    """
    roi = image[y:y+h, x:x+w]
    small_roi = cv2.resize(roi, (w//factor, h//factor), interpolation=cv2.INTER_LINEAR)
    mosaic_roi = cv2.resize(small_roi, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = mosaic_roi
    return image

def process_image(input_path, output_dir, cascade_path):
    # Load Haar Cascade
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Read the image
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not read image {input_path}")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(f"Detected {len(faces)} faces in {input_path}")

    # Apply mosaic to each detected face
    for (x, y, w, h) in faces:
        img = mosaic_area(img, x, y, w, h)
    
    # Preserve original filename
    base_filename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, base_filename)
    # Save processed image
    cv2.imwrite(output_path, img)
    print(f"Saved processed image to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <input_image> <output_dir> <haar_xml_path>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_dir = sys.argv[2]
    haar_path = sys.argv[3]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    process_image(input_image, output_dir, haar_path)