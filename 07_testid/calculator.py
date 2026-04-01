import unittest
import math

class Kalkulaator:
  def __init__(self):
    self.sisu = "0"
    self.esimene = None
    self.tehe = None
    self.uus_arv = True

  def vajutus(self, nupp):
    if nupp.isdigit():
      if self.uus_arv:
        self.sisu = nupp
        self.uus_arv = False
      else:
        self.sisu += nupp

    elif nupp in ["+", "*", "/"]:
      self.esimene = int(self.sisu)
      self.tehe = nupp
      self.uus_arv = True

    elif nupp == "sin":
      väärtus = int(self.sisu)
      tulemus = math.sin(math.radians(väärtus))
      self.sisu = str(round(tulemus, 2))
      self.uus_arv = True

    elif nupp == "=":
      teine = int(self.sisu)

      if self.tehe == "+":
        tulemus = self.esimene + teine
      elif self.tehe == "*":
        tulemus = self.esimene * teine
      elif self.tehe == "/":
        tulemus = self.esimene // teine

      self.sisu = str(tulemus)
      self.uus_arv = True

  def ekraan(self):
    return self.sisu


class TestKalkulaator(unittest.TestCase):
  
  def setUp(self):
    self.k = Kalkulaator()

  def test_algus(self):
    self.assertEqual(self.k.ekraan(), "0")

  def test_vajutus_1(self):
    self.k.vajutus("1")
    self.assertEqual(self.k.ekraan(), "1")

  def test_vajutus_12(self):
    self.k.vajutus("1")
    self.k.vajutus("2")
    self.assertEqual(self.k.ekraan(), "12")

  def test_liitmine(self):
    self.k.vajutus("2")
    self.k.vajutus("+")
    self.k.vajutus("3")
    self.k.vajutus("=")
    self.assertEqual(self.k.ekraan(), "5")

  def test_korrutamine(self):
    self.k.vajutus("4")
    self.k.vajutus("*")
    self.k.vajutus("5")
    self.k.vajutus("=")
    self.assertEqual(self.k.ekraan(), "20")

  def test_jagamine(self):
    self.k.vajutus("8")
    self.k.vajutus("/")
    self.k.vajutus("2")
    self.k.vajutus("=")
    self.assertEqual(self.k.ekraan(), "4")

  def test_siinus(self):
    self.k.vajutus("90")
    self.k.vajutus("sin")
    self.assertEqual(self.k.ekraan(), "1.0")
    
  def test_siinus(self):
    self.k.vajutus("90")
    self.k.vajutus("sin")
    self.assertEqual(self.k.ekraan(), "1.0")


suite = unittest.TestLoader().loadTestsFromTestCase(TestKalkulaator)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Teste: {result.testsRun}')
