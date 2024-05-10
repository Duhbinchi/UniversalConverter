# Group 7 - Alpha Version
"""
Guide:
# Create facts button
# Define fact function
# Add the function to trace using lambda
# define clear function

- first version is in DataConverter class
"""

import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from tkinter.font import Font
import os
from PIL import Image, ImageTk


# Get the directory of the images
def get_image_path(image_name):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(script_dir, 'photos', image_name)
    return image_path


class LengthConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Length Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)

        # Load the background image
        self.bg_img = PhotoImage(file=get_image_path('yellow2.png'))

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)

        # Create a canvas
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.length_facts)
        self.fact_text = self.canvas.create_text(10, 340, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        # Set the updating flag to False to prevent the convert_from_* methods from running when the text variables are updated
        self.updating = False

        # Create the widgets
        self.meters_var = tk.StringVar()
        self.meters_var.trace_add("write", lambda *args: (self.convert_from_meters(), self.clear_fact(), self.check_fact()))
        meter_entry = tk.Entry(self.window, textvariable=self.meters_var, font=my_font)
        meter_entry.place(x=123, y=40, width=135)
        # Use create_text() instead of a Label
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Meters  \u33A1", anchor="nw", fill="#FFFFFF", font=my_font)

        # Repeat for the other variables
        self.feet_var = tk.StringVar()
        self.feet_var.trace_add("write", lambda *args: (self.convert_from_feet(), self.clear_fact(), self.check_fact()))
        feet_entry = tk.Entry(self.window, textvariable=self.feet_var, font=my_font)
        feet_entry.place(x=123, y=100, width=135)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Feet \u00B2", anchor="nw", fill="#FFFFFF", font=my_font)

        self.inches_var = tk.StringVar()
        self.inches_var.trace_add("write", lambda *args: (self.convert_from_inches(), self.clear_fact(), self.check_fact()))
        inches_entry = tk.Entry(self.window, textvariable=self.inches_var, font=my_font)
        inches_entry.place(x=123, y=70, width=135)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Inches \u2033", anchor="nw", fill="#FFFFFF", font=my_font)

        self.cm_var = tk.StringVar()
        self.cm_var.trace_add("write", lambda *args: (self.convert_from_cm(), self.clear_fact(), self.check_fact()))
        cm_entry = tk.Entry(self.window, textvariable=self.cm_var, font=my_font)
        cm_entry.place(x=123, y=10, width=135)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Centimeters \u339D", anchor="nw", fill="#FFFFFF", font=my_font)

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
    
    def length_facts(self, event):
        try:
            meters = float(self.meters_var.get())
            feet = float(self.feet_var.get())
            inches = float(self.inches_var.get())
            cm = float(self.cm_var.get())

        except ValueError:
            return

        if meters >= 9289000:
            self.canvas.itemconfig(self.fact_text, text="Did you know? The Trans-Siberian Railway\nis the world's longest train ride, crossing\nEurasia at a whopping 9289000 meters!")

        elif feet >= 40230:
            self.canvas.itemconfig(self.fact_text, text="Did you know the Kola Superdeep Borehole\nin Russia is the deepest man-made hole, reaching\nabout 12,262 meters (40,230 feet) below\nthe Earth's surface?")

        elif inches >= 394 or cm >= 12000:
            self.canvas.itemconfig(self.fact_text, text="Did you know the title for longest animal\ngoes to a giant siphonophore, a colonial\ncreature! Clocking in at over 120\nmeters (394 feet)")
    
    def check_fact(self, *args):
        try:
            meters = float(self.meters_var.get())
            feet = float(self.feet_var.get())
            inches = float(self.inches_var.get())
            cm = float(self.cm_var.get())
        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return
    
        if meters >= 9289000 or feet >= 40230 or inches >= 394 or cm >= 12000:
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)
        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
    
        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

class TimeConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Time Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)
        self.updating = False
        
        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)

        self.bg_img = PhotoImage(file=get_image_path('yellow3.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.time_facts)
        self.fact_text = self.canvas.create_text(10, 340, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        self.seconds_var = tk.StringVar()
        self.seconds_var.trace_add("write", lambda *args: (self.convert_from_seconds(), self.clear_fact(), self.check_fact()))
        seconds_entry = tk.Entry(self.window, textvariable=self.seconds_var, width=22, font=my_font)
        seconds_entry.place(x=100, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Seconds", anchor="nw", fill="#FFFFFF", font=my_font)

        self.minutes_var = tk.StringVar()
        self.minutes_var.trace_add("write", lambda *args: (self.convert_from_minutes(), self.clear_fact(), self.check_fact()))
        minutes_entry = tk.Entry(self.window, textvariable=self.minutes_var, width=22, font=my_font)
        minutes_entry.place(x=100, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Minutes", anchor="nw", fill="#FFFFFF", font=my_font)

        self.hours_var = tk.StringVar()
        self.hours_var.trace_add("write", lambda *args: (self.convert_from_hours(), self.clear_fact(), self.check_fact()))
        hours_entry = tk.Entry(self.window, textvariable=self.hours_var, width=22, font=my_font)
        hours_entry.place(x=100, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Hours", anchor="nw", fill="#FFFFFF", font=my_font)

        self.days_var = tk.StringVar()
        self.days_var.trace_add("write", lambda *args: (self.convert_from_days(), self.clear_fact(), self.check_fact()))
        days_entry = tk.Entry(self.window, textvariable=self.days_var, width=22, font=my_font)
        days_entry.place(x=100, y=100)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Days", anchor="nw", fill="#FFFFFF", font=my_font)

        self.weeks_var = tk.StringVar()
        self.weeks_var.trace_add("write", lambda *args: (self.convert_from_weeks(), self.clear_fact(), self.check_fact()))
        weeks_entry = tk.Entry(self.window, textvariable=self.weeks_var, width=22, font=my_font)
        weeks_entry.place(x=100, y=130)
        self.canvas.create_text(10, 130, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 130, text="Weeks", anchor="nw", fill="#FFFFFF", font=my_font)

        self.months_var = tk.StringVar()
        self.months_var.trace_add("write", lambda *args: (self.convert_from_months(), self.clear_fact(), self.check_fact()))
        months_entry = tk.Entry(self.window, textvariable=self.months_var, width=22, font=my_font)
        months_entry.place(x=100, y=160)
        self.canvas.create_text(10, 160, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 160, text="Months", anchor="nw", fill="#FFFFFF", font=my_font)

        self.years_var = tk.StringVar()
        self.years_var.trace_add("write", lambda *args: (self.convert_from_years(), self.clear_fact(), self.check_fact()))
        years_entry = tk.Entry(self.window, textvariable=self.years_var, width=22, font=my_font)
        years_entry.place(x=100, y=190)
        self.canvas.create_text(10, 190, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 190, text="Years", anchor="nw", fill="#FFFFFF", font=my_font)

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

    def time_facts(self, event):
        try:
            seconds = float(self.seconds_var.get())
            minutes = float(self.minutes_var.get())
            hours = float(self.hours_var.get())
            days = float(self.days_var.get())
        except ValueError:
            return
        
        if minutes in range(4,7):
            self.canvas.itemconfig(self.fact_text, text="Did you know? Bleeding to death can\noccur in as little as 5 minutes if\nthe bleeding isn't stopped.")

        if hours in range (8,12):
            self.canvas.itemconfig(self.fact_text, text="Did you know the current record\nholder for the longest plank ever is a\nman named Josef Šálek from the\nCzech Republic? He achieved an incredible\nfeat by holding a plank for a\nmind-blowing 9 hours, 38 minutes,\nand 47 seconds!")

        if days in range(80, 101):
            self.canvas.itemconfig(self.fact_text, text="Did you know? Dr. Joseph Dituri,\nnicknamed 'Dr. Deep Sea', braved the\nunderwater world for a\nrecord-breaking 100 days!")


    def check_fact(self, *args):
        try:
            seconds = float(self.seconds_var.get())
            minutes = float(self.minutes_var.get())
            hours = float(self.hours_var.get())
            days = float(self.days_var.get())

        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return
        
        if seconds in range(4,7) or hours in range(8,12) or days in range(80, 101):
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)

        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
    
        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

class TemperatureConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Temperature Converter")
        self.window.geometry("265x508+858+60")
        self.updating = False
        self.window.resizable(False, True)

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)

        self.bg_img = PhotoImage(file=get_image_path('yellow3.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.temp_facts)
        self.fact_text = self.canvas.create_text(10, 340, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        # Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
        self.celsius_var = tk.StringVar()
        self.celsius_var.trace_add("write", lambda *args: (self.convert_from_celsius(), self.clear_fact(), self.check_fact())) 
        celsius_entry = tk.Entry(self.window, textvariable=self.celsius_var, width=19, font=my_font)
        celsius_entry.place(x=120, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Celsius \u00B0C", anchor="nw", fill="#FFFFFF", font=my_font)

        # Fahrenheit to Celsius: (°F − 32) x 5/9 = °C
        self.fahrenheit_var = tk.StringVar()
        self.fahrenheit_var.trace_add("write", lambda *args: (self.convert_from_fahrenheit(), self.clear_fact(), self.check_fact()))
        fahrenheit_entry = tk.Entry(self.window, textvariable=self.fahrenheit_var, width=19, font=my_font)
        fahrenheit_entry.place(x=120, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Fahrenheit \u00B0F", anchor="nw", fill="#FFFFFF", font=my_font)

        # Celsius to Kelvin: K = °C + 273.15
        self.kelvin_var = tk.StringVar()
        self.kelvin_var.trace_add("write", lambda *args: (self.convert_from_kelvin(), self.clear_fact(), self.check_fact()))
        kelvin_entry = tk.Entry(self.window, textvariable=self.kelvin_var, width=19, font=my_font)
        kelvin_entry.place(x=120, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Kelvin \u212A", anchor="nw", fill="#FFFFFF", font=my_font)

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

    def temp_facts(self, event):
        try:
            celsius = float(self.celsius_var.get())
            fahrenheit = float(self.fahrenheit_var.get())
            kelvin = float(self.kelvin_var.get())

        except ValueError:
            return
        
        if celsius in range(1,11):
            self.canvas.itemconfig(self.fact_text, text="Did you know? The all-time\nnational coldest temperature record was\n6.3°C registered in Baguio City\non Jan. 18, 1961")

        elif celsius in range(38,50):
            self.canvas.itemconfig(self.fact_text, text="Did you know? The heat\nindex in Binan on April\n28 was 48 degrees Celsius!\nSo hot!")

        elif kelvin >= 1000000:
            self.canvas.itemconfig(self.fact_text, text="Did you know? The plasma\nin a nuclear explosion can\nreach temperatures exceeding several million")
    
    def check_fact(self, *args):
        try:
            celsius = float(self.celsius_var.get())
            fahrenheit = float(self.fahrenheit_var.get())
            kelvin = float(self.kelvin_var.get())

        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return
        
        if celsius in range(1,11) or celsius in range(38,50) or kelvin >= 1000000:
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)

        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
    
        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

class DataConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Data Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)
        self.updating = False

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)

        self.bg_img = PhotoImage(file=get_image_path('yellow2.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.data_facts)
        self.fact_text = self.canvas.create_text(10, 360, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        # Bits
        self.bits_var = tk.StringVar()
        self.bits_var.trace_add("write", lambda *args: (self.convert_from_bits(), self.clear_fact(), self.check_fact()))
        bits_entry = tk.Entry(self.window, textvariable=self.bits_var, font=my_font, width = 17)
        bits_entry.place(x=135, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Bits \u00B5b", anchor="nw", fill="#FFFFFF", font=my_font)
        
        self.bytes_var = tk.StringVar()
        self.bytes_var.trace_add("write", lambda *args: (self.convert_from_bytes(), self.clear_fact(), self.check_fact()))
        bytes_entry = tk.Entry(self.window, textvariable=self.bytes_var, font=my_font, width = 17)
        bytes_entry.place(x=135, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Bytes \u00B5B", anchor="nw", fill="#FFFFFF", font=my_font)
        
        self.kb_var = tk.StringVar()
        self.kb_var.trace_add("write", lambda *args: (self.convert_from_kb(), self.clear_fact(), self.check_fact()))
        kb_entry = tk.Entry(self.window, textvariable=self.kb_var, font=my_font, width = 17)
        kb_entry.place(x=135, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Kilobytes \u00B5KB", anchor="nw", fill="#FFFFFF", font=my_font)
        
        self.mb_var = tk.StringVar()
        self.mb_var.trace_add("write", lambda *args: (self.convert_from_mb(), self.clear_fact(), self.check_fact()))
        mb_entry = tk.Entry(self.window, textvariable=self.mb_var, font=my_font, width = 17)
        mb_entry.place(x=135, y=100)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Megabytes \u00B5MB", anchor="nw", fill="#FFFFFF", font=my_font)
        
        self.gb_var = tk.StringVar()
        self.gb_var.trace_add("write", lambda *args: (self.convert_from_gb(), self.clear_fact(), self.check_fact()))
        gb_entry = tk.Entry(self.window, textvariable=self.gb_var, font=my_font, width = 17)
        gb_entry.place(x=135, y=130)
        self.canvas.create_text(10, 130, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 130, text="Gigabytes \u00B5GB", anchor="nw", fill="#FFFFFF", font=my_font)
        
        self.tb_var = tk.StringVar()
        self.tb_var.trace_add("write", lambda *args: (self.convert_from_tb(), self.clear_fact(), self.check_fact()))
        tb_entry = tk.Entry(self.window, textvariable=self.tb_var, font=my_font, width = 17)
        tb_entry.place(x=135, y=160)
        self.canvas.create_text(10, 160, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 160, text="Terabytes \u00B5TB", anchor="nw", fill="#FFFFFF", font=my_font)

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
                self.mb_var.set(f"{bits / 8 / 1024 / 1024:.8f}")
                self.gb_var.set(f"{bits / 8 / 1024 / 1024 / 1024:.10f}")
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
                self.gb_var.set(f"{bytes / 1024 / 1024 / 1024:.10f}")
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

    def data_facts(self, event):
        try:
            kb = float(self.kb_var.get())
            mb = float(self.mb_var.get())
            gb = float(self.gb_var.get())
        except ValueError:
            return

        if kb in range(0, 10):
            self.canvas.itemconfig(self.fact_text, text="Did you know? The program that sent NASA\nto the moon in 1960 was only 4 Kilobytes!")

        if mb in range (20, 30):
            self.canvas.itemconfig(self.fact_text, text="Did you know? Currently, if you download\nPython 3.9 the file size is around 25\nMegabytes!")

        if gb in range(2, 5):
            self.canvas.itemconfig(self.fact_text, text="The average smartphone user in the\nPhilippines consumes around 3 Gigabytes\nof mobile data per month!")

    def check_fact(self, *args):
        try:
            kb = float(self.kb_var.get())
            mb = float(self.mb_var.get())
            gb = float(self.gb_var.get())
        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return

        if kb in range(0, 11) or mb in range(20, 31) or gb in range(2, 6):
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)
        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)

        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

class WeightConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Weight Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)
        self.updating = False

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)
        self.bg_img = PhotoImage(file=get_image_path('yellow4.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.weight_facts)
        self.fact_text = self.canvas.create_text(10, 340, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        # Microgram
        self.microgram_var = tk.StringVar()
        self.microgram_var.trace_add("write", lambda *args: (self.convert_from_microgram(), self.clear_fact(), self.check_fact()))
        microgram_entry = tk.Entry(self.window, textvariable=self.microgram_var, font=my_font, width=18)
        microgram_entry.place(x=128, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Microgram \u03BCg", anchor="nw", fill="#FFFFFF", font=my_font)

        # Milligram
        self.milligram_var = tk.StringVar()
        self.milligram_var.trace_add("write", lambda *args: (self.convert_from_milligram(), self.clear_fact(), self.check_fact()))
        milligram_entry = tk.Entry(self.window, textvariable=self.milligram_var, font=my_font, width=18)
        milligram_entry.place(x=128, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Milligram \u00B5mg", anchor="nw", fill="#FFFFFF", font=my_font)

        # Gram
        self.gram_var = tk.StringVar()
        self.gram_var.trace_add("write", lambda *args: (self.convert_from_gram(), self.clear_fact(), self.check_fact()))
        gram_entry = tk.Entry(self.window, textvariable=self.gram_var, font=my_font, width=18)
        gram_entry.place(x=128, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Gram \u0067", anchor="nw", fill="#FFFFFF", font=my_font)

        # Kilogram
        self.kilogram_var = tk.StringVar()
        self.kilogram_var.trace_add("write", lambda *args: (self.convert_from_kilogram(), self.clear_fact(), self.check_fact()))
        kilogram_entry = tk.Entry(self.window, textvariable=self.kilogram_var, font=my_font, width=18)
        kilogram_entry.place(x=128, y=100)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Kilogram \u00B5kg", anchor="nw", fill="#FFFFFF", font=my_font)

        # Metric Ton
        self.metric_ton_var = tk.StringVar()
        self.metric_ton_var.trace_add("write", lambda *args: (self.convert_from_metric_ton(), self.clear_fact(), self.check_fact()))
        metric_ton_entry = tk.Entry(self.window, textvariable=self.metric_ton_var, font=my_font, width=18)
        metric_ton_entry.place(x=128, y=130)
        self.canvas.create_text(10, 130, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 130, text="Metric Ton \u2126", anchor="nw", fill="#FFFFFF", font=my_font)

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

    def weight_facts(self, event):
        try:
            microgram = float(self.microgram_var.get())
            milligram = float(self.milligram_var.get())
            gram = float(self.gram_var.get())
            kilogram = float(self.kilogram_var.get())
        except ValueError:
            return

        if kilogram in range(1,11):
            self.canvas.itemconfig(self.fact_text, text="Did you know one tree\ncan produce a 1.2 kg\nof oxygen :D")
        
        if kilogram in range(150_000, 200_000):
            self.canvas.itemconfig(self.fact_text, text="Did you know that the\nweight of a blue whale\ncan reach up to 200,000\nkilograms!")
        
        if gram in range(1300, 1500):
            self.canvas.itemconfig(self.fact_text, text="Did you know? The average weight of an\nadult human being is 1400\ngrams!")

    def check_fact(self, *args):
        try:
            microgram = float(self.microgram_var.get())
            milligram = float(self.milligram_var.get())
            gram = float(self.gram_var.get())
            kilogram = float(self.kilogram_var.get())
        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return

        if kilogram in range(1, 11) or kilogram in range(150_000, 200_000) or gram in range(1300, 1500):
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)
        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)

        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

# I show
class SpeedConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Speed Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)
        self.bg_img = PhotoImage(file=get_image_path('yellow2.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.speed_facts)
        self.fact_text = self.canvas.create_text(10, 330, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        self.updating = False

        # Miles per second
        self.mps_var = tk.StringVar()
        self.mps_var.trace_add("write", lambda *args: (self.convert_from_mps(), self.clear_fact(), self.check_fact()))
        mps_entry = tk.Entry(self.window, textvariable=self.mps_var, font=my_font, width=17)
        mps_entry.place(x=135, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Miles mi/s", anchor="nw", fill="#FFFFFF", font=my_font)

        # Kilometers per hour
        self.kph_var = tk.StringVar()
        self.kph_var.trace_add("write", lambda *args: (self.convert_from_kph(), self.clear_fact(), self.check_fact()))
        kph_entry = tk.Entry(self.window, textvariable=self.kph_var, font=my_font, width=17)
        kph_entry.place(x=135, y=100)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Kilometers km/h", anchor="nw", fill="#FFFFFF", font=my_font)

        # Miles per hour
        self.mph_var = tk.StringVar()
        self.mph_var.trace_add("write", lambda *args: (self.convert_from_mph(), self.clear_fact(), self.check_fact()))
        mph_entry = tk.Entry(self.window, textvariable=self.mph_var, font=my_font, width=17)
        mph_entry.place(x=135, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Miles mi/h", anchor="nw", fill="#FFFFFF", font=my_font)
        
        # Knots
        self.kts_var = tk.StringVar()
        self.kts_var.trace_add("write", lambda *args: (self.convert_from_kts(), self.clear_fact(), self.check_fact()))
        kts_entry = tk.Entry(self.window, textvariable=self.kts_var, font=my_font, width=17)
        kts_entry.place(x=135, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Knots kn", anchor="nw", fill="#FFFFFF", font=my_font)

        # Feet per second
        self.fps_var = tk.StringVar()
        self.fps_var.trace_add("write", lambda *args: (self.convert_from_fps(), self.clear_fact(), self.check_fact()))
        fps_entry = tk.Entry(self.window, textvariable=self.fps_var, font=my_font, width=17)
        fps_entry.place(x=135, y=130)
        self.canvas.create_text(10, 130, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 130, text="Feet ft/s", anchor="nw", fill="#FFFFFF", font=my_font)

        # Meter per second
        self.ms_var = tk.StringVar()
        self.ms_var.trace_add("write", lambda *args: (self.convert_from_ms(), self.clear_fact(), self.check_fact()))
        ms_entry = tk.Entry(self.window, textvariable=self.ms_var, font=my_font, width=17)
        ms_entry.place(x=135, y=160)
        self.canvas.create_text(10,160, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 160, text="Meter m/s", anchor="nw", fill="#FFFFFF", font=my_font)

        
    def clear_except(self, field_to_keep):
        fields = [self.mps_var, self.kph_var, self.mph_var, self.kts_var, self.fps_var, self.ms_var]
        for field in fields:
            if field is not field_to_keep:
                field.set("")

    # Converting from other units
    def convert_from_mps(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.mps_var.get() == "":
            self.clear_except(self.mps_var)
        else:
            try:
                mps = float(self.mps_var.get())
                self.kph_var.set(f"{mps * 3.6:.2f}")
                self.mph_var.set(f"{mps * 2.237:.2f}")
                self.kts_var.set(f"{mps * 1.944:.2f}")
                self.fps_var.set(f"{mps * 3.28084:.2f}")
                self.ms_var.set(f"{mps * 1609.344 :.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_kph(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.kph_var.get() == "":
            self.clear_except(self.kph_var)
        else:
            try:
                kph = float(self.kph_var.get())
                self.mps_var.set(f"{kph / 3.6:.2f}")
                self.mph_var.set(f"{kph * 0.621371:.2f}")
                self.kts_var.set(f"{kph * 0.539957:.2f}")
                self.fps_var.set(f"{kph * 3.28084 / 1.60934:.2f}")
                self.ms_var.set(f"{kph * 0.2777777778:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_mph(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.mph_var.get() == "":
            self.clear_except(self.mph_var)
        else:
            try:
                mph = float(self.mph_var.get())
                self.mps_var.set(f"{mph * 0.44704:.2f}")
                self.kph_var.set(f"{mph * 1.60934:.2f}")
                self.kts_var.set(f"{mph * 0.868976:.2f}")
                self.fps_var.set(f"{mph * 2.237:.2f}")
                self.ms_var.set(f"{mph * 0.44704:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_kts(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.kts_var.get() == "":
            self.clear_except(self.kts_var)
        else:
            try:
                kts = float(self.kts_var.get())
                self.mps_var.set(f"{kts * 1.68781:.2f}")
                self.kph_var.set(f"{kts * 1.852:.2f}")
                self.mph_var.set(f"{kts * 1.15078:.2f}")
                self.fps_var.set(f"{kts * 3.28084 * 1.68781:.2f}")
                self.ms_var.set(f"{kts * 0.5144444444:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_fps(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.fps_var.get() == "":
            self.clear_except(self.fps_var)
        else:
            try:
                fps = float(self.fps_var.get())
                self.mps_var.set(f"{fps * 0.3048:.2f}")
                self.kph_var.set(f"{fps * 0.44704:.2f}")
                self.mph_var.set(f"{fps * 0.681818:.2f}")
                self.kts_var.set(f"{fps * 0.592484:.2f}")
                self.ms_var.set(f"{fps * 0.3048:.2f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_ms(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.ms_var.get() == "":
            self.clear_except(self.ms_var)
        else:
            try:
                ms = float(self.ms_var.get())
                self.mps_var.set(f"{ms * 0.000621371:.2f}")
                self.kph_var.set(f"{ms * 3.6:.2f}")
                self.mph_var.set(f"{ms * 2.2369362921:.2f}")
                self.kts_var.set(f"{ms * 1.9438444924:.2f}")
                self.fps_var.set(f"{ms * 3.280839895:.2f}")
            except ValueError:
                pass
        self.updating = False

    def speed_facts(self, event):
        try:
            kph = float(self.kph_var.get())
            mph = float(self.mph_var.get())
        except ValueError:
            return

        if kph in range(350, 400):
            self.canvas.itemconfig(self.fact_text, text="Did you know the peregrine\nfalcon is Earth's fastest animal?\nIt can hit speeds over\n240 mph (386 km/h) when\ndiving for prey")

        if mph in range(16_500, 17_500):
            self.canvas.itemconfig(self.fact_text, text="Did you know spacecraft reentering\nEarth's atmosphere from space face\nincredible speeds? The Space Shuttle,\nfor instance, could reach over\n17,000 miles per hour (27,000\nkilometers per hour).")

        if kph in range(480, 500):
            self.canvas.itemconfig(self.fact_text, text="Did you know kamikaze pilots\ndived at speeds over 300\nmph during World War II,\naiming to maximize crash impact?")

    def check_fact(self, *args):
        try:
            kph = float(self.kph_var.get())
            mph = float(self.mph_var.get())
        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return

        if kph in range(350, 400) or mph in range(16_500, 17_500) or kph in range(480, 500):
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)
        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)

        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

class VolumeConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Volume Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)
        self.bg_image = PhotoImage(file=get_image_path('yellow4.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor='nw')

        self.updating = False

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.volume_facts)
        self.fact_text = self.canvas.create_text(10, 330, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)


        # Milliliters
        self.ml_var = tk.StringVar()
        self.ml_var.trace_add("write", lambda *args: (self.convert_from_ml(), self.clear_fact(), self.check_fact()))
        ml_entry = tk.Entry(self.window, textvariable=self.ml_var, font=my_font, width=19)
        ml_entry.place(x=120, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Milliliters \u03BCl", anchor="nw", fill="#FFFFFF", font=my_font)

        # Centiliters
        self.cl_var = tk.StringVar()
        self.cl_var.trace_add("write", lambda *args: (self.convert_from_cl(), self.clear_fact(), self.check_fact()))
        cl_entry = tk.Entry(self.window, textvariable=self.cl_var, font=my_font, width=19)
        cl_entry.place(x=120, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Centiliters \u00B5cl", anchor="nw", fill="#FFFFFF", font=my_font)

        # Deciliters
        self.dl_var = tk.StringVar()
        self.dl_var.trace_add("write", lambda *args: (self.convert_from_dl(), self.clear_fact(), self.check_fact()))
        dl_entry = tk.Entry(self.window, textvariable=self.dl_var, font=my_font, width=19)
        dl_entry.place(x=120, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Deciliters \u00B7dl", anchor="nw", fill="#FFFFFF", font=my_font)

        # Liters
        self.l_var = tk.StringVar()
        self.l_var.trace_add("write", lambda *args: (self.convert_from_l(), self.clear_fact(), self.check_fact()))
        l_entry = tk.Entry(self.window, textvariable=self.l_var, font=my_font, width=19)
        l_entry.place(x=120, y=100)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Liters \u004C", anchor="nw", fill="#FFFFFF", font=my_font)

        # Kiloliters
        self.kl_var = tk.StringVar()
        self.kl_var.trace_add("write", lambda *args: (self.convert_from_kl(), self.clear_fact(), self.check_fact()))
        kl_entry = tk.Entry(self.window, textvariable=self.kl_var, font=my_font, width=19)
        kl_entry.place(x=120, y=130)
        self.canvas.create_text(10, 130, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 130, text="Kiloliters k" + "\u0332" + "L", anchor="nw", fill="#FFFFFF", font=my_font)


        self.updating = False

    def clear_except(self, field_to_keep):
        fields = [self.ml_var, self.cl_var, self.dl_var, self.l_var, self.kl_var]
        for field in fields:
            if field is not field_to_keep:
                field.set("")

    def convert_from_ml(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.ml_var.get() == "":
            self.clear_except(self.ml_var)
        else:
            try:
                ml = float(self.ml_var.get())
                self.cl_var.set(f"{ml / 10:.2f}")
                self.dl_var.set(f"{ml / 100:.2f}")
                self.l_var.set(f"{ml / 1000:.4f}")
                self.kl_var.set(f"{ml / 1000000:.6f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_cl(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.cl_var.get() == "":
            self.clear_except(self.cl_var)
        else:
            try:
                cl = float(self.cl_var.get())
                self.ml_var.set(f"{cl * 10:.2f}")
                self.dl_var.set(f"{cl / 10:.2f}")
                self.l_var.set(f"{cl / 100:.2f}")
                self.kl_var.set(f"{cl / 10000:.4f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_dl(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.dl_var.get() == "":
            self.clear_except(self.dl_var)
        else:
            try:
                dl = float(self.dl_var.get())
                self.ml_var.set(f"{dl * 100:.2f}")
                self.cl_var.set(f"{dl * 10:.2f}")
                self.l_var.set(f"{dl / 10:.2f}")
                self.kl_var.set(f"{dl / 100000:.6f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_l(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.l_var.get() == "":
            self.clear_except(self.l_var)
        else:
            try:
                l = float(self.l_var.get())
                self.ml_var.set(f"{l * 1000:.2f}")
                self.cl_var.set(f"{l * 100:.2f}")
                self.dl_var.set(f"{l * 10:.2f}")
                self.kl_var.set(f"{l / 1000:.4f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_kl(self, *args):
        if self.updating:
            return
        self.updating = True
        if self.kl_var.get() == "":
            self.clear_except(self.kl_var)
        else:
            try:
                kl = float(self.kl_var.get())
                self.ml_var.set(f"{kl * 1000000:.2f}")
                self.cl_var.set(f"{kl * 100000:.2f}")
                self.dl_var.set(f"{kl * 10000:.2f}")
                self.l_var.set(f"{kl * 1000:.2f}")
            except ValueError:
                pass
        self.updating = False


    def volume_facts(self, event):
        try:
            ml = float(self.ml_var.get())
            cl = float(self.cl_var.get())
            dl = float(self.dl_var.get())
            l = float(self.l_var.get())
            kl = float(self.kl_var.get())
        except ValueError:
            return

        if kl > 1_000_000 and kl < 30_000_000:
            self.canvas.itemconfig(self.fact_text, text="Did you know that some\nvolcanoes, like Yellowstone Caldera in\nthe US, can hold about\n15 million kiloliters of magma\nin their chambers?")

        elif kl > 30_000_000:
            self.canvas.itemconfig(self.fact_text, text="Did you know that the\nThree Gorges Dam in China,\nthe world's largest hydroelectric dam\nby capacity, holds an astonishing\n39.3 million kiloliters of water\nin its reservoir?")

        if l in range(100, 200):
            self.canvas.itemconfig(self.fact_text, text="Did you know that camels\ncan store the most water\nin their bloodstream among mammals?\nThey're capable of drinking up\nto 118 liters per day,\nmaking them exceptionally adapted to\nsurvive in arid environments!")
    
    def check_fact(self, *args):
        try:
            ml = float(self.ml_var.get())
            cl = float(self.cl_var.get())
            dl = float(self.dl_var.get())
            l = float(self.l_var.get())
            kl = float(self.kl_var.get())
        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)
            self.canvas.update()
            return

        if kl > 1_000_000 and kl < 30_000_000 or kl > 30_000_000 or l in range(100, 200):
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)
        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)

        self.canvas.update()

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")

class VoltageConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Voltage Converter")
        self.window.geometry("265x508+858+60")
        self.window.resizable(False, True)
        self.updating = False

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)
        self.bg_img = PhotoImage(file=get_image_path('yellow3.png'))
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        # Fact Button
        self.image = Image.open(get_image_path('venti_sleep.png'))
        self.venti = ImageTk.PhotoImage(self.image)
        self.fact_button = self.canvas.create_image(10, 400, image=self.venti, anchor='nw')
        self.canvas.tag_bind(self.fact_button, "<Button-1>", self.voltage_facts)
        self.fact_text = self.canvas.create_text(10, 360, text="", anchor="nw", fill="#FFFFFF", font=my_font_s)
        self.idea_image = Image.open(get_image_path('venti_idea.png'))
        self.venti_idea = ImageTk.PhotoImage(self.idea_image)

        # Nanovolts
        self.nanov_var = tk.StringVar()
        self.nanov_var.trace_add("write", lambda *args: (self.convert_from_nanov(), self.clear_fact(), self.check_fact()))
        nanovolts_entry = tk.Entry(self.window, textvariable=self.nanov_var, font=my_font, width=18)
        nanovolts_entry.place(x=126, y=10)
        self.canvas.create_text(10, 10, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 10, text="Nanovolts nV", anchor="nw", fill="#FFFFFF", font=my_font)

        # Microvolts
        self.microv_var = tk.StringVar()
        self.microv_var.trace_add("write", lambda *args: (self.convert_from_microv(), self.clear_fact(), self.check_fact()))
        microvolts_entry = tk.Entry(self.window, textvariable=self.microv_var, font=my_font, width=18)
        microvolts_entry.place(x=126, y=40)
        self.canvas.create_text(10, 40, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 40, text="Microvolts \u03BCV", anchor="nw", fill="#FFFFFF", font=my_font)

        # Millivolts
        self.milliv_var = tk.StringVar()
        self.milliv_var.trace_add("write", lambda *args: (self.convert_from_milliv(args), self.clear_fact(), self.check_fact()))
        millivolts_entry = tk.Entry(self.window, textvariable=self.milliv_var, font=my_font, width=18)
        millivolts_entry.place(x=126, y=70)
        self.canvas.create_text(10, 70, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 70, text="Millivolts mV", anchor="nw", fill="#FFFFFF", font=my_font)

        # Volts
        self.volts_var = tk.StringVar()
        self.volts_var.trace_add("write", lambda *args: (self.convert_from_volts(args), self.clear_fact(), self.check_fact()))
        volts_entry = tk.Entry(self.window, textvariable=self.volts_var, font=my_font, width=18)
        volts_entry.place(x=126, y=100)
        self.canvas.create_text(10, 100, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 100, text="Volts V", anchor="nw", fill="#FFFFFF", font=my_font)

        # Kilovolts
        self.kilov_var = tk.StringVar()
        self.kilov_var.trace_add("write", lambda *args: (self.convert_from_kilov(), self.clear_fact(), self.check_fact()))
        kilovolts_entry = tk.Entry(self.window, textvariable=self.kilov_var, font=my_font, width=18)
        kilovolts_entry.place(x=126, y=130)
        self.canvas.create_text(10, 130, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 130, text="Kilovolts kV", anchor="nw", fill="#FFFFFF", font=my_font)

        # Megavolts
        self.megav_var = tk.StringVar()
        self.megav_var.trace_add("write", lambda *args: (self.convert_from_megav(), self.clear_fact(), self.check_fact()))
        megavolts_entry = tk.Entry(self.window, textvariable=self.megav_var, font=my_font, width=18)
        megavolts_entry.place(x=126, y=160)
        self.canvas.create_text(10, 160, text="\u27A2", anchor="nw", fill="#faff00", font=my_font)
        self.canvas.create_text(30, 160, text="Megavolts MV", anchor="nw", fill="#FFFFFF", font=my_font)

        
    def clear_except(self, field_to_keep):
        fields = [
            self.nanov_var,
            self.microv_var,
            self.milliv_var,
            self.volts_var,
            self.kilov_var,
            self.megav_var,
        ]

        for field in fields:
            if field is not field_to_keep:
                field.set("")

    def convert_from_nanov(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.nanov_var.get() == "":
            self.clear_except(self.nanov_var)
        else:
            try:
                nanov = float(self.nanov_var.get())
                self.microv_var.set(f"{nanov * 0.0001:.4f}")
                self.milliv_var.set(f"{nanov * 0.0000010:.6f}")
                self.volts_var.set(f"{nanov * 0.0000000010:.8f}")
                self.kilov_var.set(f"{nanov * 0.0000000000010:.10f}")
                self.megav_var.set(f"{nanov * 0.0000000000000010:.12f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_microv(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.microv_var.get() == "":
            self.clear_except(self.microv_var)
        else:
            try:
                microv = float(self.microv_var.get())
                self.nanov_var.set(f"{microv * 1000:.2f}")
                self.milliv_var.set(f"{microv * 0.001:.4f}")
                self.volts_var.set(f"{microv * 0.0000010:.6f}")
                self.kilov_var.set(f"{microv * 0.0000000010:.8f}")
                self.megav_var.set(f"{microv * 0.0000000000010:.10f}")

            except ValueError:
                pass
        self.updating = False

    def convert_from_milliv(self, *args):
        if self.updating:
            return
        self.updating = True

        if self.milliv_var.get() == "":
            self.clear_except(self.milliv_var)
        else:
            try:
                milliv = float(self.milliv_var.get())
                self.nanov_var.set(f"{milliv * 1000000:.2f}")
                self.microv_var.set(f"{milliv * 1000:.2f}")
                self.volts_var.set(f"{milliv * 0.001:.4f}")
                self.kilov_var.set(f"{milliv * 0.0000010:.6f}")
                self.megav_var.set(f"{milliv * 0.0000000010:.8f}")

            except ValueError:
                pass
        self.updating = False

    def convert_from_volts(self,*args):
        if self.updating:
            return
        self.updating = True

        if self.volts_var.get() == "":
            self.clear_except(self.volts_var)
        else:
            try:
                volts = float(self.volts_var.get())
                self.nanov_var.set(f"{volts * 1000000000:.2f}")
                self.microv_var.set(f"{volts * 1000000:.2f}")
                self.milliv_var.set(f"{volts * 1000:.2f}")
                self.kilov_var.set(f"{volts * 0.001:.4f}")
                self.megav_var.set(f"{volts * 0.0000010:.6f}")
            except ValueError:
                pass
        self.updating = False

    def convert_from_kilov(self,*args):
        if self.updating:
            return
        self.updating = True

        if self.kilov_var.get() == "":
            self.clear_except(self.kilov_var)
        else:
            try:
                kilov = float(self.kilov_var.get())
                self.nanov_var.set(f"{kilov * 1000000000000:.2f}")
                self.microv_var.set(f"{kilov * 1000000000:.2f}")
                self.milliv_var.set(f"{kilov * 1000000:.2f}")
                self.volts_var.set(f"{kilov * 1000:.2f}")
                self.megav_var.set(f"{kilov * 0.001:.4f}")

            except ValueError:
                pass
        self.updating = False
    
    def convert_from_megav(self,*args):
        if self.updating:
            return
        self.updating = True

        if self.megav_var.get() == "":
            self.clear_except(self.megav_var)
        else:
            try:
                megav = float(self.megav_var.get())
                self.nanov_var.set(f"{megav * 1000000000000000:.2f}")
                self.microv_var.set(f"{megav * 1000000000000:.2f}")
                self.milliv_var.set(f"{megav * 1000000000:.2f}")
                self.volts_var.set(f"{megav * 1000000:.2f}")
                self.kilov_var.set(f"{megav * 1000:.2f}")

            except ValueError:
                pass
        self.updating = False

    def voltage_facts(self, event):
            try:
                millivolts = float(self.milliv_var.get())
                volts = float(self.volts_var.get())

            except ValueError:
                return
            
            if millivolts in range(0,70):
                self.canvas.itemconfig(self.fact_text, text="Did you know? the nervous system\ncommunicates using tiny electrical signals, typically\nranging from -70 to +70 millivolts!")

            if volts in range(1,10):
                self.canvas.itemconfig(self.fact_text, text="Did you know? the average human body\nvoltage is around 3 volts!")

            if volts >= 500_000:
                self.canvas.itemconfig(self.fact_text, text="Did you know? Tesla coils can generate\nvoltages exceeding 1 million volts!")

    def check_fact(self, *args):
        try:
            millivolts = float(self.milliv_var.get())
            volts = float(self.volts_var.get())
        except ValueError:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)  # Move the button back to the original position
            return
    
        if millivolts in range(1,70) or volts in range(1,10) or volts >= 500_000:
            self.canvas.itemconfig(self.fact_button, image=self.venti_idea)
            self.canvas.coords(self.fact_button, 10, 390)  # Move the button up
        else:
            self.canvas.itemconfig(self.fact_button, image=self.venti)
            self.canvas.coords(self.fact_button, 10, 400)  # Move the button back to the original position

    def clear_fact(self, *args):
        self.canvas.itemconfig(self.fact_text, text="")
        

# Not Finished
class MainMenu:
    def __init__(self, window):
        # Widgets
        self.window = window
        self.window.title("Main Menu")
        self.window.geometry("750x500+100+60")
        self.window.resizable(False, False)
        self.window.configure(bg="blue") ; self.window.resizable(False, False)

        # Set Icon
        icon_logo = get_image_path('logo.ico')
        self.window.iconbitmap(icon_logo)
        
        global my_font
        my_font = ("Nirmala UI", 10, "bold")

        global my_font_s
        my_font_s = ("Consolas", 8, "bold")

        # Get the directory of the script
        bg_image_path = get_image_path('menu3.png')

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
        self.speed_converter_window = None
        self.volume_converter_window = None
        self.volts_converter_window = None

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
        temperature_converter_button.place(x=57, y=310, width=100, height=50)

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
        data_converter_button.place(x=415, y=310, width=100, height=50)

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
        volume_converter_button.place(x=235, y=310, width=100, height=50)
        
        # Voltage Converter Button
        volts_image_path = get_image_path('voltage.png')
        self.volts_image = PhotoImage(file=volts_image_path)
        volts_converter_button = tk.Button(
            self.window, 
            command=self.open_volts_converter,
            compound="center",
            image = self.volts_image,
            bd=0,
        )
        volts_converter_button.place(x=595, y=310, width=100, height=50)



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

    def open_speed_converter(self):
        if not self.speed_converter_window:
            self.speed_converter_window=tk.Toplevel(self.window)
            self.speed_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_speed_converter)
            SpeedConverter(self.speed_converter_window)
        else:
            self.speed_converter_window.deiconify()

    def on_closing_speed_converter(self):
        self.speed_converter_window.destroy()
        self.speed_converter_window = None

    def open_volume_converter(self):
        if not self.volume_converter_window:
            self.volume_converter_window = tk.Toplevel(self.window)
            self.volume_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_volume_converter)
            VolumeConverter(self.volume_converter_window)
        else:
            self.volume_converter_window.deiconify()

    def on_closing_volume_converter(self):
        self.volume_converter_window.destroy()
        self.volume_converter_window = None
        
    def open_volts_converter(self):
        if not self.volts_converter_window:
            self.volts_converter_window = tk.Toplevel(self.window)
            self.volts_converter_window.protocol("WM_DELETE_WINDOW", self.on_closing_volts_converter)
            VoltageConverter(self.volts_converter_window)
        else:
            self.volts_converter_window.deiconify()

    def on_closing_volts_converter(self):
        self.volts_converter_window.destroy()
        self.volts_converter_window = None

# Run the application
window = tk.Tk()
MainMenu(window)
window.mainloop()
