#!/bin/bash

ls 1>"$1.txt" #Lee los archivos del directorio y los guarda en un archivo

#ls 2> errores.txt        # Solo errores
#ls 1> out.txt 2> err.txt # Stdout y stderr por separado
#ls > todo.txt 2>&1       # Ambos al mismo archivo
