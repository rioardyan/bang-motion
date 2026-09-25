import re,sys
SRC='projects/promo-6/index.html'
LP='projects/lp-pajak/lp_pajak_v1_asli.html'
GSAP='gsap.min.js'  # unduh dari npm gsap@3.12.5/dist
OUT='projects/lp-pajak/lp_pajak_v2.html'
s=open(SRC).read()
css=re.search(r'<style>(.*?)</style>',s,re.S).group(1)
body=re.search(r'<body>\s*(.*?)\s*<div id="ui">',s,re.S).group(1)
js=re.search(r'<script>\n(.*?)</script>',s,re.S).group(1)
ids=sorted(set(re.findall(r'id="([^"]+)"',body)),key=len,reverse=True)
P='d6-'
def pref(txt):
    for i in ids: txt=re.sub(r'#'+re.escape(i)+r'(?![\w-])','#'+P+i,txt)
    return txt
# --- HTML: id prefiks
body=re.sub(r'id="([^"]+)"',lambda m:'id="'+P+m.group(1)+'"',body)
# --- CSS: buang aturan global, jadikan lingkup .d6
css=css.replace(':root{','.d6{')
css=re.sub(r'\*\{margin:0;padding:0;box-sizing:border-box\}','',css)
css=re.sub(r'html,body\{[^}]*\}','',css)
css=re.sub(r'#ui\{[^}]*\}\s*#ui\.on\{[^}]*\}#scrub\{[^}]*\}','',css)
css=css.replace('#stage{position:fixed;left:50%;top:50%;width:1080px;height:1350px;transform:translate(-50%,-50%);overflow:hidden;',
                '#stage{position:absolute;left:0;top:0;width:1080px;height:1350px;transform-origin:0 0;overflow:hidden;')
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
css=pref(css)
out=[]
for rule in css.split('}'):
    if '{' not in rule: continue
    sel,decl=rule.split('{',1)
    sel=','.join(('.d6' if x.strip()=='.d6' else '.d6 '+x.strip()) for x in sel.split(','))
    out.append(sel+'{'+decl.strip()+'}')
css='\n'.join(out)
css+='\n.d6,.d6 *{box-sizing:border-box;margin:0;padding:0}'
css+='\n.d6-box{position:relative;width:100%;max-width:480px;margin:28px auto 0;aspect-ratio:1080/1350;border-radius:18px;overflow:hidden;box-shadow:0 24px 50px -24px rgba(10,90,97,.55);background:#0A5A61}'
css+='\n.d6{position:absolute;inset:0;font-family:"IBM Plex Sans",system-ui,sans-serif;line-height:normal;text-align:left}'
# --- JS
glue=js.index('/* ============ perekat')
js=js[:glue]
js=js.replace("'#'+id","'#"+P+"'+id")
js=pref(js)
js=js.replace('const Q=new URLSearchParams(location.search);\n','')
js+=r"""/* ============ perekat versi LP ============ */
const box=document.querySelector('.d6-box'),stage=$('#d6-stage');
const fit=()=>{stage.style.transform=`scale(${box.clientWidth/W})`;};
fit();if(window.ResizeObserver)new ResizeObserver(fit).observe(box);else addEventListener('resize',fit);
(function loop(){render(tl.time());requestAnimationFrame(loop);})();
tl.eventCallback('onComplete',()=>tl.play(0));
let ready=false,visible=false;
const sync=()=>{if(ready&&visible)tl.play();else tl.pause();};
if(window.IntersectionObserver)new IntersectionObserver(es=>{visible=es[0].isIntersecting;sync();},{threshold:.35}).observe(box);else visible=true;
const rebuild=()=>{const t=tl.time(),p=tl.paused();build();tl.time(t,false);if(p)tl.pause();};
document.fonts.addEventListener('loadingdone',rebuild);
document.fonts.ready.then(()=>{build();tl.pause(0);ready=true;sync();});
window.D6DEMO={tl,DURATION,seek:t=>{tl.pause();tl.time(t,false);if(gsap.ticker.tick)gsap.ticker.tick();render(t);},W,H};
"""
js='(function(){\n'+js+'})();\n'
section=f'''<!-- ===== DEMO TOOLS (animasi, tanpa file video) ===== -->
<section id="demo-tools">
  <div class="wrap-sm">
    <p class="badge font-mono" style="color:var(--teal);text-align:center;display:block;">Bonus tools · lihat cara kerjanya</p>
    <h2 class="font-display" style="font-size:1.6rem;text-align:center;font-weight:600;margin-top:12px;">Lihat Tools-nya Bekerja</h2>
    <p style="text-align:center;color:var(--ink-soft);margin-top:10px;">Pre-Assessment Klien dan Kalkulator Fee: nilai kondisi data klien, lalu tetapkan fee yang tidak merugikan Anda — dalam satu alur.</p>
    <div class="d6-box"><div class="d6">
{body}
    </div></div>
    <p class="preview-disclaimer">*Demo dengan data contoh.</p>
  </div>
</section>

'''
lp=open(LP).read()
# poin 2: kartu form-pre-assessment disesuaikan dengan tools asli
old2=lp[lp.index('<div class="formprev">'):lp.index('</div>',lp.index('class="fp-result"'))+6]
new2='''<div class="formprev">
            <div class="fp-label">Ketersediaan laporan keuangan (0–10 · bobot 2)</div><div class="fp-bar"></div>
            <div class="fp-label">Riwayat pemeriksaan &amp; sengketa (0–10 · bobot 3)</div><div class="fp-bar"></div>
            <div class="fp-check"><span class="fp-box"></span> Red flag: sengketa pajak aktif tidak diungkapkan</div>
            <div class="fp-check"><span class="fp-box"></span> Red flag: minta fee sangat rendah</div>
            <div class="fp-result">Skor: 50/100 → Kategori C · Fee +55%</div>'''
