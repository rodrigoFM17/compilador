#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from tkinter.font import Font

# Importamos los analizadores
try:
    from lexClaude import AnalizadorLexico, Token, TipoToken
    from sintaticClaude import AnalizadorSintactico, Nodo, ErrorSintactico
    from semanticClaude import AnalizadorSemantico, TipoDato, ErrorSemantico
except ImportError:
    messagebox.showerror("Error de importación", "No se pudieron importar los módulos de análisis. Asegúrese de que lexClaude.py, sintaticClaude.py y semanticClaude.py estén en el mismo directorio.")
    sys.exit(1)

class AnalizadorApp:
    """Aplicación para el análisis léxico, sintáctico y semántico de código."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador de Lenguaje")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Configurar el estilo
        self.configurar_estilo()
        
        # Crear los widgets principales
        self.crear_menu()
        self.crear_widgets()
        
        # Variables para almacenar resultados de análisis
        self.tokens = []
        self.ast = None
        self.errores_semanticos = []
        
        # Archivo actual
        self.archivo_actual = None
        
        # Configuración inicial
        self.actualizar_titulo()
    
    def configurar_estilo(self):
        """Configura el estilo de la aplicación."""
        # Crear un estilo ttk
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0")
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TNotebook", background="#f0f0f0")
        self.style.configure("TNotebook.Tab", font=("Arial", 10))
        
        # Fuente para el editor y las áreas de resultado
        self.fuente_editor = Font(family="Consolas", size=11)
        self.fuente_resultados = Font(family="Consolas", size=10)
        
    def crear_menu(self):
        """Crea la barra de menú de la aplicación."""
        menu_bar = tk.Menu(self.root)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menu_bar, tearoff=0)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_command(label="Guardar como", command=self.guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        
        # Menú Analizar
        menu_analizar = tk.Menu(menu_bar, tearoff=0)
        menu_analizar.add_command(label="Análisis Léxico", command=self.ejecutar_analisis_lexico)
        menu_analizar.add_command(label="Análisis Sintáctico", command=self.ejecutar_analisis_sintactico)
        menu_analizar.add_command(label="Análisis Semántico", command=self.ejecutar_analisis_semantico)
        menu_analizar.add_separator()
        menu_analizar.add_command(label="Análisis Completo", command=self.ejecutar_analisis_completo)
        menu_bar.add_cascade(label="Analizar", menu=menu_analizar)
        
        # Menú Ayuda
        menu_ayuda = tk.Menu(menu_bar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
        
        self.root.config(menu=menu_bar)
    
    def crear_widgets(self):
        """Crea los widgets principales de la aplicación."""
        # Crear panel principal con dos secciones
        self.panel_principal = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.panel_principal.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Panel izquierdo para editor de código
        self.panel_editor = ttk.Frame(self.panel_principal)
        self.panel_principal.add(self.panel_editor, weight=1)
        
        # Panel derecho para resultados
        self.panel_resultados = ttk.Frame(self.panel_principal)
        self.panel_principal.add(self.panel_resultados, weight=1)
        
        # Configurar panel del editor
        self.configurar_panel_editor()
        
        # Configurar panel de resultados
        self.configurar_panel_resultados()
        
        # Barra de estado
        self.barra_estado = ttk.Label(self.root, text="Listo", relief=tk.SUNKEN, anchor=tk.W)
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
    
    def configurar_panel_editor(self):
        """Configura el panel del editor de código."""
        # Etiqueta
        ttk.Label(self.panel_editor, text="Editor de Código").pack(pady=(0, 5))
        
        # Editor de código
        self.editor = scrolledtext.ScrolledText(self.panel_editor, wrap=tk.WORD, font=self.fuente_editor)
        self.editor.pack(fill=tk.BOTH, expand=True)
        
        # Barra de botones
        panel_botones = ttk.Frame(self.panel_editor)
        panel_botones.pack(fill=tk.X, pady=5)
        
        ttk.Button(panel_botones, text="Nuevo", command=self.nuevo_archivo).pack(side=tk.LEFT, padx=2)
        ttk.Button(panel_botones, text="Abrir", command=self.abrir_archivo).pack(side=tk.LEFT, padx=2)
        ttk.Button(panel_botones, text="Guardar", command=self.guardar_archivo).pack(side=tk.LEFT, padx=2)
        ttk.Button(panel_botones, text="Analizar", command=self.ejecutar_analisis_completo).pack(side=tk.LEFT, padx=2)
    
    def configurar_panel_resultados(self):
        """Configura el panel de resultados del análisis."""
        # Notebook para diferentes pestañas de resultados
        self.notebook = ttk.Notebook(self.panel_resultados)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña para resultados léxicos
        self.tab_lexico = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_lexico, text="Análisis Léxico")
        
        # Pestaña para resultados sintácticos
        self.tab_sintactico = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_sintactico, text="Análisis Sintáctico")
        
        # Pestaña para resultados semánticos
        self.tab_semantico = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_semantico, text="Análisis Semántico")
        
        # Pestaña para errores
        self.tab_errores = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_errores, text="Errores")
        
        # Área de resultados léxicos
        self.area_lexico = scrolledtext.ScrolledText(self.tab_lexico, wrap=tk.WORD, font=self.fuente_resultados)
        self.area_lexico.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Área de resultados sintácticos
        self.area_sintactico = scrolledtext.ScrolledText(self.tab_sintactico, wrap=tk.WORD, font=self.fuente_resultados)
        self.area_sintactico.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Área de resultados semánticos
        self.area_semantico = scrolledtext.ScrolledText(self.tab_semantico, wrap=tk.WORD, font=self.fuente_resultados)
        self.area_semantico.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Área de errores
        self.area_errores = scrolledtext.ScrolledText(self.tab_errores, wrap=tk.WORD, font=self.fuente_resultados)
        self.area_errores.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.area_errores.tag_configure("error", foreground="red")
    
    def actualizar_titulo(self):
        """Actualiza el título de la ventana con el nombre del archivo actual."""
        if self.archivo_actual:
            self.root.title(f"Analizador de Lenguaje - {os.path.basename(self.archivo_actual)}")
        else:
            self.root.title("Analizador de Lenguaje - Nuevo Archivo")
    
    def nuevo_archivo(self):
        """Crea un nuevo archivo de código."""
        if self.editor.get("1.0", tk.END).strip():
            if not messagebox.askyesno("Confirmar", "¿Desea descartar los cambios actuales?"):
                return
        
        self.editor.delete("1.0", tk.END)
        self.archivo_actual = None
        self.actualizar_titulo()
        self.limpiar_resultados()
        self.barra_estado.config(text="Nuevo archivo creado")
    
    def abrir_archivo(self):
        """Abre un archivo de código existente."""
        if self.editor.get("1.0", tk.END).strip():
            if not messagebox.askyesno("Confirmar", "¿Desea descartar los cambios actuales?"):
                return
        
        archivo = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if archivo:
            try:
                with open(archivo, "r") as f:
                    contenido = f.read()
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", contenido)
                self.archivo_actual = archivo
                self.actualizar_titulo()
                self.limpiar_resultados()
                self.barra_estado.config(text=f"Archivo abierto: {os.path.basename(archivo)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
    
    def guardar_archivo(self):
        """Guarda el código actual en el archivo actual."""
        if not self.archivo_actual:
            return self.guardar_como()
        
        try:
            with open(self.archivo_actual, "w") as f:
                f.write(self.editor.get("1.0", tk.END))
            self.barra_estado.config(text=f"Archivo guardado: {os.path.basename(self.archivo_actual)}")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
            return False
    
    def guardar_como(self):
        """Guarda el código actual en un nuevo archivo."""
        archivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if archivo:
            self.archivo_actual = archivo
            self.actualizar_titulo()
            return self.guardar_archivo()
        return False
    
    def limpiar_resultados(self):
        """Limpia todas las áreas de resultados."""
        self.area_lexico.delete("1.0", tk.END)
        self.area_sintactico.delete("1.0", tk.END)
        self.area_semantico.delete("1.0", tk.END)
        self.area_errores.delete("1.0", tk.END)
        self.tokens = []
        self.ast = None
        self.errores_semanticos = []
    
    def ejecutar_analisis_lexico(self):
        """Ejecuta el análisis léxico del código actual."""
        codigo = self.editor.get("1.0", tk.END)
        self.area_lexico.delete("1.0", tk.END)
        self.area_errores.delete("1.0", tk.END)
        
        try:
            analizador = AnalizadorLexico(codigo)
            self.tokens = analizador.analizar()
            
            self.area_lexico.insert("1.0", "=== ANÁLISIS LÉXICO ===\n\n")
            for token in self.tokens:
                self.area_lexico.insert(tk.END, f"{token}\n")
            
            self.barra_estado.config(text="Análisis léxico completado")
            self.notebook.select(self.tab_lexico)
            return True
        except Exception as e:
            self.area_errores.insert("1.0", f"Error en análisis léxico: {str(e)}\n", "error")
            self.barra_estado.config(text="Error en análisis léxico")
            self.notebook.select(self.tab_errores)
            return False
    
    def ejecutar_analisis_sintactico(self):
        """Ejecuta el análisis sintáctico usando los tokens del análisis léxico."""
        if not self.tokens:
            if not self.ejecutar_analisis_lexico():
                return False
        
        self.area_sintactico.delete("1.0", tk.END)
        
        try:
            analizador = AnalizadorSintactico(self.tokens)
            self.ast = analizador.analizar()
            
            if self.ast:
                self.area_sintactico.insert("1.0", "=== ANÁLISIS SINTÁCTICO ===\n\n")
                self.area_sintactico.insert(tk.END, "Análisis sintáctico completado con éxito.\n\n")
                self.area_sintactico.insert(tk.END, "=== ÁRBOL SINTÁCTICO ===\n\n")
                self.imprimir_ast(self.ast)
                
                self.barra_estado.config(text="Análisis sintáctico completado")
                self.notebook.select(self.tab_sintactico)
                return True
            else:
                self.area_errores.insert(tk.END, "Error en análisis sintáctico: No se pudo generar el AST\n", "error")
                self.barra_estado.config(text="Error en análisis sintáctico")
                self.notebook.select(self.tab_errores)
                return False
        except ErrorSintactico as e:
            self.area_errores.insert(tk.END, f"Error sintáctico: {str(e)}\n", "error")
            self.barra_estado.config(text="Error en análisis sintáctico")
            self.notebook.select(self.tab_errores)
            return False
        except Exception as e:
            self.area_errores.insert(tk.END, f"Error inesperado en análisis sintáctico: {str(e)}\n", "error")
            self.barra_estado.config(text="Error en análisis sintáctico")
            self.notebook.select(self.tab_errores)
            return False
    
    def ejecutar_analisis_semantico(self):
        """Ejecuta el análisis semántico usando el AST del análisis sintáctico."""
        if not self.ast:
            if not self.ejecutar_analisis_sintactico():
                return False
        
        self.area_semantico.delete("1.0", tk.END)
        
        try:
            analizador = AnalizadorSemantico(self.ast)
            resultado = analizador.analizar()
            self.errores_semanticos = analizador.errores
            
            self.area_semantico.insert("1.0", "=== ANÁLISIS SEMÁNTICO ===\n\n")
            
            if resultado:
                self.area_semantico.insert(tk.END, "Análisis semántico completado con éxito.\n")
                self.area_semantico.insert(tk.END, "No se encontraron errores semánticos.\n")
                self.barra_estado.config(text="Análisis semántico completado")
            else:
                self.area_semantico.insert(tk.END, "Errores semánticos encontrados:\n")
                for error in self.errores_semanticos:
                    self.area_semantico.insert(tk.END, f"  - {error}\n")
                    self.area_errores.insert(tk.END, f"Error semántico: {error}\n", "error")
                self.barra_estado.config(text="Análisis semántico completado con errores")
            
            self.notebook.select(self.tab_semantico)
            return resultado
        except Exception as e:
            self.area_errores.insert(tk.END, f"Error en análisis semántico: {str(e)}\n", "error")
            self.barra_estado.config(text="Error en análisis semántico")
            self.notebook.select(self.tab_errores)
            return False
    
    def ejecutar_analisis_completo(self):
        """Ejecuta el análisis léxico, sintáctico y semántico en secuencia."""
        self.limpiar_resultados()
        
        if self.ejecutar_analisis_lexico():
            if self.ejecutar_analisis_sintactico():
                if self.ejecutar_analisis_semantico():
                    messagebox.showinfo("Análisis Completo", "Análisis completado con éxito. No se encontraron errores.")
                else:
                    messagebox.showwarning("Análisis Completo", "Análisis completado con errores semánticos.")
            else:
                messagebox.showwarning("Análisis Completo", "Análisis sintáctico fallido.")
        else:
            messagebox.showwarning("Análisis Completo", "Análisis léxico fallido.")
    
    def imprimir_ast(self, nodo, nivel=0):
        """Imprime el AST en el área de resultados sintácticos."""
        if not nodo:
            return
        
        prefijo = "  " * nivel
        
        if isinstance(nodo, Nodo):
            self.area_sintactico.insert(tk.END, f"{prefijo}{nodo.tipo}\n")
            for hijo in nodo.hijos:
                self.imprimir_ast(hijo, nivel + 1)
        else:
            tipo = nodo.tipo.name if hasattr(nodo, 'tipo') and hasattr(nodo.tipo, 'name') else str(nodo)
            lexema = nodo.lexema if hasattr(nodo, 'lexema') else str(nodo)
            self.area_sintactico.insert(tk.END, f"{prefijo}[{tipo}] '{lexema}'\n")
    
    def mostrar_acerca_de(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo(
            "Acerca de",
            "Analizador de Lenguaje\n\n"
            "Versión 1.0\n\n"
            "Este programa realiza análisis léxico, sintáctico y semántico de código.\n\n"
            "Desarrollado como parte del curso de Compiladores."
        )


def main():
    """Función principal para iniciar la aplicación."""
    root = tk.Tk()
    app = AnalizadorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()