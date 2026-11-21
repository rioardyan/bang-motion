# Naskah VO: Pengurus Yayasan Pesantren, Satu Tiang (siap ElevenLabs)

Satu naskah utuh, satu kali generate. Berkas siap tempel: `vo/vo-pesantren.txt`. Model **eleven_v4**, suara **Bram** (sama dengan audio proyek lain), atau Finn bila kamu mau.

## Tempel ini ke ElevenLabs

```
Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. [pause]
Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. [pause]
Semuanya bisa ditulis. Mulai dari keputusan. [short pause]
Dua puluh sembilan keputusan, jelas siapa yang berwenang. [short pause]
Lalu, laporan semua unit terbaca di satu tempat. [short pause]
Terakhir, tanah wakaf tercatat, bukan cuma diingat. [pause]
Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen. [pause]
Unit bertambah, keputusan tetap jalan. [short pause]
Rapikan kerja pondok sekarang.
```

Tag `[short pause]` dan `[pause]` jalan di v4 (model ini tidak membaca `<break>`). Kalau tag ikut terbaca keras, hapus semua tag.

## Kenapa disusun begini

Tiap kalimat menyambung dari kalimat sebelumnya, tanpa loncat.

| Kalimat | Perannya |
|---|---|
| Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. | Hook, teks layar persis (hook pilihanmu). Sapaan "PENGURUS YAYASAN PESANTREN," tidak dibaca, cukup di layar. |
| Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. | Dua masalah tambahan. Menyebut **laporan** dan **wakaf**, supaya kalimat jembatan sesudahnya bisa berdiri sendiri di telinga. Di layar dua butir ini tertulis terpisah. |
| **Semuanya** bisa ditulis. Mulai dari keputusan. | Jembatan. "Semuanya" merujuk ke keputusan, laporan, wakaf yang baru disebut. |
| Dua puluh sembilan keputusan, jelas siapa yang berwenang. | Jawaban pertama (matriks). |
| **Lalu**, laporan semua unit terbaca di satu tempat. | Jawaban kedua (dashboard). |
| **Terakhir**, tanah wakaf tercatat, bukan cuma diingat. | Jawaban ketiga (berita acara). Jatuh saat matahari terbit. |
| **Ini** Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen. | Produk sekilas. "Empat belas kategori" cukup di layar. |
| Unit bertambah, keputusan tetap jalan. | Teks hasil. Mengulang "unit bertambah" dari hook, jadi cerita menutup. |
| Rapikan kerja pondok sekarang. | CTA, **sama persis dengan tombol**. |

Yang tidak dibaca (cukup di layar): sapaan pembuka, "14 kategori", chip dan label dokumen. Dua baris masalah digabung jadi satu kalimat.

## Cara baca

- Hook: tenang dan berat, tiga ketukan. "satu orang" ditahan sebentar.
- Tiga jawaban: ringan dan rapat, seperti membuka daftar. "Lalu" dan "Terakhir" jangan ditekan.
- "tercatat, bukan cuma diingat" turun, yakin. Ini titik lega, saat fajar.
- "Unit bertambah, keputusan tetap jalan." hangat. "Rapikan kerja pondok sekarang." tegas, tanpa nada jualan.

## Durasi: 169 suku kata, jeda 3.7 detik

| Kecepatan baca | Selesai di |
|---|---|
| 5,4 suku kata/dtk | **34.9 dtk** |
| 5,8 | 32.8 dtk |
| 6,2 | 30.9 dtk |

Video sekarang 28,8 detik. Waktu visual akan mengikuti audio, bukan sebaliknya. Audio ini lebih panjang dari video sekarang, jadi video v2 kemungkinan 31–35 detik. Kalau terasa terlalu panjang, jeda antar kalimat kupangkas di pascaproduksi (suara tidak diubah).

## Perkiraan jatuh di suara (@5,4 / @6,2)

| Kalimat | @5,4 | @6,2 | Visual |
|---|---|---|---|
| Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang. | 0.1–4.9 | 0.1–4.3 | hook (layar 0–3,8) |
| Bukan cuma keputusan. Laporan dan tanah wakaf juga lewat satu orang. | 5.5–9.9 | 4.8–8.7 | adegan 2: tiga baris masalah |
| Semuanya bisa ditulis. Mulai dari keputusan. | 10.5–13.6 | 9.3–12.0 | jembatan |
| Dua puluh sembilan keputusan, jelas siapa yang berwenang. | 14.0–17.7 | 12.4–15.6 | dokumen 1: matriks |
| Lalu, laporan semua unit terbaca di satu tempat. | 18.0–21.3 | 15.9–18.8 | dokumen 2: dashboard |
| Terakhir, tanah wakaf tercatat, bukan cuma diingat. | 21.7–24.8 | 19.2–21.9 | dokumen 3: berita acara, fajar |
| Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen. | 25.4–29.8 | 22.5–26.3 | angka 172 |
| Unit bertambah, keputusan tetap jalan. | 30.4–32.8 | 26.9–29.0 | teks hasil |
| Rapikan kerja pondok sekarang. | 33.2–35.0 | 29.4–31.0 | tombol |