assert old2.count('fp-result')==1; lp=lp.replace(old2,new2)
lp=lp.replace('<b>Formulir Pre-Assessment Kesehatan Data Klien.</b> Isi skoring 10 poin, rekomendasi jenis jasa dan penyesuaian fee langsung keluar — bukan cuma konsep, ini tools yang benar-benar dipakai.',
 '<b>Formulir Pre-Assessment Kesehatan Data Klien.</b> Nilai 10 aspek berbobot, skor 0–100 langsung jadi rekomendasi jenis jasa dan penyesuaian fee (+25%, +55%, atau +90%) — bukan cuma konsep, ini tools yang benar-benar dipakai.')
# poin 3: kartu kalkulator disesuaikan dengan F06 (analisis skenario tax planning)
lp=lp.replace('<span class="pcard__title">kalkulator-tax-planning.xlsx</span>','<span class="pcard__title">kalkulator-skenario-tax-planning.xlsx</span>')
lp=lp.replace('''<b>Kalkulator Fee &amp; Estimasi Skenario Tax Planning.</b> Klien tanya "kalau pindah skema pajak, hematnya berapa?" — tinggal isi file Excel ini, angka penghematan per skenario langsung keluar.''',
 '''<b>Kalkulator Fee &amp; Estimasi Skenario Tax Planning.</b> Klien tanya "kalau pakai skema lain, hematnya berapa?" — bandingkan skenario di file Excel 6-sheet ini, selisih pajak tiap skenario langsung terlihat.''')
assert 'kalkulator-skenario-tax-planning.xlsx' in lp and 'bobot 3' in lp and '+25%, +55%, atau +90%' in lp and 'file Excel 6-sheet ini' in lp
# sisipkan section demo sebelum Paket & Harga
anchor='<!-- ===== PAKET & HARGA ===== -->'; assert lp.count(anchor)==1
lp=lp.replace(anchor,section+anchor)
# font tambahan untuk demo (domain sama dengan font LP)
link='<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,500;0,600;1,500;1,600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
lp=lp.replace('<style>\n',link+'<style>\n',1)
# CSS demo di akhir blok style LP
lp=lp.replace('</style>\n</head>','\n  /* ===== Demo tools (animasi) ===== */\n'+css+'\n</style>\n</head>',1)
# GSAP + skrip demo sebelum </body>
g=open(GSAP).read()
lp=lp.replace('</body>','<script>\n/* GSAP 3.12.5 — disertakan langsung supaya tidak perlu domain tambahan di CSP */\n'+g+'\n</script>\n<script>\n'+js+'</script>\n</body>',1)
open(OUT,'w').write(lp)
print('ok',len(lp),'ids',len(ids))
