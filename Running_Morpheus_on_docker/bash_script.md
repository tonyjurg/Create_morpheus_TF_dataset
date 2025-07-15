# Bash script to perform morphological lookup on Morpheus

# 1 - Introduction 

The following bash script looks up the morphology of all Greek words in the Greek New Testament (GNT). 

# 2 - The script

The following bash script accepts a text file containing all GNT words in Betacode as input. The script runs within a docker container, where it reads the words from the inputfile and pipes them using `echo` to a`cruncher`; the Morpheus binary tool that performs the actual morphological analysis.

```bash
#!/bin/bash

# Variables
INPUT_FILE="gnt_words.txt"   # Input file with GNT words
OUTPUT_FILE="gnt_morphology_results.txt"  # Output file for morphology results
CRUNCHER_COMMAND="MORPHLIB=stemlib bin/cruncher"  # Path to the cruncher command

# Check if the input file exists
if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: Input file '$INPUT_FILE' not found."
    exit 1
fi

# Clear or create the output file
> "$OUTPUT_FILE"

echo "Processing words in '$INPUT_FILE'..."

# Process each word
while IFS= read -r word; do
    # Run cruncher and capture the result
    result=$(echo "$word" | $CRUNCHER_COMMAND -d)

    # Append the result to the output file
    if [[ -n "$result" ]]; then
        echo "Word: $word" >> "$OUTPUT_FILE"
        echo "$result" >> "$OUTPUT_FILE"
        echo "-----------------------------" >> "$OUTPUT_FILE"
    else
        echo "Word: $word" >> "$OUTPUT_FILE"
        echo "Error: No response for '$word'" >> "$OUTPUT_FILE"
        echo "-----------------------------" >> "$OUTPUT_FILE"
    fi
done < "$INPUT_FILE"

echo "Morphology lookup complete. Results saved to '$OUTPUT_FILE'."
```

Running the script (after opening terminal/containder console in Portainer). In my case the script is called `process_words.sh`:

```bash
root@morpheus:/# /mnt/process_words.sh
```

