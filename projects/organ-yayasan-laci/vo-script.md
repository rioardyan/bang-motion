# Naskah VO v2: Organ Yayasan Tiga Laci (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Berkas siap tempel: `vo/vo-laci.txt`. Model **eleven_v4**, suara **Bram - Warm, Expressive and Welcoming** (sama dengan audio yang kamu pakai sebelumnya).

## Tempel ini ke ElevenLabs

```
Setiap organ yayasan punya pegangan kerja yang jelas. [short pause]
Pembina memegang panduan rapat dan format pengesahan. [short pause]
Pengurus memegang uraian tugas dan alur persetujuan. [short pause]
Pengawas memegang program pemeriksaan dan tindak lanjut. [pause]
Semuanya sudah disusun lengkap. [short pause]
Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen dalam empat belas kategori. [pause]
Hasilnya, tiap organ tahu tugasnya, tiap keputusan ada pegangannya. [pause]
Dapatkan sekarang.
```

Tag `[short pause]` dan `[pause]` jalan di v4 (model ini tidak membaca `<break>`). Kalau tag ikut terbaca keras, hapus semua tag dan biarkan titik yang mengatur jeda.

## Kenapa disusun begini

Tiap kalimat menyambung dari kalimat sebelumnya, tanpa loncat.

| Kalimat | Perannya |
|---|---|
| Setiap organ yayasan punya pegangan kerja yang jelas. | Janji (headline persis). |
| Pembina / Pengurus / Pengawas **memegang** … | Jawaban atas janji. "Memegang" menyambung ke "pegangan", dan cocok dengan gambar: tiap organ menarik pegangan lacinya. Isi kartu diringkas (yang lengkap ada di layar). |
| **Semuanya** sudah disusun lengkap. | Merangkum tiga laci. Ini isi sub-headline ("Lengkap dengan … yang sudah disusun"). |
| **Ini** Sistem Tata Kelola Yayasan, 172 dokumen dalam 14 kategori. | Produk sekilas (revisi baru). "Ini" menyambung dari "Semuanya". |
| **Hasilnya**, tiap organ tahu tugasnya, tiap keputusan ada pegangannya. | Teks hasil (dipilih pengguna). "Hasilnya" membuat sebab-akibat eksplisit. Mengulang kata "pegangan" dari pembuka. |
| Dapatkan sekarang. | CTA, **sama persis dengan tombol**. |

Angka ditulis dengan huruf ("seratus tujuh puluh dua"). "148 Word + 24 Excel berformula" tidak dibaca, cukup di layar. Chip tidak dibaca.

## Cara baca

- Tenang dan yakin, bukan nada jualan.
- Tekan nama organ: **Pembina**, **Pengurus**, **Pengawas**. "memegang" jangan ditekan.
- "Ini Sistem Tata Kelola Yayasan" naik sedikit, lalu mengalir ke angka.
- "Hasilnya, …" hangat dan mantap. "Dapatkan sekarang." turun, tegas.

## Durasi: 149 suku kata

| Kecepatan baca | Selesai di |
|---|---|
| 5,5 suku kata/dtk (rata-rata take ElevenLabs sebelumnya) | **30.1 dtk** |
| 6,0 | 27.8 dtk |
| 6,5 | 25.9 dtk |

Video v1 24 detik. Video v2 mengikuti audio, jadi sekitar 27–30 detik. Batas 30 detik. Kalau audio melewati 30 detik, kirim saja. Aku pangkas jeda di pascaproduksi.

## Perkiraan jatuh di suara (@5,5 / @6,5)

| Kalimat | @5,5 | @6,5 | Visual |
|---|---|---|---|
| Setiap organ yayasan punya pegangan kerja yang jelas. | 0.1–3.4 | 0.1–2.9 | chip, headline, tiga pegangan menyala |
| Pembina memegang panduan rapat dan format pengesahan. | 3.7–6.9 | 3.2–5.9 | laci Pembina, SOP Rapat Pembina terbit |
| Pengurus memegang uraian tugas dan alur persetujuan. | 7.2–10.9 | 6.2–9.3 | laci Pengurus, Uraian Tugas terbit |
| Pengawas memegang program pemeriksaan dan tindak lanjut. | 11.2–14.5 | 9.6–12.4 | laci Pengawas, Program Pengawasan terbit |
| Semuanya sudah disusun lengkap. | 15.1–17.1 | 13.0–14.7 | tiga laci terbuka serentak, sub-headline, 12 · 15 · 10 |
| Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen dalam empat belas kategori. | 17.4–23.5 | 15.0–20.2 | produk sekilas: 172 dokumen, tab A–N |
| Hasilnya, tiap organ tahu tugasnya, tiap keputusan ada pegangannya. | 24.1–28.5 | 20.8–24.5 | teks hasil naik di atas kabinet |
| Dapatkan sekarang. | 29.1–30.2 | 25.1–26.0 | tombol |

## Perubahan visual yang sudah direncanakan (menunggu audio)

1. Teks hasil di bingkai akhir: "Tiap organ tahu tugasnya, tiap keputusan ada pegangannya." (bukan headline yang diulang).
2. CTA tombol: **"Dapatkan Sekarang"**.
3. Adegan produk sekilas seperti Satu Tiang v1: angka 172 menghitung naik, "148 Word + 24 Excel berformula", "14 kategori", empat belas tab A–N di atas kabinet (B, C, D berwarna organ).
4. Waktu semua adegan digeser mengikuti batas kalimat di audio. Tombol suara di artifact. MP4 baru kurender setelah kamu bilang "render".

## Catatan generate

Aku coba generate lewat konektor ElevenLabs, tapi ditolak: *"Unusual activity has been detected on your account, so Free Tier access has been disabled … upgrade to a paid subscription"*. Jadi generate manual di akunmu. Simpan hasilnya sebagai `vo/vo-laci.mp3` lalu kirim. Aku ukur batas kalimat (silencedetect + Whisper) dan kerjakan revisi.

Pengaturan awal: Stability 50–60, Similarity 75–80, Style rendah.
