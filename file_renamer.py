#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeRename - File Renamer & Price Calculator

This program:
1. Gets folder path from user
2. Finds PDF and image files
3. Sorts by modification date
4. Renames images based on PDF reference names
5. Extracts and sums prices from PDF names
6. Writes results to fiyatlar.txt file

Keywords: file-renamer, pdf-organizer, invoice-manager, bulk-rename, price-calculator
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Dict


def get_folder_path() -> Path:
    """
    Kullanıcıdan klasör yolu alır ve Path objesi döndürür.
    
    Returns:
        Path: Geçerli klasör yolu
    """
    while True:
        folder_path = input("Lütfen işlem yapmak istediğiniz klasörün yolunu girin: ").strip()
        
        if not folder_path:
            print("Klasör yolu boş olamaz!")
            continue
            
        path = Path(folder_path)
        
        if not path.exists():
            print(f"'{folder_path}' klasörü bulunamadı!")
            continue
            
        if not path.is_dir():
            print(f"'{folder_path}' bir klasör değil!")
            continue
            
        return path


def get_supported_files(folder_path: Path) -> List[Path]:
    """
    Klasördeki PDF ve resim dosyalarını bulur.
    
    Args:
        folder_path (Path): Aranacak klasör yolu
        
    Returns:
        List[Path]: Bulunan dosyaların listesi
    """
    # Desteklenen dosya uzantıları
    pdf_extensions = {'.pdf'}
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp'}
    
    all_extensions = pdf_extensions | image_extensions
    supported_files = []
    
    try:
        for file_path in folder_path.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in all_extensions:
                supported_files.append(file_path)
    except PermissionError:
        print(f"'{folder_path}' klasörüne erişim izni yok!")
        return []
    
    return supported_files


def sort_files_by_modification_time(files: List[Path]) -> List[Path]:
    """
    Dosyaları değiştirme tarihine göre sıralar.
    
    Args:
        files (List[Path]): Sıralanacak dosyalar
        
    Returns:
        List[Path]: Tarihe göre sıralanmış dosyalar
    """
    def get_modification_time(file_path: Path) -> float:
        try:
            # st_mtime = değiştirme tarihi (modification time)
            return file_path.stat().st_mtime
        except (OSError, FileNotFoundError):
            # Dosya erişilemezse 0 döndür
            return 0.0
    
    # Eskiden yeniye sıralama (artan sıralama)
    sorted_files = sorted(files, key=get_modification_time)
    
    # Sıralama sonucunu göster
    print("\nDosyalar değiştirme tarihine göre sıralandı (eskiden yeniye):")
    for i, file_path in enumerate(sorted_files, 1):
        try:
            modification_time = file_path.stat().st_mtime
            from datetime import datetime
            readable_time = datetime.fromtimestamp(modification_time).strftime("%Y-%m-%d %H:%M:%S")
            print(f"  {i}. {file_path.name} ({readable_time})")
        except (OSError, FileNotFoundError):
            print(f"  {i}. {file_path.name} (tarih okunamadı)")
    
    return sorted_files


def extract_price_from_filename(filename: str) -> float:
    """
    Dosya adından fiyat bilgisini çıkarır.
    
    Args:
        filename (str): Dosya adı
        
    Returns:
        float: Bulunan fiyat (bulunamazsa 0.0)
    """
    # Regex kalıbı: (\d+(?:\.\d+)?)\s*TL
    pattern = r'(\d+(?:\.\d+)?)\s*TL'
    match = re.search(pattern, filename, re.IGNORECASE)
    
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return 0.0
    
    return 0.0


def get_safe_filename(folder_path: Path, base_name: str, extension: str) -> str:
    """
    Çakışma olmayan güvenli dosya adı oluşturur.
    
    Args:
        folder_path (Path): Klasör yolu
        base_name (str): Temel dosya adı
        extension (str): Dosya uzantısı
        
    Returns:
        str: Güvenli dosya adı
    """
    counter = 1
    original_name = f"{base_name}{extension}"
    safe_name = original_name
    
    while (folder_path / safe_name).exists():
        name_without_ext = base_name
        safe_name = f"{name_without_ext}_{counter}{extension}"
        counter += 1
    
    return safe_name


