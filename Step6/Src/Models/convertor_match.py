from Src import reference


#
# Описательная модель в которой содержится информация о конвертиации 
#
class convertor_match:
    _source_type = None
    _dest_type = None
    _convertor = None
    
    @property
    def source_type(self):
        """

        Returns:
            _type_: Тип данных который будет сконвертирован
        """
        return self._source_type
    
    @source_type.setter
    def source_type(self, value):
        """

        Args:
            value (_type_): Любой исходный тип данных в том числе None
        """
        self._source_type = value
        
    @property
    def dest_type(self):
        """

        Returns:
            _type_: Тип данных в которы будет сконвертировано
        """
        return self._dest_type
    
    @dest_type.setter
    def dest_type(self, value):
        """

        Args:
            value (reference.reference): Любой класс наследний от reference.reference

        Raises:
            Exception: Некорректный тип данных
        """
        if not isinstance(value, reference.reference):
            raise Exception("Некорректно передан тип данных!")
        
        self._dest_type = value
    
    @property
    def convertor(self):
        """

        Returns:
            _type_: Объект, который будет производить конвертиацию данных
        """
        return self._convertor
    
    @convertor.setter
    def convertor(self, value:reference.reference):
        """
            Объект, который будет заниматься конвертацией        
        """
    def convertor(self, value: reference.reference ):
        if not  isinstance(value, reference.reference):
            raise Exception("Некорректно передан тип данных!")
        
        self._convertor = value
        