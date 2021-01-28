# 1. Измените класс Image так, чтобы в нем появился метод resize(width, height). Если новая ширина или высота меньше
# текущего значения, все цвета, оказавшиеся за пределами новых границ изображения, должны удаляться.
# Если в качестве нового значения ширины или высоты передается None, соответствующее значение ширины или высоты должно
# оставаться без изменений.

class CoordError(Exception):
    pass


class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration
        self.__num += 1
        return self.__num


class Image:
    def __init__(self, width, height, background="_"):
        self.__width = width
        self.__height = height
        self.__background = background
        self.__pixels = {}
        self.__colors = {self.__background}

    def resize(self, width=None, height=None):
        # здесь должна быть проверка на корректность введенных данных
        self.__width = width if width is not None else self.__width
        self.__height = height if height is not None else self.__height
        for (width, height) in self.__pixels.copy():
            if (width > self.width) or (height > self.height):
                self.__pixels.pop((width, height))


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __checkCoord(self, coord):
        # а что если придет список??
        if isinstance(coord, tuple) and len(coord) != 2:
            raise CoordError("Координаты точки должны быть двухмерным кортежем")

        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__height):
            print(coord, 0 <= coord[0] < self.__width, 0 <= coord[1] < self.__height, self.__width, self.__height)
            raise CoordError("Значение координат выходят за пределы изображения")

    def __getitem__(self, coord):
        self.__checkCoord(coord)
        return self.__pixels.get(coord, self.__background)

    def __setitem__(self, coord, color):
        self.__checkCoord(coord)
        if color == self.__background:
            self.__pixels.pop(coord, None)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)

    def __iter__(self):
        return ImageYIterator(self)


class ImageYIterator:
    def __init__(self, img: Image):
        self.__limit = img.height
        self.img = img
        self.__y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            print("Достигнут максимум")
            raise StopIteration
        self.__y += 1
        return ImageXIterator(img, self.__y - 1)


class ImageXIterator:
    def __init__(self, img: Image, y: int):
        self.__limit = img.width
        self.img = img
        self.__y = y
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration
        self.__x += 1
        return self.img[self.__x - 1, self.__y]


img = Image(20, 4)

print(img.width, img.height)
img[1, 1] = "*"
img[2, 1] = "*"
img[3, 1] = "*"
for row in img:
    for pixel in row:
        print(pixel, end=' ')
    print()

img.resize(4,7)

img[3, 3] = "*"

for row in img:
    for pixel in row:
        print(pixel, end=' ')
    print()

img.resize(2)

for row in img:
    for pixel in row:
        print(pixel, end=' ')
    print()