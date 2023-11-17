# AtvSim

## Project Overview

This project aims to elevate the performance of LNCT's Society of Automotive Engineer's (SAE) ATV through the implementation of a telemetry system. Leveraging an MPU9250 sensor, an ESP32 board, and Arduino for wireless data transmission, the project integrates seamlessly with Unity for real-time data visualization.

## Key Features

### Telemetry System Design

- **Hardware:** Utilized MPU9250 sensor and ESP32 board for robust telemetry data collection.
  
- **Wireless Data Transmission:** Established wireless communication to a local PC using Arduino and the WebSockets protocol.

- **Real-time Data Fetching:** Implemented Python APIs for seamless integration with Unity's C# script or any third-party integrations.

### Data Analysis and Visualization

- **Python Scripting:** Created a Python script using Matplotlib for real-time data analysis, providing valuable insights into the telemetry data.

- **Integration with Unity:** Improved testing sessions by enabling the ATV's animated CAD model to respond to real-time sensor data, simulating real-life movements using Unity and C#.

### Upcoming Developments

- **Frontend Dashboard:** In the pipeline is the development of a frontend dashboard to offer a user-friendly interface for monitoring and analyzing telemetry data.

- **Real-Time Data Logging System:** Future plans include implementing a Python system that feeds data in real-time into a database and Excel sheets every time a session is activated, ensuring comprehensive and organized data logging.

- **Deployment:** Planning to deploy the project on the web, making it accessible to all club members. This will enable easy access and usage for monitoring and analyzing ATV performance.

### Comprehensive Project Scope

- **Hardware-Software Integration:** Successfully combined hardware integration, software development, and 3D modeling within a single project.

- **Technology Stack:** Python, Flask, Matplotlib, C#, Arduino.

### Project Showcase

Here you can find images and videos showcasing the project in action. (Sidenote : I apologize for the quality of media and the lack of context for each of them. I had'nt give it a lot of thought when I was making the project ;-;)

1. First Time I got the Animated ATV model to work in-sync with the Sensors

https://github.com/lag25/AtvSim/assets/116341862/daae8f61-f133-4ec7-880d-651e81ac1952

2. Showcasing Rotations using an ESP32 

https://github.com/lag25/AtvSim/assets/116341862/1916d595-a784-42e0-a7e2-bba7a44a8636

3. Python Script visualizing Vehicular Pitch,Yaw and Roll in real time
![WhatsApp Image 2023-08-01 at 21 34 27_1fac0a6e](https://github.com/lag25/AtvSim/assets/116341862/ea88300d-f0f1-4e3a-9f61-b494043f88e1)

4. My ESP32 Board and an MPU-9250 sensor (Plus my Shaft Encoder which I later decided to not use for this project)
![sensors](https://github.com/lag25/AtvSim/assets/116341862/a1fa92e4-ea76-4e5c-811c-391fae36e3e0)


## Project Repository

Find the code and documentation in the [GitHub Repository](insert_link_here).

## Getting Started

To get started with the project, follow the instructions in the [Wiki](insert_wiki_link_here) for installation and usage guidelines.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.

## License

This project is licensed under the [MIT License](insert_license_link_here) - see the [LICENSE.md](insert_license_link_here) file for details.

