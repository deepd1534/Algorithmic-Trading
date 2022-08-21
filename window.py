
from tkinter import *



def login():
    from NorenRestApiPy.NorenApi import  NorenApi

    class ShoonyaApiPy(NorenApi):
        def __init__(self):
            NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')
            global api
            api = self

    username = entry0.get()
    password = entry1.get()
    pan = entry2.get()
    imei = entry3.get()
    key = entry4.get()


    import logging
 
    #enable dbug to see request and responses
    logging.basicConfig(level=logging.DEBUG)

    #start of our program
    api = ShoonyaApiPy()
    ret = api.login(userid=username, password=password, twoFA=pan, vendor_code=username + "_U", api_secret=key, imei=imei)
    if ret['stat'] != "Ok":
        print("Login failed")
    else:#login successful
        window.destroy()
        #work here
        def btn_clicked():
            print(ret['email'])
            print("Login Successful")


        window1 = Tk()

        window1.geometry("450x310")
        window1.configure(bg = "#162830")
        window1.title("ScalperX")
        canvas = Canvas(
            window1,
            bg = "#162830",
            height = 310,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        entry0_img1 = PhotoImage(file = f"img_textBox0.png")
        entry0_bg1 = canvas.create_image(
            131.0, 50.5,
            image = entry0_img1)

        entry01 = Entry(
            bd = 0,
            bg = "#224957",
            highlightthickness = 0)

        entry01.place(
            x = 38.0, y = 36,
            width = 186.0,
            height = 27)

        entry1_img1 = PhotoImage(file = f"img_textBox1.png")
        entry1_bg1 = canvas.create_image(
            386.0, 50.5,
            image = entry1_img1)

        entry11 = Entry(
            bd = 0,
            bg = "#224957",
            highlightthickness = 0)

        entry11.place(
            x = 367.0, y = 36,
            width = 38.0,
            height = 27)

        entry2_img1 = PhotoImage(file = f"img_textBox2.png")
        entry2_bg1 = canvas.create_image(
            260.0, 132.0,
            image = entry2_img1)

        entry21 = Entry(
            bd = 0,
            bg = "#224957",
            highlightthickness = 0)

        entry21.place(
            x = 244.0, y = 116,
            width = 32.0,
            height = 30)

        entry3_img1 = PhotoImage(file = f"img_textBox3.png")
        entry3_bg1 = canvas.create_image(
            325.0, 203.0,
            image = entry3_img1)

        entry31 = Entry(
            bd = 0,
            bg = "#224957",
            highlightthickness = 0)

        entry31.place(
            x = 289.0, y = 182,
            width = 72.0,
            height = 40)

        entry4_img1 = PhotoImage(file = f"img_textBox4.png")
        entry4_bg1 = canvas.create_image(
            163.0, 130.0,
            image = entry4_img1)

        entry41 = Entry(
            bd = 0,
            bg = "#224957",
            highlightthickness = 0)

        entry41.place(
            x = 147.0, y = 114,
            width = 32.0,
            height = 30)

        entry5_img1 = PhotoImage(file = f"img_textBox5.png")
        entry5_bg = canvas.create_image(
            66.0, 130.0,
            image = entry5_img1)

        entry51 = Entry(
            bd = 0,
            bg = "#224957",
            highlightthickness = 0)

        entry51.place(
            x = 50.0, y = 114,
            width = 32.0,
            height = 30)

        canvas.create_text(
            260.0, 97.5,
            text = "TRAIL",
            fill = "#ffffff",
            font = ("None", int(12.0)))

        canvas.create_text(
            304.0, 49.5,
            text = "QUANTITY",
            fill = "#ffffff",
            font = ("None", int(12.0)))

        canvas.create_text(
            66.5, 97.5,
            text = "TARGET",
            fill = "#ffffff",
            font = ("None", int(12.0)))

        canvas.create_text(
            161.5, 97.5,
            text = "SL",
            fill = "#ffffff",
            font = ("None", int(12.0)))

        img0 = PhotoImage(file = f"img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 43, y = 195,
            width = 55,
            height = 22)

        img1 = PhotoImage(file = f"img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b1.place(
            x = 131, y = 195,
            width = 55,
            height = 22)

        img2 = PhotoImage(file = f"img2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b2.place(
            x = 306, y = 119,
            width = 44,
            height = 22)

        img3 = PhotoImage(file = f"img3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b3.place(
            x = 371, y = 119,
            width = 44,
            height = 22)

        window1.resizable(False, False)
        window1.mainloop()


        

#-------------------------------Login Page---------------------------------------------------------------------
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#093545")
window.title("ScalperX-Login")
canvas = Canvas(
    window,
    bg = "#093545",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_1.png")
background = canvas.create_image(
    640.0, 664.5,
    image=background_img)

img0 = PhotoImage(file = f"img0_1.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login,
    relief = "flat")

b0.place(
    x = 490, y = 577,
    width = 300,
    height = 45)

entry0_img = PhotoImage(file = f"img_textBox0_1.png")
entry0_bg = canvas.create_image(
    640.0, 187.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#224957",
    highlightthickness = 0)

entry0.place(
    x = 500.0, y = 165,
    width = 280.0,
    height = 43)

canvas.create_text(
    542.0, 149.0,
    text = "Username",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(14.0)))

entry1_img = PhotoImage(file = f"img_textBox1_1.png")
entry1_bg = canvas.create_image(
    640.0, 265.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#224957",
    highlightthickness = 0)

entry1.place(
    x = 500.0, y = 243,
    width = 280.0,
    height = 43)

canvas.create_text(
    539.5, 228.0,
    text = "Password",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(14.0)))

entry2_img = PhotoImage(file = f"img_textBox2_1.png")
entry2_bg = canvas.create_image(
    640.0, 345.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#224957",
    highlightthickness = 0)

entry2.place(
    x = 500.0, y = 323,
    width = 280.0,
    height = 43)

canvas.create_text(
    525.5, 309.0,
    text = "PAN",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(14.0)))

entry3_img = PhotoImage(file = f"img_textBox3_1.png")
entry3_bg = canvas.create_image(
    640.0, 519.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#224957",
    highlightthickness = 0)

entry3.place(
    x = 500.0, y = 497,
    width = 280.0,
    height = 43)

canvas.create_text(
    524.5, 478.0,
    text = "IMEI",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(14.0)))

entry4_img = PhotoImage(file = f"img_textBox4_1.png")
entry4_bg = canvas.create_image(
    640.0, 425.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#224957",
    highlightthickness = 0)

entry4.place(
    x = 500.0, y = 403,
    width = 280.0,
    height = 43)

canvas.create_text(
    524.0, 388.0,
    text = "Key",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(14.0)))

canvas.create_text(
    640.0, 83.0,
    text = "Login",
    fill = "#ffffff",
    font = ("LexendDeca-Regular", int(64.0)))

window.resizable(False, False)
window.mainloop()
#----------------------------------------------------------------------------------------------------------------