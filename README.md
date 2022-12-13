# Proyecto Final 
Realizado por Villalba Portunato Matias

El proyecto esta basado en un Blog/Foro, en donde los usuarios pueden registrarse, 
loguearse y crear Publicaciones(Posts) las cuales las van a poder visualizar a todas,
las categorias estan pre establecidas por el administrador de la pagina.

Una vez creado las publicaciones(Posts), estos van a poder verse en el boton del navbar.
Luego pueden ver con mas detalle cada una para poder ver el contenido escrito por los autores,
podran ser eliminados o actualizados solo si el autor creo dicho Post.

Tambien puede actualizar la informacion del perfil, cambiar la clave, eliminar el usuario y
desloguearse.

Por fines didacticos se hay un usuario administrador, user: admin y clave: admin



## Home

En la pagina del home, se va a mostrar una imagen con un mensaje de bienvenida.

## Botones: Navbar

En el navbar se pueden apreciar 6 botones, 5 botones primarios y 1 es un boton desplegable

### Registrarse

Este boton nos permite registrarnos al Blog/Foro ya que si no estamos registrados solo podremos ver el home.

### Login

Una vez registrados se autoridigira al login, dando un mensaje si el usuario se creo correctamente, para poder ingresar con nuestra cuenta


### Desplegable-usuario

Este boton sera visible una vez que iniciemos sesion en nuestra pagina, y este desplegara
las opciones: Perfil, Admin, Logout.
La opcion de Admin solo sera visible si el usuario es superusuario, sino no es visible.

Las otras opciones seran explicadas mas abajo

### Agregar Post
Este boton nos va a servir cuando estemos logueados poder crear nuestro Post el cual 
nos va a pedir unos datos para poder crearlo, luego nos rededirigira a los Posts ya
creados
## Ver Posts

Cuando vayamos a ver los posts creados por los usuarios veremos que podremos ver el detalle, elimianar o actualizar


### Ver Posts: Detalle
Esta opcion solo sera visible cuando queramos ver mas en detalle los posts, ya que 
los posts no se ve el cuerpo de la imagenes.

Una vez que le de en detalles vera las mismas 2 teclas de antes (eliminar, actualizar),
Ya que se dejaron en ambos lados por default.


## Botones: Perfil

Podremos ver nuestro perfil, informacion basica de nuestro usuario, donde podremos verlo
y ademas seran visibles 3 opciones: Cambio de clave, Cambiar Contraseña y Eliminar Usuario

Estas 3 opciones seran explicadas luego.

### Perfil: Cambio de clave

El usuario podra cambiar la informacion de su perfil. Nombre, Apellido, Email, Username

### Perfil: Admin

Si el usuario es superusuario podra visualizar este boton, que este llevara directamente
al django-admin


### Perfil: Logout

El usuario podra cerrar sesion de su cuenta, cuando suceda eso se lo va a redirigir a una pagina
donde va a encontrarse con un template diciendo: Has cerrado sesion


## Botones: Informacion

Estos botones se componen de 5, en el cual se encuentran el About, Contact, Terms Of Use,
Privacy Policy y el de LinkedIn.

### About
Este boton muestra un poco sobre el autor del proyecto final, el trabajo que esta realizando
y un poco su meta a futuro.

### Contact ; Terms of Use ; Privacy Policy

Estos se encuentran por el momento sin informacion, con lo cual se renderiza en los 3
un html que dice: No hay paginas aun

### LinkedIn

Este boton al hacer click nos lleva al LinkedIn del autor del proyecto
## Installation

### virtualenv

Vamos a suponer que ya se tiene instalado Python3, pip y virtualenv.

Con lo cual restaria crear el entorno virtual para levantar nuestro servidor.

En el mismo nivel que se encuentra la carpeta MVT:

C:\EntregaFinalVillalbaPortunato\MVT

Se va ejecutar el siguiente comando en nuestra powershell:
```
  virtualenv venv

```
Luego activamos el entorno virtual:
```
  .\venv\Scripts\activate

```
Una vez activo entramos a la carpeta MVT
```
  cd MVT

```
Y por ultimo iniciamos el servidor con este comando (este paso lo realizaremos Luego
de haber leido los demas pasos de instalacion ya que sino nos dara error al querer
iniciar nuestro servidor):
```
  python manage.py runserver

```

### Decouple

Para instalar decouple necesitaremos ejecutar lo siguiente:
```
pip install python-decouple
```
Lo que se va a realizar a continuacion se hace para poder nosotros poder hacer un gitignore
al archivo .env que vamo a crear y asi no subir a github nuestra SECRET_KEY y el DEBUG

Necesitamos instalar una libreria de Python, podemos instalarla global o en nuestro entorno virtual.
Esto lo dejo a criterio de cada uno.

Una vez instalado abriremos nuestro settings.py y pegaremos este import:
```
from decouple import config
```

Vamos a necesitar crear un archivo con extension .env en el directorio MVT

El cual deberemos de copiar desde nuestro settings.py las constantes:

SECRET_KEY ; DEBUG

Debemos copiar todo, hasta su valor y las pegaremos en nuestro archivo creado .env
Ahi lo que haremos va a ser borrar el espaciado y las comillas
```
SECRET_KEY = 'valor' DEBUG = 'valor'
```
Quedando asi: 
```
SECRET_KEY=valor
```
Replicamos lo mismo con DEBUG 
```
DEBUG=valor
```

Luego volveremos a nuestro settings.py y lo que haremos va a ser donde estaba SECRET_KEY y DEBUG

Lo remplazaremos y por este valor:
```
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
```

### Pillow

Estando con el entorno virtual activado debemos de instalar Pillow para la manipulacion de nuestras imagenes.

Ejecutaremos el siguiente comando:
```
pip install Pillow
```

### ckeditor

Por ultimo se debe de instalar ckeditor en el entorno virtual para la manipulacion del
texto, ya que tiene herramientas para poner en negrita, adjuntar fotos, etc.
```
pip install django-ckeditor
```
## FAQ

#### ¿Por que la guia de instalacion es muy breve y solo a un SO?

Por el momento la guia de instalacion esta orientada a Windows ya que es el SO que poseo,
ademas de eso es breve ya que esta orientada a un publico que ya posee los recursos para
abrir Django, de igual manera se va a ampliar mas en un futuro.



## About Us

Actualmente me ocupo trabajando como soporte nivel 1 en una empresa terciarizada para la
cuenta de MercadoLibre.

Entre a coderhouse para poder desempeñarme en un futuro cercano como desarrollador backend

El proyecto fue realizado de manera individual, solamente por mi, ya que no tuve grupo:



Villalba Portunato Matias
