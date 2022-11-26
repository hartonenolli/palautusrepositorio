import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilisiirto_metodia_kutsutaan_oikeilla(self):
        pankki_mock = Mock()
        varasto_mock = Mock()
        Viitegeneraattori_mock = Mock()

        Viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, Viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', '33333-44455', 5)

    def test_lisätään_kaksi_eri_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(t_id):
            if t_id == 1:
                return 5
            elif t_id == 2:
                return 3
        
        def varasto_hae_tuote(t_id):
            if t_id == 1:
                return Tuote(1, "banaani", 6)
            elif t_id == 2:
                return Tuote(2, "muumimuki", 9)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("olli", "0100")

        pankki_mock.tilisiirto.assert_called_with('olli', 42, '0100', '33333-44455', 15)

    def test_lisätään_2_samaa_tuotetta(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(t_id):
            if t_id == 1:
                return 5
        
        def varasto_hae_tuote(t_id):
            if t_id == 1:
                return Tuote(1, "kahvipaketti", 7)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("kolli", "2468")

        pankki_mock.tilisiirto.assert_called_with('kolli', 42, '2468', '33333-44455', 14)

    def test_lisätään_tuote_ja_loppunut_tuote(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(t_id):
            if t_id == 1:
                return 3
            elif t_id == 2:
                return 0
        
        def varasto_hae_tuote(t_id):
            if t_id == 1:
                return Tuote(1, "kissanhiekka", 6)
            elif t_id == 2:
                return Tuote(2, "kossu", 10)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("jari", "5555")

        pankki_mock.tilisiirto.assert_called_with('jari', 42, '5555', '33333-44455', 6)

    def test_aloita_asiointi_nollaantuu(self):
        pankki_mock = Mock()
        varasto_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.side_effect = [42, 43]

        def varasto_saldo(t_id):
            if t_id == 1:
                return 5
        
        def varasto_hae_tuote(t_id):
            if t_id == 1:
                return Tuote(1, "kossuvissy", 7)
        
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekko", "1975")

        pankki_mock.tilisiirto.assert_called_with('pekko', 42, '1975', '33333-44455', 7)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("simo", "8888")

        pankki_mock.tilisiirto.assert_called_with('simo', 43, '8888', '33333-44455', 7)

    def test_poista_korista(self):
        pankki_mock = Mock()
        varasto_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(t_id):
            if t_id == 1:
                return 3
            elif t_id == 2:
                return 4
        
        def varasto_hae_tuote(t_id):
            if t_id == 1:
                return Tuote(1, "rommitoti", 6)
            elif t_id == 2:
                return Tuote(2, "kissakalenteri", 10)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("jamppa", "6666")

        pankki_mock.tilisiirto.assert_called_with('jamppa', 42, '6666', '33333-44455', 10)