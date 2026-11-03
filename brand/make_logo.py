# Logo VentoLand definitivo (2026-11-03): due archi laterali sottili, V passante
# che sfuma sopra e resta piena sotto, con l'angolo interno appoggiato al cerchio.
ARCS = "M32.3,-38.1 A50,50 0 0 1 5.6,49.7 M-32.3,-38.1 A50,50 0 0 0 -5.6,49.7"
V = "M-43.2,-83.2 L0,58.5 L43.2,-83.2"
VFLAT = "M-33.6,-62.5 L0,58.5 L33.6,-62.5"   # versione piatta: aste tagliate dove finisce la sfumatura
def svg(color, bg=None, flat=False):
    # contenuto visibile: x ±53, y da -64 (fine sfumatura) a +69 (punta)
    vb = "-64 -70 128 140" if not bg else "-70 -70 140 140"
    bgr = f'<rect x="-70" y="-70" width="140" height="140" fill="{bg}"/>' if bg else ''
    if flat:
        vtop = f'<path d="{VFLAT}" stroke="{color}" stroke-width="6"/>'
        defs = ''
    else:
        defs = f'<defs><radialGradient id="g" gradientUnits="userSpaceOnUse" cx="0" cy="0" r="67"><stop offset="0.79" stop-color="{color}" stop-opacity="1"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient><clipPath id="t"><rect x="-80" y="-100" width="160" height="100"/></clipPath><clipPath id="b"><rect x="-80" y="0" width="160" height="100"/></clipPath></defs>'
        vtop = f'<path d="{V}" stroke="url(#g)" stroke-width="6" clip-path="url(#t)"/><path d="{V}" stroke="{color}" stroke-width="6" clip-path="url(#b)"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{defs}{bgr}<g fill="none" stroke-linecap="butt" stroke-linejoin="miter"><path d="{ARCS}" stroke="{color}" stroke-width="3"/>{vtop}</g></svg>'
files = {
 "public/logo/ventoland-white.svg": svg("#ffffff"),
 "public/logo/ventoland-black.svg": svg("#000000"),
 "public/logo/ventoland-flat-white.svg": svg("#ffffff", flat=True),
 "public/logo/ventoland-flat-black.svg": svg("#000000", flat=True),
 "public/favicon.svg": svg("#ffffff", bg="#0b0c0e", flat=True),
 "brand/ventoland-white-on-black.svg": svg("#ffffff", bg="#0b0c0e"),
 "brand/ventoland-black-on-white.svg": svg("#000000", bg="#ffffff"),
}
for p,c in files.items(): open(p,"w").write(c)
print("ok")
