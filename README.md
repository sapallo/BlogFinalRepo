Blog en Django

Este proyecto es una aplicación web de blog construida con el framework Django, en
el marco del curso Informatorio impulsado por el Gobierno de la Provincia del Chaco,
Argentina.
Permite a los usuarios registrados crear, editar y eliminar publicaciones, así como navegar por diferentes categorías, comentar publicaciones, y gestionar su perfil de usuario. También incluye una interfaz de administración para moderar contenido y usuarios.

Características

Autenticación de Usuarios: Registro, inicio de sesión y gestión de perfiles.
Publicaciones de Blog: Creación, edición y eliminación de entradas por parte de los usuarios.
Categorías: Organización de las publicaciones por categorías.
Comentarios: Los usuarios registrados pueden comentar en las publicaciones.
Cargar Imágenes: Posibilidad de subir imágenes para las publicaciones y los perfiles.
Moderación: Sistema de administración para gestionar el contenido y los usuarios.
Paginación: Navegación por las publicaciones mediante un sistema de páginas.
Requisitos Previos

Requisitos

Python 3.8 o superior
Django 3.0 o superior
pip (para instalar las dependencias)
Una base de datos (MySQL por defecto)

Uso

1. Página principal
La página principal muestra una lista de las publicaciones más recientes. Los usuarios pueden navegar por las publicaciones, hacer clic para leer una publicación completa y ver los comentarios.

2. Autenticación de usuarios
Los usuarios pueden registrarse, iniciar sesión y gestionar su perfil desde la barra de navegación. Los usuarios no autenticados solo podrán ver las publicaciones, pero no podrán crear ni comentar.

3. Crear y editar publicaciones
Una vez autenticado, un usuario puede crear una nueva publicación desde el botón "Crear publicación". También podrá editar o eliminar sus propias publicaciones desde la vista de detalles de cada entrada.

4. Comentarios
Los usuarios registrados pueden dejar comentarios en las publicaciones. Los comentarios pueden ser moderados desde el panel de administración.

