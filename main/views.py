from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi': 'Pacil Cafe',
        'nama': 'Novita Mulia Sari',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)