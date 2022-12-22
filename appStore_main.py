from tkinter import *
import platform
import psutil
import pyperclip
import random
import string
import png
from tkinter import messagebox
import tkinter.messagebox
import pyqrcode
from pyqrcode import QRCode
from tkinter import font
import pyscreenrec
import PIL
from PIL import ImageTk, Image
from tkinter.filedialog import  *
from pickletools import optimize


root = Tk()
root.title('App Container')
# root.geometry("850x500+300+170")
root.geometry("845x640")
root.resizable(0,0)
root.configure(bg='#292e2e')

#apps_link
def imageCom():
    master = Toplevel()
    master.geometry("365x800")
    master.resizable(False, False)
    master.title("Image Compressor")

    img = PhotoImage(file="/home/bhargav/My_projects/app_container/imgCom_images/background.png")
    label = Label(master,image=img)
    label.image = img
    label.pack()

    def nextPage():
        master.destroy()
        new = Toplevel()
        new.geometry("640x370")
        new.resizable(False, False)
        new.title("Image Compressor")
        new.config(bg="black")
        qual = IntVar()
        qual.set(0)

        Label(new, text="\n\n\nDefine the quality in number.\nHigh value low compression, low value high compression: ",
            font=("arial", 12, "bold"), bg="black", fg="white").pack()
        Entry(new, textvariable=qual, bd=0, width=25, border=1).place(x=195, y=200)


        def compress():

            file_path = askopenfilename()
            Image = PIL.Image.open(file_path)
            height, width = Image.size
            Img = Image.resize((height, width),      PIL.Image.Resampling.LANCZOS)
            save_path = asksaveasfilename()

            # qual = int(input("Define the quality in size. High value hlow compression, low value high compression: "))
            Img.save(f"{save_path}" + ".jpg", optimize=True, quality=qual.get())


        Button(new, text="COMPRESS", command=compress,
            bd=0, bg="#EFF2F0"). place(x=260, y=250)

    # continue button
    continue_img = PhotoImage(file="/home/bhargav/My_projects/app_container/imgCom_images/Rectangle 1.png")
    continue1 = Button(master, image=continue_img,bd=0, command=nextPage, bg="white")
    continue1.image = continue_img
    continue1.place(x=150, y=720)


def passwdGen():
    global backg
    global continue_img
    ws = Toplevel()
    ws.title('Password Generator')
    ws.geometry('363x800')

    backg = PhotoImage(file="/home/bhargav/My_projects/app_container/passwd_images/welcome-page.png")
    label1 = Label(ws,image=backg)
    label1.image = backg
    label1.pack()

    def nextPage():
        global backgPass
        ws.destroy()
        new = Toplevel()
        new.geometry("365x800")
        new.resizable(False, False)
        passwrd = StringVar()
        pass_len = IntVar()
        pass_len.set(0)
        new.title("Password Generator")

        backgPass = PhotoImage(file="/home/bhargav/My_projects/app_container/passwd_images/Android Large - 1.png")
        label1 = Label(new,image=backgPass)
        label1.image = backgPass
        label1.pack()


        def generate():
            """
            This is the main function of the program to generate secure passwords
            """
            # set of characters
            set1 = string.ascii_lowercase
            set2 = string.ascii_uppercase
            set3 = string.digits
            set4 = string.punctuation

            # concatenating all sets
            s = []
            s.extend(list(set1))
            s.extend(list(set2))
            s.extend(list(set3))
            s.extend(list(set4))

            # shuffling the list
            random.shuffle(s)
            password = ""
            for x in range(pass_len.get()):
                password = password + random.choice(s)
            passwrd.set(password)


        # function to copy the passcode
        def copyclipboard():
            random_password = passwrd.get()
            pyperclip.copy(random_password)
        Entry(new, textvariable=pass_len, bd=0, width=30, border=2).place(x=28, y=350)
        Entry(new, textvariable=passwrd, bd=0, width=30, border=2).place(x=28, y=440)

        # generate button
        gen_img = PhotoImage(file="/home/bhargav/My_projects/app_container/passwd_images/generate.png")
        gen = Button(new, image=gen_img, bd=0, command=generate, bg="white", font=("MS Serif", 18, "bold"))
        gen.image = gen_img
        gen.place(x=115, y=660)

        # copy button
        copy_img = PhotoImage(file="/home/bhargav/My_projects/app_container/passwd_images/copy.png")
        copy = Button(new, image=copy_img, bd=0, command=copyclipboard, bg="white", font=("MS Serif", 18, "bold"))
        copy.image = copy_img
        copy.place(x=115, y=730)

    # continue button
    continue_img = PhotoImage(file="/home/bhargav/My_projects/app_container/passwd_images/continue.png")
    continue1 = Button(ws, image=continue_img,bd=0,command=nextPage)
    continue1.image = continue_img
    continue1.place(x=110, y=725)

