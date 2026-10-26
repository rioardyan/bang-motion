"""Bangun artifact.html dari index.html: python3 -I tools/build-artifact.py
Aturan Artifact: tanpa doctype/html/head/body, <title> di atas, GSAP dari cdnjs (versi dipatok),
font dari Google Fonts, warna lewat token, latar body eksplisit. index.html tetap sumber utama."""
import re, pathlib
src = pathlib.Path('index.html').read_text()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1)
body = body.replace('<script src="vendor/gsap.min.js"></script>', '')
css = css.replace("html,body{width:100%;height:100%;background:#000;", "html,body{width:100%;height:100%;background:var(--bg);")
css = css.replace(":root{\n  --deep:", ":root{\n  --bg:#0C2A30; color-scheme:dark;\n  --deep:", 1)
assert '--bg:#0C2A30' in css and 'background:var(--bg)' in css
head = '''<title>Promo Organ Yayasan Estafet</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Instrument+Sans:wght@500;600;700&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>''' + css + '</style>\n'
pathlib.Path('artifact.html').write_text(head + body.strip() + '\n')
print('artifact.html', len(head + body))
