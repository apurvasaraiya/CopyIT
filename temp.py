import tkinter as tk
from simulator import paste as pa

# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
# import Tkinter as tk

list1=[]
str1=''

class test(tk.Tk):

    def destroy(self):
        print("Yo!",list1)
        super().destroy()
        pa(list1[int(str1[0])])


def popup(ll):

    global list1
    list1=ll
    root = test()
    # root.protocol("WM_DELETE_WINDOW", _delete_window)
    # def _destroy(event):
    #     print("Destroyed...")
    #     pa(ll[int(str1[0])])
    #
    # root.bind("<Destroy>", _destroy)




    w = tk.Label(root, text="Select text to paste...")
    w.pack()
    l= tk.Listbox(root)
    l.pack()
    l.insert(1,ll[0])
    l.insert(2,ll[1])
    l.insert(3,ll[2])
    l.insert(4,ll[3])
    l.insert(5,ll[4])
    def exe():
        global str1
        str1=l.curselection()
        w1["text"]=list1[int(str1[0])]
        w1.pack()

    def paste():

        if str1:
            print("iiiii")
            root.destroy()
            print("***")
            # pa(ll[int(str1[0])])



    w1=tk.Label(root, text="")
    w1.pack()
    b1 = tk.Button(root, text='Select',command=exe)
    b1.pack()

    b2 = tk.Button(root, text='Paste',command=paste)
    b2.pack()

    root.mainloop()
