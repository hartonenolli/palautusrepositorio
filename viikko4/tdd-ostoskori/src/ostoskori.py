from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.maara = 0
        self.summa = 0
        self.tuotteet = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.tuotteet.append(lisattava)
        self.maara += 1
        self.summa += lisattava._hinta

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        index = 0
        for tavara in self.tuotteet:
            if tavara is poistettava:
                self.tuotteet.pop(index)
                self.maara -= 1
                break
            index += 1

    def tyhjenna(self):
        self.summa = 0
        self.maara = 0
        self.tuotteet = []
        # tyhjentää ostoskorin

    def ostokset(self):
        lista = []
        for tuote in self.tuotteet:
            if tuote not in lista:
                lista.append(tuote)
        return lista

        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
