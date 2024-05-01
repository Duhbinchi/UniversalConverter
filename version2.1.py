"""
Version 2.1 Notes

x Done
- Used Image Backgrounds and Buttons for UI design

x Goals To Do
- Functions for:
-- speed converter class
-- volume coverter class
- Enable TKinter to download images from the internet for the main menu background
- add symbols to the labels (unicode / unit of measurement)

x Ideas
- In the main menu class, load all the images to be used later as background images for the other windows
- game title screen-like user interface in the main menu

"""

import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.font import Font
import os


# Get the directory of the images
def get_image_path(image_name):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Build the full image path
    image_path = os.path.join(script_dir, 'photos', image_name)
    return image_path


class LengthConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Length Converter")
        self.window.geometry("275x135")
        
        # Load the background image
        self.bg_img = PhotoImage(file=get_image_path('blue.png'))
        
        # Create a canvas
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
    
        # Set the updating flag to False to prevent the convert_from_* methods from running when the text variables are updated
        self.updating = False
        
        # Create the widgets
        self.meters_var = tk.StringVar()
        self.meters_var.trace_add("write", self.convert_from_meters)
        meter_entry = tk.Entry(self.window, textvariable=self.meters_var, font=my_font)
        meter_entry.place(x=100, y=40)
        # Use create_text() instead of a Label
        self.canvas.create_text(10, 40, text="Meters", font=my_font, anchor='nw', fill='white')
        
        # Repeat for the other variables
        self.feet_var = tk.StringVar()
        self.feet_var.trace_add("write", self.convert_from_feet)
        feet_entry = tk.Entry(self.window, textvariable=self.feet_var, font=my_font)
        feet_entry.place(x=100, y=100)
        self.canvas.create_text(10, 100, text="Feet", font=my_font, anchor='nw', fill='white')
        
        self.inches_var = tk.StringVar()
        self.inches_var.trace_add("write", self.convert_from_inches)
        inches_entry = tk.Entry(self.window, textvariable=self.inches_var, font=my_font)
        inches_entry.place(x=100, y=70)
        self.canvas.create_text(10, 70, text="Inches", font=my_font, anchor='nw', fill='white')
        
        self.cm_var = tk.StringVar()
        self.cm_var.trace_add("write", self.convert_from_cm)
        cm_entry = tk.Entry(self.window, textvariable=self.cm_var, font=my_font)
        cm_entry.place(x=100, y=10)
        self.canvas.create_text(10, 10, text="Centimeters", font=my_font, anchor='nw', fill='white')

#clearing fields with selected exeption
    def clear_except(self, field_to_keep):
        fields = [self.meters_var, self.feet_var, self.inches_var, self.cm_var]
        for field in fields:
            if field is not field_to_keep:
                field.set("")

