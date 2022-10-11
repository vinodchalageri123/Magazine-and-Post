from django.http import HttpResponseRedirect
from django.shortcuts import render
from Magazine.models import Magazines
from Magazine.forms import MagazinesForm
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def home(request):
    return render(request, "authentication/base.html")


def all_magazine(request):
    magazine_list = Magazines.objects.all()
    return render(request, 'authentication/display_magazine.html', {'magazine_list': magazine_list})


def add_magazine(request):
    submitted = False
    if request.method == "POST":
        form = MagazinesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_magazine?submitted=True')
    else:
        form = MagazinesForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'authentication/add_magazine.html', {'form': form, 'submitted': submitted})


# def search_magazine(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         magazines = Magazines.objects.filter(magazine_name=searched)
#         return render(request, 'authentication/search_magazine.html', {'searched': searched, 'magazines': magazines})
#     else:
#         return render(request, 'authentication/search_magazine.html', {})


def magazine_pdf(request):
    buf = io.BytesIO()

    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # lines = [
    #     "this is 1",
    #     "this is 2",
    #     "this is 3",
    # ]
    magazines = Magazines.objects.all()

    lines = []

    for magazine in magazines:
        lines.append(magazine.magazine_name)
        # lines.append(magazine.published_at)
        # lines.append(magazine.magazine_copy)
        # lines.append(magazine.uploaded_by)
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='magazine.pdf')
