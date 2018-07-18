#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:00:45 2018

@author: apple
"""
import numpy as np
import cv2 as cv

def build_filters():
    filters = []
    ksize = 31      ##51,151,531
    ##theta = 11.25,22.5,33.75,45,56.25,67.5,78.75,90,101.25,112.5,123.75,135,146.25,157.5,168.75,180
    for theta in np.arange(0, np.pi, np.pi / 16):
        ##cv2.getGaborKernel(ksize, sigma, theta, lambda, gamma, psi, ktype)
        kern = cv.getGaborKernel((ksize, ksize), 5.0, theta, 10.0, 0.5, 0, ktype=cv.CV_32F)
        kern /= 1.5*kern.sum()      ##sigma=2.0,3.0,5.0,6.0     ##lambda=8-12   ##gamma=0.3-1.0     ##psi=0,10,50,90
        filters.append(kern)
    return filters
 
def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv.filter2D(img, cv.CV_8UC3, kern)
        np.maximum(accum, fimg, accum)
    return accum
 
if __name__ == '__main__':
    import sys
    
    print(__doc__)
    try:
        img_fn = sys.argv[1]
        img_fn_after = sys.argv[1]
    except:
        img_fn = '/Users/apple/Desktop/web/5after.jpg'
        img_fn_after = '/Users/apple/Desktop/web/5before.jpg'
        
    img = cv.imread(img_fn)
    img_after = cv.imread(img_fn_after)
    if img is None:
        print('Failed to load image file:', img_fn)
        sys.exit(1)
        
    if img_after is None:
        print('Failed to load image file:', img_fn_after)
        sys.exit(1)
        
    filters = build_filters()
    
    res1 = process(img, filters)
    res2 = process(img_after, filters)
    
    #cv.imshow('img', img)
    ##cv.imshow('img after',img_after)
    cv.imshow('result', res1)
    cv.imshow('result after',res2)
    
    cv.waitKey(0)
    cv.destroyAllWindows()