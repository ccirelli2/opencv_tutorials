import cv2
import os
from matplotlib import pyplot as plt


# Image Addition ------------------------------------------
'''cv2.add():   Add two images or use numpy operation img1 + img2
                Note:  both images should be of the same depth and type.
                What does this mean depth and type?
'''

# Load Images
os.chdir('/home/ccirelli2/Desktop/repositories/OpenCV_tutorial/data')
img1 = cv2.imread('cyber_image.jpg', 0)
img2 = cv2.imread('punisher.jpg', 0)

# Get Dimensions of the Images -----------------------------
def get_img_shape(img, image_name):
    print('Image Name = {}'.format(image_name))
    print('Shape = {}'.format(img.shape))
    print('Size  = {}'.format(img.size))
    print('D-type= {}'.format(img.dtype))
    cv2.waitKey(0)


# Resize Image --------------------------------------------
'Lets resize the punisher image since its bigger'

def image_resize(img1, img2, show_img = None):
    '''img1     = image whose dimensions we want to use
        img2    = image that we want to reshape'''
        
    # Target Image Dimensions
    img1_dim    = img1.shape

    # Resize Image
    img_new = cv2.resize(img2, (img1_dim[0], img1_dim[1]))
    
    if show_img is True:
        print('Image 1 Shape    = {}'.format(img1_dim))
        
        # Image we want to reshape
        print('Image 2 Shape    = {}'.format(img2.shape))
        
        # New Image Dimensions
        print('New Image dimensions = {}'.format(img_new.shape))
        
        # Show Image
        cv2.imshow('New Image', img_new)
        cv2.waitKey(0)

    # Return the Resized Image
    return img_new



# Add Images ------------------------------------------------

def add_images(img1, img2):
    'img1 = image, no change; img2 = image that has been resized'
    img_combined = cv2.add(img1, img2)
    cv2.imshow('New Image', img_combined)
    cv2.waitKey(0)


# Image Blending -------------------------------------------

def image_blend(img1, w1, img2, w2):
    ''' syntax:  (img, weight, img, weight, gamma)
        weights:    Do they change the intensity or affect the pixels in another way?
    '''
    dst = cv2.addWeighted(img1, w1, img2, w2, 0)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




















