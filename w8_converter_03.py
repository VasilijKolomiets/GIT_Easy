"""
 Python program to  create a simple GUI
 weight converter using Tkinter

 https://www.geeksforgeeks.org/python-weight-conversion-gui-using-tkinter/?ref=lbp

"""
import tkinter as tk

from_kg_converters = dict(Gram=1000, Pound=2.2046, Ounce=35.274, Пуд=1/16)

def from_kg():
    """Convert weight mesures.

        Function to convert weight
        given in kg to
        grams, pounds and ounces
    """
    # convert in str to float
    try:
        kg_in = float(var_in_value.get())

        for key, converter in from_kg_converters.items():
            texts[key]['value_to_show'] = kg_in * converter
        
    except ValueError:
        for key, converter in from_kg_converters.items():
            texts[key]['value_to_show'] = 'enter a number above'
    

    # Enters the converted weight to the text widget
    for key, element in texts.items():
        element['frame'].delete("1.0", tk.END)
        element['frame'].insert(tk.END, element['value_to_show'])


if __name__ == '__main__':
    # Create a GUI window
    window = tk.Tk()

    # grid method is used for placing
    # the widgets at respective positions
    # in table like in structure.

    # Create the Label widget - row 0, col 0
    lbl_main = tk.Label(window, text="Enter the weight in Kg")
    lbl_main.grid(row=0, column=0)

    var_in_value = tk.StringVar()
    
    ent_main_kg_in = tk.Entry(window, textvariable=var_in_value)
    ent_main_kg_in.grid(row=0, column=1)

    # Create the Button Widget- row 0, col 2
    btn_convert_it = tk.Button(window, text="Convert", command=from_kg)
    btn_convert_it.grid(row=0, column=len(from_kg_converters)-1)

    labels = dict()
    for i, key in enumerate(from_kg_converters.keys()):
        labels[key] = tk.Label(window, text=key)
        labels[key].grid(row=1, column=i)

    # Create the Text Widgets - output conwerted values
    texts = dict()
    for i, key in enumerate(from_kg_converters.keys()):
        texts[key] = dict(frame=tk.Text(window, height=1, width=20), value_to_show=0.0)
        texts[key]['frame'].grid(row=2, column=i)   
 
     # Start the GUI loop
    window.mainloop()
