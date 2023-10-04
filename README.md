# Tugas 5

# Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    - elemen selector digunakan untuk memilih element HTML tertentu berdasarkan nama elemennya. Sehinnga ketika melakukan perubahan pada HTML kita dapat menentukan apakah perubahan tersebut difungsika untuk universal atau hanya di beberapa elemen saja. Dalam kode saya, saya menggunakan elemen selctor dengan tipe class. sehingga perubahan saya hanya berada pada class itu saja.

# Jelaskan HTML5 Tag yang kamu ketahui
    - <a>: Elemen ini digunakan untuk membuat tautan (link) ke halaman web lain atau ke bagian lain di dalam halaman yang sama.
    - <head>: Elemen ini digunakan untuk menampung informasi tentang dokumen seperti judul, meta informasi, dan link ke berkas eksternal seperti stylesheet.
    - <html>: Ini adalah elemen root yang digunakan untuk mengelilingi seluruh isi halaman web.
    - <style>: Ini digunakan untuk menempatkan kode CSS langsung di dalam halaman HTML.
    <img>: Ini digunakan untuk menyisipkan gambar dalam halaman web.

# Jelaskan perbedaan antara margin dan padding.
    - Margin adalah ruang di luar batas luar elemen. Margin digunakan untuk mengatur jarak antara elemen dengan elemen lainnya di sekitarnya, yang dapat memengaruhi tata letak elemen tersebut terhadap elemen lain di halaman.
    - Padding adalah ruang di antara batas elemen dan kontennya. Padding digunakan untuk mengatur jarak antara konten elemen dan batas elemen tersebut. Dengan kata lain, padding mengatur ruang di dalam elemen. 

    ![Alt text](<Screen Shot 2023-10-04 at 08.42.16.png>)
    diatas merupakan gambaran perbedaan dari margin dan padding


# Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    - Tailwind CSS dan Bootstrap adalah dua framework CSS yang memiliki pendekatan yang berbeda dalam desain dan pengembangan web. Bootstrap menyediakan komponen siap pakai dengan gaya bawaan yang lebih kaku, sementara Tailwind memberikan utilitas CSS yang sangat fleksibel sehingga lebih baik digunakan ketika diperlukan banyak kustomisasi. Sedangkan Bootsstrap sebaiknya digunakan ketika tidak butuh banyak kustomisasi.
    
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - saya melakuakn pewarnaan dasar pada setiap laman web dan pada elemen html tertentu. Saya melakukan pewarnaan dasar dengan menggunakan :
    body {
        background-color: rgb(249, 220, 220);
    
        
    }

    - lalu saya mmbuat class (elemen selector) dan membuat dasar dasar atau merubah warna sesuai dengan keinginan saya, seperti contohnya pada login html, saya membuat ;
    .container {
        display: flex;
        flex-direction: column; 
        align-items: center; 
        text-align: center; 
    }

    .login {
        background-color: rgb(232, 187, 187);
        padding: 50px;
        border-radius: 100px;
        
    }

    .heading {
        background-color: rgb(211, 155, 155);
        padding:  25px;
        border-radius: 50px;
        margin-bottom: 20px;
    }


    container merupakan class yang isinya adalah class login dan heading, sehingga saya bisa megatur tata letak login dan heading pada container, lalu saya mengkutomisasi login dan headingnya spesifik di kelas login dan heading karenna saya mau bentuk yang berbeda pada login dan heading. 
    Hal tersebut saya gunakan di setiap laman html saya. 






















# Tugas 4

#  Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

- Django UserCreationForm merupakan kerangka kerja djanggo yang digunakan untuk pembuatan atau registrasi pengguna (user) pada web yang dibangun dengan django. Django UserCrationForm akan membuat formulir pengguna sehingga operasi umum yang dilakukan adalah berkaitan dengan pengguna dan otentikasi. 
- Kelebihan : 
 1. UserCreationForm membantu memvalidasi data pengguna secara otomatis 
 2. Form ini telah disediakan oleh Django, sehingga sangat mudah untuk digunakan, tanpa perlu menulis kode secara manual
 3. Terhubung dengan model pengguna Django (user) secara otomatis, sehingga data yang dimasukkan akan disimpan di database yang benar
 4. Dapat dikostumisasi dengan mudah

 - Kekurangan :
 1. Tampilan yang dihasilkan tidak terlalu bagus
 2. Form ini dirancang untuk pengguna biasa sehingga memiliki fungsionalitas terbatas

# Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

- Autentikasi adalah proses verifikasi pengguna , tujuannya adalah memastikan bahwa pengguna yang mengakses aplikasi adalah dirinya sendiri. Proses ini contohnya ketika memasukkan username dan password. 
- Otorisasi adalah proses mengontrol hak akses pengguna setalah mereka berhasil di autentikasi. Pada proses ini akan ditentukan apakah pengakses boleh merubah, melihat dan menghapus sesuatu pada aplikasi sehingga pada proses ini akan ditentukan apakah mereka mengakses atau melakukan sesuatu sesuai dengan peran dan izin. 
- Autentikasi dan otorisasi sangat penting karena kedua hal ini memastikan apakah pengguna yang mengakses suatu web/aplikasi merupakan orang yang tepat dan yang dilakukan oleh pengguna tersebut merupakan aktivitas yang sesuai dengan peran atau izin. 

# Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

- cookies adalah data kecil yang disimpan di perangkat pengguna saat pengguna mengunjungi situs web. Cookies adalah salah satu mekanisme yang umum digunakan dalam pengembangan web untuk menyimpan informasi pada perangkat pengguna dan mengidentifikasi sesi pengguna.
- Saat seorang pengguna masuk atau mengakses sesuatu yang memerlukan identifikasi, Django akan menyimpan data sesi tersebut di server. Data sesi ini dapat berisi informasi seperti ID pengguna yang masuk, preferensi, atau apa pun yang perlu diingat selama sesi.Django kemudian mengirimkan cookie dengan nama sessionid kepada perangkat pengguna. Cookie ini berisi ID sesi yang digunakan oleh Django untuk mengidentifikasi sesi pengguna di server.Setiap kali pengguna membuat permintaan ke situs web, cookie sessionid akan disertakan dalam permintaan HTTP. Django akan mengidentifikasi sesi pengguna berdasarkan cookie ini.  Django akan menggunakan ID sesi yang ditemukan dalam cookie untuk mencari data sesi yang sesuai di server. Data sesi ini kemudian digunakan untuk mengidentifikasi pengguna, mengembalikan preferensi, dan melakukan tindakan lain yang diperlukan selama sesi.

# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
- Penggunaan cookies sebenarnya aman jika di implementasikan dengan benar. Namun, tetap terdapat risiko potensial yang harus diwaspadai, yaitu tekait dengan keamanan data serta kebocoran informasi. 
- Cookies bisa saja menyimpan data sensitif, sehingga diperlukannya enkripsi sebelum menyimpan data pada cookies. Kebocoran informasi juga bisa diakibatkan oleh cookies dimana data sensitif yang terdapat pada cookies diakses oleh orang yang tidak sah. Cookies juga dapat digunakan untuk serangan seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF) jika tidak diimplementasikan dengan benar. Pengembang harus memastikan bahwa aplikasi mereka memiliki langkah-langkah keamanan yang tepat untuk melindungi cookies dari jenis serangan ini. Penggunaan cookies aman juga tergantung pada penggunaan protokol HTTPS yang mengenkripsi lalu lintas antara server dan perangkat pengguna. Tanpa HTTPS, cookies dapat dengan mudah disadap oleh pihak ketiga selama transmisi.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1.  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

- Pada awalnya kita membuat fungsi dan Form registrasi. Fungsi register yang memiliki parameter request dibuat pada views.py pada direktori main. Lalu, membuat form registrasi dengan membuat file register.html dan mengisi dengan template pada main/tempalate. Selanjutnya impor fungsi yang telat dibuat tadi di urls.py pada main dan tambahkan path url dalam urlpatterns
- Membuat fungsi login pada di views.py pada main beserta impor login pada bagian atas. Selanjutnya membuat berkas login.html pada main/template. Lalu impor dan tambahkan path url dalam urlpatterns di urls.py pada main. 
- Membuat fungsi logout yang menerima parameter request beserta import logout-nya. Tambahkan potongan kode pada fungsi logout da pada berkas main.html. Terakhir tambahkan import dan tambahkan path url ke dalam urlpatterns
- Untuk merestrikasi Akses Halaman main import : 
    from django.contrib.auth.decorators import login_required
