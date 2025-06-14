import tensorflow as tf

def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ])
    model.compile("adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model