Meleset ±10% tergantung suara. Kuukur ulang setelah audio ada.

## Setelah audio jadi

1. Generate satu kali, simpan sebagai `vo/vo-pesantren.mp3`.
2. Kirim ke aku. Aku ukur batas kalimat (silencedetect + Whisper), geser waktu visual mengikuti suara, lalu bangun versi bersuara. MP4 kurender setelah kamu bilang "render".

Pengaturan awal: Stability 50–60, Similarity 75–80, Style rendah.

---

# Versi 2: expressive, tag lebih rinci (v4)

Kata-katanya **sama persis** dengan versi 1 (alur sudah kamu uji, jadi tidak kuubah). Yang berubah: arah emosi per baris, penekanan, dan jeda. Berkas: `vo/vo-pesantren-v2.txt`.

## Tempel ini ke ElevenLabs

```
[serious] [slowly] Santri bertambah. [short pause] Unit bertambah. [pause]
[tired] Semua keputusan masih menunggu... SATU orang. [pause]
[concerned] Bukan cuma keputusan. [short pause] Laporan dan tanah wakaf juga lewat SATU orang. [pause]
[exhales] [calmly] [warmly] Semuanya bisa ditulis. [short pause] Mulai dari keputusan. [short pause]
[clearly] Dua puluh sembilan keputusan — jelas siapa yang berwenang. [short pause]
[upbeat] Lalu, laporan semua unit — terbaca di satu tempat. [short pause]
[relieved] [hopeful] Terakhir, tanah wakaf TERCATAT, bukan cuma diingat. [pause]
[confident] Ini Sistem Tata Kelola Yayasan — seratus tujuh puluh dua dokumen. [pause]
[warmly] Unit bertambah, keputusan tetap JALAN. [short pause]
[firmly] [confident] Rapikan kerja pondok sekarang.
```

## Lengkung emosi

Cerita ini naik dari berat ke lega. Tag mengikuti lengkung itu:

| Bagian | Tag | Kenapa |
|---|---|---|
| Hook: "Santri bertambah. Unit bertambah." | `[serious] [slowly]` | Dua ketukan pendek, berat. |
| "Semua keputusan masih menunggu… SATU orang." | `[tired]` + titik tiga + huruf besar | "Menunggu…" ditahan, lalu "SATU" jatuh. Ini beban utamanya. |
| "Bukan cuma keputusan… Laporan dan tanah wakaf juga lewat SATU orang." | `[concerned]` | Beban bertambah, nada naik cemas. |
| Titik balik: "Semuanya bisa ditulis." | `[exhales] [calmly] [warmly]` | Satu embusan napas sebelum kalimat, tanda lega. Dari sini nada hangat. |
| "Dua puluh sembilan keputusan — jelas siapa yang berwenang." | `[clearly]` | Jawaban pertama, jernih. Tanda pisah memberi jeda pendek sebelum jawabannya. |
| "Lalu, laporan semua unit — terbaca di satu tempat." | `[upbeat]` | Sedikit lebih ringan dan cepat, seperti beban terangkat. |
| "Terakhir, tanah wakaf TERCATAT, bukan cuma diingat." | `[relieved] [hopeful]` | Titik lega, jatuh bersama matahari terbit. "TERCATAT" ditekan, "bukan cuma diingat" turun. |
| "Ini Sistem Tata Kelola Yayasan — seratus tujuh puluh dua dokumen." | `[confident]` | Perkenalan produk, mantap. |
| "Unit bertambah, keputusan tetap JALAN." | `[warmly]` | Mengulang kalimat hook, tapi arahnya terbalik. Nada hangat dan lega. |
| "Rapikan kerja pondok sekarang." | `[firmly] [confident]` | Ajakan tegas, tanpa nada jualan. |

Aturan v4 yang dipakai: tag menempel sampai tag berikutnya (jadi diganti hanya saat nada berubah); tag menggambarkan **cara ucap**, bukan gerakan; huruf besar hemat (hanya SATU, TERCATAT, JALAN); titik tiga untuk jeda panjang, tanda pisah untuk ketukan pendek; `[pause]` untuk jeda antar bagian cerita.

## Kalau hasilnya kurang pas

| Gejala | Perbaikan |
|---|---|
| Tag terbaca keras | Hapus semua tag kecuali `[pause]`/`[short pause]`. Kalau masih terbaca, hapus semua tag. |
| Terlalu dramatis di hook | Hapus `[tired]`, biarkan `[serious]`. |
| Titik balik kurang terasa | Ganti `[exhales]` dengan `[sighs]`, atau hapus tag napas dan biarkan `[pause]` sebelum "Semuanya bisa ditulis." |
| Suara tidak konsisten antar kalimat | Naikkan Stability (mis. dari 45 ke 55). Stability lebih rendah (35–45) membuat tag lebih terasa, tapi suara lebih berubah-ubah. Ini saran umum, bukan angka pasti untuk suara Bram. |
| Terlalu panjang | Lihat bawah. |

