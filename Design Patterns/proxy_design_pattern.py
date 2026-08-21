import time
class HighResImage:
    def __init__(self,filename):
        self.__filename=filename
        self.__image_data=None
        self.load_from_disk()

    def load_from_disk(self):
        time.sleep(1)
        self.__image_data=f"This isimage data of {self.__filename}"
        print(f"image data loaded for {self.__filename}")
    def display(self):
        print(f"{self.__filename} image data is {self.__image_data}")

class ProxyImage:
    def __init__(self,file_name) -> None:
        self.file_name=file_name
        self.real_image=None

    def display(self):
        if self.real_image is None:
            self.real_image=HighResImage(self.file_name)
        self.real_image.display()

class PhotoGallery:
    def __init__(self) -> None:
        self.images:list[ProxyImage]=[]
    def add_image(self,file_name:str):
        img=ProxyImage(file_name=file_name)
        self.images.append(img)
        # print("image has been added to gallery")
    def display_gallery(self):
        for x in self.images:
            x.display()

    def show_image(self,ind:int):
        print("here is the show imag function called")
        if ind<len(self.images):
            self.images[ind].display()
        else:
            print("image does not exists")

photogallery=PhotoGallery()
photogallery.add_image("image one")
photogallery.add_image("image two")
photogallery.add_image("image three")
photogallery.add_image("image four")
photogallery.add_image("image five")
photogallery.add_image("image six")    
# photogallery.display_gallery()

photogallery.show_image(2)
print("=============")
photogallery.show_image(2)
print("=============")
photogallery.show_image(2)
print("=============")
photogallery.show_image(2)
print("=============")
photogallery.show_image(2)