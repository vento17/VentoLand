import os
ARC = "M-26.2,-42.6 A50,50 0 1 0 26.2,-42.6"
V = "M-43.2,-83.2 L0,20 L43.2,-83.2"
def svg(color, bg=None, flat=False, size=None):
    vb = "-55 -64 110 118" if not bg else "-64 -69 128 128"
    w = f' width="{size}" height="{int(size*118/110)}"' if size else ''
    bgr = f'<rect x="-64" y="-69" width="128" height="128" fill="{bg}"/>' if bg else ''
    if flat:
        stroke = color
        defs = ''
        vpath = "M-34.8,-63 L0,20 L34.8,-63"
    else:
        stroke = "url(#g)"
        defs = f'<defs><radialGradient id="g" gradientUnits="userSpaceOnUse" cx="0" cy="0" r="72"><stop offset="0.736" stop-color="{color}" stop-opacity="1"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs>'
        vpath = V
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{w}>{defs}{bgr}<g fill="none" stroke-width="6" stroke-linecap="butt" stroke-linejoin="miter"><path d="{ARC}" stroke="{color}"/><path d="{vpath}" stroke="{stroke}"/></g></svg>'''
files = {
 "public/logo/ventoland-white.svg": svg("#ffffff"),
 "public/logo/ventoland-black.svg": svg("#000000"),
 "public/logo/ventoland-flat-white.svg": svg("#ffffff", flat=True),
 "public/logo/ventoland-flat-black.svg": svg("#000000", flat=True),
 "public/favicon.svg": svg("#ffffff", bg="#0b0c0e", flat=True),
 "brand/ventoland-white-on-black.svg": svg("#ffffff", bg="#0b0c0e"),
 "brand/ventoland-black-on-white.svg": svg("#000000", bg="#ffffff"),
}
for p,c in files.items():
    open(p,"w").write(c)
print("ok")
