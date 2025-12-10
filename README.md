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
git clone [https://github.com/Gburr1to/Slovenski-meme-generator.git](https://github.com/Gburr1to/Slovenski-meme-generator.git)
cd Slovenski-meme-generator
