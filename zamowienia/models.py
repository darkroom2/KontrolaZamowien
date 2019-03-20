from django.db import models


# Create your models here.


class Pracownik(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)

    def __unicode__(self):
        return '{} {}'.format(self.imie, self.nazwisko)


class Wyplata(models.Model):
    pracownik = models.ForeignKey(Pracownik, on_delete=models.PROTECT)
    kwota = models.DecimalField(default=0)

    def __unicode__(self):
        return '{}, {}zł'.format(self.pracownik, self.kwota)


class Sprzet(models.Model):
    nazwa = models.CharField(max_length=200)

    def __unicode__(self):
        return '{}'.format(self.nazwa)


class Cena(models.Model):
    sprzet = models.ForeignKey(Sprzet, on_delete=models.PROTECT)
    cena = models.DecimalField(default=0)
    data_wprowadzenia_ceny = models.DateTimeField('obowiązuje od')

    def __unicode__(self):
        return '{} {}'.format(self.imie, self.nazwisko)


class Pozycja(models.Model):
    sprzet = models.ForeignKey(Sprzet, on_delete=models.PROTECT)
    ilosc = models.IntegerField(default=0)
    poczatek_uzywania = models.DateTimeField('początek używania')
    koniec_uzywania = models.DateTimeField('koniec używania')


class Zamowienie(models.Model):
    pracownik_skladajacy = models.ForeignKey(Pracownik, on_delete=models.PROTECT)
    czy_nowe = models.BooleanField(default=True)
    data_zlozenia = models.DateTimeField(auto_now_add=True)


class ListaPozycji(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.PROTECT)
    pozycja = models.ForeignKey(Pozycja, on_delete=models.PROTECT)


class ListaObslugujacych(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.PROTECT)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.PROTECT)
    data_przypisania = models.DateTimeField(auto_now_add=True)
