# ProjectMultivariados

Los paquetes de Python se instalan en `.venv`, dentro de esta carpeta del proyecto.

Para instalar las dependencias registradas:

```sh
uv --cache-dir .cache/uv sync --locked
```

Para ejecutar todas las celdas de `bloodactividad/blood.qmd` y renderizar el HTML:

```sh
sh render-blood.sh
```

El resultado se guarda en `bloodactividad/blood.html`, con las tablas y gráficas
incluidas. El script usa el Python de `.venv` y guarda las cachés en `.cache`.
Quarto debe estar instalado en el equipo.
