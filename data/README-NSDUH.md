# Datos NSDUH 2023

El archivo `NSDUH_2023.txt.gz` contiene los mismos datos que
`NSDUH_2023.txt`, comprimidos sin pérdida. El archivo original ocupa
361.29 MiB y supera el límite por archivo de GitHub; el comprimido ocupa
27.68 MiB.

Para recuperar el TXT después de clonar el repositorio, ejecuta desde la
carpeta principal:

```sh
gzip -dk data/NSDUH_2023.txt.gz
```

Este comando conserva el comprimido. Si el TXT ya existe, no es necesario
volver a descomprimirlo. El TXT queda excluido de Git mediante `.gitignore`.

También puedes leer el archivo comprimido directamente con pandas:

```python
import pandas as pd

drugs = pd.read_csv("data/NSDUH_2023.txt.gz", sep="\t")
```

Esa ruta corresponde a ejecutar Python desde la carpeta principal del
repositorio. Si lo ejecutas desde `drogas/`, usa
`../data/NSDUH_2023.txt.gz`.
