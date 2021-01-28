# Создайте менеджер контекста для безопасной обработки элементов словаря. В случае возникновения исключения словарь
# должен оставаться без изменений. Иначе (при успешной работе) он сохранял бы все изменения.

class ProtectDict:
    def __init__(self, save_dict: dict):
        self.__save_dict = save_dict

    def __enter__(self):
        self.temp = self.__save_dict.copy()
        return self.temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type, exc_val)
        else:
            self.__save_dict.update(self.temp)


test1 = {char: index for index, char in enumerate(ProtectDict.__name__)}
test2 = {char: index for index, char in enumerate(ProtectDict.__name__)}
print(test1)
print(test2)

try:
    with ProtectDict(test1) as temp:
        for key, value in test2.items():
            temp[key] += value
except Exception:
    print("Ошибка", test1)
    raise Exception
print("решил")
print(test1)
