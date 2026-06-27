import math
import numpy as np
import cv2
#import sys

# # Implement the functions below.


def extract_red(image):
    """ Returns the red channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the red channel.
    """
    red = image[:, :, 2]

    return red
    #raise NotImplementedError


def extract_green(image):
    """ Returns the green channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the green channel.
    """
    green = image[:, :, 1]

    return green
    #raise NotImplementedError


def extract_blue(image):
    """ Returns the blue channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the blue channel.
    """
    blue = image[:, :, 0]

    return blue
    #raise NotImplementedError


def swap_green_blue(image):
    """ Returns an image with the green and blue channels of the input image swapped. It is highly
    recommended to make a copy of the input image in order to avoid modifying the original array.
    You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 3D array with the green and blue channels swapped.
    """
    temp_image = np.copy(image)

    blue = image[:, :, 0].copy()
    green = image[:, :, 1].copy()

    image[:, :, 0] = green
    image[:, :, 1] = blue
    
    return image

    #raise NotImplementedError


def copy_paste_middle(src, dst, shape):
    """ Copies the middle region of size shape from src to the middle of dst. It is
    highly recommended to make a copy of the input image in order to avoid modifying the
    original array. You can do this by calling:
    temp_image = np.copy(image)

        Note: Assumes that src and dst are monochrome images, i.e. 2d arrays.

        Note: Where 'middle' is ambiguous because of any difference in the oddness
        or evenness of the size of the copied region and the image size, the function
        rounds downwards.  E.g. in copying a shape = (1,1) from a src image of size (2,2)
        into an dst image of size (3,3), the function copies the range [0:1,0:1] of
        the src into the range [1:2,1:2] of the dst.

    Args:
        src (numpy.array): 2D array where the rectangular shape will be copied from.
        dst (numpy.array): 2D array where the rectangular shape will be copied to.
        shape (tuple): Tuple containing the height (int) and width (int) of the section to be
                       copied.

    Returns:
        numpy.array: Output monochrome image (2D array)
    """

    src_img = src 
    dst_img = dst
    
    src_h, src_w = src_img.shape
    dst_h, dst_w = dst_img.shape
    
    src_h_middle = int(src_h/2)-int(shape[0]/2)
    src_w_middle = int(src_w/2)-int(shape[1]/2)
    

    dst_h_middle = int(dst_h/2)-int(shape[0]/2)
    dst_w_middle = int(dst_w/2)-int(shape[1]/2)

    
   
    
    src_clip = src_img[src_h_middle:src_h_middle+shape[0], src_w_middle:src_w_middle+shape[1]]

    dst_img[dst_h_middle:dst_h_middle+shape[0], dst_w_middle:dst_w_middle+shape[1]] = src_clip


    
    return dst_img
    
##    raise NotImplementedError



def copy_paste_middle_circle(src, dst, radius):
    """ Copies the middle circle region of radius "radius" from src to the middle of dst. It is
    highly recommended to make a copy of the input image in order to avoid modifying the
    original array. You can do this by calling:
    temp_image = np.copy(image)

        Note: Assumes that src and dst are monochrome images, i.e. 2d arrays.

    Args:
        src (numpy.array): 2D array where the circular shape will be copied from.
        dst (numpy.array): 2D array where the circular shape will be copied to.
        radius (scalar): scalar value of the radius.

    Returns:
        numpy.array: Output monochrome image (2D array)
    """

    src_cimg = src
    dst_cimg = dst

    radius = int(radius)

    
    src_ch, src_cw = src_cimg.shape
    dst_ch, dst_cw = dst_cimg.shape
    
    src_h_cmiddle = int(src_ch/2)
    src_w_cmiddle = int(src_cw/2)

    dst_h_cmiddle = int(dst_ch/2)
    dst_w_cmiddle = int(dst_cw/2)

 

    cmask = np.zeros(src_cimg.shape, dtype=np.uint8)
    cmask = cv2.circle(cmask, (src_w_cmiddle, src_h_cmiddle), radius, 255, -1)

    cresult = src_cimg & cmask

    cresult = cresult[int(src_h_cmiddle)-int(radius):int(src_h_cmiddle)+int(radius)+1,int(src_w_cmiddle)-int(radius):int(src_w_cmiddle)+int(radius)+1]

    cresult_h, cresult_w = cresult.shape


    cmask = np.zeros(dst_cimg.shape, dtype=np.uint8)
    cmask = cv2.circle(cmask, (dst_w_cmiddle, dst_h_cmiddle), radius, 255, -1)

    cmask1 = 255 - cmask


    dst_cimg = dst_cimg & cmask1

    cmask[int(dst_h_cmiddle)-int(radius):int(dst_h_cmiddle)+int(radius)+1,int(dst_w_cmiddle)-int(radius):int(dst_w_cmiddle)+int(radius)+1] = cresult
    cresult_h, cresult_w = cmask.shape


    cresult = dst_cimg | cmask

 
    return cresult
    #raise NotImplementedError


