# Naskah VO: Organ yayasan, estafet keputusan (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Jeda diatur dengan tag `<break>`. Berkas siap tempel: `vo/vo-organ.txt`.

## Tempel ini ke ElevenLabs

```
Pembina, Pengurus, Pengawas! <break time="0.2s" />
Setiap organ yayasan punya pegangan kerja yang jelas. <break time="0.5s" />
Pembina: panduan rapat, mekanisme keputusan, dan format pengesahan. <break time="0.5s" />
Pengurus: uraian tugas, es-o-pe kerja, dan alur persetujuan. <break time="0.5s" />
Pengawas: program pemeriksaan, format laporan, dan mekanisme tindak lanjut. <break time="0.6s" />
Lengkap dengan es-o-pe, uraian tugas, dan alur keputusan. <break time="0.8s" />
Lihat Sistem Kerjanya.
```

- "SOP" ditulis **es-o-pe** supaya tidak terbaca "sop".
- Kalimat pembuka ("Pembina, Pengurus, Pengawas!") adalah sapaan, sama seperti chip "Khusus Pembina, Pengurus & Pengawas Yayasan" di layar.
- Isi kartu dibaca sama dengan teks layar. Kalimat penutup adalah CTA di tombol.
- Tag `<break>` setahuku untuk model Multilingual v2, Turbo, dan Flash (maksimal 3 detik per tag). Cek di model yang kamu pakai.

## Durasi: pas atau tidak?

123 suku kata, jeda 3,1 detik. Tergantung kecepatan baca:

| Kecepatan | Selesai di | Pas untuk video 26 detik? |
|---|---|---|
| tenang (4,4 suku kata/dtk) | 31,2 dtk | tidak |
| **normal (4,8)** | **28,8 dtk** | **tidak, butuh ±3 detik lebih** |
| cepat (5,2) | 26,9 dtk | hampir |

Video sekarang 26 detik. VO ini butuh sekitar **29,4 detik** (28,8 + ekor 0,6) di kecepatan normal. Masih di dalam 20–30 detik, tapi video harus diperpanjang di adegan 1, 2, dan 5. Kalau audio ternyata lebih dari 29,5 detik, pasang speed 1,05–1,1 di ElevenLabs.

## Jatuh di visual (kecepatan normal)

| Kalimat | VO | Di layar | Waktu video sekarang → baru |
|---|---|---|---|
| Pembina, Pengurus, Pengawas! | 0,1–2,0 | chip pembuka | chip 0,05 → 0,05 |
| Setiap organ yayasan punya pegangan kerja yang jelas. | 2,2–5,9 | headline, dua beat | 0,35 / 1,8 → **2,2 / 3,9** |
| Pembina: ... format pengesahan. | 6,4–11,2 | label, 3 butir, cap DISAHKAN | adegan mulai 4,2 → **6,2**; cap 7,4 → **11,0** |
| Pengurus: ... alur persetujuan. | 11,7–16,3 | label, 3 butir, cap DIJALANKAN | adegan mulai 9,2 → **11,5**; cap 13,2 → **16,1** |
| Pengawas: ... tindak lanjut. | 16,8–21,8 | label, 3 butir, cap DIPERIKSA | adegan mulai 14,2 → **16,6**; cap 18,2 → **21,6** |
| Lengkap dengan es-o-pe, ... alur keputusan. | 22,4–26,6 | sub-headline, jalur surat, tiga tumpukan | adegan mulai 19,2 → **22,1** |
| Lihat Sistem Kerjanya. | 27,4–28,8 | tombol meletup | adegan mulai 23,4 → **27,0**; tombol 24,45 → **27,4** |

Total video: **26 → ±29,4 detik**. Adegan 1 jadi 6,2 detik (sekarang 4,2) karena sapaan dan headline dibaca berurutan.

## Setelah audio jadi

1. Generate satu kali, simpan sebagai `vo/vo-organ.mp3`.
2. Kirim ke saya. Saya ukur batas tiap kalimat (`scripts/vo-pauses.html` atau `ffmpeg silencedetect`) dan geser waktu visual mengikuti audio, bukan sebaliknya.
3. Perkiraan di atas dihitung dari suku kata (`tools/vo-hitung.py`). Meleset sekitar ±10% tergantung pengisi suara.

Pengaturan awal ElevenLabs (nilai awal, nama dan rentangnya bisa beda di versimu): suara dewasa berbahasa Indonesia yang tenang dan yakin, Stability 50–60, Similarity 75–80, Style rendah, Speaker boost nyala, Speed 1,0.
Saya tidak punya akses ke ElevenLabs dari sesi ini, jadi audionya kamu yang generate.
