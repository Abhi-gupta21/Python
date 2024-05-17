import tkinter

window = tkinter.Tk()
window.config(padx = 100, pady = 100)
head_label = tkinter.Label(text = "Miles to Kilometres")
head_label.config(padx = 50, pady = 50)
head_label.pack()

miles_entry = tkinter.Entry(width = 10)

miles_entry.pack()

kms_label = tkinter.Label(text = "kms will be shown here")
kms_label.config(padx = 25, pady = 25)
kms_label.pack()

def con_button_clicked():
    miles = float(miles_entry.get())
    kms = miles * 1.6
    kms_label["text"] = str(kms) + " kms"

convert_button = tkinter.Button(text = "Convert", command = con_button_clicked)

convert_button.pack()


window.mainloop()