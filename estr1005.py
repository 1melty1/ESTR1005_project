import tkinter as tk
import numpy as np
from fractions import Fraction

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
    for widget in Frame4.winfo_children():
       widget.destroy()
    for widget in Frame5.winfo_children():
       widget.destroy()
    n = int(game_size.get())
    precision = int(precision_input.get())
    payoff = []
    precision_show_label = tk.Label(Frame2, text=f"Precision is: {precision}", fg='lime', bg='black')
    precision_show_label.grid(row=0, column=0)
    for i in range(n):
        line = []
        for j in range(n):
            if(i==0):
                temp = tk.Label(Frame3, text=j+1, fg='lime', bg='black')
                temp.grid(row=j+1, column=0)
            if(j==0):
                temp = tk.Label(Frame3, text=i+1, fg='lime', bg='black')
                temp.grid(row=0, column=i+1)
            temporarytext1 = tk.StringVar()
            temp = tk.Entry(Frame3, width=3, textvariable=temporarytext1)
            temp.grid(row=i+1, column=j+1, padx=1, pady=1)
            line.append(temporarytext1)
        payoff.append(line)

    calculate_btn = tk.Button(Frame4, text='Calculate', highlightbackground='grey', bg='grey', fg='lime', command=lambda: CalNash(n, payoff, precision))
    calculate_btn.grid(row=j+2, column = int(i/2+1))

def DNE(error):
    nash_label = tk.Label(Frame5, text='Nash equilibrium does not exist or cannot be calculated using this algorithm', bg='black', fg='red')
    nash_label.grid(row=1, column=0, sticky='W')
    error_label = tk.Label(Frame5, text=error, bg='black', fg='red')
    error_label.grid(row=2, column=0, sticky='W')

def CalNash(n, payoff, precision):
    a = [[int(j.get()) for j in i] for i in payoff]
    A = np.array(a)
    print("a", a) #for testing
    b = np.ones(n)
    print("x", b) #for testing

    if(np.linalg.det(A)<=0):
        DNE("Not full-rank payoff matrix / Nash equilibrium does not exist")
        return
    row_optimal_strategy = np.linalg.solve(np.transpose(A), b)
    row_optimal_strategy = row_optimal_strategy * (1/np.sum(row_optimal_strategy))
    col_optimal_strategy = np.linalg.solve(A, b)
    col_optimal_strategy =  col_optimal_strategy = col_optimal_strategy * (1/np.sum(col_optimal_strategy)) #probability have to add up to 1
    print("row_optimal_strategy:", row_optimal_strategy)
    print("col_optimal_strategy:", col_optimal_strategy)
    if(not (all(prob >=0 for prob in row_optimal_strategy) and all(prob >=0 for prob in row_optimal_strategy))):
        DNE("Nash equilibrium does not exist")
        return

    ShowAns(row_optimal_strategy, col_optimal_strategy, precision)

def ShowAns(row_optimal_strategy, col_optimal_strategy, precision):
    #check if all probability greater thanor equal to 0

    #formatting output
    row_optimal_strategy_approx = ""
    row_optimal_strategy_exact = str(row_optimal_strategy)
    col_optimal_strategy_approx = ""
    col_optimal_strategy_exact = str(col_optimal_strategy)

    for prob in np.nditer(row_optimal_strategy):
         #limit the size of denominator to prevent accuracy of conversion problem
        row_optimal_strategy_approx += str(Fraction(prob.item(0)).limit_denominator(max_denominator=10*precision)) + '   '
    for prob in np.nditer(col_optimal_strategy):
        col_optimal_strategy_approx += str(Fraction(prob.item(0)).limit_denominator(max_denominator=10*precision)) + '   '

    for symbol, formatted in {'[':'', ']':''}.items():
        row_optimal_strategy_exact = row_optimal_strategy_exact.replace(symbol, formatted)
        col_optimal_strategy_exact = col_optimal_strategy_exact.replace(symbol, formatted)

    for widget in Frame5.winfo_children(): #refresh
        widget.destroy()

    nash_label = tk.Label(Frame5, text='Nash equilibrium', bg='black', fg='red')
    nash_label.grid(row=1, column=0, sticky='W')

    row_text_label = tk.Label(Frame5, text=f'Optimal strategy for row player(Approximate Fraction): ', bg='black', fg='red')
    row_text_label.grid(row=2, column=0, sticky='W')

    row_ans_label = tk.Label(Frame5, text=row_optimal_strategy_approx, bg='black', fg='red')
    row_ans_label.grid(row=2, column=1, sticky='W')

    col_text_label = tk.Label(Frame5, text=f'Optimal strategy for col player(Approximate Fraction): ', bg='black', fg='red')
    col_text_label.grid(row=3, column=0, sticky='W')

    col_ans_label = tk.Label(Frame5, text=col_optimal_strategy_approx, bg='black', fg='red')
    col_ans_label.grid(row=3, column=1, sticky='W')
    
    row_text_label = tk.Label(Frame5, text=f'Optimal strategy for row player(Exact): ', bg='black', fg='red')
    row_text_label.grid(row=4, column=0, sticky='W')

    row_ans_label = tk.Label(Frame5, text=row_optimal_strategy_exact, bg='black', fg='red')
    row_ans_label.grid(row=4, column=1, sticky='W')

    col_text_label = tk.Label(Frame5, text=f'Optimal strategy for col player(Exact): ', bg='black', fg='red')
    col_text_label.grid(row=5, column=0, sticky='W')

    col_ans_label = tk.Label(Frame5, text=col_optimal_strategy_exact, bg='black', fg='red')
    col_ans_label.grid(row=5, column=1, sticky='W')

Frame1 = tk.Frame(root, bg="Grey")
Frame1.grid() #setup layout
Frame2 = tk.Frame(root, bg="Grey")
Frame2.grid() #display precision
Frame3 = tk.Frame(root, bg="black")
Frame3.grid() #payoff matrix layout
Frame4 = tk.Frame(root, bg="black")
Frame4.grid() #calculate button layout
Frame5 = tk.Frame(root, bg="black")
Frame5.grid() #answer layout



game_size_label = tk.Label(Frame1, text='Row & column player strategy number:', bg='grey', fg='lime')
game_size_label.grid(row=0, column=0, sticky='W')
game_size = tk.Entry(Frame1, bg='grey', fg='white')
game_size.grid(row=0, column=1)

precision_label = tk.Label(Frame1, text='Maximum digits of denominator for fraction display(recommended 5):', bg='grey', fg='lime')
precision_label.grid(row=1, column=0, sticky='W')
precision_input = tk.Entry(Frame1, bg='grey', fg='white')
precision_input.grid(row=1, column=1)

set_size_btn = tk.Button(Frame1, text='Set size', highlightbackground='grey', bg='grey', fg='lime', command=Layout_setup)
set_size_btn.grid(row=2, column = 1)

root.mainloop()