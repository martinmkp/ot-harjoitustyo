import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)
    
    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)
    
    def test_rahan_ottaminen_kortilta(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_nosto_ei_yli_saldon(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(self.maksukortti.saldo, 10)
    
    def test_nosto_palauttaa_true_jos_rahat_riittavat(self):
        totta = self.maksukortti.ota_rahaa(8)
        self.assertEqual(totta, True)
        ei_totta = self.maksukortti.ota_rahaa(4)
        self.assertFalse(ei_totta, False)

    def test_saldo_pyoristetty_oikein(self):
        pyoristetty_saldo = self.maksukortti.__str__()
        self.assertEqual(pyoristetty_saldo, "saldo: 0.1")