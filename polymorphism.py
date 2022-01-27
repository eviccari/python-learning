from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TexBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw_components(controls):
    for control in controls:
        control.draw()  

ddl = DropDownList()
tb = TextBox()

print(isinstance(ddl, UIControl))
print(isinstance(tb, UIControl))
draw_components([tb, ddl])
