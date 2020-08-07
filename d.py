from simpleimage import SimpleImage
import tkinter
from PIL import ImageTk
from PIL import Image

python = 'image/python.png'
standford = 'image/standford.jpg'
corona = 'image/coronavirus.jpg'
worldwide = 'image/worldwide.png'
online = 'image/online.png'
year = 'image/2020.jpg'
knowledge = 'image/knowledge.png'
funny = 'image/funny.jpg'
nonprofit = 'image/nonprofit.png'
course = 'image/course.jpg'
right = 'image/right.jpg'
congrats = 'image/congrats.jpg'
welcome = 'image/welcome.png'

def main():
    canvas = make_canvas(1000, 1000, 'Congrats')
    image = ImageTk.PhotoImage(Image.open('image/congrats.jpg'))
    canvas.create_image(100, 400, anchor='w', image=image)
    canvas.create_text(160, 700, anchor='w', font='Courier 30', text="Congrats! You have met course condition.")
    canvas.mainloop()

def make_canvas(width, height, title=None):
    object = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width = width + 1, height = height + 1)
    canvas.pack()
    return canvas



if __name__ == '__main__':
    main()