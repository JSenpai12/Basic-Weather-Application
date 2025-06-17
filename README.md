# Basic-Weather-Application
Trying  API's

A simple weather application built with Python and PySide6.

📦 Features
Search weather by city name

Displays:

Temperature
Humidity
Wind Speed
Weather Icon
Error handling with pop-up messages
Uses custom icons from the Weather_Icons/ folder

GUI Image:
![image](https://github.com/user-attachments/assets/0aaf6818-889f-4f3c-b186-39a7b1b22e05)

FOLDER STRUCTURE:

WeatherApp/
│
├── Weather_Icons/           - Folder containing icon images (PNG format)
│   ├── cloudy.png
│   ├── heavy_rain.png
│   ├── light-rain.png
│   ├── mist.png
│   ├── snow.png
│   ├── storm.png
│   ├── sun.png
│   ├── lava.png
│   ├── windstorm.png
│   └── wind.png
│
├── weather.ui               - Qt Designer UI file
├── weather_design.py        - Auto-generated PySide6 Python code from the .ui
├── main.py                  - Main application code (backend logic)
└── README.md                - This file

▶️ How to Run:

1. Clone this repository.
```bash
git clone https://github.com/yourusername/WeatherApp.git
cd WeatherApp
```
2. Install dependencies
Make sure you have Python 3.9+ installed.
```bash
pip install -r requirements.txt
```

If requirements.txt isn't included, manually install:
```bash
pip install PySide6 requests
```

3. Generate weather_design.py from weather.ui
   ```bash
   pyside6-uic weather.ui -o weather_design.py
   ```
   Note: You can skip this if weather_design.py is already present.

4. Run the app.
   ```bash
   python main.py
   ```
   
⚠️ Important Notes:
  Make sure the Weather_Icons/ folder is in the same directory as your main.py.
  You must replace the absolute image paths in main.py

❌ Example:
```bash
r"C:\Users\Jhon Mekier\Desktop\Weather_Icons\sun.png"
```
✅ With:
```bash
"Weather_Icons/sun.png"
```
This ensures compatibility across devices and platforms.

🔑 API Key
This app uses the OpenWeatherMap API.
1. Sign up for a free API key at https://openweathermap.org/api
2. Replace the existing API key in main.py:
  ```bash
  api_key = "your_api_key_here"
  ```

Author:
  Mekier.
