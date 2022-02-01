# Desafío Tecnología Área de Desarrollo

Construir una aplicación web que permita obtener el valor de la UDIS y el dólar. Debe
cumplir las siguientes condiciones:

- Definir el rango de tiempo (fecha inicial y fecha final) a consultar.
- La información debe ser consumida desde el web service oficial de Banxico [Link](https://www.banxico.org.mx/SieAPIRest/service/v1/)
- El sistema debe responder desplegando los siguientes datos:
    - Los valores en pesos de las UDIS para cada día para el rango definido
    - El promedio, valor máximo y mínimo de las UDIS para el rango definido
    - Un gráfico que despliegue los valores de las UDIS para cada día para el rango definido
    - Los valores en pesos del dólar para cada día para el rango definido
    - El promedio, valor máximo y mínimo del dólar para el rango definido
    - Un gráfico que despliegue los valores del dólar para cada día para el rango definido
    

## Link de deploy para visualizar su funcionamiento

Link: [Demo](http://devkushiahu.pythonanywhere.com/)

## Instalación local

Se uso Python 3.10 y Django 4.0, para su uso local, se requiere de un entorno virtual, una vez activado el entorno virtual, puede ahora si realizar la instalación de las librerías que se requiere para su correcto funcionamiento. 

Dicho archivo se llama `requeriments.txt`

```bash
pip install -r requeriments.txt
```

Para su correcto uso local, verificar el archivo `__init__.py`, dentro la carpeta *banxico/settings/*

```python
# from .prod import *   -> este es para uso en prod
from .local import *
```

y con eso debería poder ya ejecutar el servidor de Django

```python
python manage.py runserver
```
