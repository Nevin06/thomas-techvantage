#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 18:09:05 2018

@author: apple
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import compare_ssim as ssim #structural_similarity

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    
    # show the images
    plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
before = cv2.imread("/Users/apple/Desktop/web/5after.jpg")
after = cv2.imread("/Users/apple/Desktop/web/5before.jpg")
 
# convert the images to grayscale
before = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
after = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Before",before), ("After", after)
 
# loop over the images
for (i, (name, image)) in enumerate(images):
    # show the image
    ax = fig.add_subplot(1, 3, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap = plt.cm.gray)
    plt.axis("off")
    
# show the figure
plt.show()

# compare the images
compare_images(before, before, "Before Accident vs. Before Accident")
compare_images(after, after, "After Accident vs. After Accident")
compare_images(before, after, "Before Accident vs. After Accident")
