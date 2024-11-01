class BankaHesabi:

    def __init__(self,hesap_sahibi,bakiye=0):

        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye

    def para_yatir(self,miktar):
        self.bakiye += miktar
        return "{} miktar yatırıldı. Yeni bakiye {}.".format(miktar,self.bakiye)

    def para_cek(self,miktar):

        if (self.bakiye >= miktar):
            self.bakiye -= miktar
            return "{} miktar çekildi. Hesapta kalan para {}".format(miktar,self.bakiye)

        else:
            return "Yetersiz bakiye... lütfen başka miktar giriniz."

    def bakiye_sorgulama(self):
        return "Hesaptaki mevcut para {} ".format(self.bakiye)


banka_hesabi = BankaHesabi("Ali Savran")

print(banka_hesabi.para_yatir(1000))
print(banka_hesabi.para_cek(500))
print(banka_hesabi.bakiye_sorgulama())
