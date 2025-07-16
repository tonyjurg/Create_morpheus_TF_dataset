# Decoding the Morpheus output format

> Status — living document  │  Last updated: 22 June 2025
> 
> This document distils what I currently know about the full-detail output of the Morpheus Greek morphological analyser.  While extensive, it is not yet exhaustive, please report omissions or corrections so I can refine this page and the code denoding on it (like the [morphkit](https://tonyjurg.github.io/morphkit/) package). The main intention of this page is to provide details on the way data-extraction from the Morpheus internal database was implemented.

## Morpheus the morphological parser

A descriptive document about the function and usage of Morpheus is available online [in raw format at GitHub](https://github.com/PerseusDL/morpheus/blob/master/doc/morpheus.html) or as a nicely [HTML rendered webpage via GitHack](https://raw.githack.com/PerseusDL/morpheus/master/doc/morpheus.html). This document describes the inner workings at a high level and provides build instructions. The most formal source — which, as far as I know, is not publicly available in digital form — that describes Morpheus’s architecture is:

```
Generating and Parsing Classical Greek 
GREGORY CRANE
Literary and Linguistic Computing, Volume 6, Issue 4, 1991, Pages 243–245,
https://doi.org/10.1093/llc/6.4.243
Published: 01 January 1991
```

Morpheus’s operations fundamentally differ from a simple lookup method to determine morphological interpretations of a given word. Instead, it attempts to analyse the textual form by identifying components such as the stem and the ending, and then infers the morphological features. A [comment by Zachary Fletcher](https://github.com/perseids-tools/morpheus/issues/8#issuecomment-1692565071)  offers insight into how Morpheus works internally:

> ... Morpheus works differently from a relational database. When you ask it about καλῶν, it first tries to separate the stem from the ending and then checks both of them separately in its collection of stems and endings. The stems and endings are in the [/stemlib/Greek](https://github.com/PerseusDL/morpheus/tree/master/stemlib/Greek) directory I linked above. Morpheus also has some special case logic to deal with elision, crasis, dialectical differences (e.g. συν- vs. ξυν-), etc. If you'd like to figure out the logic, [/src/anal/checkstring.c](https://github.com/PerseusDL/morpheus/blob/master/src/anal/checkstring.c) is a good place to start.  (hyperlinks added by TJ)

Also included in the same discussion is an [image from Gregory Crane's article](https://github.com/perseids-tools/morpheus/issues/8#issuecomment-1691701680), which illustrates the high-level analytical flow of the Morpheus software.

Additional derived information and technical details can be found in open-access resources such as the [digitalclassicist's wiki page](https://wiki.digitalclassicist.org/Morpheus).

### The API interface to Morpheus

Several versions of Morpheus are available. Some provide an XML API to perform morphological lookups. One example is the build provided by the [alpheios-project](https://github.com/alpheios-project/morpheus). Although they share a codebase with the “standard” Morpheus, the Alpheios Project version includes more [recent updates on their stem files](https://github.com/alpheios-project/morpheus/tree/master/stemlib/Greek).

To maintain clarity about data provenance and ensure full compatibility with the Perseids tools, this project uses the plain, vanilla Morpheus implementation, as the dataset is named Morpheus. Fortunately, a [Docker container](https://hub.docker.com/r/perseidsproject/morpheus-api) was available that provided a plain version with an API.  

The process of installing the Morpheus Docker is described [here](../Running_Morpheus_on_docker/README.md). After starting the Docker container, an API becomes available at the Docker's IP address in my local LAN using port 1315. The impact of the options used is shown below (see Jupyter notebook [compare_response_two_API_calls.ipynb](compare_response_two_API_calls.ipynb) for details).

When called with `?opts=d?opts=n` the responce is:

```txt
:raw a)/nqrwpou

:workw a)nqrw/pou
:lem a)/nqrwpos
:prvb 				
:aug1 				
:stem a)nqrwp	 masc			os_ou
:suff 				
:end ou	 masc gen sg			os_ou

:raw a)/nqrwpou

:workw a_)nqrwpou=
:lem a)nqrwpo/omai
... etc ...
```

And when called with `?opts=n` the responce is:

```text
a)/nqrwpou
<NL>N a)nqrw/pou,a)/nqrwpos  masc gen sg			os_ou</NL><NL>V a_)nqrwpou=,a)nqrwpo/omai  imperf ind mp 2nd sg	doric aeolic	contr	ow_pr,ow_denom</NL><NL>V a)nqrwpou=,a)nqrwpo/omai  pres imperat mp 2nd sg		contr	ow_pr,ow_denom</NL><NL>V a)nqrwpou=,a)nqrwpo/omai  imperf ind mp 2nd sg	homeric ionic	contr unaugmented	ow_pr,ow_denom</NL><NL>N a)nqrwpou=,a)nqrwpw/  fem nom/voc/acc dual		contr	w_oos</NL>
```

In this project, the core component of Morpheus — the "cruncher" — was invoked using the `-d` flag. This option dumps internal database information, providing the maximum level of detail available. The decoding schema described on this page corresponds specifically to the output format generated with these flags (i.e. `?opts=d?opts=n`). This is independ from the method used to obtain the results, either the script I initially used (which can be found [here](../Running_Morpheus_on_docker/bash_script.md)) or the use of an API.


### Overview workflow

When Morpheus successfully analyses a token, it prints *one or multiple* records, each representing a distinct morphological parse.  Every record is a block of colon-prefixed lines (e.g. `:lem`, `:stem`, `:end`).  The analyser’s [PrntAnalyses function](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L12) writes these lines in a fixed order. There is a [maximum of 25 blocks](analysis_limits.ipynd) that can be returned for any word.

For instance, the following four analysis blocks are returned when executing  [`morphkit.get_word_blocks('*ai)gupti/wn', base_url`)](https://github.com/tonyjurg/morphkit/blob/main/morphkit/get_word_blocks.py):

```text
:raw *ai)gupti/wn
:workw *ai)gupti/wn
:lem *ai)gu/ptios
:prvb
:aug1
:stem *ai)gupti                os_h_on
:suff
:end wn fem gen pl                     os_h_on

:raw *ai)gupti/wn
:workw *ai)gupti/wn
:lem *ai)gu/ptios
:prvb
:aug1
:stem *ai)gupti                os_h_on
:suff
:end wn masc/neut gen pl                os_h_on

:raw *ai)gupti/wn
:workw *ai)gupti/wn
:lem *ai)guptio/w
:prvb
:aug1
:stem *ai)gupti                ow_pr,ow_denom
:suff
:end wn imperf ind act 3rd pl doric aeolic contr   ow_pr

:raw *ai)gupti/wn
:workw *ai)gupti/wn
:lem *ai)guptio/w
:prvb
:aug1
:stem *ai)gupti                ow_pr,ow_denom
:suff
:end wn imperf ind act 1st sg doric aeolic contr   ow_pr
```

When using the function [`morphkit.analyse_word_with_morpheus('*ai)gupti/wn', base_url)`](https://github.com/tonyjurg/morphkit/blob/main/morphkit/analyse_word_with_morpheus.py), it will also gather these blocks, but also analyse all it's elements and store them in a dictionary with labeled morphological details according to the schema detailed on this page.

# Decoding the Morpheus blocks

## Record schema overview

The following tables can be used to break down each line into it constituent information elements. 

Tag/field | Always data present? | Typical contents | Notes/description
---|---|---|---
[:raw](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L479) | yes | Token as supplied (Beta Code) | The raw form of the word, as it was inputted. This may include ellipsis (indicated with '). [Crane provides as example ἐπέμπετ᾽](https://github.com/gregorycrane/Homerica/blob/1ad202eec627414e7153f5512d6cb43abc22e308/Tb%2BMorpheus#L77), which could stand for ἐπέμπετε ("you [pl] were sending") or ἐπέμπετο ("s/he was being sent")
[:workw](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L480) | yes | The working token after basic normalisation | In most cases, the raw and work word are identical.
[:lem](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L481) | yes | The lemma (Beta Code) | Determined dictionary form or root of the Greek word.
[:prvb](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L483) | | Preverb(s); dialect; morph‑flags| Details about attached preposition (e.g., ἐν- or meta-).
[:aug1](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L488) | | Augment / reduplication; dialect; morph‑flags| Augment, indicating a prefix marking past/perfect tense (typically absent in non-past forms).
[:stem](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L493) | | Stem; inherent morphology; dialect; morph‑flags; stem‑type code(s) | The base or stem type of the word. It also shows the paradigm the analysis was based upon (e.g. `os_h_on`, `aor2`).
[:suff](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L498) | | Suffix segment; | Suffixes, if any. Mostly empty in GNT corpora? (see [suffix_gstr_of](https://github.com/perseids-tools/morpheus/blob/ab6898ffed335fc6169fa02c9940657a9b5a78e0/src/includes/gkstring.h#L131))
[:end](https://github.com/PerseusDL/morpheus/blob/master/src/anal/prntanal.c#L503) | |  Ending; full morph features; dialect; morph‑flags; paradigm code(s) | Analysis ending details (=Core morphological data) including grammatical information like case, number, gender, mood, tense, and dialect.

## Field-by-field reference

While the first three lines (`:raw`, `:workw` and `:lem`) always contain only one argument, the lines that follow may have a varying amount of items. Items on each line are separted by tabs. (`\t`)

### `:raw`

The untouched input string.  If an apostrophe appears at the end (classical elision) Morpheus _does not_ expand it; instead, a separate record will appear under `:workw` for each plausible expansion.

### `:workw`

The token after Morpheus applies minimal normalisation. When Morpheus is run with the `-S` switch, it performs minimal normalisation on each input token. This includes (in certain situations?) decapitalisation, which means that the leading asterisk in '*tou=to' (which marks an uppercase first letter) is removed. In that case we recieve output like: ':raw *tou=to' and ':workw tou=to'. Accents are also regularised so that the token matches a lexicon entry. For instance, the raw input `kai\` is changed to `kai/`.

All analysis lines that follow — within the same output block — are based on this normalised `:workw` form.

### `:lem`

Lemma in Beta-Code format.  My exporter adds a Unicode copy to the dictionairy under the key `lemma`. [note: it should also take care of multiple senses!]

In certain cases, there are two lemma entries, indicated by a number concatenated to the Betacode lemma. In such cases, the entries differ in grammatical role and meaning and should be treated as two separate lexemes that merely share the lemma string (homonymy).

For example, the word `h)\` (betacode for the single‐letter word ἢ) has two lemma entries, `h)/1` and `h)/2`. Note the back slash  `\` and forward slash `/` are accent marks belonging to the lemma; only the final number functions numeric suffix, just as in the standard way of tagging homonyms (think ἢ¹ vs. ἢ²). Entry 1 has the part-of-speech tag `conj` (co-ordinating conjunction “or”), where entry 2 has the part-of-speech tag `exclam` (exclamatory particle “ah!”, “verily”, etc.).

For certain lemmata Morpheus adds a betacode suffix `-pl` (-πλ). Examining its occurenses in the GNT all instances where Morpheus adds the suffix `-pl` can be linked mostly to persons, in a few instances  to places (e.g., `*(ierosolu/mois`; Ἱεροσολύμοις).

### `:prvb` (Preverb Line)

The following table shows the 5 columns structure of the line (columns are separted with tabs; `\t`).

Label| Prepostionpart | Unknown | Dialect | MorphFlags | Unknown 
---|---|---|---|---|---
`:prvb`|E.g.: `a)po/`,`a)na/` | - | E.g.: `epic`, `doric` | E.g.: `prevb_aug`, `doubled_cons` | - 

Prepostionpart: This can be either empty, one or two prepositions. Eg. διακατηλέγχετο ('diakathle/gxeto'; Acts 18:28) has 2: dia/,kata/.

Dialect: contains dialect details arranged according C.D. Buck, The Greek Dialects (Chicago, 1955),p9. The values are defined in [dialect.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/dialect.h).

MorphFlags: contains details about morphological peculiarities. There are many possible values which are defined in file [morphflags.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/morphflags.h).


### `:aug1` (Augment/Reduplication Line)

Same 5‑column structure as `:prvb`.  The Augmentpart (col 1) shows the actual augment characters, e.g. `e)>h)`.

Label| Augmentpart | Unknown | Dialect | MorphFlags | Unknown
---|---|---|---|---|---
`:aug1`| E.g.: `e)>h)`| - |E.g.: `attic`, `ionic` | E.g.: `syll_augment` | -

Dialect: contains dialect details arranged according C.D. Buck, The Greek Dialects (Chicago, 1955),p9. The values are defined in [dialect.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/dialect.h).

MorphFlags: contains details about morphological peculiarities. There are many possible values which are defined in file [morphflags.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/morphflags.h) and/or [morphkeys.h](https://github.com/PerseusDL/morpheus/blob/master/src/morphlib/morphkeys.h).

### `:stem`

Label| Stempart | Morphology | Dialect | MorphFlags | Stemtype
---|---|---|---|---|---
`:stem`| E.g.: `eu)xarist` | E.g.: `fem`, `masc sg`, `masc voc sg`| E.g.: `doric aeolic`| E.g.: `unaugmented` | E.g.: `aor2`, `os_h_on`, `numi`

Morphology: the usual morphological elements (number, gender, case, etc).

Dialect: contains dialect details arranged according C.D. Buck, The Greek Dialects (Chicago, 1955),p9. The values are defined in [dialect.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/dialect.h).

MorphFlags: contains details about morphological peculiarities. There are many possible values which are defined in file [morphflags.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/morphflags.h) and/or [morphkeys.h](https://github.com/PerseusDL/morpheus/blob/master/src/morphlib/morphkeys.h).

Stemtype: list the paradigm code controlling endings & accent. There are many possible values which seems are defined in various tables in the code.

### `:suff`

label| Suffixpart | Unknown | Unknown | Unknown | Unknown
---|---|---|---|---|---
`:suff`| always empty? | | | |

No occurences in our GNT data. Is this due to a 'dummy' [suffixtype.h](https://github.com/PerseusDL/morpheus/blob/master/src/includes/suffixtype.h)?

### `:end` (Ending & Morphology)

This line is of particular interest as it contains most the morphological data I would like to capture.

label| prepostion |Morphology | Dialect | MorphFlags | PoS and decl
---|---|---|---|---|---
`:end`| E.g.: `io/ntwn` | E.g.: `aor ind act 3rd sg` |E.g.: `doric laconia` | E.g. `nu_movable` | E.g. `ew_pr`, `reg_fut`


# Atribution and footnotes

* [Morpheus documentation (via GitHack)](https://raw.githack.com/PerseusDL/morpheus/master/doc/morpheus.html)
* Gregory Crane, _Morpheus––Homerica_ (source & commentary) [github.com/gregorycrane/Homerica](https://github.com/gregorycrane/Homerica)
* Morpheus source code [github.com/PerseusDL/morpheus](https://github.com/PerseusDL/morpheus)
* [Digital Classicist Wiki](https://wiki.digitalclassicist.org/Morpheus)
* Python package [Morphkit](https://tonyjurg.github.io/morphkit/) providing a clean and easy to use method to analyse the Morpheus analytic blocks.
* The notebook [OBSOLETE-Morpheus_Morphological_Extractor.ipynb](OBSOLETE-Morpheus_Morphological_Extractor.ipynb) is an earlier implementation.
* [Analyses limits](analysis_limits.ipynd): There is a capping of 25 Morpheus analyses blocks for a single word.

# Version

<div style="float: left;">
  <table>
    <tr>
      <td><strong>Author</strong></td>
      <td>Tony Jurg</td>
    </tr>
    <tr>
      <td><strong>Version</strong></td>
      <td>2.3</td>
    </tr>
    <tr>
      <td><strong>Date</strong></td>
      <td>22 June 2025</td>
    </tr>
  </table>
</div>
