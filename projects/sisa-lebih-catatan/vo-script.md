# VO promo sisa lebih (ElevenLabs, suara "Ganesh - Warm, Intimidating and Clear", model eleven_v4)

Audio akhir: `audio/vo.mp3` (15,0 detik, mono). Rekaman mentah: `audio/take2-mentah.mp3` (19,07 detik). Waktu per kalimat: `audio/timing.json`.

## Teks yang dibaca (take 2, apa adanya dari ElevenLabs)

Kenapa surplus yayasan kena pajak, padahal harusnya NOL? [short pause] Pemberitahuan tidak dikirim. Sisa lebih tidak dicatat. Laporan tidak ada. [short pause] Satu surat tidak dikirim, surplus jadi tagihan. [short pause] Panduan, surat, dan Excel hitung mundur. [short pause] Mendesak! [short pause] Ambil Excel-nya.

## Pengolahan agar muat 15 detik

- Rekaman mentah 19,07 detik: ±4 detik adalah jeda (tag `[short pause]` dan tanda tanya memanjangkannya).
- Delapan kalimat dipotong di batas jeda, jeda antarkalimat dipendekkan jadi 0,12 detik, lalu seluruhnya dipercepat 1,13× (`atempo`, nada tetap). Hasilnya ±6,2 suku kata per detik, sama dengan kisaran rekaman organ yayasan.
- Selesai bicara di 14,58 detik. Tombol "Ambil Excel-nya" muncul tepat saat kalimat itu dibaca (13,95).

| Kalimat | Mulai–selesai | Di layar |
|---|---|---|
| Kenapa surplus yayasan kena pajak, padahal harusnya nol? | 0,13–3,32 | headline diketik, "nol" menghentak 3,1 |
| Pemberitahuan tidak dikirim. | 3,51–4,83 | masalah 1 diketik lalu dicentang |
| Sisa lebih tidak dicatat. | 5,03–6,29 | masalah 2 |
| Laporan tidak ada. | 6,49–7,60 | masalah 3 |
| Satu surat tidak dikirim, surplus jadi tagihan. | 7,80–10,43 | persamaan, "=" menghentak di koma (±9,2) |
| Panduan, surat, dan Excel hitung mundur. | 10,63–12,96 | Excel dibangun, hitung mundur 12,3–13,15 |
| Mendesak! | 13,15–13,75 | baris 2021 menyala, status Mendesak |
| Ambil Excel-nya. | 13,95–14,58 | tombol meletup, 172 menghitung naik |

## Catatan

- Kata "NOL" berhuruf kapital sempat terbaca "eno/enol" saat transkripsi potongan. Pada transkripsi seluruh kalimat hook, take 2 terbaca "nol" dengan benar. Kalau saat didengar ternyata dieja, generate ulang dengan "nol" huruf kecil (naskah ringkas ada di riwayat percakapan).
- Naskah ringkas (±68 suku kata, tanpa tag jeda) belum sempat digenerate karena server ElevenLabs sedang sibuk.
