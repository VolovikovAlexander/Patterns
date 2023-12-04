import unittest
from Src.Logics.nomenclature_factory import nomenclature_factory


#
# Набор автотестов для проверки работы шаблонных методов
#
class  static_test(unittest.TestCase):

    #
    # Проверить работы создание номенклатуры
    #
    def test_create_default_nomenclature(self):
        # Действие
        item = nomenclature_factory.create_default_nomenclature(nomenclature_factory._storage)

        # Проверки
        assert item is not None
        assert len(nomenclature_factory._storage) == 3

if __name__ == '__main__':
    unittest.main()   