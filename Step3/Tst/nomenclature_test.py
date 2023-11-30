from Src.Models.group_nomenclature import group_nomenclature
from Src.Models.nomenclature import nomenclature
from Src.Models.unit_nomenclature import unit_nomenclature
import unittest

#
# Набор автотестов для проверки работы моделей связанных с номенклатурой
#
class nomenclature_test(unittest.TestCase):

    # 
    # Проверить создание новой карточки номенклатуры
    #
    def test_create_nomenclature(self):
        # Подготовка
        group = group_nomenclature("test group")
        item = nomenclature("test")
        unit = unit_nomenclature("test unit")

        # Действие
        item.description = "test description"
        item.group = group
        item.unit = unit

        # Проверка
        assert item is not None

    # 
    # Проверить создание новой карточки номенклатуры с ошибкой
    #
    def test_create_nomenclature_fail_name(self):
        # Подготовка
        group = group_nomenclature("test group")
        item = nomenclature("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
        unit = unit_nomenclature("test unit")

        # Действие
        item.description = "test description"
        item.group = group
        item.unit = unit

        # Проверка
        print(item._error.error)
        assert item is not None
        assert item.is_error == True


    
if __name__ == '__main__':
    unittest.main()    