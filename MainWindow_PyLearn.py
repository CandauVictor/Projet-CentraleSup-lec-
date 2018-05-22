import tkinter as tk
from math import*
import numpy as np
import matplotlib




#Window creation:
main_window= tk.Tk()

#First label:
welcome_label= tk.Label(main_window, text="Select parameters for PyLearn")

welcome_label.pack()

#Options:

## Choice of machine learning
var_type_learning = tk.StringVar()

choice_deep_learning = tk.Radiobutton(main_window, text="Deep Learning", variable=var_type_learning, value="Deep Learning")
choice_genetic = tk.Radiobutton(main_window, text="Genetic Algorithm", variable=var_type_learning, value="Genetic Algorithm")

choice_deep_learning.pack()
choice_genetic.pack()

## Choice of the number of hidden layers
layers_label= tk.Label(main_window, text="Select number of hidden layers")

layers_label.pack()

var_num_layers = tk.IntVar()
line_layers = tk.Entry(main_window, textvariable=var_num_layers, width=10)
line_layers.pack()

## Choice of the number of inputs
inputs_label= tk.Label(main_window, text="Select number of inputs")

inputs_label.pack()

var_num_inputs = tk.StringVar()
line_inputs = tk.Entry(main_window, textvariable=var_num_inputs, width=10)
line_inputs.pack()

## Choice of the number of outputs
outputs_label= tk.Label(main_window, text="Select number of outputs")

outputs_label.pack()

var_num_outputs = tk.StringVar()
line_outputs = tk.Entry(main_window, textvariable=var_num_outputs, width=10)
line_outputs.pack()

##Choice of initial weight and bias

wnb_label= tk.Label(main_window, text="Select initial weight and bias")

wnb_label.pack()

var_init_w = tk.StringVar()
line_init_w = tk.Entry(main_window, textvariable=var_init_w, width=10)
line_init_w.pack()

var_init_b = tk.StringVar()
line_init_b = tk.Entry(main_window, textvariable=var_init_b, width=10)
line_init_b.pack()



#Next button:
next_button=tk.Button(main_window, text="Start", command=None)
next_button.pack()


##Asking the size of each layer
n=3
if n!=0:
    layer_window = tk.Tk()


    list_size_layers=[i for i in range(n+2)]

    list_size_layers[0] = [var_num_inputs]

    list_size_layers[-1] = [var_num_outputs]

    Texts=[]
    Lines=[]
    for i in range(n):
        Texts.append(tk.Label(layer_window, text="Select size of layer %s"%str(i+1)))
        size_layer=tk.StringVar()
        Lines.append(tk.Entry(layer_window,textvariable=size_layer, width=10))
        list_size_layers[i+1]=size_layer

    for i in range(n):
        Texts[i].pack()
        Lines[i].pack()
    layer_window.mainloop()






#Opening window loop:
main_window.mainloop()




