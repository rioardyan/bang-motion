"""Rakit klip VO jadi satu trek yang cocok dengan timeline video.
Pakai: python3 -I tools/vo-rakit.py [durasi_video=26]   -> vo/vo-final.wav
Tiap klip diletakkan di detik 'start' dari vo/cues.csv (ffmpeg adelay + amix)."""
import csv, sys, subprocess, pathlib
DUR = float(sys.argv[1]) if len(sys.argv) > 1 else 26.0
rows = list(csv.DictReader(open('vo/cues.csv')))
files = []
for r in rows:
    f = next((p for p in pathlib.Path('vo').glob(r['id'] + '.*') if p.suffix in ('.mp3','.wav','.m4a')), None)
    if not f: sys.exit(f"klip {r['id']} belum ada di vo/")
    files.append((f, float(r['start'])))
cmd = ['ffmpeg','-y','-v','error']
for f, _ in files: cmd += ['-i', str(f)]
parts = [f"[{i}:a]aresample=48000,aformat=channel_layouts=mono,adelay={int(s*1000)}:all=1[a{i}]" for i,(f,s) in enumerate(files)]
mix = ''.join(f"[a{i}]" for i in range(len(files))) + f"amix=inputs={len(files)}:normalize=0,apad,atrim=0:{DUR}[o]"
cmd += ['-filter_complex', ';'.join(parts + [mix]), '-map', '[o]', '-ar', '48000', 'vo/vo-final.wav']
subprocess.run(cmd, check=True); print('vo/vo-final.wav', DUR, 'detik')
