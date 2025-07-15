# Example use

The following snippet shows how a certain Greek word in Betacode can be analysed by Morpheus running on the docker container:

```text
root@morpheus:/mnt# echo "a)/eide" | MORPHLIB=/morpheus/stemlib /morpheus/bin/cruncher -S -d

:raw a)/eide

:workw a_)/eide
:lem a)ei/dw
:prvb 
:aug1 a)>a_)            doric aeolic
:stem a)eid             epic ionic              w_stem,reg_conj
:suff 
:end e   imperf ind act 3rd sg                  w_stem

```
