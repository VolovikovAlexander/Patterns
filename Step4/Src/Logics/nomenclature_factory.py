from Src.Models.group_nomenclature import group_nomenclature
from Src.Models.unit_nomenclature import unit_nomenclature
from Src.Models.nomenclature import nomenclature

# 
# Класс для создания различных элемиентов номенклатуры
#
class nomenclature_factory:

    @property
    def elements(self):
        " Получить набор элементов "
        return {}

    @staticmethod
    def create_default_nomenclature():
        " Фабричный метод: Создать номенкалутуру по умолчанию"
        elements = {}
        
        # 1. Определяем группу по умолчанию
        group_key = "group_nomenclature"
        groups = elements.get[group_key]
        if groups is None:
            elements[group_key] = {}
            group =  nomenclature_factory.create_default_group()
            elements[group_key][group.id] = group

        # 2. Единицу измерения
        unit_key = "unit_nomenclature"
        units = elements.get[unit_key]    
        if units is None:
            elements[unit_key] = {}
            unit = nomenclature_factory.create_default_unit()
            elements[unit_key][unit.id] = unit

        if units is None or groups is None:
            nomenclature_factory.create_default_nomenclature()

        nomenclature_factory.elements = elements

        item = nomenclature("Новый")
        item.group = groups[0]
        item.unit = units[0]
        return item

    @staticmethod
    def create_default_group():
        " Фабричный метод: Создать группу номенклатуры по умолчанию"
        group =   group_nomenclature("Ингредиенты")
        return group      
    
    @staticmethod
    def create_default_unit():
        " Фабричный метод: Создать единицу измерения по умолчанию"
        unit = unit_nomenclature("кг")
        unit.description = "1 Кг (1000 грамм)"
        return unit
