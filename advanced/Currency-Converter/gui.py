import tkinter as tk
from tkinter import ttk, messagebox
from currency_converter import CurrencyConverter

class CurrencyConverterApp:
    def __init__(self):
        self.converter = CurrencyConverter("33ec7c73f8a4eb6b9b5b5f95118b2275")  # Replace with your actual API key

        self.root = tk.Tk()
        self.root.title("Currency Converter")

        self.create_widgets()

    def create_widgets(self):
        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = tk.Label(self.root, text="From:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_currency_combobox = self.create_currency_combobox()
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.to_currency_label = tk.Label(self.root, text="To:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_currency_combobox = self.create_currency_combobox()
        self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def create_currency_combobox(self):
        currencies = [
            "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF",
            "BMD", "BND", "BOB", "BRL", "BSD", "BTC", "BTN", "BWP", "BYN", "BYR", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP",
            "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD",
            "FKP", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
            "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW",
            "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK",
            "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR",
            "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG",
            "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY",
            "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XCD",
            "XDR", "XOF", "XPF", "YER", "ZAR", "ZMK", "ZMW", "ZWL"
        ]
        combobox = ttk.Combobox(self.root, values=currencies)
        combobox.set("Select Currency")
        return combobox

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()
            if from_currency == "Select Currency" or to_currency == "Select Currency":
                raise ValueError("Please select both currencies")

            converted_amount = self.converter.convert(amount, from_currency, to_currency)
            self.result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()
