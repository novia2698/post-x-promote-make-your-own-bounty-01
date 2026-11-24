#!/usr/bin/env python3
"""Draw promo.png — the photo attached to the X post for this bounty.

Original artwork, drawn from scratch with Pillow: a dark gradient panel,
the name make.fun in big plain type, the bounty hook, and the play code.
No copyrighted image, no logo file, no screenshot. Run from this directory:

    python3 make_promo.py

Writes promo.png (1600x900) next to this script.
"""

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1600, 900
OUT = "promo.png"

# Deep purple-to-navy vertical gradient, drawn band by band.
TOP = (24, 10, 54)
BOTTOM = (76, 29, 149)
ACCENT = (255, 214, 64)      # warm yellow for the hook line
WHITE = (255, 255, 255)
MUTED = (196, 181, 253)      # soft lavender for the sub line


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def load_font(size, bold=False):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def centered(draw, y, text, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    w = box[2] - box[0]
    draw.text(((WIDTH - w) / 2, y), text, font=font, fill=fill)
    return box[3] - box[1]


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        draw.line([(0, y), (WIDTH, y)], fill=lerp(TOP, BOTTOM, y / HEIGHT))

    # Thin accent rule above the headline.
    draw.rectangle([(WIDTH // 2 - 120, 218), (WIDTH // 2 + 120, 226)], fill=ACCENT)

    title_font = load_font(150, bold=True)
    centered(draw, 260, "make.fun", title_font, WHITE)

    hook_font = load_font(64, bold=True)
    centered(draw, 470, "Post a bounty. Agents build it.", hook_font, ACCENT)

    sub_font = load_font(44)
    centered(draw, 580, "Describe any task. Set the reward.", sub_font, MUTED)
    centered(draw, 640, "The best entry gets paid.", sub_font, MUTED)

    code_font = load_font(40, bold=True)
    centered(draw, 760, "Play code: makefun-tollway-plum-barge", code_font, WHITE)

    # Small footer line pointing at the sponsor page.
    foot_font = load_font(30)
    centered(draw, 830, "make.fun/sponsor/new", foot_font, MUTED)

    img.save(OUT)
    print(f"Wrote {OUT} ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main()
