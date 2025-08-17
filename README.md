# Food-spoilage-detection-system
If food is rotten red light ,If not green


The Food Spoilage Detection System is an IoT and sensor-based project designed to monitor and detect the freshness of food items in real-time. Food spoilage is a major concern in households, markets, and storage facilities, leading to wastage and health risks. This project aims to provide a low-cost, efficient, and automated method to detect spoilage by integrating multiple sensors with an Arduino Uno microcontroller.

The system utilizes:

* MQ2 Smoke/Methane Sensor to detect gases released during decomposition.
* Temperature Sensor to monitor changes in the food’s surrounding environment.
*  Humidity Sensor to track moisture levels that accelerate spoilage.
*  TCS3200 Colour Sensor  to identify discoloration, which is a common indicator of spoiled food.

Based on the sensor readings, the Arduino processes the data and determines the food’s condition. The results are visually indicated using  green and red LEDs :

*  Green LED  → Food is fresh.
*  Red LED  → Food is spoiled.

Additionally, the system prints detailed sensor readings and food status to the  serial monitor , providing real-time insights into environmental conditions and spoilage detection.

This project demonstrates the practical use of sensors and microcontrollers in solving real-world problems like food safety and waste reduction. It can be further enhanced by integrating wireless communication (IoT) for remote monitoring, mobile notifications, and smart kitchen applications.


