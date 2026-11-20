# Naskah: Pengurus yayasan pesantren, format Satu Tiang (video 4:5, ±29 detik, tanpa audio dulu)

Status: **terkunci (v3)**. Hook memakai versi asli pengguna. Tombol: "Rapikan kerja pondok sekarang" (dipilih pengguna). Dua dokumen (dashboard, berita acara wakaf) dipakai apa adanya, halamannya contoh dari kode; nama dokumen dicek pengguna ke Product Knowledge sebelum tayang.
Format: Satu Tiang v1 (tanya → risiko → bukti jadi pondasi → angka → tombol). Beda di isi: empat unit pesantren di atas satu tiang "PENGURUS".

## Kenapa flow draf awal kurang enak

| # | Masalah | Akibat | Perbaikan |
|---|---|---|---|
| 1 | Detik 0–3 memuat 17 kata sekaligus | Tidak terbaca di HP, hook tidak berhenti di satu pertanyaan | Hook dibuka satu per satu seperti Satu Tiang: sapaan → keadaan → pertanyaan |
| 2 | Masalah cuma satu kalimat ("menunggu satu orang"), tapi jawabannya tiga dokumen yang tidak berhubungan (matriks, dashboard, wakaf) | Loncat. Penonton bertanya "kenapa tiba-tiba dashboard?" (sama seperti keluhan VO Satu Tiang) | **Masalahnya dipecah jadi tiga, dan tiga dokumen menjawab satu per satu, urutannya sama**: keputusan → laporan → wakaf |
| 3 | Tiap dokumen langsung dijelaskan tanpa label | Penonton tidak tahu dokumen itu menjawab apa | Tiap dokumen dibuka dengan label yang sama dengan butir masalahnya: KEPUTUSAN, LAPORAN, WAKAF |
| 4 | Penutup (172 dokumen) dan tombol tidak menyambung ke pembuka | Cerita tidak bulat | Penutup memakai kata pembuka: "Unit bertambah, keputusan tetap jalan." |
| 5 | "tanpa bergantung satu orang" (tombol) | Kata depan hilang: "bergantung **pada**" | Diperbaiki |
| 6 | "satu pemutus per baris" | "Pemutus" terbaca pemutus arus. Dan belum tentu benar: satu baris matriks bisa punya lebih dari satu pihak | "jelas siapa yang berwenang" |

## Bagan fitur → manfaat → RL (BenBi, dipakai juga untuk C3H)

RL di bawah **hipotesis penyusun, belum dari pembeli**. Uji dulu sebelum tayang. Kalau kamu punya keluhan nyata pengurus pesantren (dari CS), kirim dan kuganti.

Target: pengurus harian yayasan pesantren (pembeli) yang unitnya bertambah. Pemakai: unit (Pondok, MI, MTs, TK). Fase: tumbuh, mulai kewalahan.

| Fitur (fakta) | Manfaat | RL (hipotesis) | BenBi |
|---|---|---|---|
| Matriks kewenangan, 29 keputusan | tiap keputusan punya pihak yang berwenang | Kepala MI tidak telepon Bapak untuk hal yang memang haknya. Bapak tidak dipanggil tiap malam. | Less Time, Less Stress |
| Dashboard kinerja unit **[perlu dicek]** | laporan semua unit di satu tempat | Rapat bulanan tidak diawali "laporan MTs belum masuk" | Less Effort, Less Time |
| Berita acara serah terima hibah dan wakaf **[perlu dicek]** | tiap serah terima tertulis | Saat pengurus berganti, penerus tahu tanah mana milik siapa | No Stress, Legacy & Pahala |
| 172 dokumen dalam 14 kategori | semua ada di satu sistem | Unit baru dibuka, aturannya sudah ada | Less Effort |

## Bagan C3H: masalah (kebalikan RL) dan hambatan

| RL | Masalah |
|---|---|
| keputusan unit jalan tanpa menunggu Bapak | keputusan menunggu satu orang |
| laporan semua unit terbaca sekaligus | laporan tersebar di tiap unit |
| tanah wakaf tercatat | tanah wakaf cuma diingat |

Tiga masalah ini jadi tulang punggung video: **tiga masalah di adegan 2, tiga dokumen di adegan 3, dengan urutan sama.**

Persona yang melihat iklan: pengurus harian (sapaan "Bapak", sesuai pagar produk).

## Alternatif headline hook (C3H, semua rumus Bagian I = asli)

