# Naskah VO: Pengurus Yayasan Pesantren, Satu Tiang (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Berkas siap tempel: `vo/vo-pesantren.txt`. Model **eleven_v4**, suara **Bram** (sama dengan audio proyek lain), atau Finn bila kamu mau.

## Tempel ini ke ElevenLabs

```
Pengurus yayasan pesantren, santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. [pause]
Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. [pause]
Semuanya bisa ditulis. Mulai dari keputusan. [short pause]
Dua puluh sembilan keputusan, jelas siapa yang berwenang. [short pause]
Lalu, laporan semua unit terbaca di satu tempat. [short pause]
Terakhir, tanah wakaf tercatat, bukan cuma diingat. [pause]
Semuanya ada di Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen dalam empat belas kategori. [pause]
Unit bertambah, keputusan tetap jalan. [short pause]
Rapikan kerja pondok sekarang.
```

Tag `[short pause]` dan `[pause]` jalan di v4 (model ini tidak membaca `<break>`). Kalau tag ikut terbaca keras, hapus semua tag.

## Kenapa disusun begini

Tiap kalimat menyambung dari kalimat sebelumnya, tanpa loncat.

| Kalimat | Perannya |
|---|---|
| Pengurus yayasan pesantren, santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. | Hook, teks layar persis (hook pilihanmu). |
| Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. | Dua masalah tambahan. Menyebut **laporan** dan **wakaf**, jadi kalimat jembatan sesudahnya bisa berdiri sendiri di telinga. Di layar dua butir ini tertulis terpisah. |
| **Semuanya** bisa ditulis. Mulai dari keputusan. | Jembatan. "Semuanya" merujuk ke keputusan, laporan, wakaf yang baru disebut. |
| Dua puluh sembilan keputusan, jelas siapa yang berwenang. | Jawaban pertama (matriks). |
| **Lalu**, laporan semua unit terbaca di satu tempat. | Jawaban kedua (dashboard). |
| **Terakhir**, tanah wakaf tercatat, bukan cuma diingat. | Jawaban ketiga (berita acara). Jatuh saat matahari terbit. |
| Semuanya ada di Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen dalam empat belas kategori. | Produk sekilas. |
| Unit bertambah, keputusan tetap jalan. | Teks hasil. Mengulang "unit bertambah" dari hook, jadi cerita menutup. |
| Rapikan kerja pondok sekarang. | CTA, **sama persis dengan tombol**. |

Tiga ringkasan di VO (dibanding layar): kedua baris masalah digabung jadi satu kalimat, "bukan cuma" tidak diulang, dan "148 Word + 24 Excel berformula" memang tidak ada di video ini. Chip dan label di layar tidak dibaca.

## Cara baca

- Hook: tenang dan berat, tiga ketukan ("Santri bertambah." / "Unit bertambah." / "Semua keputusan masih menunggu satu orang."). "satu orang" ditahan sebentar.
- Tiga jawaban: ringan dan rapat, seperti membuka daftar. "Lalu" dan "Terakhir" jangan ditekan.
- "tercatat, bukan cuma diingat" turun, yakin. Ini titik lega, saat fajar.
- "Unit bertambah, keputusan tetap jalan." hangat. "Rapikan kerja pondok sekarang." tegas, tanpa nada jualan.

## Durasi: 193 suku kata, jeda 3.8 detik

| Kecepatan baca | Selesai di |
|---|---|
| 5,4 suku kata/dtk | **39.6 dtk** |
| 5,8 | 37.1 dtk |
| 6,2 | 35.0 dtk |

Video sekarang 28,8 detik. Waktu visual akan mengikuti audio, bukan sebaliknya. Kalau audio lebih panjang, adegan 3 dan 4 yang kuperpanjang. Kalau lebih dari 32 detik, kirim saja: aku pangkas jeda di pascaproduksi.

## Perkiraan jatuh di suara (@5,4 / @6,2)

| Kalimat | @5,4 | @6,2 | Visual |
|---|---|---|---|
| Pengurus yayasan pesantren, santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. | 0.1–6.6 | 0.1–5.7 | hook (layar 0–3,8) |
| Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. | 7.2–11.6 | 6.3–10.2 | adegan 2: tiga baris masalah |
| Semuanya bisa ditulis. Mulai dari keputusan. | 12.2–15.4 | 10.8–13.6 | jembatan |
| Dua puluh sembilan keputusan, jelas siapa yang berwenang. | 15.7–19.4 | 13.9–17.1 | dokumen 1: matriks |
| Lalu, laporan semua unit terbaca di satu tempat. | 19.8–23.1 | 17.5–20.4 | dokumen 2: dashboard |
| Terakhir, tanah wakaf tercatat, bukan cuma diingat. | 23.5–26.6 | 20.7–23.5 | dokumen 3: berita acara, fajar |
| Semuanya ada di Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen dalam empat belas kategori. | 27.2–34.4 | 24.1–30.4 | angka 172 |
| Unit bertambah, keputusan tetap jalan. | 35.0–37.4 | 31.0–33.1 | teks hasil |
| Rapikan kerja pondok sekarang. | 37.8–39.7 | 33.5–35.1 | tombol |

Meleset ±10% tergantung suara. Kuukur ulang setelah audio ada.

## Setelah audio jadi

1. Generate satu kali, simpan sebagai `vo/vo-pesantren.mp3`.
2. Kirim ke aku. Aku ukur batas kalimat (silencedetect + Whisper), geser waktu visual mengikuti suara, pangkas jeda yang terlalu panjang, lalu bangun versi bersuara. MP4 kurender setelah kamu bilang "render".

Pengaturan awal: Stability 50–60, Similarity 75–80, Style rendah.
