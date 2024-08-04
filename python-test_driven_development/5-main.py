#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

print("")
text_indentation("Hello? Is anyone there. Yes: I am here.")
print("")
text_indentation("    Spaces at the start. Should be handled properly.")
print("")
text_indentation("End of sentence.    ")
print("")
text_indentation("\n\n\n New lines within the text.")
print("")
text_indentation("Mix of spaces and text. This should be clean:yes.")
print("")
try:
    text_indentation(123)
except Exception as e:
    print(e)
print("")
try:
    text_indentation(None)
except Exception as e:
    print(e)
