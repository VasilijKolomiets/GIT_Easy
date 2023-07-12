"""
 Python program to  create a simple GUI
 weight converter using Tkinter

 https://www.geeksforgeeks.org/python-weight-conversion-gui-using-tkinter/?ref=lbp

"""
from time import sleep
import tkinter as tk


def from_kg():
    """Convert weight mesures.

        Function to convert weight
        given in kg to
        grams, pounds and ounces
    """
    # convert in str to float
    try:
        kg_in = float(var_in_value.get())
        # convert kg to gram
        gram = kg_in*1000

        # convert kg to pound
        pound = kg_in*2.20462

        # convert kg to ounce
        ounce = kg_in*35.274
    except ValueError:
        gram, pound, ounce = 0, 'numbers to input !!', 0
    
    for_loop = [
        dict(text_frame=txt_0_out_gram, value=gram),
        dict(text_frame=txt_1_out_pound, value=pound),
        dict(text_frame=txt_2_out_ounce, value=ounce),
        ]

    for element in for_loop:
        element['text_frame'].delete("1.0", tk.END)
        element['text_frame'].insert(tk.END, element['value'])
    # # Enters the converted weight to the text widget
    # txt_0_out_gram.delete("1.0", tk.END)
    # txt_0_out_gram.insert(tk.END, gram)

    # txt_1_out_pound.delete("1.0", tk.END)
    # txt_1_out_pound.insert(tk.END, pound)

    # txt_2_out_ounce.delete("1.0", tk.END)
    # txt_2_out_ounce.insert(tk.END, ounce)


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
    btn_convert_it.grid(row=0, column=2)

    # Create the Label widget - row 0, col 0-2
    # text mesures explanations
    lbl_0_gram = tk.Label(window, text='Gram')
    lbl_0_gram.grid(row=1, column=0)

    lbl_1_pound = tk.Label(window, text='Pounds')
    lbl_1_pound.grid(row=1, column=1)

    lbl_2_ounce = tk.Label(window, text='Ounce')
    lbl_2_ounce.grid(row=1, column=2)

    # Create the Text Widgets - output conwerted values
    txt_0_out_gram = tk.Text(window, height=1, width=20)
    txt_0_out_gram.grid(row=2, column=0)

    txt_1_out_pound = tk.Text(window, height=1, width=20)
    txt_1_out_pound.grid(row=2, column=1)

    txt_2_out_ounce = tk.Text(window, height=1, width=20)
    txt_2_out_ounce.grid(row=2, column=2)

    # Start the GUI loop
    window.mainloop()
