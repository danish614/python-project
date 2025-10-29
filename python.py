import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    api_key = "510e39dcdfc23dfde6823e0ec9d8d4f8"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "City not found."))
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        
        city_label_val.config(text=city_name)
        temp_label_val.config(text=f"{temp} °C")
        cond_label_val.config(text=desc)
        hum_label_val.config(text=f"{humidity} %")
        wind_label_val.config(text=f"{wind} m/s")

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter City Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather,
          bg="blue", fg="white", font=("Arial", 10, "bold")).pack(pady=15)


frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
frame.pack(padx=20, pady=10, fill="both", expand=True)

def create_row(label_text):
    row = tk.Frame(frame, bg="white")
    row.pack(pady=5, fill="x")
    tk.Label(row, text=label_text, width=12, anchor="w", bg="white", font=("Arial", 11, "bold")).pack(side="left")
    value_label = tk.Label(row, text="--", anchor="w", bg="white", font=("Arial", 11))
    value_label.pack(side="left")
    return value_label

city_label_val = create_row(" City:")
temp_label_val = create_row(" Temp:")
cond_label_val = create_row(" Condition:")
hum_label_val = create_row("  Humidity:")
wind_label_val = create_row("  Wind:")

root.mainloop()
