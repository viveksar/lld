from typing import List
from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(FileSystemComponent):
    def __init__(self,filename) -> None:
        self.name=filename
    def show_details(self):
        print("this is the file details of :",self.name)

class Folder(FileSystemComponent):
    def __init__(self,name) -> None:
        self.name=name
        self.components:List[FileSystemComponent]=[]
    def add_component(self,comp:FileSystemComponent):
        self.components.append(comp)

    def show_details(self):
        print("Folder name: ",self.name)
        for x in self.components:
            x.show_details()

file1=File("file one")
file2=File("file two")
file3=File("file three")
folderone=Folder("folder one")
folderone.add_component(file1)
folderone.add_component(file2)
folderone.add_component(file3)

file4=File("four file")
foldertwo=Folder("folder tow")
foldertwo.add_component(file4)

parentFolder=Folder("parentFolder")
parentFolder.add_component(folderone)
parentFolder.add_component(foldertwo)

parentFolder.show_details()