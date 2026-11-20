"""Bangun artifact.html dari index.html: python3 -I tools/build-artifact.py
Aturan Artifact: tanpa doctype/html/head/body, <title> di atas, GSAP dari cdnjs (versi dipatok),
font dari Google Fonts, warna lewat token, latar body eksplisit. index.html tetap sumber utama."""
import re, pathlib
src = pathlib.Path('index.html').read_text()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1)
body = body.replace('<script src="vendor/gsap.min.js"></script>', '')
css = css.replace("html,body{width:100%;height:100%;background:#000;", "html,body{width:100%;height:100%;background:var(--page);")
css = css.replace(":root{\n  --night:", ":root{\n  --page:#06171B; color-scheme:dark;\n  --night:", 1)
assert '--page:#06171B' in css and 'background:var(--page)' in css
head = '''<title>Pengurus Pesantren Satu Tiang</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>''' + css + '</style>\n'
pathlib.Path('artifact.html').write_text(head + body.strip() + '\n')
print('artifact.html', len(head + body))
