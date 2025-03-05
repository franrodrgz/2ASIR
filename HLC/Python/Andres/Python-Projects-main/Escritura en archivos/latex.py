from pylatex import Document, Section, Subsection, Command, Tabular, Figure
from pylatex.utils import NoEscape

#Andres Tenllado Perez

#Hacer esto primero en la terminal
#python3 -m venv mi_entorno  # Crear entorno
#source mi_entorno/bin/activate  # Activar en Linux/Mac
#mi_entorno\Scripts\activate  # Activar en Windows
#pip install pylatex  # Instalar paquetes dentro del entorno
#deactivate  # Salir del entorno

# Crear documento con clase "article"
doc = Document(documentclass="article")

# Agregar título, autor y fecha
doc.preamble.append(Command('title', 'Ejemplo Completo de Documento en LaTeX'))
doc.preamble.append(Command('author', 'Andres Tenllado Perez'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))  # Mostrar título en el documento

# Sección 1: Introducción
with doc.create(Section('Introducción')):
    doc.append('Este documento es un ejemplo más completo de cómo generar archivos en LaTeX desde Python usando la librería pylatex.\n')
    doc.append('Podemos incluir texto con formato como ')
    doc.append(NoEscape(r'\textbf{negrita}'))
    doc.append(', ')
    doc.append(NoEscape(r'\textit{itálica}'))
    doc.append(' y listas:\n')
    
    doc.append(NoEscape(r'\begin{itemize}'))
    doc.append(NoEscape(r'\item Primer punto de la lista'))
    doc.append(NoEscape(r'\item Segundo punto importante'))
    doc.append(NoEscape(r'\item Tercer punto final'))
    doc.append(NoEscape(r'\end{itemize}'))

# Sección 2: Matemáticas
with doc.create(Section('Ecuaciones Matemáticas')):
    doc.append('Podemos incluir ecuaciones matemáticas en LaTeX, por ejemplo, la famosa ecuación de Einstein:')
    doc.append(NoEscape(r'\begin{equation} E = mc^2 \end{equation}'))

# Sección 3: Tablas
with doc.create(Section('Tablas')):
    doc.append('Aquí hay una tabla de ejemplo:\n')
    
    with doc.create(Tabular('c c c')) as table:
        table.add_hline()
        table.add_row(["Columna 1", "Columna 2", "Columna 3"])
        table.add_hline()
        table.add_row(["A", "B", "C"])
        table.add_row(["D", "E", "F"])
        table.add_hline()

# Sección 4: Imágenes
with doc.create(Section('Imágenes')):
    doc.append('También podemos agregar imágenes en LaTeX. Asegúrate de que el archivo de imagen exista en el mismo directorio.\n')

    with doc.create(Figure(position='h!')) as fig:
        fig.add_image('latex.png', width=NoEscape(r'0.5\textwidth'))
        fig.add_caption('Ejemplo de una imagen en LaTeX.')

# Sección 5: Conclusión
with doc.create(Section('Conclusión')):
    doc.append('Este ejemplo muestra cómo generar documentos en LaTeX con Python incluyendo texto con formato, ecuaciones, tablas e imágenes.')

# Guardar archivo .tex
doc.generate_tex('ejemplo_completo_latex')

print("Archivo LaTeX generado: ejemplo_completo_latex.tex")

#Con el archivo ya creado
#Instalar
#sudo apt install latexmk
#Usar
#latexmk -pdf ejemplo_completo_latex.tex
