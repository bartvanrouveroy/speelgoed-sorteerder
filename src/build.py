import pathlib
root=pathlib.Path(__file__).parent
src=(root/'src/app.src.html').read_text()
q=(root.parent/'libs/qrcode.min.js').read_text(); j=(root.parent/'libs/jsqr.min.js').read_text()
assert '</script' not in q.lower() and '</script' not in j.lower()
out=src.replace('/*QRCODE_LIB*/','/* qrcode-generator (MIT, Kazuhiko Arase) */\n'+q).replace('/*JSQR_LIB*/','/* jsQR (Apache-2.0, Cosmo Wolfe) */\n'+j)
d=root/'dist'; d.mkdir(exist_ok=True)
(d/'index.html').write_text(out)
print(len(out))
