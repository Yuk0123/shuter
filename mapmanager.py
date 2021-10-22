from direct.showbase.ShowBase import ShowBase
from panda3d.core import LPoint3f
from block import Block


# Класс менеджера карты
class MapManager():
    # Конструктор
    def __init__(self):
        # Список с блоками
        self.blocks = list()

    # Метод добавления нового блока цвета color в позицию position
    def addBlock(self, position, color):
        # Создаём блок
        block = Block(position, color)
        # Добавляем его в список
        self.blocks.append(block)

    # Метод создания карты, аргументы
    # colors - словарь цветов,
    #   ключ - символ цвета,
    #   значение - цвет
    # matrix - трёхмерный вложенный список цветов
    #   значения - символы цвета
    # shift - сдвиг координат для всех блоков
    def createMap(self, colors, matrix, shift):
        # удаляем все блоки
        self.clearAll()

        # проходимся по всем координатам
        for z in range(len(matrix)):
            for y in range(len(matrix[z])):
                for x in range(len(matrix[z][y])):
                    # Получаем цвет блока
                    key = matrix[z][y][x]
                    # если такой цвет есть в словаре цветов
                    if key in colors and colors[key]:
                        # Рассчитываем позицию
                        # Координата Y инвертируется !!!
                        pos = (x + shift[0],
                            - y - shift[1],
                            z + shift[2])
                        self.addBlock(pos, colors[key])

    # Метод очистки карты - удаления всех блоков
    def clearAll(self):
        for i in range(len(self.blocks)):
            self.blocks[i].remove()
            del self.blocks[i]

    def saveMap(self, filename):
        if not self.blocks:
            return 

        file = open(filename, 'wb')
        pickle.dump(len(self.blocks), file)
        
        for block in self.blocks:
            pickle.dump(block.getPos(), file)
            pickle.dump(block.getColor(), file)

        file.close()
        print("Successfully saved map to file ", filename)

    def loadMap(self, filename):
        self.clearAll()

        file = open(filename, 'rb')

        
        length = pickle.load(file)

        for i in range(length):
            pos = pickel.load(file)
            color = pickle.load(file)

            self.addBlock(pos, color)
        
        file.close()
        print("Successfully loaded map from file ", filename)

if __name__ == '__main__':
    # отладка модуля
    from direct.showbase.ShowBase import ShowBase
    from controller import Controller
 
    class MyApp(ShowBase):
 
        def __init__(self):
            ShowBase.__init__(self)
 
            self.controller = Controller()
 
            self.map_manager = MapManager()
 
            # self.accept('f1', self.map_manager.basicMap)
            # self.accept('f2', self.map_manager.generateRandomMap)
            self.accept('f3', self.map_manager.saveMap, ["testmap.dat"])
            self.accept('f4', self.map_manager.loadMap, ["testmap.dat"])
            self.accept('f5', self.createMap)
 
            print("'f1' - создать базовую карту")
            print("'f2' - создать случайную карту")
            print("'f3' - сохранить карту")
            print("'f4' - загрузить карту")
            print("'f5' - создать карту по вложенному списку")
 
            # self.map_manager.generateRandomMap()
 
        def createMap(self):
            # словарь цветовых обозначений блоков
            colors = {'R':(1.0, 0, 0, 1),
                      'G':(0, 1.0, 0, 0.5),
                      'B':(0, 0, 1.0, 0.5),
                      'Y':(1.0, 1.0, 0, 1),
                      'O':(1.0, 0.5, 0.0, 1),
                      'W':(1.0, 1.0, 1.0, 1),
                      '-':None}
 
            # вложенный список блоков
            blocks = [
                [['G','O','O','O','G'],
                 ['O','-','-','-','O'],
                 ['O','-','W','-','O'],
                 ['O','-','-','-','O'],
                 ['G','O','O','O','G']],
 
                [['G','-','-','-','G'],
                 ['-','-','-','-','-'],
                 ['-','-','W','-','-'],
                 ['-','-','-','-','-'],
                 ['G','-','-','-','G']],
 
                [['G','-','R','-','G'],
                 ['-','-','R','-','-'],
                 ['R','R','W','R','R'],
                 ['-','-','R','-','-'],
                 ['G','-','R','-','G']],
 
                [['G','-','-','-','G'],
                 ['-','-','-','-','-'],
                 ['-','-','W','-','-'],
                 ['-','-','-','-','-'],
                 ['G','-','-','-','G']],
 
                [['G','Y','Y','Y','G'],
                 ['Y','-','-','-','Y'],
                 ['Y','-','W','-','Y'],
                 ['Y','-','-','-','Y'],
                 ['G','Y','Y','Y','G']],
                ]
 
            self.map_manager.createMap(colors, blocks, (-2,-10,-2))
 
 
    app = MyApp()
    app.run()
