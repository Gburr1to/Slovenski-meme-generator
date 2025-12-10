FROM python:3.12-slim
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    # Po namestitvi POČISTIMO, da zmanjšamo velikost slike!\
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
# Uporaba cachea: Če se requirements.txt ni spremenil, se ta korak preskoči.
RUN pip install --no-cache-dir -r requirements.txt

# Kopiramo vse ostale datoteke (app.py, templates/, Impact.ttf).
COPY . .

# Okoljske spremenljivke
# Nastavimo PORT na privzeto vrednost za Flask.
ENV PORT=5000

# Informiramo Docker, da bo kontejner poslušal na tem portu.
EXPOSE 5000

# Definiramo ukaz, ki se izvede, ko se kontejner zažene.
# Uporabimo Python in app.py.
CMD ["python3", "app.py"]