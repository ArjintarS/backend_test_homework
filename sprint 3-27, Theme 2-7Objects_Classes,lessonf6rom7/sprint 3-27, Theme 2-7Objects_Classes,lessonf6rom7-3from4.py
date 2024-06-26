class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def process_text(self, text, shift, is_encrypt):
        processed_text = ''
        for char in text.lower():
            if char in self.alphabet:
                # Определяем индекс символа в алфавите
                index = self.alphabet.find(char)
                # Выполняем смещение
                if is_encrypt:
                    shifted_index = (index + shift) % len(self.alphabet)
                else:
                    shifted_index = (index - shift) % len(self.alphabet)
                # Добавляем зашифрованный/расшифрованный символ в результат
                processed_text += self.alphabet[shifted_index]
            else:
                # Сохраняем пробелы и знаки пунктуации
                processed_text += char
        return processed_text
    
# Создание экземпляра класса и использование его методов должны быть вне класса.
cipher_master = CipherMaster()
encrypted = cipher_master.process_text('Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь', 2, True)
print(encrypted)
decrypted = cipher_master.process_text('олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ', 3, False)
print(decrypted)
