import tensorflow as tf

IMG_SHAPE = (512, 512, 3)
VGG16_MODEL=tf.keras.applications.VGG16(input_shape=IMG_SHAPE,include_top=False,weights=None)
VGG16_MODEL.trainable=True
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(5,activation='softmax')
model = tf.keras.Sequential([VGG16_MODEL,global_average_layer,prediction_layer])
model.compile(optimizer=tf.train.AdamOptimizer(),loss=tf.keras.losses.sparse_categorical_crossentropy,metrics=["accuracy"])
model.summary()