# 3 - Some notes

 - Variables: The script contains the following variables: `INPUT_FILE` which points to the file with the Greek words, `OUTPUT_FILE` which provides the filename where to saves the morphological analysis, and CRUNCHER_COMMAND` which defines the details for the `cruncher` binary to be used in the `MORPHLIB` environment, its variable and desired options.

 - Processing Each Word: For each word in the input file, the script pipes the word into `cruncher` using `echo` and appends the result to the output file, along with the original inputted word.

 - Error Handling: If no result is returned, an error message (e.g., 'Error: No response for ....') is recorded in the output file.

# 4 -  Usage 

- First check that `cruncher` works for instance by running `echo 'a)/nqrwpos' | MORPHLIB=stemlib bin/cruncher -S` successfully from the terminal.

- Prepare the input file, say `gnt_words.txt` with one Greek word in betacode per line. Move the file over to the container.

- Move the script over to the docker environment (in my case I named it `process_words.sh`). 

- Important! Make the script executable inside the docker environment: 

   ```bash
   chmod +x process_words.sh
   ```
   
- Now run the script in the directory where the script is stored (in my case `/mnt`; the shared location with the Synology host. If you prefer to start from other location add path details):

   ```bash
   ./process_words.sh
   ```

## 4.1 - Windows / Linux interactions

When encountering wierd errors like `bash: $'\r': command not found` when running your script, this may be (if you created your script on a Windows machine) due to the script using Windows line endings (\r\n), but Bash expects Unix/Linux line endings (\n). \r is a carriage return (from Windows-style line endings), and Bash doesn't know what to do with it.

To fix it there are verious options (like using [dos2unix](https://dos2unix.sourceforge.io/)) or let your texteditor like [Notepad++](https://notepad-plus-plus.org/) save is as a unix fileformat (Edit -> EOL Conversion -> Unix (LF)).

You can also fix it on the fly using streaming editor ([sed](https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/)):

```bash
sed -i 's/\r$//' process_words.sh
```

Note that a similar (but not identical) interaction is pressent when porting files following the mac line feed scheme to a Linux/Unix environment.

# 5 - Customizing options

There are a few options to modify the behaviour of the `CRUNCHER_COMMAND`. The two following tables are found in [PerseusDL morpheus documentation](https://github.com/PerseusDL/morpheus/blob/master/doc/morpheus.html#L66C1-L104C9) which are here presented with minor changes.

<p>The following are the commonly used command-line switches.

<table border=1>
<tr><th>Switch</th> <th>Use</th></tr>
<tr><td>-L</td> <td>sets language to <b>L</b>atin</td></tr>
<tr><td>-I</td> <td>sets language to <b>I</b>talian</td></tr>
<tr><td>-S</td> <td>turn off <b>S</b>trict case.  For Greek, allows words with an initial capital to be recognized,
so that for example the personification <tt>*tu/xhs</tt> at Soph. OT 1080 is recognized as the genitive singular of <tt>tu/xh</tt>.
For languages in the Roman alphabet, allows words with initial capital or in all capitals to be recognized.</td></tr>
<tr><td>-n</td> <td>ignore acce<b>n</b>ts.  Allows words with no accents or breathings, or with incorrect ones, to be 
recognized.</td></tr>
</table>

<p>The following other switches are supported. </p>
    
<table border=1>
<tr><th>Switch</th> <th>Use</th></tr>
<tr><td>-d</td> <td><b>d</b>atabase format.  This switch changes the output from "Perseus format" to "database format."  Output appears in a series of tagged fields.</td></tr>
<tr><td>-e</td> <td><b>e</b>nding index.  Instead of showing the analysis in readable form, this switch gives the indices of the tense, mood, case, number, and so on (as appropriate) in the internal tables.</td></tr>
<tr><td>-k</td> <td><b>k</b>eep beta-code.  When "Perseus format" is enabled (the default), this switch does nothing.  When "Perseus format" is off, Greek output is normally converted to the old Greek Keys encoding.  This switch disables that conversion so that Greek output stays in beta-code.  Note that the handling of this switch was not updated when Latin was implemented, so when "Perseus format" is disabled, Latin and Italian will also be converted to this Greek font encoding.  Hence if you are disabling Perseus format in those languages, you should also set the -k switch.</td></tr>
<tr><td>-l</td> <td>show <b>l</b>emma.  When this switch is set, instead of printing the entire analysis, cruncher will only show the lemma or headword from which the 
given form is made.</td></tr>
<tr><td>-P</td> <td> turn off <b>P</b>erseus format.  Output will be in the form
<pre>$feminam&  is^M   &from$  femina^M      $fe_minam^M        [&stem $fe_min-& ]^M         & a_ae fem acc sg^M</pre>
Note the returns, without line feeds, between the fields.</td></tr>
<tr><td>-V</td> <td>analyze <b>V</b>erbs only.  When this switch is set, words that are not verbs will not be recognized, and words that could be analyzed as either verb forms or noun forms will be treated as certainly verbs</td></tr>
</table>

<p>The following switches, which appear in the main routine, do nothing. (note TJ: if you want to trace yourself, start at [stdiomorph.c](https://github.com/PerseusDL/morpheus/blob/master/src/anal/stdiomorph.c#L49))
<table border=1>
<tr><th>Switch</th> <th>Use</th></tr>
<tr><td>-a</td> <td>sets the SHOW_ANAL flag, which is never checked </td></tr>
<tr><td>-b</td> <td>sets the BUFFER_ANALS flag, which is no longer checked </td></tr>
<tr><td>-c</td> <td>sets the CHECK_PREVERB flag, which is no longer checked </td></tr>
<tr><td>-i</td> <td>sets the SHOW_FULL_INFO flag, which is never checked </td></tr>
<tr><td>-m</td> <td>sets the SHOW_MISSES flag, which is never checked </td></tr>
<tr><td>-p</td> <td>sets the PARSE_FORMAT flag, which is unconditionally turned on later anyway</td></tr>
<tr><td>-s</td> <td>sets the DBASESHORT flag, which is checked only in a routine that is never called</td></tr>
<tr><td>-x</td> <td>sets the LEXICON_OUTPUT flag, which is checked only in a routine that is never called</td></tr>
</table>


# 5.1 - Example output

This section shows the impact of the flags on the generated output.

```bash
root@morpheus:/morpheus# echo 'a)/eide' | MORPHLIB=stemlib bin/cruncher -S -d

:raw a)/eide

