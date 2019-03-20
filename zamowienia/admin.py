from django.contrib import admin
from zamowienia.models import Pracownik, Wyplata, Sprzet, Cena, Pozycja, Zamowienie, ListaPozycji, ListaObslugujacych
from django.contrib.admin.models import LogEntry


# Register your models here.


class ZamowienieAdmin(admin.ModelAdmin):
    list_display = (
        'pracownik_skladajacy',
        'czy_nowe',
        'data_zlozenia',
    )


class PracownikAdmin(admin.ModelAdmin):
    list_display = (
        'imie',
        'nazwisko',
    )


class WyplataAdmin(admin.ModelAdmin):
    list_display = (
        'pracownik',
        'kwota',
    )


class SprzetAdmin(admin.ModelAdmin):
    list_display = (
        'nazwa',
    )


class CenaAdmin(admin.ModelAdmin):
    list_display = (
        'sprzet',
        'cena',
        'data_wprowadzenia_ceny',
    )


class PozycjaAdmin(admin.ModelAdmin):
    list_display = (
        'sprzet',
        'ilosc',
        'poczatek_uzywania',
        'koniec_uzywania',
    )


class ListaPozycjiAdmin(admin.ModelAdmin):
    list_display = (
        'zamowienie',
        'pozycja',
    )


class ListaObslugujacychAdmin(admin.ModelAdmin):
    list_display = (
        'zamowienie',
        'pracownik',
        'data_przypisania',
    )


admin.site.register(Zamowienie, ZamowienieAdmin)
admin.site.register(Pracownik, PracownikAdmin)
admin.site.register(Wyplata, WyplataAdmin)
admin.site.register(Sprzet, SprzetAdmin)
admin.site.register(Cena, CenaAdmin)
admin.site.register(Pozycja, PozycjaAdmin)
admin.site.register(ListaPozycji, ListaPozycjiAdmin)
admin.site.register(ListaObslugujacych, ListaObslugujacychAdmin)
admin.site.register(LogEntry)
