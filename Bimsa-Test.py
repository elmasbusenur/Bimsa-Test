from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""kullanılacak tarayıcı"""
driver = webdriver.Chrome()
"""test edilecek adres"""
driver.get("https://hrwebssl.bimsa.com.tr/ikportal//")
"""ekran tam boyutu"""
driver.maximize_window()

delay = 10;

"""kullanıcıKodu elentini bul ve kullanıcı adını gir"""
kullaniciKoduElement = driver.find_element_by_name("userid")
kullaniciKoduElement.clear()
kullaniciKoduElement.send_keys("yusuf.bahadir@bimsa.com")

"""sifre elementini bul ve sifreyi gir"""
sifreElement = driver.find_element_by_name("password")
sifreElement.clear()
sifreElement.send_keys("Bb101010")

"""giriş butonunu bul ve tıkla"""
girisButonElement = driver.find_element_by_xpath(".//*[@id='Header']/tbody/tr/td[2]/table/tbody/tr[2]/td[8]/a")
girisButonElement.click()
"""
assert "INSAN KAYNAKLARI PORTAL UYGULAMASI" in driver.title"""
"""
çıkış yap butonunu bul
cikisButonElement = driver.find_element_by_id("button.logoff")
cikisButonElement.click()

yenidenGirisButonElement = driver.find_element_by_xpath("html/body/table/tbody/tr/td/table/tbody/tr/td/a")
yenidenGirisButonElement.click()

kullaniciKoduElement = driver.find_element_by_name("userid")
kullaniciKoduElement.clear()
kullaniciKoduElement.send_keys("yusuf.bahadir@bimsa.com")

sifreElement = driver.find_element_by_name("password")
sifreElement.clear()
sifreElement.send_keys("Bb101010")"""

"""try:
    waitForLoadingBar = WebDriverWait(driver, delay).until(EC.invisibility_of_element_located((By.CLASS_NAME,"loading-container")))
except TimeoutException:
    print("Loading took too much time!")"""
"""try:
    menuKapatXPATH = ".//*[@id='menu']/b/a/font"
    waitFormenuKapat = WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, menuKapatXPATH)))
    menuKapatLink = driver.find_element_by_xpath(menuKapatXPATH)
    menuKapatLink.click()
