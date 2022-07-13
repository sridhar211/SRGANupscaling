import tensorflow as tf
import tensorflow_hub as hub
import os
import cv2
import numpy as np
from SRGANupscaling.params import MODEL_TFHUB

def image_upscale(lr_images):
    '''
    Upscales lr_images by 4x resolution and returns SR images
    Takes input of shape (Batch size, height, width, rgb channels)
    '''
    model = hub.load(MODEL_TFHUB)
    temp=tf.cast(lr_images, tf.float32)
    sr_images=model(temp)
    sr_images = np.asarray(sr_images)
    #sr_image = tf.clip_by_value(sr_image, 0, 255)
    sr_images = tf.cast(sr_images, tf.uint8)
    return sr_images