## Durasi (dikalibrasi dari hasilmu)

Versi 1 dengan 169 suku kata menghasilkan **37 detik (Bram)** dan **36 detik (Finn)**. Itu kecepatan nyata ±4,6 suku kata/detik sudah termasuk jeda, bukan 5,4 seperti perkiraanku sebelumnya (jadi perkiraan 31–35 detik di atas meleset).

Versi 2 punya kata yang sama (169 suku kata), jadi perkirakan **±36–38 detik**. Tag napas dan titik tiga menambah sedikit, jeda `[pause]` yang kukurangi menguranginya.

Video v2 akan mengikuti audio, jadi **±38–40 detik** (sekarang 28,8). Itu panjang untuk iklan 4:5. Kalau mau lebih pendek, pilihanku, mulai yang paling aman:
1. Aku pangkas jeda antar kalimat di pascaproduksi (hemat 2–3 detik, suara tidak berubah).
2. Hapus "Bukan cuma keputusan." dari VO (8 suku kata, hemat ±1,7 detik). Di layar tetap tertulis.
3. Hapus "Ini Sistem Tata Kelola Yayasan," dari VO dan biarkan hanya di layar (hemat ±2 detik).

Bilang kalau mau salah satunya, nanti kutulis ulang.

---

## Hasil audio dari pengguna (21 Nov 2026): Finn, 32,76 detik

Berkas: `audio/vo.mp3` (dipakai apa adanya, jeda tidak dipangkas). Model v4, tag tidak terbaca keras.

**Yang kamu ubah dari naskah v2** (terdeteksi lewat Whisper dan dipakai sebagai acuan):

| Naskah v2 | Di audio |
|---|---|
| "Semuanya bisa ditulis. Mulai dari keputusan." | **"Harusnya semua ada sistemnya."** (jembatan baru) |
| "Terakhir, tanah wakaf tercatat, bukan cuma diingat." | Dipecah: "Terakhir" / "Tanah wakaf tercatat." / "Bukan cuma diingat." |
| "Ini Sistem Tata Kelola Yayasan, seratus tujuh puluh dua dokumen." | Dipecah: "Ini sistem Tata Kelola Yayasan." / "172 dokumen" |
| "Unit bertambah, keputusan tetap jalan." | Dipecah: "Unit bertambah" / "Keputusan tetap jalan." |
| "Lalu, laporan semua unit …" | "Lalu..." (berdiri sendiri) / "Laporan semua unit terbaca di satu tempat." |

Kalimat lain sama dengan naskah v2.

**Penyesuaian di video** (hanya yang perlu):
- Teks jembatan di layar diganti jadi "Keputusan, laporan, wakaf: harusnya semua ada sistemnya." supaya sama dengan ucapanmu dan tetap berdiri sendiri. Baris "Mulai dari keputusan." dipertahankan di layar (tidak diucapkan) karena menyambung ke label KEPUTUSAN, LALU, TERAKHIR.
- Panel produk dibuat bertahap: label "Sistem Tata Kelola Yayasan" muncul saat "Ini sistem Tata Kelola Yayasan.", angka 172 menghitung naik saat "172 dokumen".
- Selain itu teks layar tidak diubah.

**Batas kalimat (silencedetect + Whisper):** "Santri bertambah." 0,00–1,33 · "Unit bertambah." 1,62–2,73 · "Semua keputusan masih menunggu satu orang." 3,12–5,18 · "Bukan cuma keputusan." 5,60–6,90 · "Laporan dan tanah wakaf juga lewat satu orang." 7,28–9,85 · "Harusnya semua ada sistemnya." 10,28–12,21 · "29 keputusan, jelas siapa yang berwenang." 12,67–15,59 · "Lalu…" 16,07–16,54 · "Laporan semua unit terbaca di satu tempat." 16,74–19,00 · "Terakhir" 19,48–20,00 · "Tanah wakaf tercatat." 20,33–21,59 · "Bukan cuma diingat." 21,77–22,79 · "Ini sistem Tata Kelola Yayasan." 23,57–25,48 · "172 dokumen" 25,75–27,44 · "Unit bertambah" 28,02–29,01 · "Keputusan tetap jalan." 29,23–30,69 · "Rapikan kerja pondok sekarang." 31,17–32,49.

**Catatan:** nama produk "Tata Kelola Yayasan" terdengar agak menempel di Finn (Whisper membacanya "tataklola yayasan"). Sama seperti di proyek lain. Kalau mau lebih jelas, generate ulang satu kalimat itu dengan "Tata Kelola Yayasan" dipisah koma (mis. "Ini sistem Tata, Kelola, Yayasan.") atau pakai suara Bram.

Video v2 = 33,2 detik (audio 32,76 + ekor 0,44).
