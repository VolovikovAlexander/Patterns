from Src.Logics.nomenclature_factory import nomenclature_factory
from Src.Models.nomenclature_history import nomenclature_history
from Src.settings import app_settings
from Src.Logics.convertor_factory import convertor_factory
from Src.reference import reference
from Src.Models.nomenclature import nomenclature

import random
import json
from random import randrange
from datetime import timedelta, datetime

#
# Фабрика для генерации набора данных
#
class data_factory:
    @staticmethod
    def nomenclature():
        """
            Получить текущий список номенклатуры
        Returns:
            _type_: list
        """
        return nomenclature_factory._storage.get(nomenclature_factory._nomenclature_key)
    
    @staticmethod
    def random_date(start, end):
        """

        Args:
            start (datetime): Начало отсчета
            end (datetime): Окончание отсчета

        Returns:
            datetime: Возвращает дату случайно укладывающуюся в указанный период
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)
    
    @staticmethod
    def create_nomenclature(settings: app_settings):
        """
            Сформировать список номенклатуры
        Args:
            settings (app_settings): Текущие настройки    
        """
        
        if settings is None:
            raise Exception("Некорректно переданы параметры!")
        
        # Очищаем старую структуру
        nomenclature_factory._storage = {}
        
        # Загружаем настройки
        list =  settings.data["nomenclature"]
        if list is None:
            raise Exception("Некорректно выполнены настройки. В файле settings.json нет данных по номенклатуре!")
        
        factory = convertor_factory()
        
        # Формируем объекты номенклатуры
        for row in list:
            # Обычные свойства
            item = factory.convert(row, reference)
            # Группа номенклатуры
            group = factory.convert(row["group"],  reference)
            # Единица измерения
            unit = factory.convert(row["unit"], reference)
            
            element = nomenclature()
            element.name = item.name
            element.description = item.description
            element.id = item.id
            
            element.group = group
            element.unit = unit
            
            # Добавим элемент в хранилище
            items = nomenclature_factory.add_nomenclature(element)
            
            
    @staticmethod
    def create_history(length):
        """
            Сформировать список элементов типа nomenclature_history
        Returns:
            Массив: Список элементов nomenclature_history
            
        Raises:
            Exception: Количество указано не верно    
        """
        items = []
        if len(nomenclature_factory._storage.get(nomenclature_factory._nomenclature_key)) == 0:
            raise Exception("Исходный список номенклатуры пуст!")
        
        if length <= 0:
            raise Exception("Некорректно указано количество записей для генерации истории!")
        
        for nomenclature_pair in nomenclature_factory._storage[nomenclature_factory._nomenclature_key]:
            for number in range(length):
                item = nomenclature_history()
                item.nomenclature_code = nomenclature_pair[0]
                item.period = data_factory.random_date(datetime.strptime("2023-12-01", "%Y-%m-%d"),
                                                        datetime.strptime("2024-01-01", "%Y-%m-%d"))
                item.turn = random.uniform(-50, 50)
                item._comments = f"Номер записи: {number}"
                items.append(item)
            
        return items    
    
    
    @staticmethod
    def create_receipe(length):
        """
           Сформировать рецепты
        Args:
            length (_type_): количество

        Raises:
            Exception: _description_
            Exception: _description_
        """
        items = []
        if len(nomenclature_factory._storage.get(nomenclature_factory._nomenclature_key)) == 0:
            raise Exception("Исходный список номенклатуры пуст!")
        
        if length <= 0:
            raise Exception("Некорректно указано количество записей для генерации истории!")
        
        
        
  
    