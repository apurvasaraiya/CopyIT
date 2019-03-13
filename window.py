import tkinter as tk
from simulator import paste as pa
import threading
import queue
# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
# import Tkinter as tk
ff=True
def popup(ll):

    root = tk.Tk()

    # root.protocol("WM_DELETE_WINDOW", _delete_window)
    w = tk.Label(root, text="Select text to paste...")
    w.pack()
    l= tk.Listbox(root)
    l.pack()
    l.insert(1,ll[0])
    l.insert(2,ll[1])
    l.insert(3,ll[2])
    l.insert(4,ll[3])
    l.insert(5,ll[4])
    str1=''
    def exe():
        nonlocal str1
        str1=l.curselection()
        w1["text"]=ll[int(str1[0])]
        w1.pack()

    def dd(q):
        global ff
        root.destroy()
        ff= False
        q.put(ff)

    def paste():
        q=queue.Queue()
        if str1:
            # t1=threading.Thread(target=dd,args=(q,))
            dd(q)
            def pp(q):
                # while q.get():
                print(q.get())
                pa(ll[int(str1[0])])
            t2=threading.Thread(target=pp,args=(q,))
            # # t1.start()
            t2.start()
            # pa(ll[int(str1[0])])



    w1=tk.Label(root, text="")
    w1.pack()
    b1 = tk.Button(root, text='Select',command=exe)
    b1.pack()

    b2 = tk.Button(root, text='Paste',command=paste)
    b2.pack()

    root.mainloop()
