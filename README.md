# 📁 LeRename - File Renamer & Price Calculator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.com)
[![Downloads](https://img.shields.io/badge/Downloads-Ready-brightgreen.svg)](https://github.com)

**English | [Türkçe](#türkçe)**

## 🚀 What is LeRename?

LeRename is a powerful Python tool that automatically renames image files based on PDF filenames and extracts price information from PDF names. Perfect for organizing invoices, receipts, and documents with their related images.

### Key Features:
- **Smart File Renaming**: Automatically renames images based on PDF reference names
- **Price Extraction**: Extracts price information from PDF filenames using regex
- **Batch Processing**: Process multiple folders continuously
- **Safe Operations**: Prevents file conflicts with intelligent naming
- **Date Sorting**: Sorts files by modification date for proper sequence
- **Price Summary**: Creates detailed price reports in text format

---

## 🎯 Use Cases

- **Invoice Management**: Organize invoices and their related photos
- **Receipt Processing**: Sort receipts with their images
- **Document Organization**: Structure PDF documents with related images
- **Accounting**: Extract and sum prices from document names
- **File Management**: Bulk rename files based on reference documents

---

## 📋 Supported File Formats

### PDF Files
- `.pdf`

### Image Files
- `.jpg`, `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.tiff`, `.tif`
- `.webp`

---

# Türkçe

## 📁 LeRename - Dosya Yeniden Adlandırma ve Fiyat Toplama Programı

Bu program, PDF ve resim dosyalarını otomatik olarak yeniden adlandırır ve PDF dosyalarındaki fiyat bilgilerini toplar. Özellikle fatura, makbuz gibi belgelerin organize edilmesi için tasarlanmıştır.

### Ana Özellikler:
- **Akıllı Dosya Adlandırma**: PDF dosyalarını referans alarak resim dosyalarını yeniden adlandırır
- **Fiyat Çıkarma**: PDF dosya isimlerinden regex ile fiyat bilgilerini çıkarır
- **Toplu İşlem**: Birden fazla klasörü sürekli işleyebilir
- **Güvenli İşlemler**: Akıllı adlandırma ile dosya çakışmalarını önler
- **Tarih Sıralaması**: Dosyaları değiştirme tarihine göre sıralar
- **Fiyat Özeti**: Detaylı fiyat raporları oluşturur

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

## 🛠️ Installation & Usage

### 📥 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/LeRename.git
   cd LeRename
   ```

2. **Run with Python:**
   ```bash
   python file_renamer.py
   ```

### 🐍 Python Installation

1. Ensure Python 3.7+ is installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python file_renamer.py
   ```

### 📦 EXE Version

#### Automatic Build (Recommended)

1. **Console Version** (shows error messages):
   ```bash
   build_exe_console.bat
   ```

2. **Window Version** (runs in background):
   ```bash
   build_exe.bat
   ```

#### Manual Build

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build EXE file:
   ```bash
   # Console version
   pyinstaller --onefile --name="LeRename" --distpath=. --workpath=build --specpath=. file_renamer.py
   
   # Window version (background)
   pyinstaller --onefile --windowed --name="LeRename" --distpath=. --workpath=build --specpath=. file_renamer.py
   ```

3. The compiled file will be at `LeRename.exe`.

---

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

## 📖 How It Works?

1. **Folder Selection**: Program asks for folder path when started
2. **File Scanning**: Finds PDF and image files in the folder
3. **Date Sorting**: Sorts files by modification date
4. **Renaming Process**: 
   - When PDF file is found, it's saved as reference name
   - Following image files are renamed as `PDF_name_1`, `PDF_name_2`, etc.
   - When new PDF is found, reference changes
5. **Price Extraction**: Extracts prices from PDF names using `(\d+(?:\.\d+)?)\s*TL` regex
6. **Report Generation**: Creates `fiyatlar.txt` file with all prices and total

---

## 📖 Nasıl Çalışır?

1. **Klasör Seçimi**: Program çalıştırıldığında klasör yolu istenir
2. **Dosya Tarama**: Klasördeki PDF ve resim dosyaları bulunur
3. **Tarih Sıralaması**: Dosyalar değiştirme tarihine göre sıralanır
4. **Yeniden Adlandırma**: 
   - PDF dosyası bulunduğunda referans isim olarak kaydedilir
   - Sonraki resim dosyaları `PDF_ismi_1`, `PDF_ismi_2` şeklinde adlandırılır
   - Yeni PDF bulunduğunda referans değişir
5. **Fiyat Çıkarma**: PDF isimlerinden `(\d+(?:\.\d+)?)\s*TL` regex'i ile fiyatlar çıkarılır
6. **Rapor Oluşturma**: `fiyatlar.txt` dosyasında tüm fiyatlar ve toplam yazılır

## 💡 Example Usage

### Before Processing:
```
folder/
├── invoice_150.50_TL.pdf
├── image1.jpg
├── image2.png
├── receipt_75.25_TL.pdf
├── photo1.jpg
└── photo2.png
```

### After Processing:
```
folder/
├── invoice_150.50_TL.pdf
├── invoice_150.50_TL_1.jpg
├── invoice_150.50_TL_2.png
├── receipt_75.25_TL.pdf
├── receipt_75.25_TL_1.jpg
├── receipt_75.25_TL_2.png
└── fiyatlar.txt
```

### fiyatlar.txt Content:
```
PDF Dosyaları ve Fiyatları
==============================

invoice_150.50_TL: 150.50 TL
receipt_75.25_TL: 75.25 TL

==============================
Toplam: 225.75 TL
```

---

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

fatura_150.50_TL: 150.50 TL
makbuz_75.25_TL: 75.25 TL

==============================
Toplam: 225.75 TL
```

## ⚠️ Important Notes

- **Safe Operation**: Adds numbers if files with same name exist
- **Date Sorting**: Sorts files by modification date
- **Price Format**: `number TL` (e.g., `150.50 TL`, `75 TL`)
- **Unicode Support**: Supports Turkish characters
- **Error Handling**: Safely stops on error conditions

---

## ⚠️ Önemli Notlar

- **Güvenli İşlem**: Aynı isimde dosya varsa numara ekler
- **Tarih Sıralaması**: Dosyaları değiştirme tarihine göre sıralar
- **Fiyat Formatı**: `sayı TL` (örn: `150.50 TL`, `75 TL`)
- **Unicode Desteği**: Türkçe karakter desteği vardır
- **Hata Yönetimi**: Hata durumlarında güvenli şekilde durur

## 🐛 Troubleshooting

### "Folder not found" Error
- Ensure folder path is correct
- Check if folder exists

### "Access denied" Error
- Ensure you have write permissions to folder
- Try running as administrator

### EXE Build Issues
- Ensure Python and pip are up to date
- Check if antivirus is blocking

---

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

## 🤝 Contributing

1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

This program was developed for educational and practical purposes.

## ⭐ Star This Project

If you like this project, please give it a star! ⭐

---

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

---

## 🔍 Keywords

`file-renamer` `pdf-organizer` `invoice-manager` `receipt-processor` `bulk-rename` `price-calculator` `document-organizer` `python-tool` `file-management` `automation` `turkish` `fatura` `makbuz` `dosya-adlandırma` `fiyat-hesaplama`

