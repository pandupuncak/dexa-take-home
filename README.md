# dexa-take-home
Cara menjalankan adalah dengan:
1. Masuk ke dalam terminal di folder "dexa-take-home" ini.
2. Install libraries dengan menjalankan komando "pip install -r requirements.txt"
3. Jalankan server dengan memasukkan command "uvicorn sql_app.main:app --reload"
4. Buka URL yang dituliskan pada terminal pada browser pilihan.
   1. Biasanya URL adalah "http://127.0.0.1:8000", tambahkan '/docs' di akhir URL tersebut menjadi http://127.0.0.1:8000/docs untuk mengakses API dari UI nya.