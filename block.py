from direct.showbase.ShowBase import ShowBase
from panda3d.core import Texture
from panda3d.core import TransparencyAttrib
 
# класс элемента строительного блока
class Block():
    # конструктор блока.
    # аргументы:
    #   position - позиция блока на сцене
    #   color - цвет заливки
    def __init__(self, position=(0, 0, 0), color=(1, 1, 1, 1)):
        # загружаем модель блока
        self.block = loader.loadModel('block.egg')
        # загружаем текстуру к ней
        tex = loader.loadTexture('block.png')
        # устанавливаем текстуру на модель
        self.block.setTexture(tex)
        # Устанавливаем учёт прозрачности цвета
        self.block.setTransparency(TransparencyAttrib.MAlpha)
        # перемещение модели в рендер, смена родителя
        self.block.reparentTo(render)
        self.block.setPos(position)
        self.block.setColor(color)
if __name__ == "__main__":
    class Game(ShowBase):
        def __init__(self):
            ShowBase.__init__(self)
    
            b1 = Block((0,10,0), (0.5,1,0,1))
            b2 = Block((1,10,0), (1,0,0.5,1))
            b3 = Block((0,10,2), (0,0.5,1,1))
            b4 = Block((-2,15,-2), (1,0.5,1,1))
    
    game = Game()
    game.run()
