# Example homework assignment 1

from PIL import Image
import numpy as np

def to_grayscale(img):
    """Converts an RGB image to grayscale
    Args:
        img: numpy array of the input 3-channel RGB image
    Returns:
        numpy output array of single channel grayscale image
    """
    gray = img.mean(axis=2)
    return gray.astype(img.dtype)

def split_channels(img):
    """Splits an RGB image into 3 grayscale channel images
    Args:
        img: numpy array of the input 3-channel RGB image
    Returns:
        List of grayscale channel images as numpy arrays
    """
    channels = [img[:,:,i] for i in range(3)]
    return channels
    
def average(img1, img2):
    """Averages two images together at the pixel level
    Args:
        img2: numpy array of the first input 3-channel RGB image
        img1: numpy array of the second input 3-channel RGB image
    Returns:
        numpy output array of the averaged pixels of the input
    """
    averaged = np.mean(np.array([img1, img2]), axis=0)
    return averaged.astype(img1.dtype)
    
def lighten(img1, img2):
    """Performs the "lighten" blend operation on two images
        Lighten operation takes the maximum value between the two images
        for each channel and pixel location
    Args:
        img2: numpy array of the first input 3-channel RGB image
        img1: numpy array of the second input 3-channel RGB image
    Returns:
        numpy output array of the lightened pixels of the input
    """
    lightened = np.max(np.array([img1, img2]), axis=0)
    return lightened.astype(img1.dtype)
    
def darken(img1, img2):
    """Performs the "darken" blend operation on two images
        Darken operation takes the minimum value between the two images
        for each channel and pixel location
    Args:
        img2: numpy array of the first input 3-channel RGB image
        img1: numpy array of the second input 3-channel RGB image
    Returns:
        numpy output array of the darkened pixels of the input
    """
    darkened = np.min(np.array([img1, img2]), axis=0)
    return darkened.astype(img1.dtype)
    
def glow(img1, img2):
    """Performs the "glow" blend operation on two images
        Glow operation applies the following formula to each pixel:
        (image1 ** 2) / (255 - image2)
    Args:
        img2: numpy array of the upper input 3-channel RGB image
        img1: numpy array of the lower input 3-channel RGB image
    Returns:
        numpy output array of the darkened pixels of the input
    """
    glowing = img1.astype(np.float32) ** 2
    glowing = glowing / (255 - img2)
    glowing = np.clip(glowing, 0, 255)
    return glowing.astype(img1.dtype)
    
def main():
    print 'Loading balloon image'
    balloon = Image.open('images/balloon.jpg')
    balloon.show()
    balloon = np.array(balloon)
    
    print 'Testing to_grayscale'
    output = to_grayscale(balloon)
    gray = Image.fromarray(output, 'L')
    gray.show()
    
    print 'Testing split_channels'
    for channel in split_channels(balloon):
        split = Image.fromarray(channel, 'L')
        split.show()
        
    print 'Loading balloon image'
    sky = Image.open('images/sky.jpg')
    sky.show()
    sky = np.array(sky)
    
    print 'Testing average'
    output = average(balloon, sky)
    averaged = Image.fromarray(output)
    averaged.show()
    
    print 'Testing lighten'
    output = lighten(balloon, sky)
    lightened = Image.fromarray(output)
    lightened.show()
    
    print 'Testing darken'
    output = darken(balloon, sky)
    darkened = Image.fromarray(output)
    darkened.show()
    
    print 'Testing glow'
    output = glow(balloon, sky)
    glowing = Image.fromarray(output)
    glowing.show()

if __name__ == "__main__":
    main()
