import tkinter as tk
from tkinter import filedialog
import zipfile 
import os

class BobZipFileViewer:
    def __init__(self, root):
        self.root = root
        self.root.title('Bob\'s ZipViewer') # Diagonal invertida (escape) convierte al siguiente caracter en ASCII
        self.root.geometry('888x600')
        self.root.resizable(0,0)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'archivo.png')
        image_path2 = os.path.join(script_dir, 'carpeta.png')
        self.btn1 = tk.PhotoImage(file=image_path)
        self.btn2 = tk.PhotoImage(file=image_path2)
        image_path3 = os.path.join(script_dir, 'apple.png')
        self.favicon = tk.PhotoImage(file=image_path3)
        self.root.iconphoto(True, self.favicon)
        self.root.call('wm', 'iconphoto', self.root._w, self.favicon)

        self.crear_ventana()
        

    def crear_ventana(self):


        panel1 = tk.Frame(self.root, bg="#199552")
        panel1.pack(side='top', fill=tk.X) 

        expnd = tk.Frame(panel1, width=350, bd=0, bg="#199552")
        expnd.pack(side='left', fill=tk.X) 

        self.boton = tk.Button(panel1, image=self.btn1, relief='flat', bd=0, command=self.cargar_zip, width=60, height=60, font=("Arial", 12, "bold"), fg="#fff", bg="#199552")
        self.boton.pack(side='left', padx=20, fill=tk.X)
        self.boton.config(cursor="hand2")

        self.extraer=tk.Button(panel1, image=self.btn2, relief='flat', bd=0, command=self.extraer_zip, width=60, height=60, fg="#fff", bg="#199552")
        self.extraer.pack(side='left', fill=tk.X)
        self.extraer.config(cursor="hand2")

        expnd = tk.Frame(panel1, width=300, bd=0, bg="#199552")
        expnd.pack(side='left', fill=tk.X) 

        panel2 = tk.Frame(self.root)
        panel2.pack(side='bottom', fill='both', expand=True)

        self.lista = tk.Listbox(panel2, selectmode='single')
        self.lista.pack(fill='both', expand=True)

       


    def cargar_zip(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[('Archivos .zip', '*.zip'), ('Todos los archivos', '*.*')])
        if ruta_archivo:
            self.archivo_zip = zipfile.ZipFile(ruta_archivo, 'r')
            self.lista.delete(0, tk.END)
            self.lista_zip = self.archivo_zip.namelist()
            for nombre_archivo in self.lista_zip:
                self.lista.insert(tk.END, nombre_archivo)
                

    def extraer_zip(self):
        indice = self.lista.curselection()
        if indice:
           indice = indice[0]
           archivo_seleccionado = self.lista_zip[indice]
           ruta_extraccion = filedialog.askdirectory()
           if ruta_extraccion:
               self.archivo_zip.extract(archivo_seleccionado, ruta_extraccion)
               tk.messagebox.showinfo('Extracción exitosa', f'El archivo {archivo_seleccionado} se extrajo en {ruta_extraccion}')     

if __name__=='__main__':
    root = tk.Tk()
    app = BobZipFileViewer(root)
    root.mainloop()



