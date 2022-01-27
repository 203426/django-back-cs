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