#converting from other units
    def convert_from_meters(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.meters_var.get() == "":
            self.clear_except(self.meters_var)

        else:
            try:
                meters = float(self.meters_var.get())
                self.feet_var.set(f"{meters * 3.28084:.2f}")
                self.inches_var.set(f"{meters * 39.3701:.2f}")
                self.cm_var.set(f"{meters * 100:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_feet(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.feet_var.get() == "":
            self.clear_except(self.feet_var)

        else:
            try:
                feet = float(self.feet_var.get())
                self.meters_var.set(f"{feet / 3.28084:.2f}")
                self.inches_var.set(f"{feet * 12:.2f}")
                self.cm_var.set(f"{feet * 30.48:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_inches(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.inches_var.get() == "":
            self.clear_except(self.inches_var)

        else:
            try:
                inches = float(self.inches_var.get())
                self.meters_var.set(f"{inches / 39.3701:.2f}")
                self.feet_var.set(f"{inches / 12:.2f}")
                self.cm_var.set(f"{inches * 2.54:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_cm(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.cm_var.get() == "":
            self.clear_except(self.cm_var)
        else:
            try:
                cm = float(self.cm_var.get())
                self.meters_var.set(f"{cm / 100:.2f}")
                self.feet_var.set(f"{cm / 30.48:.2f}")
                self.inches_var.set(f"{cm / 2.54:.2f}")
            except ValueError:
                pass
        self.updating = False


class TimeConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Time Converter")
        self.window.geometry("250x225")
        self.updating = False

        self.seconds_var = tk.StringVar()
        self.seconds_var.trace_add("write", self.convert_from_seconds)
        seconds_entry = tk.Entry(self.window, textvariable=self.seconds_var)
        seconds_entry.place(x=100, y=10)

        seconds_label = tk.Label(self.window, text="Seconds")
        seconds_label.place(x=10, y=10)

        self.minutes_var = tk.StringVar()
        self.minutes_var.trace_add("write", self.convert_from_minutes)
        minutes_entry = tk.Entry(self.window, textvariable=self.minutes_var)
        minutes_entry.place(x=100, y=40)

        minutes_label = tk.Label(self.window, text="Minutes")
        minutes_label.place(x=10, y=40)

        self.hours_var = tk.StringVar()
        self.hours_var.trace_add("write", self.convert_from_hours)
        hours_entry = tk.Entry(self.window, textvariable=self.hours_var)
        hours_entry.place(x=100, y=70)

        hours_label = tk.Label(self.window, text="Hours")
        hours_label.place(x=10, y=70)

        self.days_var = tk.StringVar()
        self.days_var.trace_add("write", self.convert_from_days)
        days_entry = tk.Entry(self.window, textvariable=self.days_var)
        days_entry.place(x=100, y=100)

        days_label = tk.Label(self.window, text="Days")
        days_label.place(x=10, y=100)

        self.weeks_var = tk.StringVar()
        self.weeks_var.trace_add("write", self.convert_from_weeks)
        weeks_entry = tk.Entry(self.window, textvariable=self.weeks_var)
        weeks_entry.place(x=100, y=130)

        weeks_label = tk.Label(self.window, text="Weeks")
        weeks_label.place(x=10, y=130)

        self.months_var = tk.StringVar()
        self.months_var.trace_add("write", self.convert_from_months)
        months_entry = tk.Entry(self.window, textvariable=self.months_var)
        months_entry.place(x=100, y=160)

        months_label = tk.Label(self.window, text="Months")
        months_label.place(x=10, y=160)

        self.years_var = tk.StringVar()
        self.years_var.trace_add("write", self.convert_from_years)
        years_entry = tk.Entry(self.window, textvariable=self.years_var)
        years_entry.place(x=100, y=190)

        years_label = tk.Label(self.window, text="Years")
        years_label.place(x=10, y=190)

    def clear_except(self, field_to_keep):
        fields = [
            self.seconds_var,
            self.minutes_var,
            self.hours_var,
            self.days_var,
            self.weeks_var,
            self.months_var,
            self.years_var,
        ]
        
        for field in fields:
            if field is not field_to_keep:
                field.set("")

    def convert_from_seconds(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.seconds_var.get() == "":
            self.clear_except(self.seconds_var)

        else:
            try:
                seconds = float(self.seconds_var.get())
                self.minutes_var.set(f"{seconds / 60:.2f}")
                self.hours_var.set(f"{seconds / 3600:.5f}")
                self.days_var.set(f"{seconds / 86400:.8f}")
                self.weeks_var.set(f"{seconds / 604800:.12f}")
                self.months_var.set(
                    f"{seconds / 2628000:.12f}"
                )  # Approximate conversion
                self.years_var.set(f"{seconds / 31536000:.12f}")

            except ValueError:
                pass
        self.updating = False

    def convert_from_minutes(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.minutes_var.get() == "":
            self.clear_except(self.minutes_var)

        else:
            try:
                minutes = float(self.minutes_var.get())
                self.seconds_var.set(f"{minutes * 60:.2f}")
                self.hours_var.set(f"{minutes / 60:.4f}")
                self.days_var.set(f"{minutes / 1440:.6f}")
                self.weeks_var.set(f"{minutes / 10080:.8f}")
                self.months_var.set(f"{minutes / 43800:.10f}")  # Approximate conversion
                self.years_var.set(f"{minutes / 525600:.10f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_hours(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.hours_var.get() == "":
            self.clear_except(self.hours_var)

        else:
            try:
                hours = float(self.hours_var.get())
                self.seconds_var.set(f"{hours * 3600:.2f}")
                self.minutes_var.set(f"{hours * 60:.2f}")
                self.days_var.set(f"{hours / 24:.2f}")
                self.weeks_var.set(f"{hours / 168:.2f}")
                self.months_var.set(f"{hours / 730:.5f}")  # Approximate conversion
                self.years_var.set(f"{hours / 8760:.5f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_days(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.days_var.get() == "":
            self.clear_except(self.days_var)

        else:
            try:
                days = float(self.days_var.get())
                self.seconds_var.set(f"{days * 86400:.2f}")
                self.minutes_var.set(f"{days * 1440:.2f}")
                self.hours_var.set(f"{days * 24:.2f}")
                self.weeks_var.set(f"{days / 7:.2f}")
                self.months_var.set(f"{days / 30.44:.4f}")  # Approximate conversion
                self.years_var.set(f"{days / 365:.6f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_weeks(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.weeks_var.get() == "":
            self.clear_except(self.weeks_var)

        else:
            try:
                weeks = float(self.weeks_var.get())
                self.seconds_var.set(f"{weeks * 604800:.2f}")  # 1 week = 604800 seconds
                self.minutes_var.set(f"{weeks * 10080:.2f}")  # 1 week = 10080 minutes
                self.hours_var.set(f"{weeks * 168:.2f}")  # 1 week = 168 hours
                self.days_var.set(f"{weeks * 7:.2f}")
                self.months_var.set(f"{weeks / 4.34524:.2f}")
                self.years_var.set(f"{weeks / 52.1775:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_months(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.months_var.get() == "":
            self.clear_except(self.months_var)

        else:
            try:
                months = float(self.months_var.get())
                self.seconds_var.set(f"{months * 2628000:.2f}")
                self.minutes_var.set(f"{months * 43800:.2f}")
                self.hours_var.set(f"{months * 730:.2f}")
                self.days_var.set(f"{months * 30.44:.2f}")
                self.weeks_var.set(f"{months * 4.34524:.2f}")
                self.years_var.set(f"{months / 12:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_years(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.years_var.get() == "":
            self.clear_except(self.years_var)

        else:
            try:
                years = float(self.years_var.get())
                self.seconds_var.set(
                    f"{years * 31536000:.2f}"
                )  # 1 year = 31536000 seconds
                self.minutes_var.set(f"{years * 525600:.2f}")  # 1 year = 525600 minutes
                self.hours_var.set(f"{years * 8760:.2f}")  # 1 year = 8760 hours
                self.days_var.set(f"{years * 365:.2f}")  # 1 year = 365 days
                self.weeks_var.set(f"{years * 52.1775:.2f}")  # 1 year = 52.1775 weeks
                self.months_var.set(f"{years * 12:.2f}")
            except ValueError:
                pass
        self.updating = False


class TemperatureConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Temperature Converter")
        self.window.geometry("250x100")
        self.updating = False

        self.celsius_var = tk.StringVar()
        self.celsius_var.trace_add("write", self.convert_from_celsius)
        celsius_entry = tk.Entry(self.window, textvariable=self.celsius_var)
        celsius_entry.place(x=100, y=10)

        celsius_label = tk.Label(self.window, text="Celsius")
        celsius_label.place(x=10, y=10)

        self.fahrenheit_var = tk.StringVar()
        self.fahrenheit_var.trace_add("write", self.convert_from_fahrenheit)
        fahrenheit_entry = tk.Entry(self.window, textvariable=self.fahrenheit_var)
        fahrenheit_entry.place(x=100, y=40)

        fahrenheit_label = tk.Label(self.window, text="Fahrenheit")
        fahrenheit_label.place(x=10, y=40)

        self.kelvin_var = tk.StringVar()
        self.kelvin_var.trace_add("write", self.convert_from_kelvin)
        kelvin_entry = tk.Entry(self.window, textvariable=self.kelvin_var)
        kelvin_entry.place(x=100, y=70)

        kelvin_label = tk.Label(self.window, text="Kelvin")
        kelvin_label.place(x=10, y=70)

    def clear_except(self, field_to_keep):
        fields = [self.celsius_var, self.fahrenheit_var, self.kelvin_var]
        for field in fields:
            if field is not field_to_keep:
                field.set("")

    def convert_from_celsius(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.celsius_var.get() == "":
            self.clear_except(self.celsius_var)

        else:
            try:
                celsius = float(self.celsius_var.get())
                self.fahrenheit_var.set(f"{celsius * 9/5 + 32:.2f}")
                self.kelvin_var.set(f"{celsius + 273.15:.2f}")

            except ValueError:
                pass
        self.updating = False

    def convert_from_fahrenheit(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.fahrenheit_var.get() == "":
            self.clear_except(self.fahrenheit_var)

        else:
            try:
                fahrenheit = float(self.fahrenheit_var.get())
                self.celsius_var.set(f"{(fahrenheit - 32) * 5/9:.2f}")
                self.kelvin_var.set(f"{(fahrenheit + 459.67) * 5/9:.2f}")

            except ValueError:
                pass
        self.updating = False

    def convert_from_kelvin(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.kelvin_var.get() == "":
            self.clear_except(self.kelvin_var)

        else:
            try:
                kelvin = float(self.kelvin_var.get())
                self.celsius_var.set(f"{kelvin - 273.15:.2f}")
                self.fahrenheit_var.set(f"{kelvin * 9/5 - 459.67:.2f}")

            except ValueError:
                pass
        self.updating = False


class DataConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Data Converter")
        self.window.geometry("250x300")
        self.updating = False

        self.bits_var = tk.StringVar()
        self.bits_var.trace_add("write", self.convert_from_bits)
        bits_entry = tk.Entry(self.window, textvariable=self.bits_var)
        bits_entry.place(x=100, y=10)

        bits_label = tk.Label(self.window, text="Bits")
        bits_label.place(x=10, y=10)

        self.bytes_var = tk.StringVar()
        self.bytes_var.trace_add("write", self.convert_from_bytes)
        bytes_entry = tk.Entry(self.window, textvariable=self.bytes_var)
        bytes_entry.place(x=100, y=40)

        bytes_label = tk.Label(self.window, text="Bytes")
        bytes_label.place(x=10, y=40)

        self.kb_var = tk.StringVar()
        self.kb_var.trace_add("write", self.convert_from_kb)
        kb_entry = tk.Entry(self.window, textvariable=self.kb_var)
        kb_entry.place(x=100, y=70)

        kb_label = tk.Label(self.window, text="Kilobytes")
        kb_label.place(x=10, y=70)

        self.mb_var = tk.StringVar()
        self.mb_var.trace_add("write", self.convert_from_mb)
        mb_entry = tk.Entry(self.window, textvariable=self.mb_var)
        mb_entry.place(x=100, y=100)

        mb_label = tk.Label(self.window, text="Megabytes")
        mb_label.place(x=10, y=100)

        self.gb_var = tk.StringVar()
        self.gb_var.trace_add("write", self.convert_from_gb)
        gb_entry = tk.Entry(self.window, textvariable=self.gb_var)
        gb_entry.place(x=100, y=130)

        gb_label = tk.Label(self.window, text="Gigabytes")
        gb_label.place(x=10, y=130)

        self.tb_var = tk.StringVar()
        self.tb_var.trace_add("write", self.convert_from_tb)
        tb_entry = tk.Entry(self.window, textvariable=self.tb_var)
        tb_entry.place(x=100, y=160)

        tb_label = tk.Label(self.window, text="Terabytes")
        tb_label.place(x=10, y=160)

    def clear_except(self, field_to_keep):
        fields = [
            self.bits_var,
            self.bytes_var,
            self.kb_var,
            self.mb_var,
            self.gb_var,
            self.tb_var,
        ]
        for field in fields:
            if field is not field_to_keep:
                field.set("")

    def convert_from_bits(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.bits_var.get() == "":
            self.clear_except(self.bits_var)
        else:
            try:
                # 1024 or 1000
                bits = float(self.bits_var.get())
                self.bytes_var.set(f"{bits / 8:.2f}")
                self.kb_var.set(f"{bits / 8 / 1024:.4f}")
                self.mb_var.set(f"{bits / 8 / 1024 / 1024:.6f}")
                self.gb_var.set(f"{bits / 8 / 1024 / 1024 / 1024:.8f}")
                self.tb_var.set(f"{bits / 8 / 1024 / 1024 / 1024 / 1024:.14f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_bytes(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.bytes_var.get() == "":
            self.clear_except(self.bytes_var)
        else:
            try:
                bytes = float(self.bytes_var.get())
                self.bits_var.set(f"{bytes * 8:.2f}")
                self.kb_var.set(f"{bytes / 1024:.4f}")
                self.mb_var.set(f"{bytes / 1024 / 1024:.6f}")
                self.gb_var.set(f"{bytes / 1024 / 1024 / 1024:.8f}")
                self.tb_var.set(f"{bytes / 1024 / 1024 / 1024 / 1024:.12f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_kb(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.kb_var.get() == "":
            self.clear_except(self.kb_var)
        else:
            try:
                kb = float(self.kb_var.get())
                self.bits_var.set(f"{kb * 8 * 1024:.2f}")
                self.bytes_var.set(f"{kb * 1024:.2f}")
                self.mb_var.set(f"{kb / 1024:.4f}")
                self.gb_var.set(f"{kb / 1024 / 1024:.6f}")
                self.tb_var.set(f"{kb / 1024 / 1024 / 1024:.10f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_mb(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.mb_var.get() == "":
            self.clear_except(self.mb_var)
        else:
            try:
                mb = float(self.mb_var.get())
                self.bits_var.set(f"{mb * 8 * 1024 * 1024:.2f}")
                self.bytes_var.set(f"{mb * 1024 * 1024:.2f}")
                self.kb_var.set(f"{mb * 1024:.2f}")
                self.gb_var.set(f"{mb / 1024:.4f}")
                self.tb_var.set(f"{mb / 1024 / 1024:.10f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_gb(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.gb_var.get() == "":
            self.clear_except(self.gb_var)
        else:
            try:
                gb = float(self.gb_var.get())
                self.bits_var.set(f"{gb * 8 * 1024 * 1024 * 1024:.2f}")
                self.bytes_var.set(f"{gb * 1024 * 1024 * 1024:.2f}")
                self.kb_var.set(f"{gb * 1024 * 1024:.2f}")
                self.mb_var.set(f"{gb * 1024:.2f}")
                self.tb_var.set(f"{gb / 1024:.4}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_tb(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.tb_var.get() == "":
            self.clear_except(self.tb_var)
        else:
            try:
                tb = float(self.tb_var.get())
                self.bits_var.set(f"{tb * 8 * 1024 * 1024 * 1024 * 1024:.2f}")
                self.bytes_var.set(f"{tb * 1024 * 1024 * 1024 * 1024:.2f}")
                self.kb_var.set(f"{tb * 1024 * 1024 * 1024:.2f}")
                self.mb_var.set(f"{tb * 1024 * 1024:.2f}")
                self.gb_var.set(f"{tb * 1024:.2f}")
            except ValueError:
                pass
        self.updating = False


class WeightConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Weight Converter")
        self.window.geometry("250x250")
        self.updating = False

        self.microgram_var = tk.StringVar()
        self.microgram_var.trace_add("write", self.convert_from_microgram)
        microgram_entry = tk.Entry(self.window, textvariable=self.microgram_var)
        microgram_entry.place(x=100, y=10)

        microgram_label = tk.Label(self.window, text="Microgram")
        microgram_label.place(x=10, y=10)

        self.milligram_var = tk.StringVar()
        self.milligram_var.trace_add("write", self.convert_from_milligram)
        milligram_entry = tk.Entry(self.window, textvariable=self.milligram_var)
        milligram_entry.place(x=100, y=40)

        milligram_label = tk.Label(self.window, text="Milligram")
        milligram_label.place(x=10, y=40)

        self.gram_var = tk.StringVar()
        self.gram_var.trace_add("write", self.convert_from_gram)
        gram_entry = tk.Entry(self.window, textvariable=self.gram_var)
        gram_entry.place(x=100, y=70)

        gram_label = tk.Label(self.window, text="Gram")
        gram_label.place(x=10, y=70)

        self.kilogram_var = tk.StringVar()
        self.kilogram_var.trace_add("write", self.convert_from_kilogram)
        kilogram_entry = tk.Entry(self.window, textvariable=self.kilogram_var)
        kilogram_entry.place(x=100, y=100)

        kilogram_label = tk.Label(self.window, text="Kilogram")
        kilogram_label.place(x=10, y=100)

        self.metric_ton_var = tk.StringVar()
        self.metric_ton_var.trace_add("write", self.convert_from_metric_ton)
        metric_ton_entry = tk.Entry(self.window, textvariable=self.metric_ton_var)
        metric_ton_entry.place(x=100, y=130)

        metric_ton_label = tk.Label(self.window, text="Metric Ton")
        metric_ton_label.place(x=10, y=130)

    def clear_except(self, field_to_keep):
        fields = [
            self.microgram_var,
            self.milligram_var,
            self.gram_var,
            self.kilogram_var,
            self.metric_ton_var,
        ]
        for field in fields:
            if field is not field_to_keep:
                field.set("")

    def convert_from_microgram(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.microgram_var.get() == "":
            self.clear_except(self.microgram_var)
        else:
            try:
                microgram = float(self.microgram_var.get())
                self.milligram_var.set(f"{microgram / 1000:.4f}")
                self.gram_var.set(f"{microgram / 1000000:.6f}")
                self.kilogram_var.set(f"{microgram / 1000000000:.8f}")
                self.metric_ton_var.set(f"{microgram / 1000000000000:.10f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_milligram(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.milligram_var.get() == "":
            self.clear_except(self.milligram_var)
        else:
            try:
                milligram = float(self.milligram_var.get())
                self.microgram_var.set(f"{milligram * 1000:.2f}")
                self.gram_var.set(f"{milligram / 1000:.4f}")
                self.kilogram_var.set(f"{milligram / 1000000:.6f}")
                self.metric_ton_var.set(f"{milligram / 1000000000:.10f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_gram(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.gram_var.get() == "":
            self.clear_except(self.gram_var)
        else:
            try:
                gram = float(self.gram_var.get())
                self.microgram_var.set(f"{gram * 1000000:.2f}")
                self.milligram_var.set(f"{gram * 1000:.2f}")
                self.kilogram_var.set(f"{gram / 1000:.4f}")
                self.metric_ton_var.set(f"{gram / 1000000:.6f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_kilogram(self,*args):
        if self.updating:
            return
        self.updating = True

        if self.kilogram_var.get() == "":
            self.clear_except(self.kilogram_var)
        else:
            try:
                kilogram = float(self.kilogram_var.get())
                self.microgram_var.set(f"{kilogram * 1000000000:.2f}")
                self.milligram_var.set(f"{kilogram * 1000000:.2f}")
                self.gram_var.set(f"{kilogram * 1000:.2f}")
                self.metric_ton_var.set(f"{kilogram / 1000:.4f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_metric_ton(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.metric_ton_var.get() == "":
            self.clear_except(self.metric_ton_var)
        else:
            try:
                metric_ton = float(self.metric_ton_var.get())
                self.microgram_var.set(f"{metric_ton * 1000000000000:.2f}")
                self.milligram_var.set(f"{metric_ton * 1000000000:.2f}")
                self.gram_var.set(f"{metric_ton * 1000000:.2f}")
                self.kilogram_var.set(f"{metric_ton * 1000:.2f}")
            except ValueError:
                pass
        self.updating = False


# Not Finished
class SpeedConverter:
    ...

# Not Finished
class VolumeConverter:
    ...

# Not Finished
class MainMenu:
    def __init__(self, window):
        # Widgets
        self.window = window
        self.window.title("Main Menu")
        self.window.geometry("750x500")
        self.window.configure(bg="blue") ; self.window.resizable(False, False)
        
        global my_font
        my_font = Font(family="Verdana", size=10)

        # Get the directory of the script
        bg_image_path = get_image_path('menu2.png')

        # Load the image
        self.bg_image = PhotoImage(file=bg_image_path)
        self.window.geometry(f"{self.bg_image.width()}x{self.bg_image.height()}")

        # Create a canvas and Add the image to the canvas                                               # Remember
        bg_canvas = tk.Canvas(self.window, width=self.bg_image.width(), height=self.bg_image.height(), highlightthickness=0)
        bg_canvas.pack(fill="both", expand=True)
        bg_canvas.create_image(0, 0, image=self.bg_image, anchor="nw")


        # Set window to None
        self.length_converter_window = None
        self.time_converter_window = None
        self.temperature_converter_window = None
        self.data_converter_window = None
        self.weight_converter_window = None

        # Length Converter Button
        length_image_path = get_image_path('length2.png')
        self.length_image = PhotoImage(file=length_image_path)

        length_converter_button = tk.Button(
            self.window,
            command=self.open_length_converter,  
            compound="center",
            image = self.length_image,
            bd=0,
        )
        length_converter_button.place(x=57, y=150, width=100, height=50)

        # Time Converter Button
        time_image_path = get_image_path('time.png')
        self.time_image = PhotoImage(file=time_image_path)
        time_converter_button = tk.Button(
            self.window, 
            command=self.open_time_converter,
            compound="center",
            image = self.time_image,
            bd=0,
        )
        time_converter_button.place(x=235, y=150, width=100, height=50)

        # Temperature Converter Button
        temperature_image_path = get_image_path('temp.png')
        self.temperature_image = PhotoImage(file=temperature_image_path)
        temperature_converter_button = tk.Button(
            self.window,
            command=self.open_temperature_converter,
            compound="center",
            image = self.temperature_image,
            bd=0,
        )
        temperature_converter_button.place(x=147, y=310, width=100, height=50)

        # Data Converter Button
        data_image_path = get_image_path('data.png')
        self.data_image = PhotoImage(file=data_image_path)
        data_converter_button = tk.Button(
            self.window, 
            command=self.open_data_converter,
            compound="center",
            image = self.data_image,
            bd=0,
        )
        data_converter_button.place(x=515, y=310, width=100, height=50)

        # Weight Converter Button
        weight_image_path = get_image_path('weight.png')
        self.weight_image = PhotoImage(file=weight_image_path)
        weight_converter_button = tk.Button(
            self.window,
            command=self.open_weight_converter,
            compound="center",
            image = self.weight_image,
            bd=0,
        )
        weight_converter_button.place(x=415, y=150, width=100, height=50)

        # Speed Converter Button
        speed_image_path = get_image_path('speed.png')
        self.speed_image = PhotoImage(file=speed_image_path)
        speed_converter_button = tk.Button(
            self.window,
            command=self.open_speed_converter,
            compound="center",
            image = self.speed_image,
            bd=0,
        )
        speed_converter_button.place(x=595, y=150, width=100, height=50)

        # Volume Converter Button
        volume_image_path = get_image_path('volume.png')
        self.volume_image = PhotoImage(file=volume_image_path)
        volume_converter_button = tk.Button(
            self.window,
            command=self.open_volume_converter,
            compound="center",
            image = self.volume_image,
            bd=0,
        )
        volume_converter_button.place(x=330, y=310, width=100, height=50)


    # Functions
    def open_length_converter(self):
        if not self.length_converter_window:
            self.length_converter_window = tk.Toplevel(self.window)
            self.length_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_length_converter)
            LengthConverter(self.length_converter_window)
        else:
            self.length_converter_window.deiconify()

    def on_closing_length_converter(self):
        self.length_converter_window.destroy()
        self.length_converter_window = None

    def open_time_converter(self):
        if not self.time_converter_window:
            self.time_converter_window = tk.Toplevel(self.window)
            self.time_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_time_converter)
            TimeConverter(self.time_converter_window)
        else:
            #The deiconify method is used to bring the window to the front if it is already open.
            self.time_converter_window.deiconify()

    def on_closing_time_converter(self):
        self.time_converter_window.destroy()
        self.time_converter_window = None

    def open_temperature_converter(self):
        if not self.temperature_converter_window:
            self.temperature_converter_window = tk.Toplevel(self.window)
            self.temperature_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_temperature_converter)
            TemperatureConverter(self.temperature_converter_window)
        else:
            self.temperature_converter_window.deiconify()

    def on_closing_temperature_converter(self):
        self.temperature_converter_window.destroy()
        self.temperature_converter_window = None

    def open_data_converter(self):
        if not self.data_converter_window:
            self.data_converter_window = tk.Toplevel(self.window)
            self.data_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_data_converter)
            DataConverter(self.data_converter_window)
        else:
            self.data_converter_window.deiconify()

    def on_closing_data_converter(self):
        self.data_converter_window.destroy()
        self.data_converter_window = None

    def open_weight_converter(self):
        if not self.weight_converter_window:
            self.weight_converter_window = tk.Toplevel(self.window)
            self.weight_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_weight_convert)
            WeightConverter(self.weight_converter_window)
        else:
            self.weight_converter_window.deiconify()

    def on_closing_weight_convert(self):
        self.weight_converter_window.destroy()
        self.weight_converter_window = None

    # To be coded...
    def open_speed_converter(self):
        pass

    def on_closing_speed_converter(self):
        pass

    def open_volume_converter(self):
        pass

    def on_closing_volume_converter(self):
        pass


# Run the application
window = tk.Tk()
MainMenu(window)
window.mainloop()

