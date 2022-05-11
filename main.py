# Matthew Rayl
# Project 2

import cv2
from deepface import DeepFace

inputimage = input('Enter image path: ')
image = cv2.imread(inputimage)


analyze = DeepFace.analyze(image, actions=('emotion', 'age', 'gender', 'race'))
print(f'Dominant Emotion: {analyze["dominant_emotion"]}')
print(f'Age: {analyze["age"]}')
print(f'Gender: {analyze["gender"]}')
print(f'Race: {analyze["dominant_race"]}')
