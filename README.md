[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept) 

# Create morpheus TF dataset

## Introduction

This repository documents the creation of a new morphology-focused feature-set for the Nestle 1904 Greek New Testament Text-Fabric dataset [(N1904-TF)](https://github.com/CenterBLC/N1904). The main goal is to add all possible morphological analyses to each Greek word, based on its textual form. To achieve this, the project uses the well-known [Perseus Morpheus analyzer](https://github.com/perseids-tools/morpheus/).  The parses produced by Morpheus are ranked using a heuristic that compares them with existing Text-Fabric morphological features (such as [`case`](https://centerblc.github.io/N1904/features/case.html), [`number`](https://centerblc.github.io/N1904/features/number.html), and [`tense`](https://centerblc.github.io/N1904/features/tense.html)). The highest-ranked parse is the one that most closely matches the generally accepted interpretation of the word *in its specific context*. 

This repository provides insight into the processing pipeline, including the Python code (primarily embedded in Jupyter Notebooks with comments), intermediate data, and the resulting Text-Fabric feature files. The final feature files (*.tf) are included in the package available at the [tonyjurg/N1904addons](https://tonyjurg.github.io/N1904addons/) repository. This repository also explains how an executable instance of Morpheus was set up to run inside a [Docker virtualization environment](Running_Morpheus_on_docker/running_morpheus_on_docker.md).

The dataset builds on a previously developed Text-Fabric feature that added a betacode representation to each surface-level word. A new word-node feature, [`betacode`](https://tonyjurg.github.io/N1904addons/docs/features/betacode.html), was created to store the betacode equivalent of the Unicode text found in the [`text`](https://centerblc.github.io/N1904/features/text.html) feature. The tools used to generate the [tonyjurg/create_TF_feature_betacode] feature are available in the (https://github.com/tonyjurg/create_TF_feature_betacode) repository.

All procedures and tools are fully documented and openly accessible to ensure complete reproducibility. The workflow is implemented in Python using Jupyter Notebooks, with each stage of the process modularized into standalone notebooks or scripts. This openness aims to encourage reuse and highlight Text-Fabric's transparency and flexibility.

## Setting up environment

 - [Running_Morpheus_on_docker](Running_Morpheus_on_docker/README.md)
 - [Decoding the Morpheus output](Decoding_Morpheus_output/README.md)

## Production pipeline

 - [Create GNT word list in Betacode](Creating_GNT_betacode_wordlist/create_NT_wordlist_from_Betacode-feature.ipynb)
 - [run morpheus and convert to SP tags](api_the_morpheus/Morpheus_Morphological_Parser_UPDATE.ipynb)
 - [volatility_analyses](volitilty_analyses/Morpho-Syntactic-Volatility-update.ipynb)

## Validation

 - [Validation](Validation/README.md): Section on validation of the data and its conversion
 
## Related projects

 - [Sandborg-Petersen-decoder](https://github.com/tonyjurg/Sandborg-Petersen-decoder): decoding the morphological tags.
 - [Morphkit](https://tonyjurg.github.io/morphkit/): Python package for interfacing with Morpheus and performing output analysis.
 - [Creating the TF feature betcode](https://github.com/tonyjurg/create_TF_feature_betacode): the foundational feature used to bridge Morpheus and Text-Fabric world