def image_stats(image):
    """ Returns the tuple (min,max,mean,stddev) of statistics for the input monochrome image.
    In order to become more familiar with Numpy, you should look for pre-defined functions
    that do these operations i.e. numpy.min.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.

    Returns:
        tuple: Four-element tuple containing:
               min (float): Input array minimum value.
               max (float): Input array maximum value.
               mean (float): Input array mean / average value.
               stddev (float): Input array standard deviation.
    """
    min_green = 0.0
    max_green = 0.0
    mean_green = 0.0
    stddev_green = 0.0

    min_green = image.min()
    max_green = image.max()
    
    # confirm pixel range is 0-255
    
    mean, std = cv2.meanStdDev(image, mask = None)

    mean_green = mean[0][0]
    stddev_green = std[0][0]
    
    #raise NotImplementedError
    return float(min_green),float(max_green),mean_green,stddev_green

 
def center_and_normalize(image, scale):
    """ Returns an image with the same mean as the original but with values scaled about the
    mean so as to have a standard deviation of "scale".

    Note: This function makes no defense against the creation
    of out-of-range pixel values.  Consider converting the input image to
    a float64 type before passing in an image.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.
        scale (int or float): scale factor.

    Returns:
        numpy.array: Output 2D image.
    """
    original_nimage = image
    n_scale = int(scale)

    original_nimage = original_nimage.astype(np.float64)

 #   n_mean, n_std = cv2.meanStdDev(original_nimage, mask = None)

    n_mean = np.mean(original_nimage)
    n_std = np.std(original_nimage)
    
    new_nimage = (((original_nimage - n_mean) / n_std) * scale) + n_mean

    final_nimage = new_nimage  #.astype(np.uint8)
  


    return final_nimage

    
    

    


    #raise NotImplementedError


def shift_image_left(image, shift):
    """ Outputs the input monochrome image shifted shift pixels to the left.

    The returned image has the same shape as the original with
    the BORDER_REPLICATE rule to fill-in missing values.  See

    http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/copyMakeBorder/copyMakeBorder.html?highlight=copy

    for further explanation.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.
        shift (int): Displacement value representing the number of pixels to shift the input image.
            This parameter may be 0 representing zero displacement.

    Returns:
        numpy.array: Output shifted 2D image.
    """
 #   timage = np.copy(image)
 #   rows,cols = timage.shape
 #   matrix = np.float64([[1,0,shift],[0,1,0]])
 #   new_img = cv2.warpAffine(timage,matrix,(cols,rows))

    shifted_img = cv2.copyMakeBorder(image[:,shift:], 0, 0, 0, shift, cv2.BORDER_REPLICATE)
   
    return shifted_img
    
    #raise NotImplementedError


