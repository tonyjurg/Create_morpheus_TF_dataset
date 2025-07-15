# Creating Morpheus TF dataset - Testing

The following table contains links to some notebooks and scripts that were used as testing tools at various moments. They are roughly listed in the order they were used. The data shown does not necessarily represent the final state of the dataset.

Item | Description
---|---
[test_obtaining_pos_from_morpheus.ipynb](test_obtaining_pos_from_morpheus.ipynb) | Verify if the 'default' option for Morpheus chruncher does provide sufficient details on the Part of Speech.
[countWordForms.py](countWordForms.py) | Small script to examine further the data in the 'default' output of Morpheus
[Building the N1904-TF morph browser](Building_the_N1904-TF_morph_browser.ipynb) | colllects every unique morphological tag from the N1904-TF, adds an example word to it and provides the Morpheus analysis of that word
[Generate_test_set.ipynb](Generate_test_set.ipynb)| This notebook creates a test-set file (triplets: morph-tag, word, lemma) for testing the Morpheus to SP-tag mapping
[Unresolved words](unresolved_words/README.md) | Analysis of GNT words where Morpheus did not return any analyses block.


## Interactive data browsers

 - [all SP tags of the NT](grouped_morphology_dynamic.html): The interactive browser for unique morph tags, the example word and it Morpheus analysis blocks


## Data

 - [beta_morph_pairs.txt](beta_morph_pairs.txt): text file with tab separated betacode word with morph tag (test-set).
 - [test-set.txt](test-set.txt): text file with tab separeted morph tag, betacode word and lemma.
 - [gnt_morphology_results.txt](gnt_morphology_results.txt): Morpheus output (compact results) for all unique wordforms in the GNT.