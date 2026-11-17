# Naskah VO: Organ Yayasan Tiga Laci (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Berkas siap tempel: `vo/vo-laci.txt`.

## Tempel ini ke ElevenLabs

```
Setiap organ yayasan punya pegangan kerja yang jelas. <break time="0.6s" />
Pembina memegang panduan rapat, mekanisme keputusan, dan format pengesahan. <break time="0.5s" />
Pengurus memegang uraian tugas, es-o-pe kerja, dan alur persetujuan. <break time="0.5s" />
Pengawas memegang program pemeriksaan, format laporan, dan mekanisme tindak lanjut. <break time="0.6s" />
Semuanya lengkap dengan es-o-pe, uraian tugas, dan alur keputusan yang sudah disusun. <break time="0.6s" />
Lihat sistem kerjanya.
```

## Kenapa disusun begini

Tiap kalimat menyambung dari kalimat sebelumnya. Tidak ada loncat.

| Kalimat | Perannya |
|---|---|
| Setiap organ yayasan punya pegangan kerja yang jelas. | Janji (headline persis). |
| Pembina **memegang** …  Pengurus **memegang** …  Pengawas **memegang** … | Jawaban atas janji. Kata "memegang" menyambung ke "pegangan" di headline, dan cocok dengan gambar: tiap organ menarik pegangan lacinya sendiri. |
| **Semuanya** lengkap dengan … yang sudah disusun. | Merangkum tiga laci. Isinya sub-headline, diambil dari layar. |
| Lihat sistem kerjanya. | Ajakan. **Sama persis dengan tombol** (kali ini suara dan tombol tidak beda). |

- Chip "Khusus Pembina, Pengurus & Pengawas Yayasan" tidak dibaca. Cukup di layar.
- Isi tiga kartu dibaca sama dengan teks layar, hanya ditambah kata "memegang".
- "SOP" ditulis **es-o-pe** supaya tidak terbaca "sop".
- "formulir serta berita acara" dari layar diringkas jadi "yang sudah disusun" supaya VO tidak kepanjangan.

## Cara baca

- Tenang dan yakin, bukan nada jualan. Jeda antar organ ringan.
- "memegang" jangan ditekan. Tekan nama organnya: **Pembina**, **Pengurus**, **Pengawas**.
- "Semuanya lengkap …" naik sedikit, lalu turun di "disusun".
- "Lihat sistem kerjanya." turun, tegas.

## Durasi: 133 suku kata, jeda 2,8 detik

| Kecepatan baca | Selesai di |
|---|---|
| 5,5 suku kata/dtk (rata-rata take ElevenLabs sebelumnya) | **27,0 dtk** |
| 6,0 | 25,0 dtk |
| 6,2 (rekaman organ yayasanmu) | 24,3 dtk |

Video sekarang 24 detik. Setelah audio ada, aku geser waktu visual mengikuti suara, bukan sebaliknya. Perkiraan sampai 27 detik masih di bawah batas 30 detik. Kalau audio melewati 30 detik, pasang Speed 1,05–1,1.

## Perkiraan jatuh di suara (@5,5 / @6,2)

| Kalimat | @5,5 | @6,2 | Visual yang dipasangkan |
|---|---|---|---|
| Setiap organ yayasan punya pegangan kerja yang jelas. | 0,1–3,4 | 0,1–3,0 | chip, headline, tiga pegangan menyala |
| Pembina memegang … format pengesahan. | 4,0–8,7 | 3,6–7,8 | laci Pembina ditarik, SOP Rapat terbit |
| Pengurus memegang … alur persetujuan. | 9,2–13,7 | 8,3–12,3 | laci Pengurus, Uraian Tugas terbit |
| Pengawas memegang … mekanisme tindak lanjut. | 14,2–19,2 | 12,8–17,2 | laci Pengawas, Program Pengawasan terbit |
| Semuanya lengkap … yang sudah disusun. | 19,8–25,2 | 17,8–22,6 | tiga laci terbuka serentak, 12 · 15 · 10 |
| Lihat sistem kerjanya. | 25,8–27,1 | 23,2–24,4 | tombol naik |

Meleset ±10% tergantung suara. Kuukur ulang setelah audio ada.

## Revisi visual yang sudah kurencanakan (menunggu audio)

1. **Bingkai penutup:** headline yang diulang di akhir dibuang (itu tambahanku, tidak ada di naskah). Sub-headline tetap di atas sampai tombol muncul.
2. Waktu adegan 2–6 digeser mengikuti batas kalimat di audio. Durasi video mengikuti panjang audio.
3. Tombol suara di artifact, lalu render MP4 bersuara setelah kamu bilang "render".

## Setelah audio jadi

1. Generate satu kali, simpan sebagai `vo/vo-laci.mp3`.
2. Kirim ke aku. Aku ukur batas tiap kalimat (silencedetect + Whisper) dan lakukan revisi di atas.
3. Tag `<break>` jalan di Multilingual v2, Turbo, dan Flash. Di v4 tag itu diabaikan (tidak terbaca keras), jadi aman dibiarkan. Jeda kuatur di pascaproduksi.

Pengaturan awal: suara dewasa Indonesia yang tenang dan yakin, Stability 50–60, Similarity 75–80, Style rendah, Speed 1,0.
