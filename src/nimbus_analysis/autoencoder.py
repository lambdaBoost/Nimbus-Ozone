import tensorflow as tf
from tensorflow.keras import layers, losses
from tensorflow.keras.models import Model
import keras



@keras.saving.register_keras_serializable()
class global_conv_autoencoder(keras.Model):
    def __init__(self, **kwargs):
        super(global_conv_autoencoder, self).__init__(**kwargs)
        self.encoder = tf.keras.Sequential([
        layers.Input(shape=(180, 288, 1)),
        layers.Conv2D(32, (5, 5), activation='relu', padding='same', strides=2),
        layers.Conv2D(16, (3, 3), activation='relu', padding='same', strides=2),
        layers.Conv2D(8, (3, 3), activation='relu', padding='same', strides=1)])

        self.decoder = tf.keras.Sequential([
            layers.Conv2DTranspose(8, kernel_size=3, strides=1, activation='relu', padding='same'),
            layers.Conv2DTranspose(16, kernel_size=3, strides=2, activation='relu', padding='same'),
            layers.Conv2DTranspose(32, kernel_size=5, strides=2, activation='relu', padding='same'),
            layers.Conv2D(1, kernel_size=(3, 3), activation='sigmoid', padding='same')])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

    def get_config(self):
        base_config = super().get_config()
        config = {'name': 'global_conv_autoencoder'}
        
        return {**base_config, **config}
    
    

@keras.saving.register_keras_serializable()
class regional_deep_conv_autoencoder(keras.Model):
    def __init__(self, **kwargs):
        super(regional_deep_conv_autoencoder, self).__init__(**kwargs)
        self.encoder = tf.keras.Sequential([
            layers.Input(shape=(40, 40, 1)),
            layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2), padding='same'),
            layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2), padding='same'),
            layers.Conv2D(8, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2), padding='same')])


        self.decoder = tf.keras.Sequential([
            layers.Conv2D(8, (3, 3), activation='relu', padding='same'),
            layers.UpSampling2D((2, 2)),
            layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
            layers.UpSampling2D((2, 2)),
            layers.Conv2D(32, (5, 5), activation='relu', padding='same'),
            layers.UpSampling2D((2, 2)),
            layers.Conv2D(1, kernel_size=(3, 3), activation='sigmoid', padding='same')])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

    def get_config(self):
        base_config = super().get_config()
        config = {'name': 'regional_deep_conv_autoencoder'}
        
        return {**base_config, **config}
    
