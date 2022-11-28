import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisäys_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 6)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisäys_hinta(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 6)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 9)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_2_korissa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisäys_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(str(ostos), "Maito hinta 3 euroa")

    def test_kahden_tuotteen_lisäys_korissa_2_tuotetta(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 6)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
    
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskori_sisältää_sama_nimi_ja_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()
        self.assertEqual(str(ostos), "[Maito hinta 3 euroa]")