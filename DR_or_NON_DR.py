import os
# import pickle
# import random
import shutil
import numpy as np
# import keras
import pandas as pd
# import csv

from PIL import Image


# def make_only_two_classes():
#         File1 = 'train.csv'
#         File2 = 'train_class.csv'
#
#         with open(File1, "r") as r, open(File2, "w") as w:
#             reader = csv.reader(r, lineterminator = "\n")
#             writer = csv.writer(w, lineterminator = "\n")
#             for row in reader:
#                 if(str(row[1])=='0'):
#                     line = row[0]+","+row[1]+"\n"
#                 else:
#                     line = row[0]+"," + "1"+"\n"
#                 print(row,line)
#                 w.write(line)
#
# def baseline_model(input_shape):
#     model = keras.models.Sequential()
#     model.add(keras.layers.BatchNormalization(input_shape=input_shape))
#     model.add(keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
#     model.add(keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
#     model.add(keras.layers.Dropout(0.25))
#
#     # model.add(keras.layers.BatchNormalization())
#     model.add(keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
#     model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
#     model.add(keras.layers.Dropout(0.25))
#
#     model.add(keras.layers.Flatten())
#     model.add(keras.layers.Dense(32, activation='relu'))
#     model.add(keras.layers.Dropout(0.5))
#     model.add(keras.layers.Dense(2, activation='softmax'))
#
#     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#     model.summary()
#
#
#     return model



# model = baseline_model((512,512,1))

class_dr = "C:/Users/urani/Documents/Diabetic Retinopathy/DR_images/"
class_non_dr = "C:/Users/urani/Documents/Diabetic Retinopathy/Non_DR_images/"
src = "C:/Users/urani/Documents/Diabetic Retinopathy/normalized_images/"
df = pd.read_csv('train_class.csv')
print(df)


i = 1
data = []
labels = []
for root, dirs, files in os.walk('C:/Users/urani/Documents/Diabetic Retinopathy/normalized_images'):
    for file in files:
        if file.endswith('.png'):
            s = file.split('.')[0]
            s1 = s.replace("normalized_", "")
            dfrow = df[df['id_code'] == s1].index.values.astype(int)[0]
            label = df.iloc[dfrow]['diagnosis']
            labels.append(label)
            imgpath = os.path.join(root, file)
            img = Image.open(imgpath)
            print(imgpath)
            data.append(np.array(img.getdata()).reshape((512,512,1)))
            print(len(data))
            i = i + 1
            src_img = src + s + ".png"
            if str(label) == "0":
                shutil.copy(src_img, class_non_dr)
            elif str(label) == "1":
                shutil.copy(src_img, class_dr)

# print(len(data))
#
# random.shuffle(data)
#
# for s in data:
#     print(s[1])
#
# X = []
# y = []
# for im, la in data:
#     X.append(im)
#     y.append(la)
#
# X = np.array(X).reshape(-1, 512, 512, 1)
#
# y = np.array(y)
# p_out = open("X.pickle", "wb")
# pickle.dump(X, p_out)
# p_out.close()
#
# p_out = open("y.pickle", "wb")
# pickle.dump(y, p_out)
# p_out.close()
#
# X = pickle.load(open("X.pickle", "rb"))
# y = pickle.load(open("y.pickle", "rb"))
#
# print(y)
#
# model.fit(X,y,validation_split=0.1,epochs=10)
