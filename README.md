># RegistroPeticiones

## Descripción del proyecto

Este proyecto tiene como finalidad registrar las peticiones hechas en Remedy por los diferentes usuarios.

- Siendo esta guardada en archivos `.csv`.
- Este junta la infomacion de los seridores 1, 2, 4 y 5. 

## Estado del proyecto

Este proyecto actualmente se encuentra en uso y está desplegado en el ambiente de desarrollo.

## Requerimientos

Se recomienda encarecidamente respetar estos puntos para poder usar la aplicación de forma correcta:

-   Tener instalado Python 2.7.5

## Ejecutar

Para ejecutar esta aplicación basta con solo seleccionar el botón para ejecutar incluido en el IDE donde se abra esta app.

## Despliegue en el servidor

Para desplegar la aplicación, se requiere colocar los archivos `conOra.py`, `tabla.py` y `CrearTabla.sh` en el servidor de aplicaciones, siguiendo estos pasos:

1.  Accede al servidor de aplicaciones.
2.  Navega hasta la ubicación `/home/remedy/RegistroPeticiones/Serv_(el numero del servidor)` del servidor.
3.  Eliminar o renombrar los arhcivos `conOra.py`, `tabla.py` y `CrearTabla.sh`.
4.  En la anterior ruta mencionada, coloca los arhcivos `conOra.py`, `tabla.py` y `CrearTabla.sh`, ubicado en la ruta `/RegistroPeticiones/*` del proyecto.

## Importante 

Aunque este proyecto se encuentre en el servidor de desarrollo es el proyecto final.