def difference_image(img1, img2):
    """ Returns the difference between the two input images (img1 - img2). The resulting array must be normalized
    and scaled to fit [0, 255].

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        img1 (numpy.array): Input 2D image.
        img2 (numpy.array): Input 2D image.

    Returns:
        numpy.array: Output 2D image containing the result of subtracting img2 from img1.
    """
    sub_img1 = np.copy(img1)
    sub_img2 = np.copy(img2)

    sub_img1 = sub_img1.astype(np.float32)
    sub_img2 = sub_img2.astype(np.float32)

 #   sub_image = cv2.subtract(sub_img1,sub_img2)
    sub_image = sub_img1 - sub_img2

    sub_image = cv2.normalize(sub_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    
    return sub_image
    #raise NotImplementedError


def add_noise(image, channel, sigma):
    """ Returns a copy of the input color image with Gaussian noise added to
    channel (0-2). The Gaussian noise mean must be zero. The parameter sigma
    controls the standard deviation of the noise.

    The returned array values must not be clipped or normalized and scaled. This means that
    there could be values that are not in [0, 255].

    Note: This function makes no defense against the creation
    of out-of-range pixel values.  Consider converting the input image to
    a float64 type before passing in an image.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): input RGB (BGR in OpenCV) image.
        channel (int): Channel index value.
        sigma (float): Gaussian noise standard deviation.

    Returns:
        numpy.array: Output 3D array containing the result of adding Gaussian noise to the
            specified channel.
    """

    g_image = image
    c_image = g_image[:, :, channel]
    
    rows, cols = c_image.shape
    noisy_img = c_image + np.random.normal(0, sigma, c_image.shape)


    g_image[:,:,channel] = noisy_img
    
    return g_image
    #raise NotImplementedError


def build_hybrid_image(image1, image2, cutoff_frequency):
    """ 
    Takes two images and creates a hybrid image given a cutoff frequency.
    Args:
        image1: numpy nd-array of dim (m, n, c)
        image2: numpy nd-array of dim (m, n, c)
        cutoff_frequency: scalar
    
    Returns:
        hybrid_image: numpy nd-array of dim (m, n, c)

    Credits:
        Assignment developed based on a similar project by James Hays. 
    """

    image1 = image1.astype(np.float32)

    image2 = image2.astype(np.float32)

    filter = cv2.getGaussianKernel(ksize=cutoff_frequency*4+1,
                                   sigma=cutoff_frequency)
    filter = np.dot(filter, filter.T)
    
    low_frequencies = cv2.filter2D(image1,-1,filter)

    high_frequencies = image2 - cv2.filter2D(image2,-1,filter)

 #   low_frequencies_l = low_frequencies.astype(np.float32)

 #   high_frequencies_h = high_frequencies.astype(np.float32)

    hybrid_lh = low_frequencies + high_frequencies


    hybrid_lh = cv2.normalize(hybrid_lh, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
   
 

    hybrid = hybrid_lh.astype(np.uint8)

    
    
    return hybrid 


def vis_hybrid_image(hybrid_image):
    """ 
    Tools to visualize the hybrid image at different scale.

    Credits:
        Assignment developed based on a similar project by James Hays. 
    """


    scales = 5
    scale_factor = 0.5
    padding = 5
    original_height = hybrid_image.shape[0]
    num_colors = 1 if hybrid_image.ndim == 2 else 3

    output = np.copy(hybrid_image)
    cur_image = np.copy(hybrid_image)
    for scale in range(2, scales+1):
      # add padding
      output = np.hstack((output, np.ones((original_height, padding, num_colors),
                                          dtype=np.float32)))

      # downsample image
      cur_image = cv2.resize(cur_image, (0, 0), fx=scale_factor, fy=scale_factor)

      # pad the top to append to the output
      pad = np.ones((original_height-cur_image.shape[0], cur_image.shape[1],
                     num_colors), dtype=np.float32)
      tmp = np.vstack((pad, cur_image))
      output = np.hstack((output, tmp))

    return output
