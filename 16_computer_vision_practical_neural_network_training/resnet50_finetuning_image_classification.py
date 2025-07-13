from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.optimizers import Adam

def load_train(path, subset='training'):
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.25)
    data_flow = datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=32,
        class_mode='sparse',
        subset=subset,
        shuffle=(subset=='training'),
        seed=12345
    )
    return data_flow

def create_model(input_shape):
    base_model = ResNet50(weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                      include_top=False, input_shape=input_shape)
    base_model.trainable = True  # Полностью разморожен!
    model = Sequential()
    model.add(base_model)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(12, activation='softmax'))
    model.compile(
        optimizer=Adam(learning_rate=1e-5),  # Для полного fine-tune лучше маленький lr
        loss='sparse_categorical_crossentropy',
        metrics=['acc']
    )
    return model

def train_model(model, train_data, test_data, batch_size=None, epochs=2,
                steps_per_epoch=None, validation_steps=None):
    if steps_per_epoch is None:
        steps_per_epoch = train_data.samples // train_data.batch_size
    if validation_steps is None:
        validation_steps = test_data.samples // test_data.batch_size
    model.fit(
        train_data,
        validation_data=test_data,
        batch_size=batch_size,
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2
    )
    return model
