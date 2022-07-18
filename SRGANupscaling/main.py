from pyexpat import model
import numpy as np
from SRGANupscaling.model import image_upscale, image_upscale_model
from PIL import Image

def find_split_size(img_height, img_width):
    '''
    Determines the ideal shape and size for spliting images of input size
    '''
    height_options = [i for i in range(32,img_height+1) if img_height%i== 0]
    width_options = [i for i in range(32,img_width+1) if img_width%i== 0]
    tile_height = height_options[-1]
    tile_width = width_options[-1]
    n_rows=img_height // tile_height
    n_cols=img_width // tile_width
    return n_rows, n_cols, tile_height, tile_width

def image_split(image: np.ndarray, kernel_size: tuple, kernel_shape: tuple):
    '''
    Split image into batches of size = kernel_size
    Output is np array of shape (Batch size, height, width, rgb channels)
    '''
    img_height, img_width, channels = image.shape
    tile_height, tile_width = kernel_size
    rows, cols = kernel_shape

    tiled_array = image.reshape(rows,tile_height,
                                cols,tile_width,
                                channels)
    tiled_array = tiled_array.swapaxes(1, 2)
    return tiled_array.reshape(-1,tile_height,tile_width, channels)

def image_merge(n_rows, n_cols, tiles_upscale):
    '''
    Merge tiles of shape n_rows * n_cols into a final complete image
    '''
    image_block=[]
    index=0
    for i in range(n_rows):
        image_cols=[]
        for j in range(n_cols):
            image_cols.append(tiles_upscale[index])
            index+=1
        image_block.append(np.concatenate(image_cols,axis=1))
    image_final = np.concatenate(image_block, axis=0)
    return np.array(image_final)

def super_resolution(image_uploaded):
    '''
    Final function to call to super resolution image
    '''
    # image = cv2.imread(image_uploaded)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image=np.array(image_uploaded)
    img_height, img_width, channels = image.shape
    n_rows, n_cols, tile_height, tile_width = find_split_size(img_height, img_width)
    tiles = image_split(image, (tile_height, tile_width), (n_rows,n_cols))
    tiles_upscale = np.asarray(image_upscale(tiles))
    sr_image=image_merge(n_rows, n_cols, tiles_upscale)
    final=Image.fromarray(sr_image)
    return final


def super_resolution_model(image_uploaded, model):
    '''
    Final function to call to super resolution image with model as arguments
    '''
    image=np.array(image_uploaded)
    img_height, img_width, channels = image.shape
    n_rows, n_cols, tile_height, tile_width = find_split_size(img_height, img_width)
    tiles = image_split(image, (tile_height, tile_width), (n_rows,n_cols))
    tiles_upscale = np.asarray(image_upscale_model(tiles, model))
    sr_image=image_merge(n_rows, n_cols, tiles_upscale)
    final=Image.fromarray(sr_image)
    return final


if __name__ == '__main__':
    pass