pada views.py di main lalu tambahkan kode : 
    @login_required(login_url='/login')
diatas fungsi show_main

2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

3. Menghubungkan model Item dengan User
- Tambahkan kode : 
    from django.contrib.auth.models import User
pada models.py yang ada pada subdirektori main. Tambahkan juga potongan kode 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
pada models Item yang sudah dibuat. 
- Pada view.py di main, ubah potongan create_item mejadi : 
    def create_item(request):
 form = ItemForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))
dan ubah fungsi show_main menjad berikut :
    def show_main(request):
    item = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    }
- Setelah itu, lakukan migrasi 

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- pada views.py tambahkan import :
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
- pada login_user, tambahkan fungsi last_login dengan mengganti kode menjadi berikut: 
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
- Tambahkan 'last_login': request.COOKIES['last_login'] pada show_main ke variabel context.
- Ubah fungsi logout_user menjadi :
    def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
- lalu buka main.html dan tambahkann : 
    <h5>Sesi terakhir login: {{ last_login }}</h5>
di antara tabel dan tombol logout untuk menampilkan data last login.






















# Tugas 3

# Apa perbedaan antara form post dan form get dalam djanggo?
    - Dalam hal keamanan, POST dianggap lebih aman dibandingkan GET karena data tidak akan terlihat di URL. Meskipun sebenarnya keamanan juga tetap tergantung tindak keamanan yang diambil dalam suatu server. 
    - POST biasanya digunakan untuk mengirimkan data yang berukuran besar karena tidak terdapat batasan ukuran yang ditetapkan dalam spesifikasi HTTP. Sedangkan, GET memiliki batasan ukuran data yang lebih kecil karena data dikirim melalui URL. 
    - POST merupakan metode yang digunakan untuk mengirimkan data ke server web. Sedangkan, GET merupakan metode yang digunakan untuk membaca atau mengembalikan data dari server web. 
    - POST tidak dapat di-chace sedangkan GET dapat di-cache
    - POST dapat digunakan untuk mengubah data, sedangkan GET hanya dapat digunakan untuk membaca sebuah data tanpa mengubahnya

# Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    - XML (eXtensible Markup Language):
    XML digunakan untuk mengatur dan menyimpan data secara terstruktur dan fokus utamanya adalah pada hierarki dan struktur data. XML biasanya digunakan untuk mengirim data antara sistem yang berbeda atau sebagai format penyimpanan data terstruktur. Validasi data dapat dengan mudah diimplementasikan melalui penggunaan skema XML.

    - JSON (JavaScript Object Notation):
    JSON digunakan untuk pertukaran data antara aplikasi, terutama dalam pengembangan web dan komunikasi melalui API. Format datanya sederhana, mudah dibaca oleh manusia, dan lebih efisien daripada XML. Banyak digunakan dalam komunikasi antara server dan klien dalam pengembangan web modern.Cocok untuk data yang memiliki struktur yang lebih fleksibel, seperti objek dan daftar.

    - HTML (HyperText Markup Language):
    HTML digunakan untuk merender dan menampilkan konten di browser web. HTML tidak cocok untuk pertukaran data terstruktur karena fungsinya adalah untuk mengatur tampilan dan format halaman web. Markup (tag) digunakan untuk mengatur tampilan dan hubungan antara elemen-elemen di halaman web.


# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON sering digunakan dalam pertukaran data karena memiliki format yang sangat sederhana dan mudah dibaca oleh manusia. Format JSON juga lebih ringan dibandingkan dengan XML dimana hal ini penting untuk efisiensi dan kecepatan dalam pengembangan web. JSON juga memiliki kemampuan untuk mengakomodasi tipe data yang umum digunakan dan dapat diimplementasikan dengan mudah dalam berbagai bahasa pemrograman. Dengan fleksibilitas dalam pengaturan struktur data dan kemampuannya untuk menyisipkan informasi, JSON menjadi format data yang sangat sesuai untuk berbagai keperluan pertukaran data dalam lingkungan web modern.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
        - Membuat file baru dengan mama forms.py pada main untuk membuat struktu form yang dapat menerima produk baru. Lalu tambahkan kode dibawah : 
            from django.forms import ModelForm
            from main.models import Item
            class ItemForm(ModelForm):
                class Meta:
                    model = Item
                    fields = ["name", "amount", "description"]
        - sesuai dengan ketentuan soal, yaitu modelnya bernama Item.
        - Buka views.py pada main dan tambahkan import :  
            from django.http import HttpResponseRedirect
            from main.forms import ItemForm
            from django.urls import reverse
        - Membuat fungsi baru bernama "create_item" pada "views.py". Isi dengan : 
            def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_Item.html", context)
        - nama creat item karena product pada tutorial diganti dengan Item, sesuai dengan ketentuan soal
        - Ubah fungsi show_main pada views.py menjadi :
            def show_main(request):
                items = Item.objects.all()
                context = {
                'nama_aplikasi': 'Pacil Cafe',
                'nama': "Novita Mulia Sari",
                'kelas': "PBP A", 
                'items': items,
            }

                return render(request, "main.html", context)
        - fungsi Item.objects.all() digunakan untuk mengambil seluruh object item pada database. 
        - buka urls.py pada main dan import crate_item 
            from main.views import show_main, create_item
        - Menambahkan path url pada "urlpatterns" yang ada di "urls.py" pada direktori "main" supaya bisa mengakses fungsi yang sudah di-import sebelumnya 
            path('create-item', create_item, name='create_item')
        - Membuat file baru bernama create_item.html pada direktori main/templates. lalu isi dengan: 
            {% extends 'base.html' %} 

            {% block content %}
            <h1>Add New Item</h1>

            <form method="POST">
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td>
                            <input type="submit" value="Add Item"/>
                        </td>
                    </tr>
                </table>
            </form>

            {% endblock %}"
        - Lalu buka "main.html" dan tambahkan kode berikut supaya bisa menampilkan data produk dalam bentuk tabel dan juga ada tombol "Add New Item" yang akan redirect ke page form
            <table>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Description</th>
                    <th>Date Added</th>
                </tr>

                {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

                {% for item in items %}
                    <tr>
                        <td>{{item.name}}</td>
                        <td>{{item.price}}</td>
                        <td>{{item.description}}</td>
                        <td>{{item.date_added}}</td>
                    </tr>
                {% endfor %}
            </table>

            <br />

            <a href="{% url 'main:create_item' %}">
                <button>
                    Add New Item
                </button>
            </a>

            {% endblock content %}"
        - Run project django dengan mengaktifkan env terlebih dahulu lalu jalankan 
            python3 manage.py runserver
            dan buka http://localhost:8000 
2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID
- Buka views.py pada main dan import : 
        from django.http import HttpResponse
        from django.core import serializers
- membuat fungsi bernama show_xml dan show_jason yang menerima parameter request dan show_xml_by_id dan show_json_by_id yang menerima paramter request dan id dengan cara berikut :
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml dan show_json akan menampilkan semuanya. sedangkan, show_xml_by_id dan show_json_by_id akan menampilkan sesuai dengan id yang dimasukkan. 

3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
- Buka file urls.py yang terdapat pada main dan import :
    from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
- Menambahkan path url pada "urlpatterns" yang ada di "urls.py" pada direktori "main" untuk mengakses fungsi yang sudah diimpor tadi dengan cara berikut : 
    - path('xml/', show_xml, name='show_xml'), 
    - path('json/', show_json, name='show_json'), 
    - path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    - path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
- Run project django dengan mengaktifkan env terlebih dahulu, lalu run dengan :
        python3 manage.py runserver
        dan buka http://localhost:8000/xml, http://localhost:8000/json, http://localhost:8000/xml/[id], http://localhost:8000/json/[id],

hasil ss url = ristek.link/pbptugas3

# Tugas 2
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

    ristek.link/PBPbagan
    
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



