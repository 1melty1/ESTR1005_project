import tkinter as tk
root = tk.Tk()
root.title('ESTR1005 Group 5 Nash Equilibrium Calculator')
root.geometry('500x500')
root.configure(background='black')

def Layout_setup():
    #when the set btn is pressed again, all previous things are cleared
    for widget in Frame2.winfo_children():
        widget.destroy()
    for widget in Frame3.winfo_children():
       widget.destroy()
    m = int(row_size_entry.get())
    n = int(col_size_entry.get())
    global payoff
    payoff = []
    for i in range(n):
        line = []
        for j in range(m):
            if(i==0):
                temp = tk.Label(Frame2, text=j+1, fg='lime', bg='black')
                temp.grid(row=j+1, column=0)
            if(j==0):
                temp = tk.Label(Frame2, text=i+1, fg='lime', bg='black')
                temp.grid(row=0, column=i+1)
            temporarytext1 = tk.StringVar()
            temp = tk.Entry(Frame2, width=3, textvariable=temporarytext1)
            temp.grid(row=j+1, column=i+1, padx=1, pady=1)
            line.append(temporarytext1)
        payoff.append(line)

    calculate_btn = tk.Button(Frame3, text='Calculate', highlightbackground='grey', bg='grey', fg='lime', command=CalNash)
    calculate_btn.grid(row=j+2, column = int(i/2+1))

def CalNash():
    global payoff
    a = [[int(j.get()) for j in i] for i in payoff]
    print(a)


Frame1 = tk.Frame(root, bg="Grey")
Frame1.grid() #upper half
Frame2 = tk.Frame(root, bg="black")
Frame2.grid() #mid half
Frame3 = tk.Frame(root, bg="black")
Frame3.grid() #lower half



row_size_label = tk.Label(Frame1, text='Enter row player strategy number:', bg='grey', fg='lime')
row_size_label.grid(row=0, column=0)
row_size_entry = tk.Entry(Frame1, bg='grey', fg='white')
row_size_entry.grid(row=0, column=1)

col_size_label = tk.Label(Frame1, text='Enter column player strategy number:', bg='grey', fg='lime')
col_size_label.grid(row=1, column=0)
col_size_entry = tk.Entry(Frame1, bg='grey', fg='white')
col_size_entry.grid(row=1, column=1)

set_size_btn = tk.Button(Frame1, text='Set size', highlightbackground='grey', bg='grey', fg='lime', command=Layout_setup)
set_size_btn.grid(row=2, column = 1)

root.mainloop()