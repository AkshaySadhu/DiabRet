import cv2
import numpy as np
import os
import shutil

disformed_image_count = 0
i = 1
unprocessable_images = "C:/Users/urani/Documents/Diabetic Retinopathy/unprocessable_images"

for root, dirs, files in os.walk("C:/Users/urani/Documents/Diabetic Retinopathy/train_images"):
    for file in files:
        if file.endswith('.png'):
            imgpath = os.path.join(root, file)
            print(imgpath)
            try:
                img = cv2.imread(imgpath)
                if img.size != 0:
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    _, th2 = cv2.threshold(grey, 8, 255, cv2.THRESH_BINARY)
                    contours, hierarchy = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    areas = [cv2.contourArea(contour) for contour in contours]
                    max_index = np.argmax(areas)
                    cnt = contours[max_index]
                    x, y, w, h = cv2.boundingRect(cnt)

                    # Ensure bounding rect should be at least 16:9 or taller
                    if w / h > 16 / 9:
                        # increase top and bottom margin
                        newHeight = w / 16 * 9
                        y = y - (newHeight - h) / 2
                        h = newHeight
                    # Crop with the largest rectangle
                    crop = img[int(y):int(y + h), int(x):int(x + w)]
                    resized_img = cv2.resize(crop, (512, 512))
                    print(imgpath)
                    cv2.imwrite(os.path.join(imgpath), resized_img)
                    cv2.waitKey(0)
                    print(str(i))
                    i = i + 1
            except:
                disformed_image_count += 1
                print("Disformed image found")
                shutil.move(imgpath,unprocessable_images)
                continue