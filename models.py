import pathlib
import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler

if __name__ == "__main__":
    path = pathlib.Path('/home/bot/testrasanlu/cities.jsonl')
    # note that we could have also used `English()` as a starting point
    # if our matching rules weren't using part of speech pip
    nlp = spacy.load("en_core_web_sm")

    # create a new rule based NER detector loading in settings from disk
    ruler = EntityRuler(nlp).from_disk(path)
    print("+++++++++++++++++++")
    print(f"Will now create model for {path}.")

    # add the detector to the model
    print("+++++++++++++++++++")
    nlp.add_pipe(ruler, before="ner")
    # nlp.add_pipe(ruler, after='parser')


    # define the name of the model as a package
    nlp.meta["name"] = "loc"
    # save the model to disk
    nlp.to_disk(nlp.meta["name"])
    print(f"spaCy model saved over at {nlp.meta['name']}.")
