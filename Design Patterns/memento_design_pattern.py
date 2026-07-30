class EditorMemento():
    def __init__(self,text) -> None:
        self.__text=text
    def get_saved_text(self):
        return self.__text

class Editor():
    def __init__(self) -> None:
        self.__text=""
    def addText(self,text):
        self.__text+=text
    def displayText(self):
        print("Text in Editor:=>",self.__text)
        return self.__text
    def save(self)->EditorMemento:
        return EditorMemento(self.__text)
    def restore(self,text:EditorMemento):
        self.__text=text.get_saved_text()

class CareTaker():
    def __init__(self) -> None:
        self.history=[]
    def add_to_history(self,memento:EditorMemento):
        self.history.append(memento)
    def undo(self):
        if len(self.history)==0:
            return EditorMemento("")
        data=self.history.pop()
        if len(self.history)>0:
            return self.history[-1]
        return EditorMemento("")
    def show_history(self):
        for i in range(0,len(self.history)):
            print(f"{i},{self.history[i].get_saved_text()}")

text_editor=Editor()
history=CareTaker()
text_editor.addText("hello")
text_editor.addText(" world")
text_editor.addText(" !!!")

text=text_editor.displayText()
print("here is the returned text==>",text)

saved_data=text_editor.save()
history.add_to_history(saved_data)


text_editor.addText("good")
text_editor.addText(" bye")
text_editor.addText(" !!!")
history.add_to_history(text_editor.save())
text=text_editor.displayText()
print("current text is:",text)
history.show_history()

# last_state=history.undo().get_saved_text()
# print("last state one==>",last_state)
# print("here is the last state==>",history.undo().get_saved_text()) 
text_editor.restore(history.undo())
history.show_history()
text=text_editor.displayText()
print("the current text is :",text)
text_editor.restore(history.undo())
text_editor.displayText()