def qrCode():
    ws  =Toplevel()
    ws.geometry("575x569")
    ws.title('QRCode Generator')
    ws.resizable(False, False)
    image_icon = PhotoImage(file="/home/bhargav/My_projects/app_container/QRCode_images/icon.png")
    ws.iconphoto(False, image_icon)


    backg = PhotoImage(file="/home/bhargav/My_projects/app_container/QRCode_images/wlcme.png")
    label1 = Label(ws,image=backg)
    label1.image = backg
    label1.pack()

    def nextPage():
        new = Toplevel()
        ws.destroy()
        new.title("QRCode Generator")
        new.geometry('514x640')
        new.config(bg="#FFF6C9")
        new.resizable(0,0)
        image_icon = PhotoImage(file="/home/bhargav/My_projects/app_container/QRCode_images/icon.png")
        new.iconphoto(False, image_icon)

        backg = PhotoImage(file="/home/bhargav/My_projects/app_container/QRCode_images/background.png")
        label1 = Label(new,image=backg)
        label1.image = backg
        label1.pack()

        def generate_QR():
            if len(user_input.get()) != 0:
                global qr, img
                file = file_name.get()
                qr = pyqrcode.create(user_input.get())
                qr.png(f'{file}.png', scale = 6)
                img = BitmapImage(new,data=qr.xbm(scale=8))
            else:
                messagebox.showwarning('warning', 'All Fields are Required!')
            try:
                display_code()
            except:
                pass


        def display_code():
            img_lbl.config(new, image=img)
            output.config(new,text="QR code of " + user_input.get())


        user_input = StringVar()
        entry = Entry(new,textvariable=user_input, width=25, border=0).place(x=210, y=120)


        file_name = StringVar()
        Entry(new, textvariable=file_name, width=25, border=0).place(x=210, y=200)


        gen_img = PhotoImage(file="/home/bhargav/QR_code/project_images/generate.png")
        button = Button(new,image=gen_img,command=generate_QR, bg="#FFF6C9")
        button.image = gen_img
        button.place(x=200,y=280)

        img_lbl = Label(new,bg='#FFF6C9')
        img_lbl.place(x=130, y=340)
        output = Label(new,text="",bg='#FFF6C9')
        output.place(x=160, y=595)

            
    # continue button
    continue_img = PhotoImage(file="/home/bhargav/My_projects/app_container/QRCode_images/Arrow 1.png")
    continue1 = Button(ws, image=continue_img, bd=0, command=nextPage, bg="#FFF6C9")
    continue1.image = continue_img
    continue1.place(x=268, y=528)


