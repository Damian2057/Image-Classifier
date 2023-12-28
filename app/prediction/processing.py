import numpy as np
import os
import logging
from datetime import datetime
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

MODEL_PATH = 'mobilenetv2.h5'
TEMP_IMAGE_PATH = 'TEMP_IMAGE_PATH'
logger = logging.getLogger(__name__)

try:
    model = load_model(MODEL_PATH)
except (OSError, ImportError):
    print("Model not found. Downloading and saving the model.")
    model = MobileNetV2(weights='imagenet')
    model.save(MODEL_PATH)

def predict_clothing(file):
    image_path = TEMP_IMAGE_PATH + datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    file.save(image_path)
    logger.info("Image saved to %s", image_path)

    # Load and preprocess the input image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    os.remove(image_path)
    logger.info("Image removed from %s", image_path)

    # Decode and print the top predicted label
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    top_label = decoded_predictions[0][1]
    logger.info("Predicted category: %s", top_label)

    return top_label