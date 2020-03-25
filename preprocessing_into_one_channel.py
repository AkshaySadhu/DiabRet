import os
import shutil
import cv2
import numpy as np
image_folder = "C:/Users/urani/Documents/Diabetic Retinopathy/train_images"
green_images_folder = "C:/Users/urani/Documents/Diabetic Retinopathy/Green Images"
clahe_images_folder = "C:/Users/urani/Documents/Diabetic Retinopathy/CLAHE_images"
normalized_images_folder = "C:/Users/urani/Documents/Diabetic Retinopathy/normalized_images"
i = 0
for root, dirs, files in os.walk(image_folder):
    for file in files:
        if file.endswith('.png'):
            image_path = os.path.join(root, file)
            print(image_path)
            file_name = file.split('.')[0]
            image = cv2.imread(image_path)
            blue, green, red = cv2.split(image)
            green_image_name = "green_channel_" + file_name + ".png"
            cv2.imwrite(green_image_name, green)

            # Creating CLAHE
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            clahe_image = clahe.apply(green)
            # cv2_imshow(cl1)
            clahe_image_name = "clahe_" + file_name + ".png"
            cv2.imwrite(clahe_image_name, clahe_image)

            # MIN-MAX NORMALIZATION
            normalizedImg = np.zeros((512, 512))
            normalizedImg = cv2.normalize(clahe_image, normalizedImg, 0, 255, cv2.NORM_MINMAX)
            normalized_image_name = "normalized_" + file_name + ".png"
            # cv2_imshow(normalizedImg)
            cv2.imwrite(normalized_image_name, normalizedImg)

            shutil.move(green_image_name, green_images_folder)
            shutil.move(clahe_image_name, clahe_images_folder)
            shutil.move(normalized_image_name, normalized_images_folder)
            i += 1
            print(i)
