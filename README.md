# PriceTracker CAC 2023

Proyecto Django. Para trabajar desde otra maquina, clonar este repositorio y usar Python 3.11 con Pipenv, segun el Pipfile.

```powershell
pipenv sync
Copy-Item Pricetracker/.env.example Pricetracker/.env
```

Completar `Pricetracker/.env` con una `SECRET_KEY` propia antes de ejecutar Django. Con el settings actual, dejar `DEBUG` vacio lo desactiva; un valor no vacio lo activa. La configuracion y la base local estan excluidas de Git.

Para crear una base SQLite local nueva y arrancar el servidor de desarrollo:

```powershell
pipenv run python Pricetracker/manage.py migrate
pipenv run python Pricetracker/manage.py runserver
```

Los registros y las credenciales del entorno anterior no se transfieren al clonar. Las ramas `Gabriel` e `ivan` contienen cambios de rutas pendientes de una decision funcional antes de integrarlos.
