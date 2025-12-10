# 🖼️ Slovenski Meme Generator

Ta projekt implementira preprost spletni generator memov z uporabo ogrodja **Flask** in knjižnice **Pillow (PIL)** za obdelavo slik. Uporabniki lahko naložijo svojo sliko in dodajo zgornji ter spodnji besedilni napis, s čimer ustvarijo klasičen meme format z belim tekstom in črno obrobo za optimalno berljivost.

Aplikacija je pakirana v **Docker kontejner** za enostaven zagon v kateremkoli okolju.

## 🚀 Funkcionalnosti

* **Nalaganje slik:** Podpira nalaganje slik preko HTML obrazca.
* **Vnos besedila:** Omogoča vnos zgornjega in spodnjega besedila (klasičen meme format).
* **Generiranje mema:** Pillow obdela sliko, izračuna dinamično velikost pisave in nariše besedilo z obrobo.
* **Prikaz:** Generirani meme se neposredno vrne in prikaže v brskalniku.

## 📦 Zahteve

Za zagon projekta potrebujete:

1.  **Docker:** Nameščen in zagnan na vašem sistemu (Docker Desktop).
2.  **Git:** Za kloniranje repozitorija.
3.  **Pisava Impact:** Za doseganje klasičnega meme videza je priporočljivo, da imate datoteko `Impact.ttf` v korenskem direktoriju projekta.

## 🐳 Zagon z Dockerjem

Sledite tem korakom za zagon aplikacije v kontejnerju.

### 1. Kloniranje repozitorija

Najprej klonirajte projekt na svoj lokalni računalnik:

```bash
git clone https://github.com/Gburr1to/Slovenski-meme-generator.git
cd Slovenski-meme-generator 
```

### 2. Sestava (Build) Docker slike

Znotraj korenskega direktorija projekta, kjer se nahaja datoteka Dockerfile, sestavite Docker sliko.

    Opomba: Dockerfile poskrbi za namestitev vseh sistemskih odvisnosti (kot so libjpeg-dev, zlib1g-dev), ki jih Pillow potrebuje za obdelavo slik.

```bash
docker build -t meme-generator .
```

### 3. Zagon (Run) Docker kontejnerja

Zaženite kontejner in preslikajte notranji port 5000 (kjer posluša Flask) na zunanji port 5000 (ali kateri koli prosti port) na vašem gostiteljskem sistemu.
```bash
docker run -d -p 5000:5000 --name meme-app meme-generator
```

### 4. Dostop do aplikacije

Aplikacija je sedaj dostopna v vašem spletnem brskalniku:

http://localhost:8080


#### 🛠️ Tehnične podrobnosti in knjižnice

    Jezik: Python 3

    Okvir: Flask

    Obdelava slik: Pillow (PIL)

    Pisava: Impact (zahteva Impact.ttf v korenskem direktoriju)

Ključna prilagoditev za Docker

Da bi Flask deloval znotraj Dockerja, je bil v datoteki app.py vgrajeni razvojni strežnik konfiguriran tako, da posluša na vseh omrežnih vmesnikih:
```Python
# app.py (zadnji del)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
To omogoča, da je aplikacija dostopna izven Docker kontejnerja (preko naslova 0.0.0.0).
