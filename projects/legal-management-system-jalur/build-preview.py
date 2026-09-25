# Gabungkan index.html + vendor/ menjadi satu berkas mandiri (preview.html) untuk dipratinjau di aplikasi.
import base64,re,pathlib
d=pathlib.Path(__file__).parent
html=(d/'index.html').read_text()
css=(d/'vendor/fonts.css').read_text()
css=re.sub(r'url\((fonts/[^)]+)\)',lambda m:'url(data:font/woff2;base64,'+base64.b64encode((d/'vendor'/m.group(1)).read_bytes()).decode()+')',css)
gsap=(d/'vendor/gsap.min.js').read_text()
html=html.replace('<link rel="stylesheet" href="vendor/fonts.css">','<style>'+css+'</style>')
html=html.replace('<script src="vendor/gsap.min.js"></script>','<script>'+gsap+'</script>')
assert 'vendor/' not in html
(d/'preview.html').write_text(html)
print('preview.html',len(html)//1024,'KB')

# Versi Artifact (halaman claude.ai): tanpa kerangka doctype/html/head/body, judul berupa nama.
import sys
if len(sys.argv)>1:
    a=html
    for t in ['<!doctype html>','<html lang="id">','<head>','</head>','<body>','</body>','</html>','<meta charset="utf-8">']:
        a=a.replace(t,'')
    a=a.replace('<title>Jalur Legal Management System</title>','<title>Jalur Legal Management System</title>')
    a=a.replace('html,body{width:100%;height:100%;background:#0E1C1E;overflow:hidden}',
                'html,body{width:100%;height:100%;background:#0E1C1E;overflow:hidden;color-scheme:dark}')
    pathlib.Path(sys.argv[1]).write_text(a.strip()+'\n')
    print('artifact',sys.argv[1])
