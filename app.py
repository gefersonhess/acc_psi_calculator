from tkinter import *

def calculate_psi(ideal_psi, ideal_temperature, scale):
    psi_dict = {}
    for temperature in range(5, 41):
        local_psi = ideal_psi + scale * (ideal_temperature - temperature)
        psi_dict[temperature] = local_psi
    return psi_dict

window = Tk()
window.title('PSI Calculator')
window.geometry('200x400')

ideal_psi_fl_label = Label(window, text="Ideal PSI FL")
ideal_psi_fl_label.grid(column=0, row=0)
ideal_psi_fr_label = Label(window, text="Ideal PSI FR")
ideal_psi_fr_label.grid(column=0, row=1)
ideal_psi_rl_label = Label(window, text="Ideal PSI RL")
ideal_psi_rl_label.grid(column=0, row=2)
ideal_psi_rr_label = Label(window, text="Ideal PSI RR")
ideal_psi_rr_label.grid(column=0, row=3)

ideal_psi_fl_entry = Entry(window, width=10)
ideal_psi_fl_entry.grid(column=1, row=0)
ideal_psi_fr_entry = Entry(window, width=10)
ideal_psi_fr_entry.grid(column=1, row=1)
ideal_psi_rl_entry = Entry(window, width=10)
ideal_psi_rl_entry.grid(column=1, row=2)
ideal_psi_rr_entry = Entry(window, width=10)
ideal_psi_rr_entry.grid(column=1, row=3)

ideal_temp_label = Label(window, text="Temperature")
ideal_temp_label.grid(column=0, row=5)
ideal_temp_entry = Entry(window, width=10)
ideal_temp_entry.grid(column=1, row=5)

scale_label = Label(window, text="Scale PSI")
scale_label.grid(column=0, row=6)
scale_entry = Entry(window, width=10)
scale_entry.grid(column=1, row=6)
 
def clicked():
    ideal_temp = float(ideal_temp_entry.get())
    scale = float(scale_entry.get())
    fl_dict = calculate_psi(float(ideal_psi_fl_entry.get()), ideal_temp, scale)
    fr_dict = calculate_psi(float(ideal_psi_fr_entry.get()), ideal_temp, scale)
    rl_dict = calculate_psi(float(ideal_psi_rl_entry.get()), ideal_temp, scale)
    rr_dict = calculate_psi(float(ideal_psi_rr_entry.get()), ideal_temp, scale)
    newWindow = Toplevel(window)
    newWindow.title("Final PSI")
    newWindow.geometry("800x600")
    sb_fl = Scrollbar(newWindow)
    sb_fl.pack(side = RIGHT, fill = Y)
    fl_list = Listbox(newWindow, yscrollcommand=sb_fl.set)
    fl_list.insert(END, "Front left tyre")
    for key, value in fl_dict.items():
        fl_list.insert(END, str(key) + 'C°: ' + '{:.1f}'.format(value) + ' PSI')
    fl_list.pack(side = LEFT, fill = BOTH)
    sb_fl.config(command=fl_list.yview)

    sb_fr = Scrollbar(newWindow)
    sb_fr.pack(side = RIGHT, fill = Y)
    fr_list = Listbox(newWindow, yscrollcommand=sb_fr.set)
    fr_list.insert(END, "Front right tyre")
    for key, value in fr_dict.items():
        fr_list.insert(END, str(key) + 'C°: ' + '{:.1f}'.format(value) + ' PSI')
    fr_list.pack(side = LEFT, fill = BOTH)
    sb_fr.config(command=fr_list.yview)

    sb_rl = Scrollbar(newWindow)
    sb_rl.pack(side = RIGHT, fill = Y)
    rl_list = Listbox(newWindow, yscrollcommand=sb_rl.set)
    rl_list.insert(END, "Rear left tyre")
    for key, value in rl_dict.items():
        rl_list.insert(END, str(key) + 'C°: ' + '{:.1f}'.format(value) + ' PSI')
    rl_list.pack(side = LEFT, fill = BOTH)
    sb_rl.config(command=rl_list.yview)
    
    sb_rr = Scrollbar(newWindow)
    sb_rr.pack(side = RIGHT, fill = Y)
    rr_list = Listbox(newWindow, yscrollcommand=sb_rr.set)
    rr_list.insert(END, "Rear right tyre")
    for key, value in rr_dict.items():
        rr_list.insert(END, str(key) + 'C°: ' + '{:.1f}'.format(value) + ' PSI')
    rr_list.pack(side = LEFT, fill = BOTH)
    sb_rr.config(command=rr_list.yview)
         
calculate_btn = Button(window, text="Calculate", command=clicked, highlightbackground='Blue')
calculate_btn.grid(column=0, row=10)


window.mainloop()
