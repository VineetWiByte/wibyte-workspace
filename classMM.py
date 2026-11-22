import tkinter as tk

window = tk.Tk()
window.title('WiByte Metro Map')
window.geometry('600x600')
window.configure(bg = 'Darkgreen')

c = tk.Canvas(window, width = 550, height=550)
c.pack()

stn_sL = ['SpriteLand', 'GoNGlide', 'Costumes', 'Broadcast', 'WiByte', 'Cloning', 'MyBlocks']

x_s = 50
y_s = 200
d_stn = 70
r_stn = 6

for stn in stn_sL:
    if stn != stn_sL[-1]:
        c.create_line(x_s, y_s, x_s + d_stn, y_s, fill = 'DarkOrange')
    c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s+r_stn, fill = 'DarkOrange')
    c.create_text(x_s, y_s+30, text = stn, fill = 'DarkOrange', font = ('Helvetica 8 bold'))
    x_s = x_s + d_stn

all_stations = stn_sL

c.create_text(50, 270, text = 'Start')
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x = 50, y = 300)



tk.mainloop()