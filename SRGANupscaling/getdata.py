from google.cloud import storage
import pandas as pd
from sklearn import linear_model
import numpy as np
import joblib
import cv2
from google.cloud import storage #, vision
# from wand.image import Image

BUCKET_NAME = 'srgan-wagon-project'
BUCKET_TRAIN_DATA_PATH = 'datasets/kaggle100-original'
MODEL_NAME = 'SRGANupscaling'
MODEL_VERSION = 'v1'

storage_client = storage.Client()
# vision_client = vision.ImageAnnotatorClient()

def download_blob(bucket_name=BUCKET_NAME, prefix='datasets/kaggle100-original/HR/', delimiter='/', source_blob_name="datasets/kaggle100-original/HR/0.png", destination_file_name="/Users/melissasiddle/code/sridhar211/SRGANupscaling/raw_data/file.png"):
    """Downloads a blob from the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)

    # print("Blobs:")
    # for blob in blobs:
    #     print(blob.name)

    lr_list = []
    for blob in blobs:
        lr_list.append(blob.name)



# def get_data():
#     """method to get the data (or a portion of it) from google cloud bucket"""

#     # file_name = file_data["name"]
#     # bucket_name = file_data["bucket"]

#     blob = storage_client.bucket(BUCKET_NAME).get_blob('/datasets/')
#     print(blob)
#     # blob_uri = f"gs://{bucket_name}/{file_name}"
#     # blob_source = vision.Image(source=vision.ImageSource(image_uri=blob_uri))
#     # current_blob.download_to_filename(temp_local_filename)

#     return


def preprocess(df):
    """method that pre-process the data"""
    df["distance"] = compute_distance(df)
    X_train = df[["distance"]]
    y_train = df["fare_amount"]
    return X_train, y_train


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