:workw a_)/eide
:lem a)ei/dw
:prvb 
:aug1 a)>a_)            doric aeolic
:stem a)eid             epic ionic              w_stem,reg_conj
:suff 
:end e   imperf ind act 3rd sg                  w_stem

:raw a)/eide

:workw a)/eide
:lem a)ei/dw
:prvb 
:aug1 
:stem a)eid             epic ionic              w_stem,reg_conj
:suff 
:end e   pres imperat act 2nd sg                        w_stem

:raw a)/eide

:workw a)/eide
:lem a)ei/dw
:prvb 
:aug1 
:stem a)eid             epic ionic      unaugmented     w_stem,reg_conj
:suff 
:end e   imperf ind act 3rd sg                  w_stem
```
Some printouts using other flags:
 
```bash

root@morpheus:/bin# echo 'a)/nqrwpos' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher
a)/nqrwpos
<NL>N a)/nqrwpos  masc nom sg                   os_ou</NL>


root@morpheus:/bin# echo 'a)/nqrwpos' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -l
form:a)/nqrwpos
a)/nqrwpos


root@morpheus:/bin# echo 'a)/nqrwpos' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -S
a)/nqrwpos
<NL>N a)/nqrwpos  masc nom sg                   os_ou</NL>


root@morpheus:/bin# echo 'a)/nqrwpos' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -d

:raw a)/nqrwpos

:workw a)/nqrwpos
:lem a)/nqrwpos
:prvb 
:aug1 
:stem a)nqrwp    masc                   os_ou
:suff 
:end os  masc nom sg                    os_ou


root@morpheus:/bin# echo 'a)/nqrwpos' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -S -d

:raw a)/nqrwpos

:workw a)/nqrwpos
:lem a)/nqrwpos
:prvb 
:aug1 
:stem a)nqrwp    masc                   os_ou
:suff 
:end os  masc nom sg                    os_ou


root@morpheus:/morpheus# echo 'a)/eide' | MORPHLIB=stemlib bin/cruncher -S
a)/eide
<NL>V a_)/eide,a)ei/dw  imperf ind act 3rd sg   epic doric ionic aeolic         w_stem,reg_conj</NL><NL>V a)ei/dw  pres imperat act 2nd sg    epic ionic              w_stem,reg_conj</NL><NL>V a)ei/dw  imperf ind act 3rd sg      epic doric ionic aeolic unaugmented     w_stem,reg_conj</NL>

root@morpheus:/mnt# echo 'a)/eide' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher 
a)/eide
<NL>V a_)/eide,a)ei/dw  imperf ind act 3rd sg   epic doric ionic aeolic         w_stem,reg_conj</NL><NL>V a)ei/dw  pres imperat act 2nd sg      epic ionic              w_stem,reg_conj</NL><NL>V a)ei/dw  imperf ind act 3rd sg        epic doric ionic aeolic unaugmented     w_stem,reg_conj</NL>
```

And a special case here there are two prepositions which is shown when invoking with switch `-d` but not by default:

```bash
root@morpheus:/mnt# echo 'diakathle/gxeto' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -d

:raw diakathle/gxeto

:workw diakathle/gxeto
:lem diakatele/gxomai
:prvb dia/,kata/
:aug1 e)>h)
:stem e)legx     ind                    w_stem,reg_conj
:suff 
:end eto         imperf ind mp 3rd sg                   w_stem

root@morpheus:/mnt# echo 'diakathle/gxeto' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher
diakathle/gxeto
<NL>V diakatele/gxomai  imperf ind mp 3rd sg                    w_stem,reg_conj</NL>

root@morpheus:/mnt# echo 'diakathle/gxeto' | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -e
diakathle/gxeto
<NL>V diakatele/gxomai  25870</NL>
```
# 5 - Attribution

* Morpheus C source code [github.com/PerseusDL/morpheus](https://github.com/PerseusDL/morpheus)
  
# 6 - Version details

<div style="float: left;">
  <table>
    <tr>
      <td><strong>Author</strong></td>
      <td>Tony Jurg</td>
    </tr>
    <tr>
      <td><strong>Version</strong></td>
      <td>1.4</td>
    </tr>
    <tr>
      <td><strong>Date</strong></td>
      <td>23 April 2025</td>
    </tr>
  </table>
</div>
