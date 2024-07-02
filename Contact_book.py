from tkinter import *
from tkinter import ttk,messagebox
import os,csv,datetime
base=Tk()
base.title("Contactbook")
sw=base.winfo_screenwidth()
sh=base.winfo_screenheight()
base.geometry(f"{sw}x{sh}")
font_size=min(sw//30,sh//30)
mainfile=f"{os.path.dirname(os.path.abspath(__file__))}\\Contact_book.csv"
if not os.path.exists(mainfile): open(mainfile,"w",newline="").close()
#menubar
menubar=Menu(base)
base.config(menu=menubar)
#menubar funcns
def switch():
    if len(tr.selection())==0:
        for i in [" Add contact "," Update contact "," Delete contact ","Sort"]:
            if i in [" Add contact ","Sort"]: menubar.entryconfig(i,state="normal")
            else :menubar.entryconfig(i,state="disabled")
    else:
        for i in [" Add contact "," Update contact "," Delete contact ","Sort"]:
            if i in [" Add contact ","Sort"]: menubar.entryconfig(i,state="disabled")
            else :menubar.entryconfig(i,state="normal")
        if len(tr.selection())!=1:menubar.entryconfig(" Update contact ",state="disabled")
def insertitem():
    clear()
    treefile=open(mainfile)
    item=list(csv.reader(treefile))
    item=sorted(item,key=lambda x: str(x[int(v.get())]),reverse=int(var.get()))
    a=[1]
    for i in item:
        a.extend(i)
        tr.insert("",END,iid=a[0],values=a)
        a=[a[0]+1]
def stringcheck(name):
    alp=0
    for i in name :
        if ord(i) in range(65,90) or ord(i) in range(97,122) :alp+=1
    if alp: return True
    return False
def add():
    def submit(n,p,e,d):
        with open(mainfile)as mfill:
            r=list(csv.reader(mfill))
        if n and p and e and d:
            na=0
            if stringcheck(n):
                if p.isdigit():
                    if "@" in e and "." in e :
                        for i in r:
                            if [n,p,e] == i[0:3]:na+=1
                        if na==0:
                            with open(mainfile,"a",newline="") as file:
                                writer=csv.writer(file)
                                writer.writerow([n.title().strip(),p,e.lower().strip().replace(" ",""),d])
                            insertitem()
                            auwin.destroy()
                        else:l1.config(text="Contact Already Exist");l1.after(1400,lambda:l1.configure(text=""))
                    else: l1.config(text="Invalid Email");l1.after(1400,lambda:l1.configure(text=""))
                else:l1.config(text="Ph no. field can only contain digits ");l1.after(1400,lambda:l1.configure(text=""))
            else: l1.config(text="Name should consist atleast 1 alphabet");l1.after(1400,lambda:l1.configure(text=""))
        else:l1.config(text="Empty Field(s) are not allowed");l1.after(1400,lambda:l1.configure(text=""))
    auwin=Toplevel(base)
    auwin.focus_force()
    auwin.resizable(False,False)
    auwin.title("Add Contact")
    for i,j in {"Name: ":1,"Phone no.: ":2,"Email: ":3}.items():
        Label(auwin,text=i,font=("Times",font_size-10)).grid(row=j,column=0)
        e1=Entry(auwin,font=("Times",font_size-10))
        e1.focus_force()
        e2=Entry(auwin,font=("Times",font_size-10))
        e3=Entry(auwin,font=("Times",font_size-10))
        b1=Button(auwin,text="Add",font=("Times",font_size-10),command=lambda:[submit(e1.get().title(),str(e2.get()).strip(),e3.get(),datetime.datetime.now())])
        b2=Button(auwin,text="Cancel",font=("Times",font_size-10),command=auwin.destroy)
        l1=Label(auwin,fg="red")
        e1.grid(row=1,column=1,sticky=W,padx=15,pady=5,columnspan=2)
        e2.grid(row=2,column=1,sticky=W,padx=15,pady=5,columnspan=2)
        e3.grid(row=3,column=1,sticky=W,padx=15,pady=5,columnspan=2)
        b1.grid(row=4,column=1,sticky=E,padx=10,pady=5)
        b2.grid(row=4,column=2,sticky=E,padx=10,pady=5)
        l1.grid(row=5,column=0,sticky=W,padx=10,pady=5)
def clear():
    for item in tr.get_children():
        tr.delete(item)
def delete():
    m=messagebox.askyesno("Deletion","Are you sure you want to delete all selected items",icon="warning")
    if m==True:
        a=[tr.item(i)["values"][1:] for i in tr.selection()]
        for i in a:
            for j in range(len(i)):
                i[j]=str(i[j])
        b=[]
        with open(mainfile)as mfil:
            for i in csv.reader(mfil):
                if i not in a:b.append(i)
        with open(mainfile,"w",newline="")as mfil:
            wr=csv.writer(mfil)
            wr.writerows(b)
        insertitem()
def update(): 
    def submit(n,p,e,d):
        with open(mainfile)as mfill:
            r=list(csv.reader(mfill))
        lst,na=[],0
        if n and p and e and d:
            if stringcheck(n):
                if p.isdigit():
                    if "@" in e and "." in e :
                        for i in r:
                            if ab[1:4] != i[0:3]:lst.append(i)
                            if [n,p,e] == i[0:3]:na+=1
                        if na==0:
                            with open(mainfile,"w",newline="") as file:
                                writer=csv.writer(file)
                                lst.append([n.title().strip(),p,e.lower().strip().replace(" ",""),d])
                                writer.writerows(lst)
                            insertitem()
                            auwin.destroy()
                        else:l1.config(text="You are trying to enter same or existing contact again");l1.after(1400,lambda:l1.configure(text=""))
                    else: l1.config(text="Invalid Email");l1.after(1400,lambda:l1.configure(text=""))
                else:l1.config(text="Ph no. field can only contain digits ");l1.after(1400,lambda:l1.configure(text=""))
            else: l1.config(text="Name should consist atleast 1 alphabet");l1.after(1400,lambda:l1.configure(text=""))
        else:l1.config(text="Empty Field(s) are not allowed");l1.after(1400,lambda:l1.configure(text=""))
    auwin=Toplevel(base)
    auwin.focus_force()
    auwin.resizable(False,False)
    auwin.title("Add Contact")
    ab=[str(i) for i in tr.item(tr.selection())["values"]]
    for i,j in {"Name: ":1,"Phone no.: ":2,"Email: ":3}.items():
        Label(auwin,text=i,font=("Times",font_size-10)).grid(row=j,column=0)
        e1=Entry(auwin,font=("Times",font_size-10))
        e1.insert(0,str(ab[j]));e1.config(state=DISABLED)
        e1.grid(row=j,column=1,sticky=W,padx=15,pady=5,columnspan=2)
    for i,j in {"Name: ":4,"Phone no.: ":5,"Email: ":6}.items():
        Label(auwin,text=i,font=("Times",font_size-10)).grid(row=j,column=0)
        e1=Entry(auwin,font=("Times",font_size-10))
        e1.focus_force()
        e2=Entry(auwin,font=("Times",font_size-10))
        e3=Entry(auwin,font=("Times",font_size-10))
        b1=Button(auwin,text="Update",font=("Times",font_size-10),command=lambda:[submit(e1.get().title(),e2.get().strip(),e3.get(),datetime.datetime.now())])
        b2=Button(auwin,text="Cancel",font=("Times",font_size-10),command=auwin.destroy)
        l1=Label(auwin,fg="red")
        e1.grid(row=4,column=1,sticky=W,padx=15,pady=5,columnspan=2)
        e2.grid(row=5,column=1,sticky=W,padx=15,pady=5,columnspan=2)
        e3.grid(row=6,column=1,sticky=W,padx=15,pady=5,columnspan=2)
        b1.grid(row=7,column=1,sticky=E,padx=10,pady=5)
        b2.grid(row=7,column=2,sticky=E,padx=10,pady=5)
        l1.grid(row=8,column=0,sticky=W,padx=10,pady=5)
def showshrt():
    swin=Toplevel(base)
    di={"Ctrl A": "To select all records","Escape": "To deselect the selected ones","Delete": "To delete the selected records"}
    for j,i in enumerate(di,start=0):
        Label(swin, text=f"{j+1}").grid(row=j,column=1,padx=5,pady=5)
        Label(swin,text=f"{i}").grid(row=j,column=2,sticky=W,padx=5,pady=5)
        Label(swin,text=f"{di[i]}").grid(row=j,column=3,sticky=W,padx=5,pady=5)
# menubar functions
menubar.add_command(label=" Add contact ",command=add)
menubar.add_command(label=" Delete contact ",command=delete,state=DISABLED)
menubar.add_command(label=" Update contact ",command=update,state=DISABLED)
search=Menu(menubar,tearoff=0)
#sortmenu
sortmenu=Menu(menubar,tearoff=0)
v=IntVar(value=0)
sortmenu.add_radiobutton(variable=v,value=0,label="Name",command=insertitem)
sortmenu.add_radiobutton(variable=v,value=1,label="Phone no.",command=insertitem)
sortmenu.add_radiobutton(variable=v,value=2,label="Email",command=insertitem)
sortmenu.add_radiobutton(variable=v,value=3,label="Acc to Date Created",command=insertitem)
sortmenu.add_separator()
var=IntVar(value=0)
sortmenu.add_radiobutton(label="A -> Z", variable=var, value=0,command=insertitem)
sortmenu.add_radiobutton(label="Z -> A", variable=var, value=1,command=insertitem)
menubar.add_cascade(label="Sort",menu=sortmenu)
menubar.add_command(label="Shortcuts",command=showshrt)
scr=Scrollbar(base)
scr.pack(side=RIGHT,fill=Y)
fr = Frame(base,width=sw,height=sh ,relief="solid")
fr.pack(fill=BOTH, padx=10, pady=10)
style=ttk.Style()
style.theme_use('clam')
tr=ttk.Treeview(fr,height=sh,selectmode = "extended",show="headings",yscrollcommand=scr.set)
tr['columns']=("Sr no.","Name","Phone no.","Email")
for i in tr['columns']:
    tr.column(i,minwidth=240)
    tr.heading(i,text=i,anchor=CENTER)
insertitem()
style = ttk.Style()
style.configure("Treeview.Heading", font=("Times",font_size-10, "italic"))
tr.pack(side=LEFT,expand=True,fill=BOTH)
scr.configure(command=tr.yview)
tr.bind("<<TreeviewSelect>>",lambda event:switch())
def selall(cmd):
    [cmd(x) for x in tr.get_children()]
    switch()
base.bind("<Control-a>",lambda event:[selall(tr.selection_add)])
base.bind("<Escape>",lambda event:[selall(tr.selection_remove)])
base.bind("<Delete>",lambda event : delete() if tr.selection() else None)
base.mainloop()