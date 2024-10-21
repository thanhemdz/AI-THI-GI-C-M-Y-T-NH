import os
from PIL import Image

def load_image(path):
    # Doc anh tu duong dan
    # Args: path
    try:
        img = Image.open(path)
        return img
    except Exception as e:
        print("loi khi doc anh", path," ",e)
        return None
def is_img (path):
    exs = (".jpg",".jpeg",".png")
    return path.lower().endswith(exs)

def getlist(fpath):
    imgList = []
    if os.path.exists(fpath) and os.path.isdir(fpath):
        filenames = os.listdir(fpath)
        for file in filenames:
            file_path = os.path.join(fpath,file)
            if os.path.isfile(file_path) and is_img(file_path):
                img = load_image(file_path)
                imgList.append(img)
    return imgList


    
            
    
    