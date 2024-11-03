print('='*60)
print('\t\t\tTRANSLATE')
print('='*60)

import pyttsx3
from googletrans import Translator

def main():
    translator = Translator()
    engine = pyttsx3.init()

    engine.setProperty('rate', 130) 
    def set_voice(language):
        voices = engine.getProperty('voices')
        for voice in voices:
            if language == 'ja' and "Microsoft Haruka Desktop" in voice.name:
                engine.setProperty('voice', voice.id)
                return True
            elif language == 'en' and "English" in voice.name:
                engine.setProperty('voice', voice.id)
                return True
        return False

    while True:
        text = input("Masukkan teks yang ingin diterjemahkan\t: ")
        bahasa = input("bahasa yang tersedia :\n en, id, ja, ko, zh-cn, zh-tw, ar, es, fr, de, it, ru, pt, nl : ")

        try:
            hasil = translator.translate(text, dest=bahasa)

            print("\n===== Hasil Terjemahan =====")
            print(f"Dari ({hasil.src})\t: {text}")
            print(f"Ke ({hasil.dest})\t\t: {hasil.text}")
            print(f"Pengucapan\t: {hasil.pronunciation}\n")

            if not set_voice(bahasa):
                print(f"Suara untuk bahasa {bahasa} tidak ditemukan, menggunakan suara default.")
            
            engine.say(hasil.text)
            engine.runAndWait()

            lanjut = input("Ingin menerjemahkan teks lain? (ketik 'ya' untuk lanjut atau 'tidak' untuk keluar): ")
            if lanjut.lower() != 'ya':
                break


        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print("Pastikan kode bahasa yang dimasukkan benar.")

    print('\n\t=======BYEEE, SAMPAI KETEMU LAGI=======')

if __name__ == "__main__":
    main()