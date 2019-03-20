from django.db import models


# Create your models here.


class Pracownik(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)

    def __str__(self):
        return '{} {}'.format(self.imie, self.nazwisko)


class Wyplata(models.Model):
    pracownik = models.ForeignKey(Pracownik, on_delete=models.PROTECT)  # TODO: pole Stanowisko (i w Pracownik)
    kwota = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return '{}zł___{}'.format(self.kwota, self.pracownik)


class Sprzet(models.Model):
    nazwa = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.nazwa)


class Cena(models.Model):
    sprzet = models.ForeignKey(Sprzet, on_delete=models.PROTECT)
    cena = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    data_wprowadzenia_ceny = models.DateTimeField('obowiązuje od', auto_now_add=True)

    def __str__(self):
        return 'od:_{}___{}zł___{}'.format(self.data_wprowadzenia_ceny.date(), self.cena, self.sprzet)


class Pozycja(models.Model):
    sprzet = models.ForeignKey(Sprzet, on_delete=models.PROTECT)
    ilosc = models.IntegerField(default=0)
    poczatek_uzywania = models.DateTimeField('początek używania')
    koniec_uzywania = models.DateTimeField('koniec używania')

    def __str__(self):
        return 'od:_{}___do:_{}___{}___{}'.format(self.poczatek_uzywania.date(), self.koniec_uzywania.date(),
                                                  self.ilosc, self.sprzet)


class Zamowienie(models.Model):
    pracownik_skladajacy = models.ForeignKey(Pracownik, on_delete=models.PROTECT)
    czy_nowe = models.BooleanField(default=True)
    data_zlozenia = models.DateTimeField('złożono', auto_now_add=True)

    def __str__(self):
        return '{}___{}___nowe: {}___{}'.format(self.id, self.data_zlozenia.date(), self.czy_nowe,
                                                self.pracownik_skladajacy)


class ListaPozycji(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.PROTECT)
    pozycja = models.ForeignKey(Pozycja, on_delete=models.PROTECT)

    def __str__(self):
        return '{}___{}'.format(self.zamowienie, self.pozycja)


class ListaObslugujacych(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.PROTECT)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.PROTECT)
    data_przypisania = models.DateTimeField('przypisano', auto_now_add=True)

    def __str__(self):
        return '{}___{}___{}'.format(self.data_przypisania.date(), self.zamowienie, self.pracownik)
