alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Fungsi encrypt yang mengambil teks dan meng-shift kan kata kata huruf sesuai input

# Enkripsi


def encrypt(text_to_encrypt=text, shift_amount=shift):
	cipher_text = ""
	for letter in text_to_encrypt:
		position = alphabet.index(letter)
		# .index, fungsi mencari suatu nilai dalam sebuah list
		new_position = (position + shift_amount) % 26
		cipher_text = cipher_text + alphabet[new_position]

	# kenapa modulus % 26, karena jika ada huruf z, dan di shift, nanti akan index out of range. hal ini disiasati dengan
	# di modulus % kan, agar             sisa dari modulus, (e.g 50 % 26 = 24) menjadi index huruf baru (24)
	# tidak out of range melebihi list. wraparound alphabet

	return cipher_text

# Dekripsi


def decode(text_to_decode=text, shift_amount=shift):
	decoded_text = ""
	for letter in text_to_decode:
		position = alphabet.index(letter)
		old_position = position - shift_amount
		decoded_text = decoded_text + alphabet[old_position]

	return decoded_text


if direction == "encode":
	print(encrypt(text, shift))

elif direction == "decode":
	print(decode(text, shift))