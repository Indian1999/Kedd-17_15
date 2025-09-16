import random
import tkinter
import tkinter.messagebox 

def generate_puzzle():
    puzzle = ""
    while len(puzzle) != 4:
        digit = random.randint(0, 9)
        if str(digit) not in puzzle:
            puzzle += str(digit)
    return puzzle

def check_tipp():
    global tippek
    tipp = textbox.get()
    if len(tipp) != 4 or not tipp.isdigit() or len(set(tipp)) != 4:
        tkinter.messagebox.showwarning("Hiba", "4 különböző számjegyet adj meg!")
        return
    jo_szamok = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)):
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok += 1
    tippek += 1
    if jo_szamok_jo_helyen == 4:
        result_label.config(text=f"Szép volt! {tippek} lépésből kitaláltad, hogy a megoldás {puzzle} volt.")
        textbox.config(state="disabled")
        btn_guess.config(state="disabled")
    else:
        feedback = f"{tipp}   ->    jó: {jo_szamok_jo_helyen},    más hely: {jo_szamok}"
        history.insert(tkinter.END, feedback)
        textbox.delete(0, tkinter.END)
    
puzzle = generate_puzzle() # pl.: 6843
tippek = 0

root = tkinter.Tk()
root.title("Színözön")

main_frame = tkinter.Frame(root)
main_frame.pack(pady=20, padx=20)

left_frame = tkinter.Frame(main_frame)
left_frame.grid(row=0, column=0, padx = (0, 20))

right_frame = tkinter.Frame(main_frame)
right_frame.grid(row = 0, column=1)

tkinter.Label(left_frame, text="Adj meg 4 különböző számjegyet:").pack(pady = 5, padx=5)

textbox = tkinter.Entry(left_frame)
textbox.pack(pady=5)
textbox.focus()
textbox.bind("<Return>", lambda event: check_tipp())

btn_guess = tkinter.Button(left_frame, text = "Tippelés", command=check_tipp)
btn_guess.pack(pady=5)

result_label = tkinter.Label(left_frame, text = "", fg="green")
result_label.pack(pady=5)

history = tkinter.Listbox(right_frame, width = 40, height=20)
history.pack(pady=10)


root.mainloop()