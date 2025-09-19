## the plan
import numpy as np
from PIL import Image
from scipy.signal import convolve2d
import pygame
from playsound import playsound

# Fourier Series Stuff
from scipy.fft import ifftn
from scipy.fft import fftn
import matplotlib.pyplot as plt
import time

image_path = "frames\output_0001.jpg"
image_input = Image.open(image_path).convert('L')

width = image_input.width
height = image_input.height

edge_kernel = np.array([[-1, -1, -1],
                        [-1, 8, -1],
                        [-1, -1, -1]])

num_frames = 6572

pygame.init()
screen = pygame.display.set_mode((width, height))
#surface = pygame.Surface((width, height))

# bad apple text converter,

def getfilepath(number):
    # Things are padded up until number 1000 therefore
    return str(number).zfill(4)



def ConvolutionKernel(kernel, data):
    return convolve2d(data, kernel, mode="same")

pygame.mixer.init()
my_sound = pygame.mixer.Sound('bad_apple_enhanced.wav') 
    
my_sound.play()
def main():
    for frame in range(num_frames):
        frame_start = time.time()

        image_path = "frames\output_" + getfilepath(frame+1) + ".jpg"
        image_input = Image.open(image_path).convert('L')

        width = image_input.width
        height = image_input.height

        image_data = np.reshape(image_input.getdata(), (height, width))

        # Image with the convolution kernel
        filtered_image = ConvolutionKernel(edge_kernel, image_data)

        # If i want to see the image, this is just for debugging
        #image_pil = Image.new(image_input.mode, image_input.size)
        #image_pil.putdata(filtered_image.flatten())

        # Apply the Fourier Series Here


        coeffs = fftn(filtered_image)

        Z = ifftn(coeffs)

        # Display The result
        Z_real = np.abs(Z)

        Z_rgb = np.stack([Z_real]*3, axis=-1)  # shape (200,200,3)

        # Rotate 90 degrees cause it faces another direction for some reason and swapping it back breaks the whole thing
        # couldnt tell you why
        Z_rgb = np.rot90(Z_rgb, k=1, axes=(0, 1))

        # make this out new surface
        surface = pygame.surfarray.make_surface(Z_rgb)

        # output the result
    
        screen.blit(surface, (0, 0))
        pygame.display.update()


        frame_end = time.time()

        ideal_time = 1/31.0091324201
        
        if (frame_end-frame_start < ideal_time):
            time.sleep(ideal_time-(frame_end-frame_start))

main()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()





