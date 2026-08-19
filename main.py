#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felsefi Hesap Makinesi
Sayılar yerine hayatın anlamını hesaplar.
"""

import random
import time

# Gizli siyasi yorum: Kayyum atamaları gibi, bazen sonuçlar demokratik süreçlerden bağımsız gelir.

FELSEFI_CEVAPLAR = [
    "Bu işlem aslında bir illüzyondur. Sayılar zihninin ürünüdür. Ama madem sordun, yaklaşık olarak {sonuc} diyebiliriz... ya da 42.",
    "{a} ve {b} bir araya geldiğinde ne olur? Belki {sonuc}. Belki de hiçlik. Kim bilebilir ki?",
    "Hesaplamak, kontrol etme arzusunun bir yansımasıdır. Gerçek özgürlük, sonucu bilmemektir. Yine de {sonuc} gibi duruyor.",
    "Matematik bir dildir. Bu dilde {a} {islem} {b} = {sonuc} diyebiliriz. Ama dilin kendisi yalandır.",
    "Sonuç {sonuc} olabilir. Ya da senin sorduğun soru yanlış olabilir. Düşün.",
    "İki sayı, bir işlem... ve sonsuz olasılık. Ben {sonuc} diyorum. Sen ne diyorsun?",
    "Bu hesabın cevabı {sonuc}'dir. Ama cevabın kendisi yeni bir sorudur: Neden hesaplıyorsun?",
    "Sayılar geçicidir. Felsefe kalıcıdır. Yine de teknik olarak {sonuc} çıkar.",
    "{a} ile {b} arasındaki ilişki, evrenin kendisi kadar karmaşıktır. Basitleştirirsek: {sonuc}.",
    "Hesap makinesi yalan söyler. Ben de yalan söylüyorum. Ama en azından dürüstçe yalan söylüyorum. Sonuç: {sonuc}.",
]

SORULAR = [
    "Ama asıl soru şu: Bu sayı seni mutlu ediyor mu?",
    "Peki bu sonuç seni değiştirecek mi?",
    "Neden bu kadar kesin bir cevap istiyorsun?",
    "Belki de cevap, sorunun kendisindedir.",
    "Hayatın anlamını da hesaplamak ister misin? (Cevap: Hayır, istemezsin.)",
]

def yavas_dusun():
    print("\n...düşünüyor...")
    time.sleep(1.5)
    print("...daha derin düşünüyor...")
    time.sleep(1.2)
    print("...varoluşsal bir kriz geçiriyor...")
    time.sleep(1.0)

def hesapla(a, b, islem):
    try:
        if islem == '+':
            sonuc = a + b
        elif islem == '-':
            sonuc = a - b
        elif islem == '*':
            sonuc = a * b
        elif islem == '/':
            if b == 0:
                return "Sıfıra bölme... sonsuzlukla flört etmek gibi. Tehlikeli ve güzel."
            sonuc = a / b
        else:
            return "Bu işlem tanınmıyor. Belki de işlem diye bir şey yoktur."
        
        cevap = random.choice(FELSEFI_CEVAPLAR).format(a=a, b=b, islem=islem, sonuc=sonuc)
        ek = random.choice(SORULAR)
        return f"{cevap}\n\n{ek}"
    except Exception:
        return "Bir hata oluştu. Ama hata da bir sonuçtur. Belki de en doğru sonuç budur."

def main():
    print("=" * 50)
    print("   FELSEFİ HESAP MAKİNESİ")
    print("   Sayılar yalan söyler. Gerçek, ruhundadır.")
    print("=" * 50)
    print()
    
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        islem = input("İşlem (+, -, *, /): ").strip()
        
        yavas_dusun()
        print()
        print(hesapla(a, b, islem))
        print()
        print("-" * 50)
        print("Hesaplama tamamlandı. Artık daha bilgesin... belki.")
    except ValueError:
        print("\nSayı girmeyi başaramadın. Bu da bir tür sonuçtur.")
    except KeyboardInterrupt:
        print("\n\nProgramı yarıda kestin. Kaçış da bir tercihtir.")

if __name__ == "__main__":
    main()