| # | Rumus | Headline | Kenapa cocok |
|---|---|---|---|
| 1 | **#27** (asli) | "Unit bertambah, Bapak kewalahan?" lalu "Tandanya:" dan tiga butir (keputusan menunggu satu orang · laporan unit tersebar · tanah wakaf cuma diingat) | Tiga butir masalah = tiga dokumen jawaban. Ini yang memperbaiki flow. |
| 2 | **#20** (asli) | "Capek, semua keputusan pondok menunggu satu orang (padahal unitnya sudah empat)?" | Kurung memamerkan keadaan: empat unit, satu orang. Pendek. Hanya satu masalah, jadi tiga dokumen tetap perlu jembatan. |
| 3 | **#29** (asli) | "Salah satu cara agar pondok tetap jalan saat pengurus berhalangan adalah ada yang tahu semua aturannya. Sayangnya, aturan itu cuma diingat satu orang. Bapak termasuk?" | Paling dekat ke Satu Tiang. Kepanjangan untuk 4,5 detik, harus dipecah di dua adegan. |
| 4 | **#7** (asli) | "Pengen pondok tetap jalan meski Bapak berhalangan, tapi belum tahu mulai dari mana?" | Pendek. Tidak menyebut tiga masalah, jadi flow tiga-tiga hilang. |
| 5 | **#19** (asli) | "Siapa, hayoo, yang ingin keputusan unit jalan tanpa menunggu satu orang?" | Pertanyaan membuat berhenti scroll. Sama: satu masalah saja. |

**Keputusan pengguna:** hook memakai **versi asli draf**, bukan salah satu rumus di atas: "PENGURUS YAYASAN PESANTREN," lalu "Santri bertambah. Unit bertambah. Semua keputusan masih menunggu satu orang." Ini bukan rumus C3H (pernyataan tiga ketukan, bukan pertanyaan). Rumus terdekatnya #20 tanpa tanya. Teks dipakai persis. Satu catatan: 17 kata di layar butuh sekitar 3,8 detik, bukan 3 detik, supaya terbaca di HP.

Konsekuensi untuk flow: hook sudah menyebut **keputusan**. Jadi adegan 2 tidak mengulang butir keputusan. Adegan 2 membuka dengan "Bukan cuma keputusan." lalu menambah dua butir lain (laporan, wakaf). Tiga butir tetap berpasangan dengan tiga dokumen.

## Rundown v3 (usulan)

| Detik | Adegan | Teks di layar | Visual |
|---|---|---|---|
| 0–3,8 | 1. Tanya | "PENGURUS YAYASAN PESANTREN," (0,3) · "Santri bertambah. Unit bertambah." (1,3) · "Semua keputusan masih menunggu satu orang." (2,6, kuning) | Empat bangunan (PONDOK, MI, MTs, TK) berderet di atas satu balok yang bertumpu pada satu tiang "PENGURUS". Titik santri menumpuk. TK jatuh menyusul. Panah dari tiap unit turun ke tiang. |
| 3,8–8,2 | 2. Bukan cuma keputusan | "Bukan cuma keputusan." (3,95) · "Laporan tiap unit juga dikirim ke satu orang." (5,2) · "Tanah wakaf juga cuma diingat satu orang." (6,6) | Bangunan miring, tiang menyala kuning dengan angka 1. Ikon laporan dan ikon wakaf meluncur ke tiang yang sama. |
| 8,2–11,9 | **Jembatan** | "Keputusan, laporan, wakaf: semuanya bisa ditulis." (8,5) · "Mulai dari **keputusan.**" (9,55) · dibiarkan terbaca sampai 11,6 | Teks berdiri sendiri di atas bangunan miring. Jeda baca sekitar 1,5 detik setelah kalimat lengkap. (Revisi 2: pertama ditambahkan, lalu diperpanjang karena terlalu cepat.) |
| 11,9–15,5 | 3a. Keputusan | Label KEPUTUSAN · "29 keputusan, jelas siapa yang berwenang." | Halaman Matriks Kewenangan jatuh berayun, jadi pondasi pertama. |
| 15,6–19,2 | 3b. Laporan | Label LALU, LAPORAN · "Laporan semua unit terbaca di satu tempat." | Halaman Dashboard Kinerja Unit, pondasi kedua. |
| 19,3–22,9 | 3c. Wakaf | Label TERAKHIR, WAKAF · "Tanah wakaf tercatat, bukan cuma diingat." | Berita Acara Serah Terima Hibah dan Wakaf, pondasi ketiga. Bangunan tegak sekali hentak, tiang tersingkir, matahari terbit. |
| 22,9–26,1 | 4. Angka | Label "Sistem Tata Kelola Yayasan" · **172 dokumen** menghitung naik · "14 kategori" | Pondasi menyatu jadi alas berisi 172 sel. Empat belas tab A–N di atas alas. |
| 26,1–28,8 | 5. Tombol | "Unit bertambah, keputusan tetap jalan." · Tombol "Rapikan kerja pondok sekarang" | Teks penutup di panel. Tombol naik dari tanah. |

