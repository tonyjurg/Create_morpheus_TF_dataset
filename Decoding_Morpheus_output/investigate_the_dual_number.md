# Investigate the use of 'dual' for number

Morpheus is built on a finite-state morphology that will return all possible analyses for which the ending-patterns match a given string, even if some of those analyses are rare or archaic.  

## Real example

In Ancient Greek many dual endings happen to overlap with singular or plural endings in certain declensions and paradigms. For example ποιήσει (lemma=ποιέω - to do, make -  future, 3p, sg) ends in -σει, matching some dual paradigms. This can be seen from the first output block of Morpheus analysis of the betacode  poih/sei (=ποιήσει) which is labeled as 'attic' dialect:


```
:raw poih/sei

:workw poih/sei
:lem poi/hsis
:prvb 				
:aug1 				
:stem poihs	 fem			is_ews
:suff 				
:end ei	 fem nom/voc/acc dual	attic epic	contr	is_ews

:raw poih/sei

:workw poih/sei+
:lem poi/hsis
:prvb 				
:aug1 				
:stem poihs	 fem			is_ews
:suff 				
:end ei+	 fem dat sg	epic		is_ews

:raw poih/sei

:workw poih/sei
:lem poi/hsis
:prvb 				
:aug1 				
:stem poihs	 fem			is_ews
:suff 				
:end ei	 fem dat sg	attic ionic	contr	is_ews

:raw poih/sei

:workw poih/sei
:lem poie/w
:prvb 				
:aug1 				
:stem poihs				aor1,ew_denom
:suff 				
:end ei	 aor subj act 3rd sg	epic	short_subj	aor1

:raw poih/sei

:workw poih/sei
:lem poie/w
:prvb 				
:aug1 				
:stem poihs				reg_fut,ew_denom
:suff 				
:end ei	 fut ind mid 2nd sg			reg_fut

:raw poih/sei

:workw poih/sei
:lem poie/w
:prvb 				
:aug1 				
:stem poihs				reg_fut,ew_denom
:suff 				
:end ei	 fut ind act 3rd sg			reg_fut
```

## In the New Testament

Regarding the occurence of 'dual' in the Greek New Testament, Porter, et. al. state:

> “Grammatical number” refers to the distinction that most Greek words make between singular and plural. Earlier Greek had endings for three different numbers—singular, plural, and dual (for two items)—but New Testament Greek has only singular and plural.

Source: Stanley E. Porter, Jeffrey T. Reed, and Matthew Brook O’Donnell, Fundamentals of New Testament Greek (Grand Rapids, MI; Cambridge: William B. Eerdmans Publishing Company, 2010), 23.

## Aproach


