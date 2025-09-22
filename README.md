# 📁 LeRename - Dosya Yeniden Adlandırma ve Fiyat Toplama Programı

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.com)

Bu program, PDF ve resim dosyalarını otomatik olarak yeniden adlandırır ve PDF dosyalarındaki fiyat bilgilerini toplar. Özellikle fatura, makbuz gibi belgelerin organize edilmesi için tasarlanmıştır.

## 🚀 Özellikler

- **Akıllı Dosya Adlandırma**: PDF dosyalarını referans alarak resim dosyalarını yeniden adlandırır
- **Fiyat Çıkarma**: PDF dosya isimlerinden regex ile fiyat bilgilerini çıkarır
- **Güvenli İşlem**: Dosya çakışmalarını önler
- **Tarih Sıralaması**: Dosyaları oluşturulma tarihine göre sıralar
- **Özet Rapor**: Tüm fiyatları `fiyatlar.txt` dosyasında toplar

## 📋 Desteklenen Dosya Formatları

### PDF Dosyaları
- `.pdf`

### Resim Dosyaları
- `.jpg`, `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.tiff`, `.tif`
- `.webp`

## 🛠️ Kurulum ve Kullanım

### 📥 Hızlı Başlangıç

1. **Repository'yi klonlayın:**
   ```bash
   git clone https://github.com/kullaniciadi/LeRename.git
   cd LeRename
   ```

2. **Python ile çalıştırın:**
   ```bash
   python file_renamer.py
   ```

### 🐍 Python ile Çalıştırma

1. Python 3.7+ yüklü olduğundan emin olun
2. Gerekli bağımlılıkları kurun:
   ```bash
   pip install -r requirements.txt
   ```
3. Programı çalıştırın:
   ```bash
   python file_renamer.py
   ```

### 📦 EXE Dosyası Olarak Çalıştırma

#### Otomatik Derleme (Önerilen)

1. **Konsol Versiyonu** (hata mesajları görünür):
   ```bash
   build_exe_console.bat
   ```

2. **Pencere Versiyonu** (arka planda çalışır):
   ```bash
   build_exe.bat
   ```

#### Manuel Derleme

1. PyInstaller'ı kurun:
   ```bash
   pip install pyinstaller
   ```

2. EXE dosyasını derleyin:
   ```bash
   # Konsol versiyonu
   pyinstaller --onefile --name="LeRename" --distpath=. --workpath=build --specpath=. file_renamer.py
   
   # Pencere versiyonu (arka planda)
   pyinstaller --onefile --windowed --name="LeRename" --distpath=. --workpath=build --specpath=. file_renamer.py
   ```

3. Derlenen dosya `LeRename.exe` konumunda bulunur.

## 📖 Nasıl Çalışır?

1. **Klasör Seçimi**: Program çalıştırıldığında klasör yolu istenir
2. **Dosya Tarama**: Klasördeki PDF ve resim dosyaları bulunur
3. **Tarih Sıralaması**: Dosyalar oluşturulma tarihine göre sıralanır
4. **Yeniden Adlandırma**: 
   - PDF dosyası bulunduğunda referans isim olarak kaydedilir
   - Sonraki resim dosyaları `PDF_ismi_1`, `PDF_ismi_2` şeklinde adlandırılır
   - Yeni PDF bulunduğunda referans değişir
5. **Fiyat Çıkarma**: PDF isimlerinden `(\d+(?:\.\d+)?)\s*TL` regex'i ile fiyatlar çıkarılır
6. **Rapor Oluşturma**: `fiyatlar.txt` dosyasında tüm fiyatlar ve toplam yazılır

## 💡 Örnek Kullanım

### Başlangıç Durumu:
```
klasör/
├── fatura_150.50_TL.pdf
├── resim1.jpg
├── resim2.png
├── makbuz_75.25_TL.pdf
├── foto1.jpg
└── foto2.png
```

### Program Çalıştıktan Sonra:
```
klasör/
├── fatura_150.50_TL.pdf
├── fatura_150.50_TL_1.jpg
├── fatura_150.50_TL_2.png
├── makbuz_75.25_TL.pdf
├── makbuz_75.25_TL_1.jpg
├── makbuz_75.25_TL_2.png
└── fiyatlar.txt
```

### fiyatlar.txt İçeriği:
```
PDF Dosyaları ve Fiyatları
==============================

fatura_150.50_TL: 150.5 TL
makbuz_75.25_TL: 75.25 TL

==============================
Toplam: 225.75 TL
```

## ⚠️ Önemli Notlar

- Program güvenli çalışır: Aynı isimde dosya varsa numara ekler
- Sadece oluşturulma tarihine göre sıralama yapar
- Fiyat formatı: `sayı TL` (örn: `150.50 TL`, `75 TL`)
- Türkçe karakter desteği vardır
- Hata durumlarında güvenli şekilde durur

## 🐛 Sorun Giderme

### "Klasör bulunamadı" Hatası
- Klasör yolunun doğru olduğundan emin olun
- Klasörün var olduğunu kontrol edin

### "Erişim izni yok" Hatası
- Klasöre yazma izniniz olduğundan emin olun
- Programı yönetici olarak çalıştırmayı deneyin

### EXE Derleme Sorunları
- Python ve pip'in güncel olduğundan emin olun
- Antivirus programının engellemediğini kontrol edin

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

Bu program eğitim ve pratik amaçlı geliştirilmiştir.

## ⭐ Yıldız Verin

Bu projeyi beğendiyseniz, lütfen bir yıldız verin! ⭐

