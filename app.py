import io
import textwrap
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Pot do klasične meme pisave (Impact).
# PISAVA MORA BITI V ISTEM DIREKTORIJU!
try:
    FONT_PATH = "Impact.ttf"  # Zamenjajte s potjo do Impact.ttf
    FONT = ImageFont.truetype(FONT_PATH, 120)
except IOError:
    # Če pisava ni na voljo, uporabimo privzeto
    FONT = ImageFont.load_default()


def generate_meme(image_file, top_text, bottom_text):
    """
    Funkcija za obdelavo slike in dodajanje besedila.
    """
    # Odpremo sliko, ki je poslana kot datoteka (v pomnilniku)
    img = Image.open(image_file).convert('RGB')
    width, height = img.size

    # Prilagodimo velikost pisave glede na širino slike
    font_size = int(width / 10)
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
    except:
        font = ImageFont.load_default(font_size)

    draw = ImageDraw.Draw(img)

    # Barve: Bel tekst z črno obrobo
    text_color = "white"
    stroke_color = "black"
    stroke_width = int(font_size / 20)

    # Funkcija za risanje besedila na določeni lokaciji
    def draw_text_with_stroke(draw, text, position, font, text_color, stroke_color, stroke_width):
        x, y = position
        # Zavijanje besedila, da se prilega širini
        wrapped_text = textwrap.wrap(text, width=int(width / (font_size * 0.6)))
        text_lines = "\n".join(wrapped_text)

        # Izračun dimenzij besedila za centriranje
        bbox = draw.textbbox((0, 0), text_lines, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Centriranje X-koordinate
        x_centered = (width - text_width) / 2

        # Risanje obrobe (konture)
        for dx, dy in [(stroke_width, 0), (-stroke_width, 0), (0, stroke_width), (0, -stroke_width), #gre skozi vseh 8 smeri, gor, dol, levo
                       (stroke_width, stroke_width), (-stroke_width, -stroke_width), #desno, robovi, se vsepovsod piše črna barva
                       (stroke_width, -stroke_width), (-stroke_width, stroke_width)]: #-za iluzijo večjega teksta
            draw.text((x_centered + dx, y + dy), text_lines, font=font, fill=stroke_color, align="center")

        # Risanje samega besedila
        draw.text((x_centered, y), text_lines, font=font, fill=text_color, align="center")
        return text_height

    # Dodajanje zgornjega teksta
    # Y-koordinata je skoraj na vrhu (npr. 2% višine)
    draw_text_with_stroke(draw, top_text.upper(), (0, height * 0.02), font, text_color, stroke_color, stroke_width)

    # Dodajanje spodnjega teksta
    # Najprej izračunamo višino spodnjega teksta, da ga lahko pravilno postavimo
    # Uporabimo začasni DrawingContext za izračun višine
    temp_draw = ImageDraw.Draw(Image.new('RGB', (width, height)))
    # Izračunamo višino spodnjega teksta
    wrapped_text = textwrap.wrap(bottom_text.upper(), width=int(width / (font_size * 0.6)))
    text_lines = "\n".join(wrapped_text)
    bbox = temp_draw.textbbox((0, 0), text_lines, font=font)
    bottom_text_height = bbox[3] - bbox[1]

    # Y-koordinata za spodnji tekst (tik nad dnom)
    bottom_y = height - bottom_text_height - (height * 0.05)
    draw_text_with_stroke(draw, bottom_text.upper(), (0, bottom_y), font, text_color, stroke_color, stroke_width)

    # Shranimo sliko v pomnilnik in jo vrnemo (IO-tok)
    byte_io = io.BytesIO()
    img.save(byte_io, 'JPEG')
    byte_io.seek(0)
    return byte_io


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Prejem datoteke in podatkov
        if 'slika' not in request.files or request.files['slika'].filename == '':
            return "Napaka: Prosim, izberite sliko.", 400

        image_file = request.files['slika']
        top_text = request.form.get('zgornji_tekst', '')
        bottom_text = request.form.get('spodnji_tekst', '')

        # 2. Obdelava (generiranje mema)
        try:
            meme_io = generate_meme(image_file, top_text, bottom_text)
        except Exception as e:
            # Vrnitev napake v primeru težav z obdelavo slike
            return f"Napaka pri obdelavi slike: {e}", 500

        # 3. Vrnitev slike
        # Generirani mem vrnemo kot datoteko, ki jo brskalnik prikaže
        return send_file(meme_io, mimetype='image/jpeg')

    # GET zahteva prikaže HTML obrazec
    return render_template('index.html')


if __name__ == '__main__':
    # Za zagon: python app.py
    app.run(host='0.0.0.0', port=5000, debug=True)