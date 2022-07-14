# GCP bucket name
BUCKET_NAME = 'srgan-wagon-project'

# Location variables for srgan-wagon-project/datasets/kaggle100-original
STORAGE_LOCATION_KAGGLE_ORG_LR = 'datasets/kaggle100-original/LR'
STORAGE_LOCATION_KAGGLE_ORG_HR = 'datasets/kaggle100-original/HR'

# Location variables for srgan-wagon-project/datasets/kaggle100
STORAGE_LOCATION_KAGGLE_LR = 'datasets/kaggle100/lr_images'
STORAGE_LOCATION_KAGGLE_HR = 'datasets/kaggle100/hr_images'

# Location variables for srgan-wagon-project/datasets/flickr25000
STORAGE_LOCATION_FLICKR_LR = 'datasets/flickr25000/lr_images'
STORAGE_LOCATION_FLICKR_HR = 'datasets/flickr25000/hr_images'

# Model url on tensorflow hub
MODEL_TFHUB = "https://tfhub.dev/captain-pool/esrgan-tf2/1"

# No. of blocks for encoder-decoder
NUMBER_BLOCKS=2

# Encoder url on tensorflow hub
ENCODE_TFHUB = f"https://tfhub.dev/emilutz/vgg19-block{NUMBER_BLOCKS}-conv2-unpooling-encoder/1"

# Decoder url on tensorflow hub
DECODE_TFHUB = f"https://tfhub.dev/emilutz/vgg19-block{NUMBER_BLOCKS}-conv2-unpooling-decoder/1"