def screenRec():
    ws = Toplevel()
    ws.geometry("400x800")
    ws.title('Xcam - Screen Recorder')
    ws.resizable(False, False)

    backg = PhotoImage(file="/home/bhargav/My_projects/app_container/screenRec_images/welcome.png")
    label1 = Label(ws,image=backg)
    label1.image = backg
    label1.pack()

    def nextPage():
        ws.destroy()
        root = Toplevel()
        root.geometry("410x808")
        root.title("Xcam - Screen Recorder")
        root.config(bg="black")
        root.resizable(False, False)
        back = PhotoImage(file="/home/bhargav/My_projects/app_container/screenRec_images/background.png")
        label1 = Label(root,image=back)
        label1.image = back
        label1.pack()   

        # ____________________________________________________________________


        # ____________________________________________________________________
        # FUNCTIONS
        def start_rec():
            file = Filename.get()
            rec.start_recording(str(file+" .mp4"), 19)
            tkinter.messagebox.showinfo("Started..")


        def pause_rec():
            rec.pause_recording()
            tkinter.messagebox.showinfo("Paused..")


        def resume_rec():
            rec.resume_recording()
            tkinter.messagebox.showinfo("Resume..")


        def stop_rec():
            rec.stop_recording()
            tkinter.messagebox.showinfo("Stopped..")

        # ____________________________________________________________________


        # entry
        Filename = StringVar()
        entry = Entry(root, textvariable=Filename, width=20, font=(
            "Lucida Console", 12),  bg="#EFF2F0", bd=0, selectborderwidth=0)
        entry.place(x=70, y=700)
        Filename.set("            File Name")

        rec = pyscreenrec.ScreenRecorder()

        # icon
        image_icon = PhotoImage(file="/home/bhargav/My_projects/app_container/screenRec_images/icon.png")
        root.iconphoto(root, image_icon)

        # ____________________________________________________________________


        Button(root, text="Start", command=start_rec,
            bd=0, bg="#EFF2F0"). place(x=78, y=275)

        Button(root, text="Resume", command=resume_rec, bd=0,
            bg="#EFF2F0", relief=RIDGE). place(x=240, y=275)

        Button(root, text="Pause", command=pause_rec,
            bd=0, bg="#EFF2F0"). place(x=78, y=443)

        Button(root, text="Stop", command=stop_rec,
            bd=0, bg="#EFF2F0"). place(x=255, y=443)


        
    # continue button
    continue_img = PhotoImage(file="/home/bhargav/My_projects/app_container/screenRec_images/Lets_go.png")
    continue1 = Button(ws, image=continue_img, text="Let's Go" ,bd=0, command=nextPage, bg="white")
    continue1.image = continue_img
    continue1.place(x=110, y=725)


def Calculator():
    # root.destroy()
    import pyCalc.Calc_main

def todo():
    import TodoList.Todo

def passManager():
    root.destroy()
    import PassManager

def dictionary():
    import dictionary.dict_main

#_________________________________________________________

Body = Frame(root, width=900, height=600, bg='#d6d6d6')
Body.pack(pady=20, padx=20)

#_______________________________________________
LHS = Frame(Body, width=310, height=805,bg='#f4f5f5', highlightbackground='#adacb1', highlightthickness=1)
LHS.place(x=10, y=10)

#_______________________________________________
rhs = Frame(Body, width=470, height=230,bg='#f4f5f5', highlightbackground='#adacb1', highlightthickness=1)
rhs.place(x=330, y=10)

system = Label(rhs, text='BATTERY:', font=("Acumin Variable Concept", 18,'bold'), bg='#f4f5f5')
system.place(x=10,y=10)

## battery
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d"% (hours, minutes, seconds)

def none():
    global battery_png
    global battery_label
    battery = psutil.sensors_battery()
    percent = battery.percent
    time = convertTime(battery.secsleft)

    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f"Plug in: {str(battery.power_plugged)}")
    lbl_time.config(text=f'{time} remaining')

    battery_label = Label(rhs, background='#f4f5f5')
    battery_label.place(x=15, y=70)

    lbl.after(1000, none)

    if battery.power_plugged == True:
        battery_png = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/full_battery.png")
        battery_label.config(image=battery_png)

    else:
        battery_png = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/low_battery.png")
        battery_label.config(image=battery_png)

lbl = Label(rhs, font=("Acumin Variable Concept", 14,'bold'), bg='#f4f5f5')
lbl.place(x=200, y=80)

lbl_plug = Label(rhs, font=("Acumin Variable Concept", 8,'bold'), bg='#f4f5f5')
lbl_plug.place(x=10, y=133)

