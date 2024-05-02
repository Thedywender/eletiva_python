from django import forms
from playlists.validators import validate_music_length, validate_name_without_numbers
from datetime import datetime


class CreateMusicForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[validate_name_without_numbers],
        label="Nome da música",
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Insira o nome da música"}),
    )
    recorded_at = forms.DateField(
        label="Data da gravação",
        widget=forms.DateInput(attrs={"type": "date"}),
        initial=datetime.today().date,
    )
    length_in_seconds = forms.IntegerField(
        validators=[validate_music_length],
        label="Duração em segundos",
        min_value=1,
        max_value=600,
        widget=forms.NumberInput(attrs={"placeholder": "Insira a duração"}),
    )


class CreatePlaylistForm(forms.Form):
    name = forms.CharField(max_length=50, validators=[validate_name_without_numbers])
    is_active = forms.BooleanField()


class CreateSingerForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        validators=[validate_name_without_numbers],
        label="Nome do cantor",
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Insira o nome do cantor"}),
    )
