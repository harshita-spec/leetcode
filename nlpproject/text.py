import spacy

nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    
    tokens = [token.text for token in doc]
    
    lemmas = [
        token.lemma_ 
        for token in doc 
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    
    entities = [
        {"text": ent.text, "label": ent.label_}
        for ent in doc.ents
    ]
    
    return {
        "tokens": tokens,
        "clean_lemmas": lemmas,
        "entities": entities
    }

# Test
text="Google is hiring engineers in Bangalore"
result = process_text(text)
print(result)