from django.shortcuts import render

def index(request):

    context = {
        "link_infografia": "/static/infografia_markdown_kit.png",
        "link_guia_pdf": "https://drive.google.com/file/d/18nkQbTFr9D7H2SbS7l5CclC30x3NQYyR/preview",
        "link_presentacion_slides": "https://docs.google.com/presentation/d/1U-y4GK-R2F9dKMSupUNpXbajrhl0YfsY/preview",
        "link_video_tutorial": "https://youtu.be/OpPGgiUCZx4?si=OwhHkCOt-5GckTfU",
    }
    return render(request, 'index.html', context)
