import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.models import load_model
import time

# Load the pre-trained model
model = load_model('/Users/macbook/Desktop/trash_classification_model.h5')

# Class labels 
class_labels = {
    0: 'cardboard',
    1: 'e-waste',
    2: 'glass',
    3: 'medical',
    4: 'metal',
    5: 'paper',
    6: 'plastic'
}

# Initialize webcam for real-time classification
cap = cv2.VideoCapture(0)
last_prediction_time = time.time()
last_label = ""  # Store the last prediction label
last_probabilities = None  # Store the last prediction probabilities

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Check if 10 seconds have passed since the last prediction
    current_time = time.time()
    if current_time - last_prediction_time >= 10:
        # Preprocess the frame for EfficientNet
        img = cv2.resize(frame, (224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Predict the class
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        last_label = class_labels[predicted_class]  # Update the last prediction label
        last_probabilities = predictions[0]  # Update the last prediction probabilities
        last_prediction_time = current_time  # Update the last prediction time

    # Display the last label on the frame
    if last_label:
        cv2.putText(frame, f'Prediction: {last_label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the probabilistic output on the frame
    if last_probabilities is not None:
        for i, (label, prob) in enumerate(zip(class_labels.values(), last_probabilities)):
            text = f'{label}: {prob:.2f}'
            cv2.putText(frame, text, (10, 60 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

    # Display the frame with the label and probabilities
    cv2.imshow('Trash Classification', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
