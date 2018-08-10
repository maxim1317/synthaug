##Легенда

f1  - Increase each pixel’s R-value (redness) by 3 to 50
f2  - Multiply each image with a random value between 0.8 and 1.2
f3  - Normalize contrast by a factor of 0.6 to 1.4, sampled randomly per image
f4  - Change images to grayscale and overlay them with the original image by varying strengths, effectively removing 0 to 80% of the color
f5  - Blur each image with a gaussian kernel with a sigma of 3.0
f6  - Blur each image using a mean over neihbourhoods that have a random size between 2x2 and 11x11
f7  - Blur each image using a mean over neihbourhoods that have random sizes, which can vary between 5 and 11 in height and 1 and 3 in width
f8  - Blur each image using a median over neihbourhoods that have a random size between 3x3 and 11x11
f9  - Sharpen an image, then overlay the results with the original using an alpha between 0.0 and 1.0
f10 - Emboss an image, then overlay the results with the original using an alpha between 0.0 and 1.0
f11 - Normalize contrast by a factor of 0.7 to 1.2, sampled randomly per image and for 50% of all images also independently per channel
f12 - Add random values between -20 and 20 to images. In 50% of all images the values differ per channel (3 sampled value). In the other 50% of all images the value is the same for all channels
f13 - Add random values between -20 and 20 to images, with each value being sampled per pixel
f14 - Add random values between -20 and 20 to images, with each value being sampled per pixel
