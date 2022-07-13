from google.cloud import storage
import tempfile
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
# from wand.image import Image

BUCKET_NAME = 'srgan-wagon-project'
STORAGE_LOCATION_hr = 'datasets/kaggle100-original/HR'
STORAGE_LOCATION_lr = 'datasets/kaggle100-original/LR'

def get_images_gcp(prefix):

    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blobs = bucket.list_blobs(prefix)
    images = []

    for blob in blobs:
        _, temp_local_filename = tempfile.mkstemp()

        # Download file from bucket.
        blob.download_to_filename(temp_local_filename)
        img = cv2.imread(temp_local_filename)
        images.append(img)
        os.remove(temp_local_filename)

    return np.array(images)


def preprocess(df):
    """method that pre-process the data"""
    images_hr=get_images_gcp(prefix=STORAGE_LOCATION_hr)
    images_lr=get_images_gcp(prefix=STORAGE_LOCATION_lr)
    X = images_lr/ 255
    y = images_hr/ 255
    return X, y


def train_model(X_train, y_train):
    """method that trains the model"""
    rgs = linear_model.Lasso(alpha=0.1)
    rgs.fit(X_train, y_train)
    print("trained model")
    return rgs


STORAGE_LOCATION = 'models/simpletaxifare/model.joblib'


def upload_model_to_gcp():


    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(STORAGE_LOCATION)

    blob.upload_from_filename('model.joblib')


def save_model(reg):
    """method that saves the model into a .joblib file and uploads it on Google Storage /models folder
    HINTS : use joblib library and google-cloud-storage"""

    # saving the trained model to disk is mandatory to then beeing able to upload it to storage
    # Implement here
    joblib.dump(reg, 'model.joblib')
    print("saved model.joblib locally")

    # Implement here
    upload_model_to_gcp()
    print(f"uploaded model.joblib to gcp cloud storage under \n => {STORAGE_LOCATION}")


if __name__ == '__main__':
    # get training data from GCP bucket
    # df = get_data()
    download_blob()

    # # preprocess data
    # X_train, y_train = preprocess(df)

    # # train model (locally if this file was called through the run_locally command
    # # or on GCP if it was called through the gcp_submit_training, in which case
    # # this package is uploaded to GCP before being executed)
    # reg = train_model(X_train, y_train)

    # # save trained model to GCP bucket (whether the training occured locally or on GCP)
    # save_model(reg)
