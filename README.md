# Penjelasan mengenai impelementasi checklist

1. Membuat sebuah proyek Djanggo baru
    - sebelum saya membuat proyek di djanggo, saya membuat sebuah folder dan membuka terminal pada folder tersebut, lalu membuat virtual environment dengan menjalankan perintah :
        python3 -m venv env
    - setelah itu saya mengaktifkan virtual environment dengan cara :
        source env/bin/activate
    - setelah itu saya membuat berkas bernama requirements.txt dan menambahkan beberapa dependencies, lalu saya memasangkan dependencies dengan cara menjalankan perintah : 
        pip install -r requirements.txt
    - Terakhir, membuat proyek djanggo dengan menjalankan perintah :
        django-admin startproject pacil_cafe .

2. membuat aplikasi dengan nama main pada proyek tersebut
    - saya membuat aplikasi main pada proyek dengan cara menjalankan : 
        python manage.py startapp main
    - lalu menambahkan aplikasi main pada proyek dengan cara menambahkan main pada installed app di setting.py pada proyek terluar. 

3. melakukan routing pada proyek agar dapat menjalankan aplikasi main
    - menambahkan main pada installed apps settings.py

4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib. 
    - membuat model dengan atribut wajib saya lakukan dengan mengisi folder models.py dengan:
      from django.db import models

        class Product(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()


5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - step ini saya lakukan dengan cara mengisi view.py dengan :
        def show_main(request):
        context = {
            'nama_aplikasi': 'Pacil Cafe',
            'nama': 'Novita Mulia Sari',
            'kelas': 'PBP A'
        }

        return render(request, "main.html", context)

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
     - Langkah pertama yang saya lakukan adalah dengan membuat berkas urls.py pada main dan isi urls.py dengan :
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
    - Buka urls.py pada proyek terluar dan impor fungsi include dari django.urls, lalu dalam variabel urlpatterns, tambahkan :
        path('main/', include('main.urls')),

# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    ristek.link/baganPBP
    
    - urls.py 
        request dari user awalnya akan diarahkan ke file urls.py untuk mencari pola url yang cocok
    - views.py 
        view function yang dipangil akan menerima request dari urls.py dan mengambil serta menyimpan data dalam database (model)
    - models.py 
        models.py akan berinteraksi dengan view function jika view function memerlukan akses ke database 
    - berkas html
        data dari proses tersebut nantinya akan ditampilkan pada file html dan dapat dilihat oleh user. 

# Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    - kita menggunakan virtual environment karena :
        1. Stable Environments
            virtual environment memberi lingkungan yang lebih stabil untuk proyek dengan mengasingkan dependensi proyek tersebut dari pengaruh sistem atau proyek lainnya.
        2. Reproducible Environments
            virtual environment memungkinkan menciptakan lingkungan yang dapat direplikasi dengan akurat menentukan versi Python dan paket lain yang dibutuhkan oleh proyek.
        3. Portable Environments
            virtual environment menyediakan lingkungan yang dapat dipindahkan untuk proyek dengan mengisolasi dependensi proyek dari sistem.

    - membuat aplikasi web berbasis django tanpa menggunakan virtual environment tetap bisa dilakukan, namun sangat disarankan untuk menggunakan virtual environment karena alasan yang telah dijelaskan diatas. Hal yang paling ditakutkan adalah terjadinya konflik antar dependensi proyek dan python. 
         

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pendekatan arsitektur yang digunakan dalam pengembangan perangkat lunak, terutama dalam konteks pembuatan aplikasi web. Pendekatan-pendekatan ini membantu dalam mengatur kode dan memisahkan peran-peran yang berbeda dalam suatu aplikasi. Berikut adalah penjelasan ringkas tentang masing-masing dan perbedaannya:

    - MVC (Model-View-Controller):
        Model: Menyimpan data dan logika bisnis aplikasi. Bertanggung jawab atas pemrosesan data, validasi, dan interaksi dengan basis data.
        View: Mengatur tampilan yang diperlihatkan kepada pengguna. Ini adalah antarmuka pengguna (UI) yang menampilkan data dari Model.
        Controller: Menangani masukan dari pengguna, mengelola permintaan, dan menghubungkan Model dengan View. Controller memproses permintaan pengguna dan memperbarui Model dan View sesuai kebutuhan.
    - MVT (Model-View-Template):
        Model: Sama seperti dalam MVC, ini menyimpan data dan logika bisnis aplikasi.
        View: Bertanggung jawab atas tampilan data kepada pengguna, mirip dengan View dalam MVC.
        Template: Bagian unik dari MVT. Template adalah berkas yang digunakan untuk menghasilkan tampilan HTML. Template berisi tag-tag dan logika template yang memungkinkan penggabungan data dari Model ke dalam tampilan.
    - MVVM (Model-View-ViewModel):
        Model: Serupa dengan Model dalam MVC, menyimpan data dan logika bisnis.
        View: Bertanggung jawab atas tampilan data kepada pengguna.
        ViewModel: Komponen perantara antara Model dan View. ViewModel memformat dan mempersiapkan data dari Model agar sesuai dengan tampilan yang diharapkan oleh View.

    - Perbedaan antara tiga model tersebut dapat diuraikan sebagai berikut:

        - Data Binding:

        MVC: Tidak memiliki mekanisme data binding bawaan, yang berarti perlu pengelolaan manual saat menghubungkan Model dan View.
        MVT: Dilengkapi dengan data binding bawaan dalam kerangka kerja Django, sehingga mempermudah pengelolaan data antara Model dan Template.
        MVVM: Menyediakan pengikatan data otomatis, artinya perubahan pada Model akan secara otomatis tercermin pada View, mengurangi kebutuhan untuk pengelolaan manual.

        -  Fungsi Umum:

        MVC: Digunakan dalam berbagai jenis aplikasi termasuk aplikasi web, mobile, dan desktop.
        MVT: Secara khusus digunakan untuk mengembangkan aplikasi web dengan bantuan Django.
        MVVM: Dikhususkan untuk pengembangan aplikasi dengan antarmuka pengguna yang kompleks, terutama pada platform seperti Xamarin dan Vue.js.
        
        - Antar Komponen:

        MVC: Dalam MVC, Controller berfungsi sebagai penghubung antara Model dan View. View mengirim input ke Controller, yang kemudian memprosesnya dan memperbarui Model serta View sesuai dengan kebutuhan pengguna.
        MVT: Pada MVT, View mengambil data dari Model dan meneruskannya ke Template untuk ditampilkan kepada pengguna.
        MVVM: Perantara antara View dan Model adalah ViewModel dalam MVVM. ViewModel mengambil data dari Model, menghubungkannya ke View, dan memformat data sesuai dengan kebutuhan tampilan.



