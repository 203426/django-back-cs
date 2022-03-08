# Ambientación del back Django

## Instalación del recurso de restframework librerias

```bash
pip install djangorestframework
```
```bash
pip install markdown
```
```bash
pip install django-filter
```

## Agregar la libretia a INSTALLED_APPS en settings
```bash
'rest_framework',
```

## Instalamos python-dotenv para ocultar credenciales importantes 
```bash
pip install python-dotenv
```
<!-- Se Agrega a settings para el uso de la libreria-->
```bash
from dotenv import load_dotenv
import os

load_dotenv()
```

## Instalamos Pillow para la gestión de las imagenes
```bash
pip install Pillow
```
<!-- Agregamos el nuevo componente a settings  -->
```bash
'loadImg',
```
## Instalamos Cors-headers para permitir el consumo de la api 
```bash
python -m pip install django-cors-headers
```
<!-- Agregamos el nuevo componente a settings  -->
```bash
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```
```bash
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```
```bash
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',   
]
```