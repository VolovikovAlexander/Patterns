
from Src.Logics.nomenclature_factory import nomenclature_factory
from Src.Models.nomenclature_history import nomenclature_history

import random
import uuid
from random import randrange
from datetime import timedelta, datetime

#
# Фабрика для генерации набора данных
#
class data_factory:
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
    def create_nomenclature(length):
        """
            Сформировать список номенклатуры
        Args:
            length (int): Количество записей    

        Raises:
            Exception: Количество указано не верно
        """
        if length <= 0:
            raise Exception("Некорректно указано количество записей для генерации номенклатуры!")
        
        nomenclature_factory._storage = {}
        for number in range(length):
            name = f"Номенклатура {number + 1}"
            nomenclature_factory.create_default_nomenclature(nomenclature_factory._storage, name)
            
            
    
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
            
    
    