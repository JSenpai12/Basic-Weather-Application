import requests
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from weather_design import Ui_MainWindow

class Weather_App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.get_weather)

        self.image_list = [
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\cloudy.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\heavy_rain.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\light-rain.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\mist.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\snow.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\storm.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\sun.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\lava.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\windstorm.png",
            r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\wind.png"
        ]
    
    def get_weather(self):
        api_key = "a2305b483e74316e4ff11f03f0d854b6"
        city_name = self.lineEdit.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200 or data['cod'] == "200":
               self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error:
            print("Status: ",response.status_code)
            match response.status_code:
                case 400:
                    self.display_error("Bad Request", "Please check your input")
                case 401:
                    self.display_error("Unathorized","Invalid API key")
                case 403:
                    self.display_error("Forbidden","Access is denied")
                case 404:
                    self.display_error("Not found","City not found")
                case 500:
                    self.display_error("Internal Server Error","Please try again later")
                case 502:
                    self.display_error("Bad gateway","Invalid response from the server")
                case 503:
                    self.display_error("Service Unavailable","Service is down")
                case 504:
                    self.display_error("Gateway timeout","No response from the server")
                case _:
                    self.display_error("HTTP error",f"Error has occured {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:","Check your internet connection")
        
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:","The request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:","Check the URL")
        
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:",f"{req_error}")
    
    def display_weather(self, data):
        country = data['sys']['country']
        city_name = data['name']
        temperature_c = data['main']['temp'] - 273.15
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']
        wind_speed = data['wind']['speed']

        self.label_3.setText(f"{city_name}, {country}")
        self.label_4.setText(f"{temperature_c:.0f}\u00b0")
        self.label_8.setText(f"{humidity}%\nHumidity")
        self.label_9.setText(f"{wind_speed}km/h\nPer Hour")

        self.weather_images(weather_id)

    def display_error(self, title ,msg_error):
        print("Error: ",msg_error) 

        box = QMessageBox()
        box.setWindowTitle(title)
        box.setIcon(QMessageBox.Critical)
        box.setText(msg_error)
        box.setStandardButtons(QMessageBox.Ok)
        box.setStyleSheet("font-size: 20px;")
        box.exec()
    
    def display_images(self, index):
        pixmap = QPixmap(self.image_list[index])
        scaled_pixmap = pixmap.scaled(81, 71, Qt.KeepAspectRatio)

        self.label.setPixmap(scaled_pixmap)
    
    def weather_images(self, weather_id):
       match weather_id:
           case _ if 200 <= weather_id <= 300:
               self.display_images(5)
           case _ if 300 <= weather_id <= 321:
               self.display_images(2)
           case _ if 500 <= weather_id <= 531:
               self.display_images(1)
           case _ if 600 <= weather_id <= 622:
               self.display_images(4)
           case _ if 701 <= weather_id <= 741:
               self.display_images(3)
           case 762:
               self.display_images(7)
           case 771:
               self.display_images(9)
           case 781:
               self.display_images(8)
           case 800:
               self.display_images(6)
           case _ if 801 <= weather_id <= 804:
               self.display_images(0)
           case _:
               self.display_images(0)
            

if __name__ == '__main__':
    app = QApplication([])
    window = Weather_App()
    window.show()
    sys.exit(app.exec())