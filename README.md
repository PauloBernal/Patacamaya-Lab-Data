# Guía para usar el compilador

Compilador de datos de laboratorio creado por *PauloBA*

Para compilar los archivos de texto con los datos del laboratorio es necesario tener el intérprete de Python instalado en el sistema. En caso de ya tener instalado el programa se procede a ejecutar el archivo `compiler.py`. Si llegara a haber un error se deben verificar las siguientes **condiciones**:

- El compilador debe estar en la misma carpeta que los archivos con los datos de laboratorio
- Los archivos con los datos deben tener extensión `.txt`
- Los archivos con los datos no pueden ser archivos binarios ni tener puntos (`.`) en el nombre del archivo aparte del que marca la extensión del mismo
- Si no se generara de forma automática se debe crear una carpeta con el nombre `compile` en el mismo directorio que el compilador

Si no fuera registrado ningún problema al momento de compilar los archivos estos deberían aparecer dentro de la carpeta `compile`. El archivo compilado aparecerá con el formato `cmp_*NOMBRE ORIGINAL*.txt`, siendo de esta forma fácil de reconocer respecto al archivo de origen.
