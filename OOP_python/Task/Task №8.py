"""Задание 8"""


#  Создайте дочерний класс Motherboard (материнская плата), которая наследуется от классов: CPU (процессор),
#  GPU (графич. сопроцессор), Memory (память). В свою очередь CPU наследуется от классов: AMD и Intel,
#  GPU от классов NVidia, GeForce.

#  Создайте экземпляр класса Motherboard и наполните ее конкретным содержимым (локальным свойствам этого объекта
#  присвойте определенные значения). Определите вспомогательные методы в базовых классах и выведите итоговую информацию
#  в консоль с помощью метода showInfo() класса Motherboard.

import Task_8_modul as tm


class Motherboard(tm.CPU, tm.GPU, tm.Memory):

    def __init__(self, model, chipset, socket, type_memory, video_slot):
        self.motherboard_list = []
        self.add(model, chipset, socket, type_memory, video_slot)
        self.current_mb = 0
        self.__navigation_dict = {'1': self.choiceMatherboard,
                                  '2': self.showInfo,
                                  '3': self.showSupportCPU,
                                  '4': self.showSupportGPU,
                                  '5': self.showSupportMemory,
                                  '6': self.showExit}
        super().__init__()

    def add(self, model, chipset, socket, type_memory, video_slot):
        """Добавление материнской платы"""
        specifications = {'model': model,
                          'chipset': chipset,
                          'socket': socket,
                          'type memory': type_memory,
                          'video slot': video_slot}

        self.motherboard_list.append(specifications)

    @property
    def __getParameters(self):
        """Возвращает параметры материнской платы"""
        return self.specifications

    def showMatherboards(self):
        """Выводит список материнских плат"""
        for index, value in enumerate(self.motherboard_list, 1):
            print(index, *value.values())

    def showInfo(self):
        """Выводит на экран параметры материнской платы"""
        for index, (key, value) in enumerate(self.motherboard_list[self.current_mb].items(), 1):
            print(f'{index}. {key.capitalize().ljust(11)}: {value}')

    def showSupportCPU(self):
        """Выводит информацию о поддерживаемых процессорах материнской платой"""
        print(f'Материнская плата {self.motherboard_list[self.current_mb]["model"]} поддерживает следующие процессоры')
        for index, value in enumerate(self.getBaseCPU, 1):
            if value['socket'] == self.motherboard_list[self.current_mb]['socket']:
                print(index, *value.values())

    def showSupportGPU(self):
        """Выводит информацию о поддерживаемых видео картах материнской платой"""
        print(f'Материнская плата {self.motherboard_list[self.current_mb]["model"]} поддерживает следующие видеокарты')
        for index, value in enumerate(self.getBaseGPU, 1):
            print(index, *value.values())

    def showSupportMemory(self):
        """Выводит информацию о поддерживаемых модулях памяти материнской платой"""
        print(
            f'Материнская плата {self.motherboard_list[self.current_mb]["model"]} поддерживает следующие модули памяти')
        for index, value in enumerate(self.getBaseMemory, 1):
            if value['type memory'] == self.motherboard_list[self.current_mb]['type memory']:
                print(index, *value.values())

    def choiceMatherboard(self):
        """Выбор материнской платы"""
        temp = [str(i) for i in range(1, len(self.motherboard_list) + 1)]
        while True:
            self.showMatherboards()
            answer = input(f'Выберите нужный пункт меню: {temp} ')
            print(answer)
            if answer in temp:
                print('Выход')
                self.current_mb = int(answer) - 1
                break
            else:
                print('\033[31m Нужный пункт меню не распознан:\033[0m')

    def showExit(self):
        """Выход"""

    def menu(self):
        print('\033[34m')
        for key, i in self.__navigation_dict.items():
            print(key, i.__doc__)
        print('\033[0m')

    def inputControl(self):
        temp = [str(i) for i in range(1, len(self.__navigation_dict) + 1)]
        while True:
            self.menu()
            answer = input(f'Выберите нужный пункт меню: {temp} ')
            if answer in temp[:-1]:
                self.__navigation_dict[answer]()
            elif answer == temp[-1]:
                print('Спасибо что воспользовались программой. Всего доброго')
                break
            else:
                print('\033[31m Нужный пункт меню не распознан:\033[0m')


base_mb = Motherboard('ASRock A320M-DVS R4.0', 'AMD A320', 'AM4', 'DDR 4', 'PCI Express 3.0')
base_mb.add('ASUS A68HM-K', 'AMD A68H', 'FM2+', 'DDR 3', 'PCI Express 3.0')
base_mb.inputControl()
