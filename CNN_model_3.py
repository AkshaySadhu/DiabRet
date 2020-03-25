import keras


class diabetic_retinopthy_CNN_model_3():

    def model(self):
        model = keras.models.Sequential()
        model.add(keras.layers.Conv2D(32, (3,3), strides=(2,2), data_format=(None, 512, 512, 1), activation='ReLU'))

