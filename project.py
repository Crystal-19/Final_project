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

dictionary = {'NGÔN NGỮ LẬP TRÌNH': 'programming language', 'TRƯỜNG ĐẠI HỌC': 'university',
            'ĐẠI DỊCH': 'pandemic', 'KHẮP THẾ GIỚI': 'worldwide',
            'TRỰC TUYẾN': 'online', 'NĂM': 'year',
            'KIẾN THỨC': 'knowledge', 'VUI VẺ': 'funny',
            'PHI LỢI NHUẬN': 'nonprofit', 'KHOÁ HỌC': 'course'}
def test():
    conti_nue = True
    while conti_nue:
        list_Vn = list(dictionary.keys())
        for vocabulary_Vn in range(len(list_Vn)):
            vocabulary_Vn+=1
            if vocabulary_Vn == 1:
                filter_python()
                guess = input("1.Meaning of word NGÔN NGỮ LẬP TRÌNH is:  ")
                if guess == dictionary['NGÔN NGỮ LẬP TRÌNH']:
                    print("You are correct !")
                    imagep = SimpleImage(python)
                    imagep.show()
                else:
                    print("You are wrong !")
                    print('NGÔN NGỮ LẬP TRÌNH : programming language')
                    imagep = SimpleImage(python)
                    imagep.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font= 'Courier 26', text = 'Total number of correct answers:0', fill = 'gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 2:
                filter_standford()
                guess = input("2.Meaning of word TRƯỜNG ĐẠI HỌC is:  ")
                if guess == dictionary['TRƯỜNG ĐẠI HỌC']:
                    print("You are correct !")
                    images = SimpleImage(standford)
                    images.show()
                else:
                    print("You are wrong !")
                    print("TRƯỜNG ĐẠI HỌC: university")
                    images = SimpleImage(standford)
                    images.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:1', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 3:
                filter_corona()
                guess = input("3.Meaning of word ĐẠI DỊCH is:  ")
                if guess == dictionary['ĐẠI DỊCH']:
                    print("You are correct !")
                    imagec = SimpleImage(corona)
                    imagec.show()
                else:
                    print("You are wrong !")
                    print("ĐẠI DICH: pademic")
                    imagec = SimpleImage(corona)
                    imagec.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:2', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 4:
                filter_worldwide()
                guess = input("4.Meaning of word KHẮP THẾ GIỚI is:  ")
                if guess == dictionary['KHẮP THẾ GIỚI']:
                    print("You are correct !")
                    imagew = SimpleImage(worldwide)
                    imagew.show()
                else:
                    print("You are wrong !")
                    print("KHẮP THẾ GIỚI: worldwide")
                    imagew = SimpleImage(worldwide)
                    imagew.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:3', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 5:
                filter_online()
                guess = input("5.Meaning of word TRỰC TUYẾN is:  ")
                if guess == dictionary['TRỰC TUYẾN']:
                    print("You are correct !")
                    imageo = SimpleImage(online)
                    imageo.show()
                else:
                    print("You are wrong !")
                    print("TRỰC TUYẾN: online")
                    imageo = SimpleImage(online)
                    imageo.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:4', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 6:
                filter_year()
                guess = input("6.Meaning of word NĂM is:")
                if guess == dictionary['NĂM']:
                    print("You are correct !")
                    imagey = SimpleImage(year)
                    imagey.show()
                else:
                    print("You are wrong !")
                    print("NĂM: year")
                    imagey = SimpleImage(year)
                    imagey.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:5', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 7:
                filter_knowledge()
                guess = input("7.Meaning of word KIẾN THỨC is:")
                if guess == dictionary['KIẾN THỨC']:
                    print("You are correct !")
                    imagek = SimpleImage(knowledge)
                    imagek.show()
                else:
                    print("You are wrong !")
                    print("KIẾN THỨC: knowledge")
                    imagek = SimpleImage(knowledge)
                    imagek.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:6', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 8:
                filter_funny()
                guess = input("8.Meaning of word VUI VẺ is:  ")
                if guess == dictionary['VUI VẺ']:
                    print("You are correct !")
                    imagef = SimpleImage(funny)
                    imagef.show()
                else:
                    print("You are wrong !")
                    print("VUI VẺ: funny")
                    imagef = SimpleImage(funny)
                    imagef.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:7', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 9:
                filter_nonprofit()
                guess = input("9.Meaning of word PHI LỢI NHUẬN is: ")
                if guess == dictionary['PHI LỢI NHUẬN']:
                    print("You are correct !")
                    imagen = SimpleImage(nonprofit)
                    imagen.show()
                else:
                    print("You are wrong !")
                    print("PHI LỢI NHUẬN: nonprofit")
                    imagen = SimpleImage(nonprofit)
                    imagen.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:8', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            if vocabulary_Vn == 10:
                filter_course()
                guess = input("10.Meaning of word KHOÁ HỌC is:  ")
                if guess == dictionary['KHOÁ HỌC']:
                    print("You are correct !")
                    imagec = SimpleImage(course)
                    imagec.show()
                    print("Total of correct answers: 10")
                    canvas = make_canvas(1000, 1000, 'Congrats')
                    image = ImageTk.PhotoImage(Image.open('image/congrats.jpg'))
                    canvas.create_image(100, 400, anchor='w', image=image)
                    canvas.create_text(160, 700, anchor='w', font='Courier 30', text="Congrats! You have met course condition.")
                    conti_nue = False
                    #break
                else:
                    print("You are wrong !")
                    print("KHOÁ HỌC: course")
                    imagec = SimpleImage(course)
                    imagec.show()
                    canvas = make_canvas(600, 600, 'Result')
                    canvas.create_text(20, 200, anchor='w', font='Courier 26', text='Total number of correct answers:9', fill='gray')
                    canvas.create_text(20, 300, anchor='w', font='Courier 26', text='Sorry ! You can not join the course.', fill='gray')
                    value = input("Do you want to test again? (y/n): ")
                    if value == 'y':
                        test()
                    else:
                        conti_nue = False
                        break
            else:
                pass

