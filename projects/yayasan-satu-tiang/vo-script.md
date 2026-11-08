# Naskah VO: Yayasan Satu Tiang (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Berkas siap tempel: `vo/vo-satu-tiang.txt`.

## Tempel ini ke ElevenLabs

```
Ketua yayasan, <break time="0.3s" />
kalau Bapak berhenti besok, <break time="0.3s" />
siapa yang tahu aturannya? <break time="2.2s" />
Yayasan sedang berdiri di atas satu orang. <break time="0.6s" />
Matriks kewenangan. <break time="0.2s" />
Berita acara rapat. <break time="0.2s" />
Form aset. <break time="0.2s" />
Panduan sisa lebih. <break time="0.2s" />
Excel keuangan. <break time="0.2s" />
Excel pemantauan. <break time="0.6s" />
Seratus tujuh puluh dua dokumen, <break time="0.3s" />
empat belas kategori. <break time="0.6s" />
Tuliskan aturan yayasan sebelum besok.
```

## Cara baca

- Headline dibaca persis seperti di layar, tiga napas: "Ketua yayasan," / "kalau Bapak berhenti besok," / "siapa yang tahu aturannya?" (nada naik di akhir).
- Jeda 2,2 detik setelah pertanyaan sengaja. Di layar ada gelembung "Kalau jawabannya ‘semua ada di kepala saya’," yang dibaca penonton sendiri. Suara kembali di "Yayasan sedang berdiri di atas satu orang." Turunkan nada dan pelankan.
- Enam nama dokumen dibaca singkat, satu per halaman (1,3 detik per halaman). Teks layarnya lebih lengkap.
- "148 Word + 24 Excel berformula" tidak dibaca, cukup di layar.
- "Tuliskan aturan yayasan sebelum besok." tegas, tanpa nada jualan. "Besok" sedikit ditekan.
- Kalau "Excel" terbaca "ekcel", ganti jadi "Eksel" di naskah.

## Durasi: 111 suku kata, jeda 5,9 detik

| Kecepatan baca | Selesai di |
|---|---|
| 5,5 suku kata/dtk (rata-rata take ElevenLabs sebelumnya) | **26,1 dtk** |
| 6,0 | 24,4 dtk |
| 6,2 (rekaman organ yayasanmu) | 23,8 dtk |

Video sekarang 24 detik. Kalau audio jadi lebih dari 24 detik, aku geser waktu visual mengikuti audio (adegan 3 dan 4 yang paling lentur), bukan sebaliknya. Kalau lebih dari 26 detik, pasang Speed 1,05–1,1 atau pangkas jeda 2,2 detik.

## Jatuh di visual (perkiraan @5,5 / @6,2)

| Kalimat | VO @5,5 | VO @6,2 | Di layar (sekarang) |
|---|---|---|---|
| Ketua yayasan, | 0,1–1,2 | 0,1–1,1 | baris 1 (0,3) |
| kalau Bapak berhenti besok, | 1,5–3,2 | 1,4–2,9 | baris 2 (1,3) |
| siapa yang tahu aturannya? | 3,5–5,3 | 3,2–4,8 | baris 3 kuning (2,8) |
| (diam, gelembung kutipan) | | | 5,1–7,0 |
| Yayasan sedang berdiri di atas satu orang. | 7,5–10,2 | 7,0–9,4 | sub-headline baris 2 (7,0) |
| Matriks kewenangan. | 10,8–11,9 | 10,0–11,0 | halaman 1 (9,5) |
| Berita acara rapat. | 12,1–13,6 | 11,2–12,5 | halaman 2 (10,8) |
| Form aset. | 13,8–14,3 | 12,7–13,1 | halaman 3 (12,1) |
| Panduan sisa lebih. | 14,5–15,8 | 13,3–14,5 | halaman 4 (13,4) |
| Excel keuangan. | 16,0–17,1 | 14,7–15,6 | halaman 5 (14,7) |
| Excel pemantauan. | 17,3–18,6 | 15,8–17,0 | halaman 6 (16,0), bangunan tegak 17,2 |
| Seratus tujuh puluh dua dokumen, | 19,1–21,3 | 17,6–19,5 | hitung naik (19,4) |
| empat belas kategori. | 21,6–23,1 | 19,8–21,1 | tab A–N (21,05) |
| Tuliskan aturan yayasan sebelum besok. | 23,7–26,2 | 21,7–24,0 | tombol (22,1) |

Perkiraan ini meleset sekitar ±10% tergantung suara. Kecepatan 5,5 membuat adegan 3 tertinggal sekitar 1 detik dari halamannya. Itu yang akan kugeser setelah audio ada.

## Setelah audio jadi

1. Generate satu kali, simpan sebagai `vo/vo-satu-tiang.mp3`.
2. Kirim ke aku. Aku ukur batas tiap kalimat (silencedetect + Whisper), geser waktu visual mengikuti audio, lalu render MP4 bersuara.
3. Tag `<break>` jalan di model Multilingual v2, Turbo, dan Flash (maksimal 3 detik per tag). Kalau kamu pakai v4 dan tag itu ikut terbaca atau diabaikan, hapus semua tag. Jeda bisa kuatur di pascaproduksi, jadi tidak perlu diulang.

Pengaturan awal: suara dewasa Indonesia yang tenang dan yakin, Stability 50–60, Similarity 75–80, Style rendah, Speed 1,0.
