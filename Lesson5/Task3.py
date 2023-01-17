

def encode(s: str) -> str:

	encoding = "" # stores output string

	i = 0
	while i < len(s):
		count = 1

		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1

		encoding += str(count) + s[i]
		i = i + 1

	return encoding

def decode(s: str) -> str:

    decoding = ''

    i = 0
    while i < len(s):
        if s[i].isdigit():
            decoding += int(s[i]) * s[i + 1]
        i += 1

    return(decoding)

def main():
    with open ("File2.txt", "r") as file:
        init_str = file.read()
    if init_str[0].isdigit():
        file = open("File2.txt", 'a')
        file.write(f'  => {decode(init_str)}')
    else:
        file = open("File2.txt", 'a')
        file.write(f'  => {encode(init_str)}')


main()



