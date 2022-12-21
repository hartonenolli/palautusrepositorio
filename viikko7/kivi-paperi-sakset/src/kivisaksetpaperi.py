from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KiviPaperiSakset:
    def __init__(self, kirjain):
        self.pelimuoto = kirjain
        self.tekoaly = Tekoaly()
        self.parannettu_tekoaly = TekoalyParannettu(10)

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        if self.pelimuoto == "a":
            toinen = KPSPelaajaVsPelaaja("a")._toisen_siirto()
            return toinen
        elif self.pelimuoto == "b":
            toinen = self.tekoaly.anna_siirto()
            print(f"Tietokone valitsi: {toinen}")
            return toinen
        if self.pelimuoto == "c":
            toinen = self.parannettu_tekoaly.anna_siirto()
            print(f"Tietokone valitsi: {toinen}")
            self.parannettu_tekoaly.aseta_siirto(ensimmaisen_siirto)
            return toinen
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    # toteutetaan metodi pelityypin mukaisesti
    def _toisen_siirto(self):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
