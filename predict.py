import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.models.load_model('models/plant.h5')

# Function to preprocess the user-uploaded image
def preprocess_image(user_image_path):
    img = image.load_img(user_image_path, target_size=(224,224,3))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  
    return img

# Function to predict the class of the user-uploaded image
def predict_image_class(user_image_path):
    img = preprocess_image(user_image_path)
    predictions = model.predict(img)
    predicted_class_index = np.argmax(predictions)
    class_labels = ['Apple_scab', 'Apple Black rot', 'Apple Cedar apple rust',
                    'Apple healthy','Blueberry healthy','Cherry healthy',
                    'Cherry Powdery mildew','Corn Cercospora leaf spot Gray leaf spot','Corn Common rust ',
                    'Corn healthy','Corn Northern Leaf Blight','Grape Black rot',
                    'Grape Esca','Grape Leaf blight','Grape healthy',
                    'Orange Haunglongbing','Peach Bacterial spot'
                    ,'Peach healthy','Pepper bell Bacterial spot','Pepper bell healthy',
                    'Potato Early blight','Potato healthy','Potato Late blight',
                    'Raspberry healthy','Soybean healthy','Squash Powdery mildew'
                    ,'Strawberry healthy','Strawberry Leaf scorch','Tomato Bacterial spot',
                    'Tomato Early blight','Tomato healthy','Tomato Late blight',
                    'Tomato Leaf Mold','Tomato Septoria leaf spot','Tomato Spider mites',
                    'Tomato Target Spot','Tomato mosaic virus','Tomato Yellow Leaf Curl Virus'] 
  

    predicted_class = class_labels[predicted_class_index]
    #confidence = predictions[0][predicted_class_index]
    return predicted_class

# Example usage
#user_uploaded_image_path = 'strowberry.jpeg'
#predicted_class, confidence = predict_image_class(user_uploaded_image_path)

#print(f"Predicted Class: {predicted_class} with confidence: {confidence:.2f}")