Prinsip waktu: **waktu baca menang atas target durasi.** Total ±29 detik (brief awal 20–25), dipakai supaya tiap teks sempat terbaca. Kalau perlu dipangkas, pangkas di jeda antar adegan, bukan di waktu baca teks.

Beda dari draf awal: dokumen **tiga**, bukan enam (Satu Tiang memakai enam). Tiap dokumen dapat 3,7 detik. Panah ke "kursi" diganti panah ke tiang, supaya benda penghubungnya tetap satu (tiang) seperti Satu Tiang.

## Cek bahasa (copy-indonesia), teks pendek dibaca lepas

| Teks | Hasil |
|---|---|
| PENGURUS YAYASAN PESANTREN, | Lolos (sapaan). |
| Santri bertambah. Unit bertambah. | Lolos. Dua kalimat sejajar (teks asli pengguna). |
| Semua keputusan masih menunggu satu orang. | Lolos (teks asli pengguna). |
| Bukan cuma keputusan. | Lolos. Menunjuk ke "keputusan" di hook. |
| Laporan tiap unit juga dikirim ke satu orang. | Lolos. "Juga" menyambung ke "bukan cuma". |
| Tanah wakaf juga cuma diingat satu orang. | Lolos. Sekali baca: hanya satu orang yang mengingatnya. |
| 29 keputusan, jelas siapa yang berwenang. | Lolos. (Draf awal: "satu pemutus per baris" gagal, lihat tabel di atas.) |
| Laporan semua unit terbaca di satu tempat. | Lolos. |
| Tanah wakaf tercatat, bukan cuma diingat. | Lolos uji dua kalimat: "Tanah wakaf tercatat. Tanah wakaf tidak cuma diingat." Satu sumbu: cara tanah wakaf disimpan. |
| Unit bertambah, keputusan tetap jalan. | Lolos. Mengulang "unit bertambah" dari pembuka, jadi penutup terasa bulat. |
| Keputusan, laporan, wakaf: semuanya bisa ditulis. | Lolos. Sekali baca, berdiri sendiri (menyebut ketiga hal, tidak bergantung pada layar sebelumnya). |
| Mulai dari keputusan. | Lolos. Kata depan "dari" ikut. |
| LALU, LAPORAN · TERAKHIR, WAKAF | Lolos. Kata sambung urutan, menyambung dari "Mulai dari keputusan." |
| Rapikan kerja pondok sekarang | Lolos. Perintah yang menyebut hasil (rapi). Pengganti "Tata pondok tanpa bergantung satu orang" (kata "pada" hilang, dan terlalu panjang untuk tombol). |

## Yang harus dicek sebelum dikunci (kejujuran)

1. **Dashboard kinerja unit**: aku tidak punya Product Knowledge di sesi ini, jadi belum bisa memastikan dokumen itu ada. Kirim nama atau kode dokumennya. Kalau tidak ada, penggantinya dari dokumen yang sudah terverifikasi: Excel laporan keuangan (EXCL-KU-013, baris "Selisih (harus nol)") atau pemantauan sisa lebih (EXCL-PJ-011).
2. **Berita acara serah terima hibah dan wakaf**: kirim nama atau kode dokumennya juga.
3. **Wakaf**: "tercatat" hanya soal catatan internal yayasan. Tidak ada klaim sah secara hukum, sertifikat wakaf, atau pengganti notaris/PPAT/BWI.
4. **29 keputusan** dan **172 dokumen · 14 kategori** sudah terverifikasi dari Product Knowledge proyek lain (Tata Kelola dan Satu Tiang).

## Pagar

Tanpa harga, tanpa nama brand Ardya, tanpa kata "template/bundle", tanpa klaim "sesuai peraturan terbaru", tanpa janji hukum, sapaan "Bapak".
