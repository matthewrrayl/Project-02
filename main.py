# Matthew Rayl
# Project 2
# Original Idea: https://www.youtube.com/watch?v=xv3G5sIx2co
# Added ideas: Loop/View Image option

import cv2
from deepface import DeepFace


def main():
    inputimage = input('Enter image path: ')  # Input path to image
    image = cv2.imread(inputimage)
    check = 1
    while check == 1:
        analyze = DeepFace.analyze(image, actions=('emotion', 'age', 'gender', 'race'))
        print(f'Dominant Emotion: {analyze["dominant_emotion"]}')
        print(f'Age: {analyze["age"]}')
        print(f'Gender: {analyze["gender"]}')
        print(f'Race: {analyze["dominant_race"]}')

        view = input('View Image? y/n: ')  # Input y or n to see the inputted image
        view = view.strip().lower()
        if view == 'y':
            cv2.imshow(inputimage, image)
            cv2.waitKey(0)  # Hit any key on keyboard to close the image
        repeat = input('Analyze another image? y/n: ')  # Input y or n to analyze new image
        repeat = repeat.strip().lower()
        if repeat == 'y':
            inputimage = input('Enter image path: ')
        elif repeat == 'n':
            check += 1


if __name__ == '__main__':
    main()
