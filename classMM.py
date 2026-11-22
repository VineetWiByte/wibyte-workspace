import tkinter as tk

window = tk.Tk()
window.title('Metro Map')
window.geometry('600x600')
window.configure(bg = 'Darkgreen')

c = tk.Canvas(window, width = 550, height = 500)
c.pack()

stn_sL = ['SpriteLand', 'GoNGlide', 'Costumes', 'Broadcast', 'WiByte', 'Cloning', 'MyBlocks']

x_s = 50
y_s = 200
d_stn = 70
r_stn = 6

# Python Line








def calculate():
    start = start_station.get()
    stop = stop_station.get()

    if start in stn_sL: 
        start_line = stn_sL
    else: 
        start_line = stn_pL 

    if stop in stn_sL:
        stop_line = stn_sL
    else: 
        stop_line = stn_pL

    if start_line is stop_line:
        n_stops = abs(start_line.index(start) - start_line.index(stop))
    else: 
        n_stops = abs(start_line.index(start) - start_line.index('WiByte'))
        n_stops = n_stops + abs(stop_line.index(stop) - stop_line.index('WiByte'))
    
    
    
    fare = n_stops*20
    fareLabel.configure(text = 'FARE = INR ' + str(fare))




for stn in stn_sL: 
    if stn != stn_sL[-1]:
        c.create_line(x_s, y_s, x_s + d_stn, y_s, fill = 'DarkOrange')
    c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill = 'DarkOrange')
    c.create_text(x_s, y_s + 30, text=stn, fill ='DarkOrange', font = ('Helvetica 6 bold'))
    x_s = x_s + d_stn

stn_pL = ['EscapeChar', 'WhileLoop', 'WiByte', 'IfElifElse', 'Range', 'Dictionary', 'TurtlePark']

x_s = 330
y_s = 40
d_stn = 70
r_stn = 6



for stn in stn_pL:
	if stn != stn_pL[-1]:
		c.create_line(x_s, y_s, x_s, y_s + d_stn, fill = 'blue')
	c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill = 'blue')
	c.create_text(x_s + 40, y_s, text = stn, fill = 'blue', font = ('Helvetica 6 bold'))
	y_s = y_s + d_stn




all_stations = stn_sL + stn_pL
all_stations.remove('WiByte')


c.create_text(50, 340, text = 'Start')
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x = 50, y = 350)


c.create_text(250, 340, text = 'Stop')
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x = 250, y = 350)


button = tk.Button(text = 'CALCULATE FARE', command = calculate)
button.pack()
fareLabel = tk.Label(text = 'FARE =  ')
fareLabel.pack()


tk.mainloop()