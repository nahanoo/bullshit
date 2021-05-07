import tkinter
from PIL import Image, ImageTk
from bullshit import Bullshit
import os

class Interface:
    def __init__(self,player):
        self.dice_pngs = dict()
        for dice_number in range(1,7):
            self.dice_pngs[dice_number] = os.path.join('dices',str(dice_number)+'.png')

        self.root = tkinter.Tk()
        self.root.geometry(str(150*player.n_dices_per_player)+'x150')
        self.root.title('Dices of '+player.name)

    def show_dices(self,player):
        dice_images = []
        for dice in player.dices.values():
            dice_image = ImageTk.PhotoImage(Image.open(self.dice_pngs[dice.dice_number]))
            dice_images.append(dice_image)

        labels = []
        for dice_image in dice_images:
            label = tkinter.Label(self.root, image=dice_image)
            label.configure(image=dice_image)
            label.pack(side=tkinter.LEFT)

        self.root.mainloop()