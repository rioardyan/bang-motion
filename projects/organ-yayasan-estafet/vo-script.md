# Naskah VO: Organ yayasan, estafet keputusan (siap ElevenLabs)

Video 26 detik, 4:5. VO dibuat **6 klip pendek**, bukan satu rekaman panjang. Tiap klip ditaruh di detik tertentu, jadi jatuhnya pas dengan cap dan tombol di layar. Daftar cue ada di `vo/cues.csv`.

## 1. Kenapa teks layar tidak dibaca semua

Hitungan suku kata (kecepatan normal 4,8 suku kata per detik):

| Teks layar | Suku kata | Durasi baca | Jendela visual | Hasil |
|---|---|---|---|---|
| Headline | 18 | 3,75 dtk | 3,45 | mepet (butuh baca cepat) |
| Pembina + 3 butir | 23 | 4,79 | 4,15 | tidak muat |
| Pengurus + 3 butir | 20 | 4,17 | 4,15 | mepet |
| Pengawas + 3 butir | 24 | 5,00 | 4,15 | tidak muat |
| Sub-headline | 35 | 7,29 | 4,10 | tidak muat |
| CTA | 7 | 1,46 | 1,60 | muat |

Semuanya dibaca = 26,5 detik bicara dalam video 26 detik, tanpa jeda. Jadi: **butir-butir kartu dan sub-headline tetap hanya di layar** (penonton tanpa suara tidak kehilangan apa pun). VO membawa kalimat yang paling menjual, dan jatuh di momen visualnya.

## 2. Klip VO

Total 66 suku kata, sekitar 14 detik bicara dari 26 detik (±53%). Sisanya jeda untuk gambar dan waktu membaca butir.

| Klip | Mulai | Teks VO | Jatuh di visual | Suku kata | Perkiraan | Jendela | Hasil |
|---|---|---|---|---|---|---|---|
| vo-01 | 0,35 | Setiap organ yayasan punya pegangan kerja yang jelas. | headline muncul | 18 | 3,33 (@5,4) | 3,45 | pas, **dibaca cepat** |
| vo-02 | 6,75 | Pembina mengesahkan. | "mengesahkan" jatuh di cap DISAHKAN (7,4) | 7 | 1,46 (@4,8) | 1,95 | pas |
| vo-03 | 12,45 | Pengurus menjalankan. | cap DIJALANKAN (13,2) | 7 | 1,40 (@5,0) | 1,40 | pas, mepet |
| vo-04 | 17,58 | Pengawas memeriksa. | cap DIPERIKSA (18,2) | 7 | 1,40 (@5,0) | 1,42 | pas, mepet |
| vo-05 | 19,45 | Lengkap dengan es-o-pe, uraian tugas, dan alur keputusan. | sub-headline, jalur surat menggambar | 20 | 3,85 (@5,2) | 3,95 | pas, cepat |
| vo-06 | 24,45 | Lihat Sistem Kerjanya. | tombol meletup | 7 | 1,52 (@4,6) | 1,55 | pas |

Catatan:
- vo-01 dan vo-05 hanya pas kalau dibaca agak cepat. Di ElevenLabs, pasang kecepatan sekitar 1,1×. Alat `vo-cek.py` (bagian 5) menghitung angka pastinya dari audio yang jadi.
- "Pembina mengesahkan / Pengurus menjalankan / Pengawas memeriksa" adalah kata baru dari VO. Kata itu mengikuti cap di layar, dan sesuai peran organ di Product Knowledge. Tidak ada klaim hukum.
- Butir isi kartu (panduan rapat, uraian tugas, program pemeriksaan) tidak dibaca. Kalau ingin dibaca, adegan 2–4 harus diperpanjang sekitar 3 detik total dan sub-headline tetap dipangkas.

## 3. Siap tempel ke ElevenLabs

Generate **satu klip per blok**. Tempel teksnya persis seperti di bawah, tanpa tag tambahan. Tiap klip hanya satu kalimat, jadi tidak perlu tag jeda. Simpan hasilnya dengan nama `vo/vo-01.mp3` dan seterusnya.

```
vo-01
Setiap organ yayasan punya pegangan kerja yang jelas.

vo-02
Pembina mengesahkan.

vo-03
Pengurus menjalankan.

vo-04
Pengawas memeriksa.

vo-05
Lengkap dengan es-o-pe, uraian tugas, dan alur keputusan.

vo-06
Lihat Sistem Kerjanya.
```

Pelafalan:
- **SOP ditulis "es-o-pe"** di vo-05. Kalau ditulis "SOP", mesin suara bisa membacanya "sop".
- Tanda baca dipertahankan. Koma di vo-05 memberi jeda alami. Titik di akhir memberi nada turun.

## 4. Pengaturan awal (nilai awal, sesuaikan dengan telinga)

- **Suara:** pria atau wanita dewasa berbahasa Indonesia, tenang dan yakin. Pembelinya Ketua Yayasan usia 40–60. Hindari nada penjual atau ceria berlebihan. Cari di Voice Library dengan filter bahasa Indonesia, lalu dengarkan dengan kalimat vo-01.
- **Model:** Multilingual v2 atau v3 (keduanya mendukung bahasa Indonesia). Pakai model yang sama untuk keenam klip.
- **Stability** sekitar 50–60, **Similarity** sekitar 75–80, **Style** rendah (0–15), **Speaker boost** nyala. Pakai suara dan pengaturan yang sama untuk semua klip supaya warna suaranya tidak berubah antarklip.
- **Speed:** mulai di 1,0, dengarkan, lalu pasang sesuai hasil `vo-cek.py`. vo-01 dan vo-05 biasanya perlu 1,05–1,12.
- Nama pengaturan dan rentang nilainya bisa berbeda di versi ElevenLabs yang kamu pakai. Cek di panelnya.

Saya tidak punya akses ke ElevenLabs dari sesi ini, jadi audionya kamu yang generate.

## 5. Setelah audio jadi

Simpan keenam klip di `vo/` (mp3, wav, atau m4a), lalu jalankan dari folder proyek:

```
python3 -I tools/vo-cek.py     # durasi asli tiap klip vs jendelanya, plus kecepatan yang perlu dipasang
python3 -I tools/vo-rakit.py   # merakit satu trek vo/vo-final.wav, tiap klip di detik cue-nya
```

- `vo-cek.py` menandai klip yang terlalu panjang dan menyebut kecepatan yang perlu dipasang. Atau potong teksnya.
- `vo-rakit.py` menghasilkan trek 26 detik. Ia sudah saya uji dengan klip sintetis.
- Kalau audio asli ternyata lebih panjang atau pendek dari perkiraan, kirim ke saya. Waktu visual saya geser mengikuti audio, bukan sebaliknya.
- Trek ini akan ikut ke MP4 saat kamu bilang "render".
