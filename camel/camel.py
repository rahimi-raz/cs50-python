def change_to_lowercase(word):

  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lowercase_letters = word[0]

  for char in word:
      if word.index(char) > 0:
        if alphabet.index(char) > 25:
            lowercase_letters += "_" + alphabet[alphabet.index(char)-26]
        else:
            lowercase_letters += char

  return lowercase_letters

word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))