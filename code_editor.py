from textwrap import wrap
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import requests
import urllib.parse
import io
from PIL import Image, ImageTk


root = Tk()

root.title('blind coding')
root.geometry("1000x700")
hid=False
isready=False

upper= Frame(root,bg="green")
lower= Frame(root,bg="blue")

upper.pack(fill=BOTH,expand=True)
lower.pack(fill=BOTH,expand=True)

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    root.title(f"blind coding - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    root.title(f"blind coding - {filepath}")

def ready():
    global isready
    txt_edit.configure(state='normal')
    isready=True

def finish(*args):
    global hid
    global isready
    frame1.place_forget()
    txt_edit.configure(state='disabled')
    hid= False
    isready=False


#upper section
    #logo
raw_data = urllib.request.urlopen('https://enigmavssut.com/static/media/logo.09be2b37.jpg').read()
im = Image.open(io.BytesIO(raw_data)).resize((300,225))
logo = ImageTk.PhotoImage(im)
logo_label=Label(upper,image=logo,bg='#000')
logo_label.pack(side=LEFT)

    #instruction section
instruction= Frame(upper,bg='#000')
instruction.pack(side=RIGHT,expand=True,fill=BOTH)
fr_buttons = Frame(instruction, bd=2,bg='#000')
fr_buttons.pack(side=BOTTOM)
# btn_open = Button(fr_buttons, text="Open", command=open_file)
# btn_save = Button(fr_buttons, text="Save As...", command=save_file)
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)hello world
# btn_save.grid(row=0, column=1, sticky="ew", padx=5)

btn_ready = Button(fr_buttons, text="Ready!", command=ready,bg='#74fc98')
btn_finish = Button(fr_buttons, text="Finish", command=finish, bg='red')
btn_ready.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_finish.grid(row=0, column=1, sticky="ew", padx=5)
#lower section

txt_edit = Text(lower,height=700,wrap=CHAR,padx=20,pady=20,state='disabled',bg='#363837',fg='#02db3c')
txt_edit.pack(fill=BOTH)

frame1= Frame(lower, bg= "#000000",height=750,width=5000)

def typehide(*args):
    global hid
    global isready
    if isready:
        frame1.place(x= 0, y=0)
        hid=True




def hide(*args):
    global hid
    if not hid:
        frame1.place(x= 0, y=0)
        hid=not hid

    else:
        frame1.place_forget()
        hid= not hid

txt_edit.bind('<Key>', typehide)


root.mainloop()

