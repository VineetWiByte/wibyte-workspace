import tkinter as tk
import random

window = tk.Tk()
window.title("Minesweeper")
window.geometry("600x600")


Nrows = 9
Ncols = 9
Nmines = 10
locs_all = [x for x in range(Nrows*Ncols)]
locs = random.sample(locs_all, Nmines)

buttons = []
field = [[0 for _ in range(Ncols)] for _ in range(Nrows)]








def display_field():
  for kk in range(Nrows):
    print(field[kk])


def find_neighbors(r0, c0):
  nn = []

  temp_c = [c0-1, c0, c0+1]
  temp_r = [r0-1, r0, r0+1]

  temp_c = [x for x in temp_c if x > -1 and x < Ncols]
  temp_r = [x for x in temp_r if x > -1 and x < Ncols]


  for r in temp_r: 
    for c in temp_c:
      nn.append((r, c))
  
  nn.remove((r0, c0))
  
  return nn


def clickOn(r, c):
  if field[r][c] == 9: 
    # Mine
    for kk in range(0, Nrows):
      for jj in range(Ncols):
          buttons[kk][jj]['state'] = 'disabled'
          buttons[kk][jj].config(relief=tk.SUNKEN)
          if field[kk][jj] == 9:
              buttons[kk][jj]["text"] = "*"
              buttons[kk][jj].config(background = 'red', disabledforeground = 'black')
  elif field[r][c] != 0: 
    # Mine in the neighborhood
    buttons[r][c]['state'] = 'disabled'
    buttons[r][c].config(relief=tk.SUNKEN)
    buttons[r][c]["text"] = str(field[r][c])
              



# Create a Nrows x Ncols grid of buttons
for kk in range(Nrows):
  buttons.append([])
  for jj in range(Ncols):
    b = tk.Button(command = lambda r=kk, c=jj: clickOn(r, c))
    b.grid(row=kk, column = jj)
    b["width"] = 3
    b["font"] = 40
    b['text'] = ' '
    buttons[kk].append(b)

for loc in locs:
  loc_xy = divmod(loc, Ncols)
  field[loc_xy[0]][loc_xy[1]] = 9

  nn = find_neighbors(loc_xy[0], loc_xy[1])

  for neighbors in nn: 
    if field[neighbors[0]][neighbors[1]] != 9:
      field[neighbors[0]][neighbors[1]] += 1


tk.mainloop()

