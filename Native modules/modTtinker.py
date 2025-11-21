'''import tkinter as mod

window = mod.Tk()
window.geometry("400x200")
window.title("Gerenciador")

fr = mod.Frame(window)
fr.pack(padx=100, pady=10, fill='x', expand=False)

lb = mod.Label(fr,text="Olá mundo")
lb.pack(fill='x', expand=True)

window.mainloop()'''

import tkinter as tk

window = tk.Tk()
window.geometry("200x200")
window.title("Cadastro do desenvolvedor")

fr = tk.Frame(window)
fr.pack(padx=100, pady=10, fill='x', expand=False)

lb = tk.Label(fr, text="Começe a desnvolver")
lb.pack()

window.mainloop()