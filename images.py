# This script is to make the main script a little cleaner
# Not much to see here

import os

image_paths=[]

for image in os.listdir("images"):
    image_paths.append(image)

print(image_paths)

urls = ["https://i.pinimg.com/736x/7b/02/89/7b0289779b3062dcfd311f345fab90ed.jpg",
        "https://i.pinimg.com/originals/4f/e5/4b/4fe54bb36d53dcb7025a970b44db90b9.jpg",
        "https://images.crystalcomments.com/1/529645227e1744308c.jpg"]