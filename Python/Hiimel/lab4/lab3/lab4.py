import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def shuffle_and_reconstruct(input_image_path):
    image = mpimg.imread(input_image_path)
    height, width, _ = image.shape

    sub_width = width // 3
    sub_height = height // 3

    sub_images = []
    indices = []  # Keep track of original indices

    for i in range(3):
        for j in range(3):
            left = j * sub_width
            upper = i * sub_height
            right = (j + 1) * sub_width
            lower = (i + 1) * sub_height

            sub_image = image[upper:lower, left:right, :]
            sub_images.append(sub_image)
            indices.append((i, j)) 
    
    shuffled_indices = list(range(9))
    random.shuffle(shuffled_indices)  

    new_image = np.zeros_like(image)

    for i, shuffled_index in enumerate(shuffled_indices):
        original_index = indices[shuffled_index]
        print(original_index)
        row, col = original_index

        left = col * sub_width
        upper = row * sub_height
        new_image[upper:upper + sub_height, left:left + sub_width, :] = sub_images[i]

    plt.imshow(new_image)
    plt.axis('off')  
    plt.show()

# Example usage
input_image_path = "lab3/OIP.jpg"
shuffle_and_reconstruct(input_image_path)
