def print_values_of(dictionary, keys):
    for key in keys:
        # added an if statement so only three of the catchphrases are printed
        if key == "lisa" or key == "bart" or key == "homer":
            # change k to key
            print(dictionary[key])

# altered to "d'oh" to removed unterminated string literal error
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}

# changed to only have two arguments, the second one being the keys of the dictionary
print_values_of(simpson_catch_phrases, simpson_catch_phrases.keys())

# commented out Expected console output
# '''
#     Expected console output:

#     BAAAAAART!
#     Eat My Shorts!
#     d'oh!

# '''

