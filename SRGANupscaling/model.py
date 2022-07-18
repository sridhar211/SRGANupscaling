import tensorflow as tf
import tensorflow_hub as hub
import os
import cv2
import numpy as np
from SRGANupscaling.params import MODEL_TFHUB, ENCODE_TFHUB, DECODE_TFHUB, MODEL

def image_upscale(lr_images):
    '''
    Upscales lr_images by 4x resolution and returns SR images
    Takes input of shape (Batch size, height, width, rgb channels)
    '''
    model = hub.load(MODEL_TFHUB)
    temp=tf.cast(lr_images, tf.float32)
    sr_images=model(temp)
    sr_images = np.asarray(sr_images)
    sr_images = tf.clip_by_value(sr_images, 0, 255)
    sr_images = tf.cast(sr_images, tf.uint8)
    return sr_images

def image_upscale_model(lr_images,model):
    '''
    Upscales lr_images by 4x resolution and returns SR images
    Takes input of shape (Batch size, height, width, rgb channels)
    '''
    temp=tf.cast(lr_images, tf.float32)
    sr_images=model(temp)
    sr_images = np.asarray(sr_images)
    sr_images = tf.clip_by_value(sr_images, 0, 255)
    sr_images = tf.cast(sr_images, tf.uint8)
    return sr_images

def image_auto_encode(sr_images):
    '''
    Auto encodes images from SRGAN to improve quality
    '''
    encoder = hub.KerasLayer(ENCODE_TFHUB)
    decoder = hub.KerasLayer(DECODE_TFHUB)
    image_batch = tf.cast(sr_images, tf.float32)
    image_features = encoder(image_batch)
    image_decoded = decoder(image_features)
    image_out = tf.cast(image_decoded, tf.uint8)
    return image_out
