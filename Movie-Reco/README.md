# Movie-Reco

Recomendador de películas – Actividad Parte 1 (MA2003B).

En este proyecto se completa el notebook `Recomendador_Pelis-Activity-1.ipynb`, donde se construyen tres tipos de recomendadores con datos de MovieLens / TMDB:

1. **Recomendador Simple:** ranking de películas con la calificación ponderada de IMDB (general y por género).
2. **Recomendador por descripción:** similitud entre sinopsis y esloganes usando TF-IDF y similitud del coseno.
3. **Recomendador por metadatos:** similitud usando género, director, actores principales y palabras clave, con un filtro final por calificación ponderada.

## Estructura

```
Movie-Reco/
├── Recomendador_Pelis-Activity-1.ipynb   # Notebook resuelto y ejecutado
├── movie-reco.yml                        # Ambiente de conda
└── data/
    ├── movies_metadata.csv
    ├── links_small.csv
    ├── keywords.csv
    ├── ratings_small.csv
    └── credits.csv.gz                    # Comprimido porque pesa más de 100 MB
```

> `credits.csv` se subió comprimido (`credits.csv.gz`) porque GitHub no permite archivos de más de 100 MB. pandas lo lee directamente, no es necesario descomprimirlo.

## Cómo correrlo

```bash
# 1. Crear el entorno a partir del archivo
conda env create --file movie-reco.yml

# 2. Activar el nuevo entorno
conda activate movie-reco

# 3. Abrir el notebook
jupyter notebook Recomendador_Pelis-Activity-1.ipynb
```
