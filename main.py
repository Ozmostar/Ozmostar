import random

# Kelime listeleri
eng_words = ['Hi', 'Bye', 'Task', 'Program']
tr_words = ['Merhaba', 'Hoşça kalın', 'Görev', 'Program']
score = 0

# Selamlama mesajı
print("Hoş geldiniz! Kelime çeviri oyununa başlamak üzeresiniz.")
print("Yeni kelimeler eklemek için '0', çeviri yapmak için '1' yazın.")
print("Çeviri modunda, 5 kelime çevirmeye çalışacaksınız!")

# Mod seçimi
mode = input("Bir mod seçin (0 veya 1): \n")
while mode not in ['0', '1']:
    mode = input("Geçersiz sembol! Sadece 0 veya 1 yazın: \n")

if mode == "1":
    print("Çevirebildiğiniz kadar kelime çevirin! Toplam 5 kelime sorulacak!")
    for i in range(5):
        number = random.randint(0, len(eng_words) - 1)
        print("Tercümesi bu şekilde olmalı: " + eng_words[number])
        user_input = input("Cevabınızı yazın: ")
        if user_input == tr_words[number]:
            print("Harika!!!")
            score += 1
        else:
            print("Bir yanlışlık var... Doğru kelime - {}".format(tr_words[number]))

    print("Toplam puanınız: {} / 5".format(score))

elif mode == "0":
    print("Yeni kelime eklemek için İngilizce ve Türkçe kelimeleri girin.")
    for _ in range(5):  # Kullanıcıdan 5 yeni kelime girmesini istiyoruz
        eng_word = input("İngilizce kelime: ")
        tr_word = input("Türkçe karşılığı: ")
        eng_words.append(eng_word)
        tr_words.append(tr_word)
    print("Yeni kelimeler eklendi!")
