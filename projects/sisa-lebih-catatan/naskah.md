# Naskah: Surplus kena pajak, padahal harusnya nol (dari iklan statis, 15 detik)

Status: **terkunci**. Sumber: iklan statis (lampiran pengguna). Isi teks dan tabel dipakai **persis**.

## Keputusan

| Item | Pilihan |
|---|---|
| Konsep | B: catatan yang ditulis langsung (#10 tanya → jawab diegetik). Layar Catatan ditulis live, tiap tulisan memicu sesuatu di Excel |
| Kata "template surat" | **Tetap persis** (permintaan pengguna: isi sama persis). Bertentangan dengan aturan "jangan sebut produk template"; sudah diberi tahu |
| Rasio / durasi | 4:5 (1080×1350) / 15 detik |
| Audio / brand | Tanpa audio. Tanpa logo dan tanpa nama brand Ardya |
| Kandidat tidak dipilih | A tiap masalah satu kolom jawaban (#3 + #9), C surat yang jadi tagihan (#7) |

## Isi persis dari iklan

- Chip: "Khusus Ketua, Pengurus & Pembina Yayasan"
- Headline: "Kenapa surplus yayasan kena pajak, padahal harusnya nol"
- Masalah 1: "Pemberitahuan rencana penggunaan ke kantor pajak tidak pernah dikirim"
- Masalah 2: "Sisa lebih tidak dicatat per tahun perolehan, jadi tidak tahu mana yang hampir 4 tahun"
- Masalah 3: "Uangnya sudah dipakai bangun kelas, tapi laporan realisasinya tidak ada"
- Persamaan: "Satu surat yang tidak dikirim = surplus jadi tagihan."
- Produk: "Panduan sisa lebih + template surat + Excel hitung mundur 4 tahun"
- Sub: "Bagian dari Sistem Tata Kelola Yayasan — 172 dokumen siap pakai"
- Tombol: "Ambil Excel-nya →"
- Tabel "SISA LEBIH PER TAHUN PEROLEHAN": kolom Tahun Perolehan · Jumlah Sisa Lebih · Batas Akhir Penggunaan · Telah Digunakan · Sisa Waktu (tahun) · Status
  - 2021 · 250.000.000 · 31/12/2025 · 0 · 0,3 · Mendesak (baris kuning)
  - 2022 · 400.000.000 · 31/12/2026 · 150.000.000 · 1,3 · Aman
  - 2023 · 300.000.000 · 31/12/2027 · 200.000.000 · 2,3 · Aman
  - 2024 · 500.000.000 · 31/12/2028 · 100.000.000 · 3,3 · Aman
- Teks UI yang ikut: judul "Catatan", jam 10.27, tab menu Excel (File, Home, Insert, Page Layout, Formulas, Data, Review, View, Help).

## Rundown

| Detik | Adegan | Teks layar | Visual |
|---|---|---|---|
| 0–3,4 | 1. Tanya | Chip. Headline diketik: "Kenapa surplus yayasan" (0,5) · "kena pajak," (1,6, distabilo) · "padahal harusnya nol" (2,3) | Layar Catatan kosong, kursor berkedip. Headline ditulis langsung. Kata *nol* mendarat dengan hentak, kursor berhenti. |
| 3,4–8,4 | 2. Tiga masalah | Masalah 1 (3,4) · masalah 2 (5,0) · masalah 3 (7,0), tiap kalimat diketik lalu dicentang | Catatan menggulung mengikuti ketikan. Centang tergambar setelah tiap kalimat selesai. "hampir 4 tahun" distabilo. |
| 8,4–10,2 | 3. Persamaan | "Satu surat yang tidak dikirim = surplus jadi tagihan." (8,5) | Tanda *=* menghentak. Ikon amplop gagal-kirim berubah jadi ikon tagihan. Catatan menggulung naik. |
| 10,2–12,6 | 4. Jawaban | Baris produk (10,3). Tabel Excel | Excel naik dari bawah. Angka tiap baris diketik. Sisa Waktu baris 2021 **menghitung mundur** 4,0 → 0,3, baris menyala kuning, status jadi **Mendesak**. Tiga baris lain: Aman. |
| 12,6–15 | 5. Ajakan | Sub (12,8) · tombol (13,5) | Angka 172 menghitung naik. Tombol meletup, lalu ditahan dengan dorongan pelan. |

## Pengembangan (bukan sekadar animasi gambar)

Layar ditulis langsung (kursor, ketikan, gulir kamera) · centang digambar setelah tiap masalah · persamaan "surat = tagihan" jadi momen hentak · Excel dibangun di layar, hitung mundur memperlihatkan arti "hitung mundur 4 tahun" · angka 172 hidup.

## Risiko

Teks padat untuk 15 detik (±83 kata). Teks yang sudah ditulis tetap di layar sampai digulung; loop membantu putaran kedua. Bila terasa terlalu cepat, solusinya durasi 18–20 detik, bukan memangkas teks.

## Pagar

Tidak ada: brand, logo, harga, testimoni, wajah, ikon peringatan merah, emoji, klaim "sesuai peraturan terbaru", nomor peraturan, janji hukum.
