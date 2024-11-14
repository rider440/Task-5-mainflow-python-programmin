import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk, Image
from tkinter import messagebox

# Create the root window
root = tk.Tk()
root.geometry("600x270")
root.title("Currency Converter")
root.iconbitmap("C:\\Users\\Ajeet\\Downloads\\Bdbd\\icon.ico")
root.maxsize(600, 270)
root.minsize(600, 270)

# Image Setup
image = Image.open("C:\\Users\\Ajeet\\Downloads\\Bdbd\\currency.png")
zoom = 0.5
pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))

panel = Label(root, image=img)
panel.place(x=190, y=35)

# Function to fetch data from API and convert
def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url = 'http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1'

    if amount == '':
        messagebox.showerror("Currency Converter", "Please Fill the amount")
    elif not amount.replace('.', '', 1).isdigit():  # Check if amount is numeric
        messagebox.showerror("Currency Converter", "Please enter a valid number for the amount")
    elif to_currency == '':
        messagebox.showerror("Currency Converter", "Please Choose the Currency")
    else:
        try:
            data = requests.get(url).json()
            if 'error' in data:
                raise Exception(data['error']['info'])
            
            currency = from_currency.strip() + to_currency.strip()
            amount = float(amount)  # Convert amount to float
            cc = data['quotes'].get(currency)
            if cc is None:
                raise ValueError(f"Exchange rate for {currency} not found.")
            
            cur_conv = cc * amount
            E2.delete(0, 'end')  # Clear previous result
            E2.insert(0, round(cur_conv, 2))  # Insert rounded conversion result
            
            # Update text with conversion details
            text.insert('end', f'{amount} {from_currency} Equals {round(cur_conv, 2)} {to_currency} \n\n Last Update: {datetime.now()}\n\n')
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to clear the entries
def clear_fields():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    text.delete(1.0, 'end')

# Labels
l1 = Label(root, text="Currency Converter Using Python", font=("verdana", "12", "bold"))
l1.place(x=158, y=15)

ant = Label(root, text="Amount", font=('roboto', 10, 'bold'))
ant.place(x=20, y=15)

# Entry for amount
E1 = Entry(root, width=20, borderwidth=1, font=('roboto', 19, 'bold'))
E1.place(x=20, y=40)  # Correct placement of entry field for amount

# Combobox for choosing currency (from)
c1 = tk.StringVar()
c2 = tk.StringVar()

currencychoose1 = ttk.Combobox(root, width=20, textvariable=c1, state='readonly', font=('verdana', 10, 'bold'))
currencychoose1['values'] = ('USD',)  # Keep it to 'USD' or populate with more options
currencychoose1.place(x=300, y=40)
currencychoose1.current(0)

# Entry for converted amount
E2 = Entry(root, width=20, borderwidth=1, font=('roboto', 10, 'bold'))
E2.place(x=20, y=80)

currencychoose2 = ttk.Combobox(root, width=20, textvariable=c2, state='readonly', font=('verdana', 10, 'bold'))
currencychoose2['values'] = (
    'ALL', 'AFN', 'ARS', 'AWG', 'AUD', 'AZN', 'BSD', 'BBD', 'BYN', 'BZD', 'BMD', 'BOB', 'BAM', 'BWP', 'BGN', 'BND',
    'KHR', 'CAD', 'KYD', 'CLP', 'CNY', 'COP', 'CRC', 'HRK', 'CUP', 'CZK', 'DKK', 'DOP', 'XCD', 'EGP', 'SVC', 'EUR', 'FKP',
    'FJD', 'GHS', 'GIP', 'GTQ', 'GGP', 'GYD', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'IMP', 'ILS', 'JMD', 'JPY',
    'KZT', 'KPW', 'KRW', 'KGS', 'LAK', 'LBP', 'LRD', 'MKD', 'MYR', 'MUR', 'MXN', 'MNT', 'MZN', 'NAD', 'NPR', 'ANG', 'NZD',
    'NIO', 'NGN', 'NOK', 'OMR', 'PKR', 'PAB', 'PYG', 'PEN', 'PHP', 'PLN', 'QAR', 'RON', 'RUB', 'SHP', 'SAR', 'RSD', 'SCR',
    'SGD', 'SBD', 'SOS', 'ZAR', 'LKR', 'SEK', 'CHF', 'SRD', 'SYP', 'TWD', 'THB', 'TTD', 'TRY', 'TVD', 'UAH', 'GBP', 'UYU',
    'UZS', 'VEF', 'VND', 'YER', 'ZWD'
)
currencychoose2.place(x=300, y=80)
currencychoose2.current()

# Text widget to display conversion details
text = Text(root, height=7, width=52, font=('verdana', '10', 'bold'))
text.place(x=100, y=120)

# Search Button
B = Button(root, text="Convert", command=show_data, font=('verdana', '10', 'bold'), borderwidth=2, bg="red", fg="white")
B.place(x=20, y=120)

# Clear Button
clear_btn = Button(root, text="Clear", command=clear_fields, font=('verdana', '10', 'bold'), borderwidth=2, bg="blue", fg="white")
clear_btn.place(x=20, y=170)

root.mainloop()
