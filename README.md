# CRUD-DJANGO

# Proyecto Concesionario de Autos
Este es un proyecto Django para gestionar un concesionario de autos, donde puedes administrar marcas, modelos, clientes, ventas, servicios, seguros, garantías, mantenimientos y reparaciones de autos, entre otros.

# Requisitos Previos
Python 3.x instalado localmente.
Entorno virtual recomendado para la gestión de dependencias.
Instalación
# Clona este repositorio en tu máquina local: 


Copiar código
git clone <[URL-del-repositorio](https://github.com/prondonp/CRUD-DJANGO.git)>
cd nombre-del-repositorio
Crea un entorno virtual para el proyecto (opcional pero recomendado):


Copiar código
python -m venv env
Activa el entorno virtual (para Windows):


Copiar código
.\env\Scripts\activate
Para sistemas basados en Unix/Linux:


Copiar código
source env/bin/activate
Instala las dependencias del proyecto:


Copiar código
pip install -r requirements.txt
Realiza las migraciones de la base de datos:


Copiar código
python manage.py makemigrations
python manage.py migrate
Crea un superusuario para acceder al panel de administración:


Copiar código
python manage.py createsuperuser
Inicia el servidor de desarrollo:


Copiar código
python manage.py runserver
Accede al panel de administración en tu navegador web:


Copiar código
http://127.0.0.1:8000/admin/
Utiliza las credenciales del superusuario creado para iniciar sesión y gestionar los datos del concesionario.

Uso
Este proyecto utiliza Django Admin para gestionar los modelos de datos. Puedes crear, leer, actualizar y eliminar registros para marcas, modelos, clientes, ventas, servicios, seguros, garantías, mantenimientos y reparaciones de autos.
