import shutil
import os
import pandas as pd
data_frame = pd.read_csv('train.csv')
class_0_images = "C:/Users/urani/Documents/Diabetic Retinopathy/Class 0"
class_1_images = "C:/Users/urani/Documents/Diabetic Retinopathy/Class 1"
class_2_images = "C:/Users/urani/Documents/Diabetic Retinopathy/Class 2"
class_3_images = "C:/Users/urani/Documents/Diabetic Retinopathy/Class 3"
class_4_images = "C:/Users/urani/Documents/Diabetic Retinopathy/Class 4"
image_count = 0
for root, dirs, files in os.walk("C:/Users/urani/Documents/Diabetic Retinopathy/train_images"):
    for file in files:
        if file.endswith('.png'):
            image_path = os.path.join(root, file)
            file_name = file.split('.')[0]
            data_frame_row = data_frame[data_frame['id_code'] == file_name].index.values.astype(int)[0]
            label  = data_frame.iloc[data_frame_row]['diagnosis']
            if str(label) == "0":
                print("Image: " + str(image_path) + "copied into class 0")
                shutil.copy(image_path,class_0_images)
            elif str(label) == "1":
                print("Image: " + str(image_path) + "copied into class 1")
                shutil.copy(image_path,class_1_images)
            elif str(label) == "2":
                print("Image: " + str(image_path) + "copied into class 2")
                shutil.copy(image_path,class_2_images)
            elif str(label) == "3":
                print("Image: " + str(image_path) + "copied into class 3")
                shutil.copy(image_path,class_3_images)
            elif str(label) == "4":
                print("Image: " + str(image_path) + "copied into class 4")
                shutil.copy(image_path,class_4_images)
            image_count += 1
            print(image_count)
