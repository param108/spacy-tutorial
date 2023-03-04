import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

lemmatizer = nlp.get_pipe("lemmatizer")
doc = nlp("South of Dracos point there is a small village. The village's name is tintorin")

print([token.lemma_ for token in doc])
matcher = Matcher(nlp.vocab)

pattern = [{"POS": "NOUN"}]

#matcher.add("ALL_NOUNS", [pattern])

matcher.add("VILLAGE_NAME", [[{"LEMMA": "village"}, {"LEMMA": "name"}]])
matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
