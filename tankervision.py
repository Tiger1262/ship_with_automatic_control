import cv2 #Загружаем библиотеку openCV
import random #Загружаем библиотеку random
import pandas #Загружаем библиотеку pandas
import pandas as pd
from datetime import datetime #Загружаем библиотеку random
oil_temp_sensor = random.randint(-30, 200) #Инициализация переменных имитирующих работу датчиков
wat_temp_sensor = random.randint(-30, 150)
wat_pressure = random.randint(0, 300)
oil_pressure = random.randint(0, 1400)
battery_voltage = random.randint(0, 32)
battery_amperage = random.randint(0, 32)
wat_pressure_time= str(datetime.now().time())  #Узнаем в какое время были зафиксированны данные
oil_pressure_time= str(datetime.now().time())
battery_voltage_time= str(datetime.now().time())
battery_amperage_time= str(datetime.now().time())
oil_temp_time= str(datetime.now().time())
wat_temp_time= str(datetime.now().time())
if (oil_temp_sensor < 20 or oil_temp_sensor > 100): #обработка данных
    oil_temp_status = "Error"
else:
    oil_temp_status = "Normal"
if (wat_temp_sensor < 20 or wat_temp_sensor > 80):
    wat_temp_status = "Error"
else:
    wat_temp_status = "Normal"
if (wat_pressure < 50 or wat_pressure > 150):
    wat_pressure_status = "Error"
else:
    wat_pressure_status = "Normal"
if (oil_pressure < 50 or oil_pressure > 150):
    oil_pressure_status = "Error"
else:
    oil_pressure_status = "Normal"
if (battery_voltage < 20 or battery_voltage > 25):
    battery_voltage_status = "Error"
else:
    battery_voltage_status = "Normal"
if (battery_amperage < 20 or battery_amperage > 25):
    battery_amperage_status = "Error"
else:
    battery_amperage_status = "Normal"
oil_temp_fin= "Time: " + oil_temp_time[0:8]+ " Data: " + str(oil_temp_sensor) + " *C"
wat_temp_fin = "Time: " + wat_temp_time[0:8] + " Data: "+ str(wat_temp_sensor ) + " *C"
wat_pressure_fin = "Time: " + wat_pressure_time[0:8]+ " Data: " + str(wat_pressure) + " Кпа"
oil_pressure_fin = "Time: " + oil_pressure_time[0:8]+ " Data: " + str(oil_pressure) + " Кпа"
battery_voltage_fin = "Time: " + battery_voltage_time[0:8]+ " Data: " + str(battery_voltage) + " В"
battery_amperage_fin = "Time: " + battery_voltage_time[0:8]+ " Data: " + str(battery_voltage) + " А"
sensors_data = pd.DataFrame({"Sensor_name": ["Temperature_oil", "Temperature_water","Pressure_water","Pressure_oil","Battery voltage", "Battery amperage"],
                            "Sensor_data and time":[oil_temp_fin, wat_temp_fin,wat_pressure_fin,oil_pressure_fin,battery_voltage_fin,battery_amperage_fin],
                            "Work_Status": [oil_temp_status, wat_temp_status,wat_pressure_status,oil_pressure_status,battery_voltage_status, battery_amperage_status]}) # ЗАписываем данные в формат DataFrame
sensors_data.to_excel('./sensors.xlsx') #Сохраняем обработанные данные в таблицу excel
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G') # Настройка для записи видеос камеры
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Захватываем изображение с камеры
width = int(camera.get(3))
height = int(camera.get(4))
size = (width, height)
output = cv2.VideoWriter("output.avi", fourcc, 30, size)
while True:
    ret, image = camera.read()
    cv2.imshow("Motor Camera", image) # Выводим изображение на экран
    k = cv2.waitKey(30) & 0xFF #
    if ret == True:

       output.write(image) # Сохраняем видеофайл
    if k == 27:    # Нажмите esc для завершения программы
        break
cv2.destroyAllWindows()
camera.release()
output.release()
