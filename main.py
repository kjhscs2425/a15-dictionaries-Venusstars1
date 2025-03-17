letters = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary
character_values = {}
for letter in letters:
    if letter in character_values:
        character_values[letter] += 1
    else:
        character_values[letter] = 1
print(character_values)