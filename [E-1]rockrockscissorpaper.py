from PIL import Image
import os , glob 
import matplotlib.pyplot as plt 

print("PIL 라이브러리 import 완료")


# Make a function for image resizing (pre-processing)

import os 

def resize_image(img_path):
    images = glob.glob(img_path + "/*.jpg")
    print(len(images), "image to be resized")

    #파일 마다 24x24 사이즈로 바꾸어 저장 진행 
    target_size = (28,28)
    for img in images:
        old_img = Image.open(img)
        new_img = old_img.resize(target_size,Image.ANTIALIAS)
        new_img.save(img, "JPEG")

    print("new image resized")

# 가위 이미지가 저장된 디렉토리의 아래 모든 jpg 파일을 읽어들여서 
image_dir_path = os.getenv("HOME") + "/aiffel/rock_scissor_paper/scissor"
resize_image(image_dir_path)

print("가위 바위보 resize 완료")