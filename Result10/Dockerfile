FROM python:3.10.14 as build
WORKDIR /app
EXPOSE 5000

# Готовим окружение
RUN pip3 install --upgrade pip
RUN pip3 install -U Flask
RUN pip3 install -U flask-restplus

# Копируем исходный код
COPY Src /app/Src
COPY main.py /app/

# Что скопировалось?
RUN echo $(ls -1)

# Запускаем
CMD [ "python", "main.py" ]


