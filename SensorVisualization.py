import serial
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
# Set up the serial connection
ser = serial.Serial('COM7', 115200)  # Replace 'COM3' with the correct serial port for your Arduino

# Create lists to store the data
timestamps = []
x_data = []
y_data = []
z_data = []

# Create the main Tkinter application
root = tk.Tk()
root.title("ADXL-335 Accelerometer Dashboard")

# Create a Figure and Axes for the plot
fig, ax = plt.subplots()
line_x, = ax.plot([], [], label='X-axis')
line_y, = ax.plot([], [], label='Y-axis')
line_z, = ax.plot([], [], label='Z-axis')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Acceleration (g)')
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def update_plot():
    global timestamps, x_data, y_data, z_data

    try:
        data = ser.readline().decode().strip()
        values = data.split('\t')

        # Assuming the first three values are X, Y, and Z-axis accelerometer data
        timestamp = len(timestamps)  # Use a simple incremental timestamp for this example
        x_acc = float(values[0])
        y_acc = float(values[1])
        z_acc = float(values[2])

        timestamps.append(timestamp)
        x_data.append(x_acc)
        y_data.append(y_acc)
        z_data.append(z_acc)

        # Limiting the number of data points to display for better performance
        max_data_points = 100
        if len(timestamps) > max_data_points:
            timestamps = timestamps[-max_data_points:]
            x_data = x_data[-max_data_points:]
            y_data = y_data[-max_data_points:]
            z_data = z_data[-max_data_points:]

        line_x.set_data(timestamps, x_data)
        line_y.set_data(timestamps, y_data)
        line_z.set_data(timestamps, z_data)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()

    except Exception as e:
        messagebox.showerror("Error", f"Error reading data from Arduino: {e}")
        root.quit()

    root.after(100, update_plot)  # Refresh plot every 100 milliseconds

def on_quit_button_click():
    ser.close()
    root.quit()

quit_button = tk.Button(root, text="Quit", command=on_quit_button_click)
quit_button.pack()


update_plot()  # Start updating the plot

root.mainloop()