def rename_files_and_collect_prices(files: List[Path]) -> Dict[str, float]:
    """
    Dosyaları yeniden adlandırır ve PDF fiyatlarını toplar.
    
    Args:
        files (List[Path]): İşlenecek dosyalar
        
    Returns:
        Dict[str, float]: PDF dosya adları ve fiyatları
    """
    pdf_prices = {}
    current_pdf_name = None
    image_counter = 1
    
    print("\nDosya işleme başlıyor...")
    print(f"Toplam {len(files)} dosya işlenecek.")
    
    # Dosya türlerini say
    pdf_count = sum(1 for f in files if f.suffix.lower() == '.pdf')
    image_count = sum(1 for f in files if f.suffix.lower() in {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp'})
    print(f"PDF dosyası: {pdf_count}, Resim dosyası: {image_count}")
    
    for i, file_path in enumerate(files, 1):
        file_extension = file_path.suffix.lower()
        print(f"\n[{i}/{len(files)}] İşleniyor: {file_path.name}")
        
        if file_extension == '.pdf':
            # PDF dosyası bulundu - referans isim olarak kaydet
            current_pdf_name = file_path.stem
            price = extract_price_from_filename(file_path.name)
            pdf_prices[current_pdf_name] = price
            
            print(f"  ✓ PDF bulundu: {file_path.name}")
            print(f"  ✓ Referans isim: {current_pdf_name}")
            print(f"  ✓ Fiyat: {price} TL")
            image_counter = 1  # Resim sayacını sıfırla
            
        elif file_extension in {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp'}:
            if current_pdf_name:
                # Resim dosyası - PDF ismiyle yeniden adlandır
                new_name = f"{current_pdf_name}_{image_counter}{file_extension}"
                safe_name = get_safe_filename(file_path.parent, f"{current_pdf_name}_{image_counter}", file_extension)
                
                new_path = file_path.parent / safe_name
                
                try:
                    file_path.rename(new_path)
                    print(f"  ✓ Yeniden adlandırıldı: {file_path.name} -> {safe_name}")
                    image_counter += 1
                except OSError as e:
                    print(f"  ✗ Hata: {file_path.name} dosyası yeniden adlandırılamadı: {e}")
            else:
                print(f"  ⚠ Resim dosyası bulundu ama henüz PDF referansı yok: {file_path.name}")
        else:
            print(f"  - Desteklenmeyen dosya türü: {file_path.name}")
    
    print(f"\nİşlem tamamlandı. {len(pdf_prices)} PDF dosyası işlendi.")
    return pdf_prices


def format_price(price: float) -> str:
    """
    Fiyatı binlik ayırıcı ile formatlar.
    
    Args:
        price (float): Formatlanacak fiyat
        
    Returns:
        str: Formatlanmış fiyat (örn: 1.001.000)
    """
    # Fiyatı string'e çevir ve nokta ile ayır
    price_str = f"{price:,.2f}"
    # Türkçe format için nokta yerine nokta kullan (zaten doğru)
    return price_str


def create_price_summary_file(folder_path: Path, pdf_prices: Dict[str, float]) -> None:
    """
    Fiyat özetini fiyatlar.txt dosyasına yazar.
    
    Args:
        folder_path (Path): Klasör yolu
        pdf_prices (Dict[str, float]): PDF dosya adları ve fiyatları
    """
    if not pdf_prices:
        print("Hiç PDF dosyası bulunamadı, fiyat dosyası oluşturulmayacak.")
        return
    
    # Güvenli dosya adı oluştur
    price_file_name = get_safe_filename(folder_path, "fiyatlar", ".txt")
    price_file_path = folder_path / price_file_name
    
    try:
        with open(price_file_path, 'w', encoding='utf-8') as f:
            f.write("PDF Dosyaları ve Fiyatları\n")
            f.write("=" * 30 + "\n\n")
            
            total_price = 0.0
            
            for pdf_name, price in pdf_prices.items():
                formatted_price = format_price(price)
                f.write(f"{pdf_name}: {formatted_price} TL\n")
                total_price += price
            
            f.write("\n" + "=" * 30 + "\n")
            formatted_total = format_price(total_price)
            f.write(f"Toplam: {formatted_total} TL\n")
        
        print(f"\nFiyat özeti '{price_file_name}' dosyasına kaydedildi.")
        formatted_total = format_price(total_price)
        print(f"Toplam fiyat: {formatted_total} TL")
        
    except IOError as e:
        print(f"Hata: Fiyat dosyası oluşturulamadı: {e}")


def process_folder():
    """
    Tek bir klasörü işler.
    """
    try:
        # 1. Klasör yolu al
        folder_path = get_folder_path()
        print(f"İşlem yapılacak klasör: {folder_path}")
        
        # 2. Desteklenen dosyaları bul
        files = get_supported_files(folder_path)
        
        if not files:
            print("Klasörde PDF veya resim dosyası bulunamadı!")
            return False
        
        print(f"Toplam {len(files)} dosya bulundu.")
        
        # 3. Dosyaları değiştirme tarihine göre sırala
        sorted_files = sort_files_by_modification_time(files)
        
        # Sıralama sonrası kontrol
        pdf_files = [f for f in sorted_files if f.suffix.lower() == '.pdf']
        image_files = [f for f in sorted_files if f.suffix.lower() in {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp'}]
        
        print(f"\nSıralama sonrası:")
        print(f"  PDF dosyaları: {len(pdf_files)}")
        print(f"  Resim dosyaları: {len(image_files)}")
        
        if not pdf_files:
            print("\n⚠ UYARI: Hiç PDF dosyası bulunamadı!")
            print("   Resim dosyaları yeniden adlandırılmayacak.")
        elif not image_files:
            print("\n⚠ UYARI: Hiç resim dosyası bulunamadı!")
            print("   Sadece PDF fiyatları toplanacak.")
        
        # 4. Dosyaları yeniden adlandır ve fiyatları topla
        pdf_prices = rename_files_and_collect_prices(sorted_files)
        
        # 5. Fiyat özeti dosyası oluştur
        create_price_summary_file(folder_path, pdf_prices)
        
        print("\n" + "="*50)
        print("İşlem tamamlandı!")
        print("="*50)
        
        return True
        
    except KeyboardInterrupt:
        print("\n\nİşlem kullanıcı tarafından iptal edildi.")
        return False
    except Exception as e:
        print(f"\nBeklenmeyen bir hata oluştu: {e}")
        return False


def main():
    """
    Ana program fonksiyonu - sürekli çalışır.
    """
    print("📁 LeRename - Dosya Yeniden Adlandırma ve Fiyat Toplama Programı")
    print("=" * 70)
    print("Birden fazla klasör işleyebilirsiniz. Çıkmak için 'q' yazın.")
    print("=" * 70)
    
    while True:
        try:
            print("\n" + "─" * 50)
            print("Klasör seçimi için hazır...")
            print("─" * 50)
            
            # Klasör işle
            success = process_folder()
            
            if success:
                print("\n✅ İşlem başarıyla tamamlandı!")
            else:
                print("\n❌ İşlem tamamlanamadı.")
            
            # Kullanıcıya seçenek sun
            print("\n" + "─" * 50)
            choice = input("Başka bir klasör işlemek ister misiniz? (E/h/q): ").strip().lower()
            
            if choice in ['q', 'quit', 'exit', 'çık', 'çıkış']:
                print("\n👋 Program sonlandırılıyor...")
                break
            elif choice in ['h', 'hayır', 'no', 'n']:
                print("\n👋 Program sonlandırılıyor...")
                break
            elif choice in ['e', 'evet', 'yes', 'y', '']:
                print("\n🔄 Yeni işlem başlatılıyor...")
                continue
            else:
                print("❓ Geçersiz seçim. Program devam ediyor...")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 Program kullanıcı tarafından sonlandırıldı.")
            break
        except Exception as e:
            print(f"\n💥 Beklenmeyen bir hata oluştu: {e}")
            choice = input("Program devam etsin mi? (E/h): ").strip().lower()
            if choice in ['h', 'hayır', 'no', 'n']:
                break
    
    print("\n🎉 Teşekkürler! Program kapatılıyor...")
    input("Çıkmak için Enter tuşuna basın...")


if __name__ == "__main__":
    main()

