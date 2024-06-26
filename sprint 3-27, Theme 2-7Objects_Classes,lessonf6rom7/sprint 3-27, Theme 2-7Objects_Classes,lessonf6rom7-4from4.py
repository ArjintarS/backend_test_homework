class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    def process_text(self, text, shift, is_encrypt):
        processed_text = ''
        for char in text.lower():
            if char in self.alphabet:
                if is_encrypt:
                    # Шифрование
                    index = (self.alphabet.find(char) + shift) % len(self.alphabet)
                else:
                    # Дешифровка
                    index = (self.alphabet.find(char) - shift) % len(self.alphabet)
                    processed_text += self.alphabet[index]
            else:
                processed_text += char  # Сохраняем пробелы и знаки пунктуации
            return processed_text

# Создание экземпляра класса и использование его методов должны быть вне класса.
cipher_master = CipherMaster()
encrypted = cipher_master.process_text('Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь', 2, True)
print(encrypted)
decrypted = cipher_master.process_text('олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ', 3, False)
print(decrypted)