def welcome():
    canvas = make_canvas(1000, 1000, 'Welcome')
    image = ImageTk.PhotoImage(Image.open('image/welcome.png'))
    canvas.create_image(50, 130, anchor='w', image=image)
    canvas.create_text(230, 130, anchor='w', font='Courier 30', text="Welcome to Code in Place by Vietnamese")
    canvas.create_text(50, 300, anchor='w', font='Courier 15',
                       text="First of all, We need to test your Vietnamese language to make sure you can get fully lesson content")
    canvas.create_text(50, 350, anchor='w', font='Courier 15',
                       text="We will give you some hints by images, if you pass 10 questions, you win!")
    canvas.create_text(400, 500, anchor='w', font='Courier 30', text="Are you ready !")
    print("Are you ready ! ")
    inp = input("")
    if inp == "":
        pass
    else:
        pass

def filter_python():
    image = SimpleImage(python)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.blue >= average:
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 225
        else:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    image.show()
def filter_standford():
    image = SimpleImage(standford)
    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, height - (y + 1), pixel)
    mirror.show()
def filter_corona():
    image = SimpleImage(corona)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red >= average:
            pixel.red = 125
            pixel.green = average
            pixel.blue = average
        else:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    image.show()
def filter_worldwide():
    image = SimpleImage(worldwide)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.blue >= average:
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 225
        else:
            pass
    image.show()
def filter_online():
    image = SimpleImage(online)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.green >= average:
            pixel.red = 0
            pixel.green = 225
            pixel.blue = 0
        else:
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    image.show()
def filter_year():
    image = SimpleImage(year)
    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, height - (y + 1), pixel)
    mirror.show()
def filter_knowledge():
    image = SimpleImage(knowledge)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average:
            pixel.red = 225
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = 0
            pixel.green = 0
            pixel.blue = 0
    image.show()
def filter_funny():
    image = SimpleImage(funny)
    for pixel in image:
        R = pixel.red
        G = pixel.green
        B = pixel.blue
        pixel.red = 0.8 * R + 0.8 * G + 0.1 * B
        pixel.green = 0.8 * R + 0.8 * G + 0.1 * B
    image.show()
def filter_nonprofit():
    image = SimpleImage(nonprofit)
    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, height - (y+1), pixel)
    mirror.show()
def filter_course():
    image = SimpleImage(course)
    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel(x, height - (y + 1), pixel)
    mirror.show()


def make_canvas(width, height, title=None):
    object = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width = width + 1, height = height + 1)
    canvas.pack()
    return canvas

def main():
    welcome()
    test()

if __name__ == '__main__':
    main()
