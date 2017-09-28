from PIL import Image
from skimage.feature import local_binary_pattern
import scipy
import time
import os
import sys

def convert_to_object(image_location):
	return Image.open(image_location, 'r')

def color_to_greyscale(img):
	return img.convert('L')

def lbp_values(img):
	return local_binary_pattern(img,8,1,method='uniform')

def pixel_values(img):
	return list(img.getdata())

def convert_to_2d_array(img):
	arr1 = pixel_values(img)
	width,height = img.size
	arr2 = []
	for i in range(height):
		arr = []
		for j in range(width):
			arr.append(arr1[i*width+j])
		arr2.append(arr)
	return arr2

def lbp_s_fun(a,b):
	if a>=b:
		return 1
	else:
		return 0

def calculate_lbp(matrix,i,j):
	center = matrix[i][j]
	ans = lbp_s_fun(matrix[i-1][j-1],center) + lbp_s_fun(matrix[i-1][j],center)*2 
	ans += lbp_s_fun(matrix[i-1][j+1],center)*4 + lbp_s_fun(matrix[i][j+1],center)*8
	ans += lbp_s_fun(matrix[i+1][j+1],center)*16 + lbp_s_fun(matrix[i+1][j],center)*32
	ans += lbp_s_fun(matrix[i+1][j-1],center)*64 + lbp_s_fun(matrix[i][j-1],center)*128
	return ans

def histogram(img):
	img = convert_to_object(img)
	img = color_to_greyscale(img)
	matrix = convert_to_2d_array(img)
	height = len(matrix)
	width = len(matrix[0])
	lbp_of_image = []
	for k in range(256):
		lbp_of_image.append(0)
	for i in range(1,height-1):
		for j in range(1,width-1):
			lbp_of_image[calculate_lbp(matrix,i,j)] += 1
	
	return lbp_of_image