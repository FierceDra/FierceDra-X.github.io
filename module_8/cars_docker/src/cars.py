import tensorflow as tf
import tensorflow.keras as keras
from keras.models import load_model
from tensorflow.python.ops.numpy_ops import np_config

np_config.enable_numpy_behavior()

import numpy as np
import streamlit as st
from PIL import Image

#пишем зашоловок и оформляем страницу тематической картинкой
st.title("Угадываем авто по фотографии")
st.image('https://img2.goodfon.ru/wallpaper/nbig/4/4a/auto-cars-ac-cobra-cobra.jpg')

#делаем справочную информацию о моделях авто, которые мы можем узнать
reference = {'0': 'Приора',
             '1':'Ford',
             '2':'Лада Самара',
             '3':'Десятка',
             '4':'Семерка классика',
             '5':'Нива',
             '6':'Калина',
             '7':'Девятка',
             '8':'Volkswagen',
             '9':'99-я',
}

#выводим справочную информацию она боковую панель
st.sidebar.markdown('**Словарь узнаваемых категорий авто:**')
for key,value in reference.items():
    st.sidebar.markdown(f'**{key}**: {value}')

img_file_buffer = st.file_uploader("Загрузите фото ваше автомобиля")

if img_file_buffer is not None:
    car_img = Image.open(img_file_buffer)
    model_size = (420,420)
    car_img = car_img.resize(model_size)
    car_array = np.array(car_img).reshape(1,420,420,3)/255
    #st.write(type(car_array))
    #st.write(car_array.shape)

#загружаем нашу прогнозную модель
model = load_model('model_xc.h5')

#делаем кнопку запуска блока расчета прогноза и под нее заводим сам расчет прогноза
result = st.button('Получите модель вашего авто')
if result:
	st.image(car_img, caption='Вот как выглядит ваш агрегат')
	
	predictions = np.argmax(model.predict(car_array), axis=1)
	
	if predictions == 0:
		st.write('## **У вас Приора, народная любовь**')
	elif predictions == 1:
		st.write('## **У вас Ford, но вы не хвастайтесь**')
	elif predictions == 2:
		st.write('## **У вас Лада-Самара, поезжайте на ней на Волгу, там красиво**')
	elif predictions == 3:
		st.write('## **У вас десятка, чудо российской автоконстукторской мысли**')
	elif predictions == 4:
		st.write('## **У вас старая лошадка семерка, классика и винтаж только растут в цене со временем**')
	elif predictions == 5:
		st.write('## **Да это же Нива!, вывезет из любого навоза**')
	elif predictions == 6:
		st.write('## **У вас калинка-малинка, потанцуем?**')
	elif predictions == 7:
		st.write('## **У вас девятка, старое зубило**')
	elif predictions == 8:
		st.write('## **У вас Volkswagen, поздравляю вы состоятельный бюргер**')
	elif predictions == 9:
		st.write('## **У вас 99, старое зубило, версия 2.0**')	
	else:
		st.write('## **Протрите мне очки, не пойму, что за агрегат!**')
