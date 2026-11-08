"""Bangun artifact.html dari index.html: python3 -I tools/build-artifact.py
Aturan Artifact: tanpa doctype/html/head/body, <title> di atas, GSAP dari cdnjs (versi dipatok),
font dari Google Fonts, warna lewat token, latar body eksplisit. index.html tetap sumber utama."""
import re, base64, pathlib
src = pathlib.Path('index.html').read_text()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
body = re.search(r'<body>(.*)</body>', src, re.S).group(1)
body = body.replace('<script src="vendor/gsap.min.js"></script>', '')
mp3 = base64.b64encode(pathlib.Path('audio/vo.mp3').read_bytes()).decode()
assert 'src="audio/vo.mp3"' in body
body = body.replace('src="audio/vo.mp3"', 'src="data:audio/mpeg;base64,' + mp3 + '"')
css = css.replace("html,body{width:100%;height:100%;background:#000;", "html,body{width:100%;height:100%;background:var(--bg);")
css = css.replace(":root{\n  --bg:#0A1517;", ":root{\n  --bg:#0A1517; color-scheme:dark;", 1)
assert 'color-scheme:dark' in css and 'background:var(--bg)' in css
head = '''<title>Yayasan Satu Tiang</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@500;600&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>''' + css + '</style>\n'
pathlib.Path('artifact.html').write_text(head + body.strip() + '\n')
print('artifact.html', len(head + body))