except TimeoutException:
    print("Loading took too much time!")"""


try:
    personelBilgileriID = "id1"
    personelBilgileriLink = driver.find_element_by_id(personelBilgileriID)
    personelBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    sicilBilgileriID = "sd2"
    sicilBilgileriLink = driver.find_element_by_id(sicilBilgileriID)
    sicilBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    ogrYabancıDilXPATH = ".//*[@id='sd3']"
    ogrYabancıDilLink = driver.find_element_by_xpath(ogrYabancıDilXPATH)
    ogrYabancıDilLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    adresBilgileriID = "sd4"
    adresBilgileriLink = driver.find_element_by_id(adresBilgileriID)
    adresBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    acilDurumBilgileriID = "sd5"
    acilDurumBilgileriLink = driver.find_element_by_id(acilDurumBilgileriID)
    acilDurumBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    aileBilgileriID = "sd6"
    aileBilgileriLink = driver.find_element_by_id(aileBilgileriID)
    aileBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    disiplinBilgileriID = "sd7"
    disiplinBilgileriLink = driver.find_element_by_id(disiplinBilgileriID)
    disiplinBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    odulBilgileriID = "sd8"
    odulBilgileriLink = driver.find_element_by_id(odulBilgileriID)
    odulBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    asgariGecimIndBilgileriID = "sd9"
    asgariGecimIndBilgileriLink = driver.find_element_by_id(asgariGecimIndBilgileriID)
    asgariGecimIndBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    isTecrübeID = "sd10"
    isTecrübeLink = driver.find_element_by_id(isTecrübeID)
    isTecrübeLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    taksitliKesintilerID = "sd11"
    taksitliKesintilerLink = driver.find_element_by_id(taksitliKesintilerID)
    taksitliKesintilerLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    zimmetBilgileriID = "sd12"
    zimmetBilgileriLink = driver.find_element_by_id(zimmetBilgileriID)
    zimmetBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    saglikTedaviBilgileriID = "sd13"
    saglikTedaviLink = driver.find_element_by_id(saglikTedaviBilgileriID)
    saglikTedaviLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    sertifikaBilgileriID = "sd14"
    sertifikaBilgileriLink = driver.find_element_by_id(sertifikaBilgileriID)
    sertifikaBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    personelYorumID = "sd15"
    personelYorumLink = driver.find_element_by_id(personelYorumID)
    personelYorumLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    cvPersonelBilgiFormID = "sd16"
    cvPersonelBilgiFormLink = driver.find_element_by_id(cvPersonelBilgiFormID)
    cvPersonelBilgiFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    yanHaklarID = "sd17"
    yanHaklarLink = driver.find_element_by_id(yanHaklarID)
    yanHaklarLink.click()
except TimeoutException:
    print("Loading took too much time!")

"""2"""
try:
    izinIslemXPATH = ".//*[@id='div_id_18']/a[2]"
    izinIslemLink = driver.find_element_by_xpath(izinIslemXPATH)
    izinIslemLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    izinBilgileriID = "sd19"
    izinBilgileriLink = driver.find_element_by_id(yanHaklarID)
    izinBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    orgIzinTakvimiID = "sd20"
    orgIzinTakvimiLink = driver.find_element_by_id(orgIzinTakvimiID)
    orgIzinTakvimiLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    gunlukIzinBilgileriID = "sd21"
    gunlukIzinBilgileriLink = driver.find_element_by_id(gunlukIzinBilgileriID)
    gunlukIzinBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    gunlukOrgIzinTakvimID = "sd22"
    gunlukOrgIzinTakvimLink = driver.find_element_by_id(gunlukOrgIzinTakvimID)
    gunlukOrgIzinTakvimLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    izinFormuOlusturID = "sd23"
    izinFormuOlusturLink = driver.find_element_by_id(izinFormuOlusturID)
    izinFormuOlusturLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    izinFormuID = "sd24"
    izinFormuLink = driver.find_element_by_id(izinFormuID)
    izinFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    persIzinTalepFormID = "sd25"
    persIzinTalepLink = driver.find_element_by_id(persIzinTalepID)
    persIzinTalepLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    onayimdaBekleyenIzinFormID = "sd26"
    onayimdaBekleyenIzinFormLink = driver.find_element_by_id(onayimdaBekleyenIzinFormID)
    onayimdaBekleyenIzinFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    onayimdaBekleyenPersIzinFormID = "sd27"
    onayimdaBekleyenPersIzinFormLink = driver.find_element_by_id(onayimdaBekleyenPersIzinFormID)
    onayimdaBekleyenPersIzinFormLink.click()
except TimeoutException:
    print("Loading took too much time!")
"""3"""
try:
    egitimBilgileriXPATH = ".//*[@id='div_id_28']/a[2]"
    egitimBilgileriLink = driver.find_element_by_xpath(egitimBilgileriXPATH)
    egitimBilgileriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    personelEgitimBilgilerID = "sd29"
    personelEgitimBilgilerLink = driver.find_element_by_id(personelEgitimBilgilerID)
    personelEgitimBilgilerLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    egitimDegerlendirmeID = "sd30"
    egitimDegerlendirmeLink = driver.find_element_by_id(egitimDegerlendirmeID)
    egitimDegerlendirmeLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    egitimKatalogID = "sd31"
    egitimKatalogLink = driver.find_element_by_id(egitimKatalogID)
    egitimKatalogLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    duzenlenecekEgitimTakvimID = "sd32"
    duzenlenecekEgitimTakvimLink = driver.find_element_by_id(duzenlenecekEgitimTakvimID)
    duzenlenecekEgitimTakvimLink.click()
except TimeoutException:
    print("Loading took too much time!")

"""4"""

try:
    aylikBordroIslemXPATH = ".//*[@id='div_id_33']/a[2]"
    aylikBordroIslemLink = driver.find_element_by_xpath(aylikBordroIslemXPATH)
    aylikBordroIslemLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    bordroZarfiID = "sd34"
    bordroZarfiLink = driver.find_element_by_id(bordroZarfiID)
    bordroZarfiLink.click()
except TimeoutException:
    print("Loading took too much time!")

"""5"""
try:
    iseAlimXPATH = ".//*[@id='div_id_18']/a[2]"
    iseAlimLink = driver.find_element_by_xpath(iseAlimXPATH)
    iseAlimLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    personelTalepFormuID = "sd36"
    personelTalepFormuLink = driver.find_element_by_id(personelTalepFormuID)
    personelTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    personelDegerlendirmeID = "sd20"
    personelDegerlendirmeLink = driver.find_element_by_id(personelDegerlendirmeID)
    personelDegerlendirmeLink.click()
except TimeoutException:
    print("Loading took too much time!")
"""6"""
try:
    formlarXPATH = ".//*[@id='div_id_38']/a[2]"
    formlarLink = driver.find_element_by_xpath(formlarXPATH)
    formlarLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    fazlaMesaiFormuID = "sd39"
    fazlaMesaiFormuLink = driver.find_element_by_id(fazlaMesaiFormuID)
    fazlaMesaiFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    onFazlaMesaiTalepFormID = "sd40"
    onFazlaMesaiTalepFormLink = driver.find_element_by_id(onFazlaMesaiTalepFormID)
    onFazlaMesaiTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    gerceklesenFazlaMesaiTalepID = "sd41"
    gerceklesenFazlaMesaiTalepLink = driver.find_element_by_id(gerceklesenFazlaMesaiTalepID)
    gerceklesenFazlaMesaiTalepLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    aylikFazlaMesaiTalepFormID = "sd42"
    aylikFazlaMesaiTalepFormLink = driver.find_element_by_id(aylikFazlaMesaiTalepFormID)
    aylikFazlaMesaiTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    avansIstekFormID = "sd43"
    avansIstekFormLink = driver.find_element_by_id(avansIstekFormID)
    avansIstekFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    taksitliKesintiTalepFormuID = "sd44"
    taksitliKesintiTalepFormuLink = driver.find_element_by_id(taksitliKesintiTalepFormuID)
    taksitliKesintiTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    gorevSeyehatFormuID = "sd45"
    gorevSeyehatFormuLink = driver.find_element_by_id(gorevSeyehatFormuID)
    gorevSeyehatFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    gelisimIhtiyacFormuID = "sd46"
    gelisimIhtiyacFormuLink = driver.find_element_by_id(gelisimIhtiyacFormuID)
    gelisimIhtiyacFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    harcamaMasrafFormuID = "sd47"
    harcamaMasrafFormuLink = driver.find_element_by_id(harcamaMasrafFormuID)
    harcamaMasrafFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    egitimTalepFormuID = "sd48"
    egitimTalepFormuLink = driver.find_element_by_id(egitimTalepFormuID)
    egitimTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    perfDegFormuID = "sd49"
    perfDegFormuLink = driver.find_element_by_id(perfDegFormuID)
    perfDegFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    perfDegFormuGoruntuID = "sd50"
    perfDegFormuGoruntuLink = driver.find_element_by_id(perfDegFormuGoruntuID)
    perfDegFormuGoruntuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    yoneticiperfDegFormuID = "sd51"
    yoneticiperfDegFormuLink = driver.find_element_by_id(yoneticiperfDegFormuID)
    yoneticiperfDegFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    vizeBilgTalepFormuID = "sd52"
    vizeBilgTalepFormuLink = driver.find_element_by_id(vizeBilgTalepFormuID)
    vizeBilgTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    duyuruFormID = "sd53"
    duyuruFormLink = driver.find_element_by_id(duyuruFormID)
    duyuruFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    oneriFormID = "sd54"
    oneriFormLink = driver.find_element_by_id(oneriFormID)
    oneriFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    sikayetFormuID = "sd55"
    sikayetFormuLink = driver.find_element_by_id(sikayetFormuID)
    sikayetFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    digerTalepFormlariID = "sd56"
    digerTalepFormlariLink = driver.find_element_by_id(digerTalepFormlariID)
    digerTalepFormlariLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    katalogTalepFormID = "sd57"
    katalogTalepFormLink = driver.find_element_by_id(katalogTalepFormID)
    katalogTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    satinAlmaTalepFormID = "sd58"
    satinAlmaTalepFormLink = driver.find_element_by_id(satinAlmaTalepFormID)
    satinAlmaTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    disiplinFormuID = "sd59"
    disiplinFormuLink = driver.find_element_by_id(disiplinFormuID)
    disiplinFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    oprFormID = "sd60"
    oprFormLink = driver.find_element_by_id(oprFormID)
    oprFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    polivalansGuncellemeID = "sd61"
    polivalansGuncellemeLink = driver.find_element_by_id(polivalansGuncellemeID)
    polivalansGuncellemeLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    GuncellemeID = "sd62"
    GuncellemeLink = driver.find_element_by_id(GuncellemeID)
    GuncellemeLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    primFormGuncellemeID = "sd63"
    primFormGuncellemeLink = driver.find_element_by_id(primFormGuncellemeID)
    primFormGuncellemeLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    hedefGerceklesenDegeriID = "sd64"
    hedefGerceklesenDegeriLink = driver.find_element_by_id(hedefGerceklesenDegeriID)
    hedefGerceklesenDegeriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    dereceGotuntulemeID = "sd65"
    dereceGotuntulemeLink = driver.find_element_by_id(dereceGotuntulemeID)
    dereceGotuntulemeLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    aylikFazlaMesaiTalepID = "sd66"
    aylikFazlaMesaiTalepLink = driver.find_element_by_id(aylikFazlaMesaiTalepID)
    aylikFazlaMesaiTalepLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    oprFormTopluOnayID = "sd67"
    oprFormTopluOnayLink = driver.find_element_by_id(oprFormTopluOnayID)
    oprFormTopluOnayLink.click()
except TimeoutException:
    print("Loading took too much time!")
"""7"""
try:
    isAkisiXPATH = ".//*[@id='div_id_68']/a[2]"
    isAkisiLink = driver.find_element_by_xpath(isAkisiXPATH)
    isAkisiLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    isAkisiFormuID = "sd69"
    isAkisiFormuLink = driver.find_element_by_id(isAkisiFormuID)
    isAkisiFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    delegrasyonIslemleriID = "sd70"
    delegrasyonIslemleriLink = driver.find_element_by_id(delegrasyonIslemleriID)
    delegrasyonIslemleriLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obAvansIstekFormID = "sd71"
    obAvansIstekFormLink = driver.find_element_by_id(obAvansIstekFormID)
    obAvansIstekFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obAvansIstekFormYoneticiID = "sd72"
    obAvansIstekFormYoneticiLink = driver.find_element_by_id(obAvansIstekFormYoneticiID)
    obAvansIstekFormYoneticiLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obDenemeSuresiOnayFormID = "sd73"
    obDenemeSuresiOnayFormLink = driver.find_element_by_id(obDenemeSuresiOnayFormID)
    obDenemeSuresiOnayFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obDigerTalepFormuID = "sd74"
    obDigerTalepFormuLink = driver.find_element_by_id(obDigerTalepFormuID)
    obDigerTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obdisiplinFormuID = "sd75"
    obdisiplinFormuLink = driver.find_element_by_id(obdisiplinFormuID)
    obdisiplinFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obDuyuruFormuID = "sd76"
    obDuyuruFormLink = driver.find_element_by_id(obDuyuruFormuID)
    obDuyuruFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obgelisimIhtiyacFormuID = "sd78"
    obgelisimIhtiyacFormuLink = driver.find_element_by_id(obgelisimIhtiyacFormuID)
    obgelisimIhtiyacFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obegitimTalepFormuID = "sd77"
    egitimTalepFormuLink = driver.find_element_by_id(egitimTalepFormuID)
    egitimTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obEgitimTalepTopFormuID = "sd79"
    obEgitimTalepTopFormuLink = driver.find_element_by_id(obEgitimTalepTopFormuID)
    obEgitimTalepTopFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obAylikFazlaMesaiTFormID = "sd80"
    obAylikFazlaMesaiTFormLink = driver.find_element_by_id(obAylikFazlaMesaiTFormID)
    obAylikFazlaMesaiTFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obFazlaMesaiFormuID = "sd81"
    obFazlaMesaiFormuLink = driver.find_element_by_id(obFazlaMesaiFormuID)
    obFazlaMesaiFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obOnFazlaMesaiTalepFormuID = "s852"
    obOnFazlaMesaiTalepFormuLink = driver.find_element_by_id(obOnFazlaMesaiTalepFormuID)
    obOnFazlaMesaiTalepFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obGerceklesenFazlaMesaiTFormID = "sd83"
    obGerceklesenFazlaMesaiTFormLink = driver.find_element_by_id(obGerceklesenFazlaMesaiTFormID)
    obGerceklesenFazlaMesaiTFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    onFazlaMesaiTalepFormYoneticiID = "sd84"
    onFazlaMesaiTalepFormYoneticiLink = driver.find_element_by_id(onFazlaMesaiTalepFormYoneticiID)
    onFazlaMesaiTalepFormYoneticiLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obOnFazlaMesaiTalepPersonelFormuID = "sd85"
    obOnFazlaMesaiTalepPersonelFormuLink = driver.find_element_by_id(obOnFazlaMesaiTalepPersonelFormuID)
    obOnFazlaMesaiTalepPersonelFormuLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obGerceklesenFazlaMesaiFormlariPersID = "sd86"
    obGerceklesenFazlaMesaiFormlariPersLink = driver.find_element_by_id(obGerceklesenFazlaMesaiFormlariPersID)
    obGerceklesenFazlaMesaiFormlariPersLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obHaftaTatiliDegisimFormID = "sd87"
    obHaftaTatiliDegisimFormLink = driver.find_element_by_id(obHaftaTatiliDegisimFormID)
    obHaftaTatiliDegisimFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obHarcamaFormID = "sd88"
    obHarcamaFormLink = driver.find_element_by_id(obHarcamaFormID)
    obHarcamaFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obGorevFormID = "sd89"
    obGorevFormLink = driver.find_element_by_id(obGorevFormID)
    obGorevFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obKatalogdanTalepFormID = "sd60"
    obKatalogdanTalepFormLink = driver.find_element_by_id(obKatalogdanTalepFormID)
    obKatalogdanTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obPersDurumDegisiklikTFormID = "sd91"
    obPersDurumDegisiklikTFormLink = driver.find_element_by_id(obPersDurumDegisiklikTFormID)
    obPersDurumDegisiklikTFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obPersTalepFormID = "sd92"
    obPersTalepFormLink = driver.find_element_by_id(obPersTalepFormID)
    obPersTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obOneriTalepFormID = "sd93"
    obOneriTalepFormLink = driver.find_element_by_id(obOneriTalepFormID)
    obOneriTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obSatinAlmaTFormID = "sd94"
    obSatinAlmaTFormLink = driver.find_element_by_id(obSatinAlmaTFormID)
    obSatinAlmaTFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obTaksitliKesintiTFormID = "sd95"
    obTaksitliKesintiTFormLink = driver.find_element_by_id(obTaksitliKesintiTFormID)
    obTaksitliKesintiTFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obVizeBilgTalepFormID = "sd96"
    obVizeBilgTalepFormLink = driver.find_element_by_id(obVizeBilgTalepFormID)
    obVizeBilgTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")

try:
    obKadroTalepFormID = "sd97"
    obKadroTalepFormLink = driver.find_element_by_id(obKadroTalepFormID)
    obKadroTalepFormLink.click()
except TimeoutException:
    print("Loading took too much time!")
