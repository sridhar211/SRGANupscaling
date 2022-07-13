from google.cloud import storage
import tempfile
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from SRGANupscaling.params import BUCKET_NAME

def get_images_gcp(n, storage_location):
    '''
    Reads n images from gcp from specified storage location and returns as np array
    '''
    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blobs = bucket.list_blobs(prefix=storage_location)
    images = []

    for idx, blob in enumerate(blobs):
        if idx >= n:
            continue
        _, temp_local_filename = tempfile.mkstemp()

        # Download file from bucket.
        blob.download_to_filename(temp_local_filename)
        img = cv2.imread(temp_local_filename)
        images.append(img)
        os.remove(temp_local_filename)
    return np.array(images)

def plot_image_comparison(lr_image, sr_image, hr_image):
    '''
    Plots a side-by-side comparison of lr, sr and hr images passed in arguments
    '''
    plt.figure(figsize=(30, 18))
    plt.subplot(231)
    plt.title('LR Image')
    plt.imshow(lr_image)
    plt.subplot(232)
    plt.title('Superresolution')
    plt.imshow(sr_image)
    plt.subplot(233)
    plt.title('Orig. HR image')
    plt.imshow(hr_image)

    plt.show();
