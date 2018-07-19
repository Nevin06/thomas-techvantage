This is used to calculate mse and ssim scores on comparing 2 images.

It’s important to note that a value of 0 for MSE indicates perfect similarity. A value greater than one implies less similarity and will continue to grow as the average difference between pixel intensities increases as well

SSIM is used to compare two windows (i.e. small sub-samples) rather than the entire image as in MSE. Doing this leads to a more robust approach that is able to account for changes in the structure of the image, rather than just the perceived change.

Unlike MSE, the SSIM value can vary between -1 and 1, where 1 indicates perfect similarity.
