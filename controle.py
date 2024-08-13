import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_sales():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for sale in fetch_sales():
        tree.insert("", tk.END, values=sale)

def periodic_update():
    update_treeview()
    root.after(5000, periodic_update)

root = tk.Tk()
root.title("Visualizador de Vendas")
root.geometry("1000x600")
root.configure(bg='#ff007f')

# Estilo do Canvas para Gradiente
canvas = tk.Canvas(root, width=1000, height=600, bg='#ff007f', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Gradiente do Canvas
canvas.create_rectangle(0, 0, 1000, 600, fill='#ff007f', outline='')
canvas.create_rectangle(0, 0, 1000, 300, fill='#ff004f', outline='')
canvas.create_rectangle(0, 300, 1000, 600, fill='#ff007f', outline='')

# Frame principal com bordas arredondadas
main_frame = tk.Frame(root, bg='#ff004f', padx=20, pady=20, bd=0, relief='flat')
main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)

# Título
title = tk.Label(main_frame, text="Visualizador de Vendas", font=('Arial', 24, 'bold'), bg='#ff004f', fg='#ffffff')
title.pack(pady=(0, 20))

# Treeview
columns = ('ID', 'Vendedor', 'Produto', 'Quantidade', 'Preço')
tree = ttk.Treeview(main_frame, columns=columns, show='headings', style='Treeview')
tree.heading('ID', text='ID')
tree.heading('Vendedor', text='Vendedor')
tree.heading('Produto', text='Produto')
tree.heading('Quantidade', text='Quantidade')
tree.heading('Preço', text='Preço')

tree.column('ID', width=100, anchor='center')
tree.column('Vendedor', width=200, anchor='center')
tree.column('Produto', width=200, anchor='center')
tree.column('Quantidade', width=150, anchor='center')
tree.column('Preço', width=150, anchor='center')

# Adicionando Treeview e Scrollbars no Frame principal
tree.pack(fill=tk.BOTH, expand=True)

vsb = tk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side='right', fill='y')

hsb = tk.Scrollbar(main_frame, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(side='bottom', fill='x')

# Botão de Atualização com bordas arredondadas
refresh_button = tk.Button(main_frame, text="Atualizar", command=update_treeview, font=('Arial', 14, 'bold'), bg='#ff007f', fg='#ffffff', relief='flat', padx=20, pady=10)
refresh_button.pack(pady=20)
refresh_button.config(borderwidth=0, highlightthickness=0)

# Estilo da Treeview
style = ttk.Style()
style.configure('Treeview',
                background='#ffffff',
                foreground='#333333',
                fieldbackground='#ffffff',
                font=('Arial', 12))
style.configure('Treeview.Heading',
                background='#ff007f',
                foreground='#ffffff',
                font=('Arial', 14, 'bold'))

# Estilo do botão
style.configure('TButton',
                background='#ff007f',
                foreground='#ffffff',
                font=('Arial', 14, 'bold'))

# Adicionando uma sombra ao botão
def add_shadow(widget):
    widget.bind("<Enter>", lambda e: widget.config(bg='#e6006c'))
    widget.bind("<Leave>", lambda e: widget.config(bg='#ff007f'))

add_shadow(refresh_button)

periodic_update()  # Atualiza a vista periodicamente

root.mainloop()
