from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Album, Song
#from django.http import Http404

# # Create your views here.
# def index(request):
#     all_albums = Album.objects.all()
#     return render(request, 'music/index.html', {'all_albums' : all_albums})
#
# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album' : album})
#

from django.views import generic

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album':album,
            'error_message': "You did not select a valid song",
        })
    else:
        if selected_song.is_favorite==False:
            selected_song.is_favorite = True
        else:
            selected_song.is_favorite = False
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
