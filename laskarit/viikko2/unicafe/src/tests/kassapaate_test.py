import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_kassapaate_setup_oikein(self):
        kassa = self.kassapaate.kassassa_rahaa
        lounaat = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(kassa, 100000)
        self.assertEqual(lounaat, 0)
    
    def test_kateisosto_edulliset(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(240)
        kassa = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa, 100240)
        self.assertEqual(palautus, 0)

        palautus = self.kassapaate.syo_edullisesti_kateisella(250)
        kassa = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa, 100480)
        self.assertEqual(palautus, 10)

        palautus = self.kassapaate.syo_edullisesti_kateisella(230)
        kassa = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa, 100480)
        self.assertEqual(palautus, 230)
    
    def test_kateisosto_maukkaat(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(400)
        kassa = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa, 100400)
        self.assertEqual(palautus, 0)

        palautus = self.kassapaate.syo_maukkaasti_kateisella(410)
        kassa = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa, 100800)
        self.assertEqual(palautus, 10)

        palautus = self.kassapaate.syo_maukkaasti_kateisella(390)
        kassa = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa, 100800)
        self.assertEqual(palautus, 390)
    
    def test_korttimaksu(self):
        edullinen_tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(edullinen_tulos, True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        maukas_tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(maukas_tulos, True)
        self.assertEqual(self.maksukortti.saldo, 360)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        maukas_tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(maukas_tulos, False)
        self.assertEqual(self.maksukortti.saldo, 360)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        edullinen_tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        edullinen_tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(edullinen_tulos, False)
        self.assertEqual(self.maksukortti.saldo, 120)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_kortille_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)