lbl_time = Label(rhs, font=("Acumin Variable Concept", 8,'bold'), bg='#f4f5f5')
lbl_time.place(x=250, y=130)

none()

#_______________________________________________
rhb = Frame(Body, width=470, height=600,bg='#f4f5f5', highlightbackground='#ffffff', highlightthickness=1)
rhb.place(x=330, y=255)

apps = Label(rhb, text='APPS:', font=("Acumin Variable Concept", 16,'bold'),bg='#f4f5f5')
apps.place(x=10, y=10)

app01_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/screenRec.png")
app01 = Button(rhb,image=app01_image,bd=0, command=screenRec)
app01.place(x=15, y=60)
scrnrec = Label(rhb, text='Screen\nrecorder', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
scrnrec.place(x=15,y=130)

app02_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/imageCumpressor.png")
app02 = Button(rhb,image=app02_image,bd=0, command=imageCom)
app02.place(x=130, y=60)
img = Label(rhb, text='Image\nCompressor', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
img.place(x=120,y=130)

app03_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/passwdGen.png")
app03 = Button(rhb,image=app03_image,bd=0,command=passwdGen)
app03.place(x=245, y=60)
passwd = Label(rhb, text='Password\nGenerator', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
passwd.place(x=240,y=130)

app04_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/QRCude.png")
app04 = Button(rhb,image=app04_image,bd=0, command=qrCode)
app04.place(x=360, y=60)
qrcude = Label(rhb, text='QR Code\nGenerator', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
qrcude.place(x=350,y=130)

app05_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/todo.png")
app05 = Button(rhb,image=app05_image,bd=0, command=todo)
app05.place(x=15, y=200)
todo = Label(rhb, text='ToDo\nList', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
todo.place(x=22,y=280)

app06_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/dictionary.png")
app06 = Button(rhb,image=app06_image,bd=0, command=dictionary)
app06.place(x=130, y=200)
dict = Label(rhb, text='English\nDictionary', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
dict.place(x=120,y=280)

app07_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/Calculator.png")
app07 = Button(rhb,image=app07_image,bd=0,command=Calculator)
app07.place(x=245, y=200)
passwd = Label(rhb, text='Scientific\nCalculator', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
passwd.place(x=240,y=280)

app08_image = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/passManager.png")
app08 = Button(rhb,image=app08_image,bd=0, command=passManager)
app08.place(x=360, y=200)
qrcude = Label(rhb, text='Password\nManager', font=("Acumin Variable Concept", 9,'bold'), bg='#f4f5f5')
qrcude.place(x=360,y=280)


#_______________________________________________

#logo
photo = PhotoImage(file="/home/bhargav/My_projects/app_container/appStore_images/logo.png")
myimage = Label(LHS, image=photo, background='#f4f5f5')
myimage.place(x=2,y=20)

my_system = platform.uname()

l1 = Label(LHS, text=my_system.node, bg='#f4f5f5', font=("Acumin Variable Concept",11,'bold'),justify="center")
l1.place(x=20,y=200)

# l2 = Label(LHS, text=f"Version:{my_system.version}", bg='#f4f5f5', font=("Acumin Variable Concept",7,'bold'),justify="center")
# l2.place(x=20,y=225)

l3 = Label(LHS, text=f"System: {my_system.system}", bg='#f4f5f5', font=("Acumin Variable Concept",11,'bold'),justify="center")
l3.place(x=20,y=240)

l4 = Label(LHS, text=f"Machine: {my_system.machine}", bg='#f4f5f5', font=("Acumin Variable Concept",11,'bold'),justify="center")
l4.place(x=20,y=265)

l5 = Label(LHS, text=f"RAM installed: {round(psutil.virtual_memory().total/1000000000,2)} GB", bg='#f4f5f5', font=("Acumin Variable Concept",11,'bold'),justify="center")
l5.place(x=20,y=290)

l6 = Label(LHS, text=f"CPU: {my_system.processor}", bg='#f4f5f5', font=("Acumin Variable Concept",11,'bold'),justify="center")
l6.place(x=20,y=315)


# main event
root.mainloop()