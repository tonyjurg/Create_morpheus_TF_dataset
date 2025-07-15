# Data example

# 1 - Morpheus

The example below shows the detailed Morpheus analysis for Αἰνεῖτε, which return four records. 

The output from Morpheus, running in my [docker environment](../Morpheus_on_docker/running_morpheus_on_docker.md) is:

```bash
-----------------------------
Word: *ai)nei=te

:raw *ai)nei=te

:workw ai)nei=te
:lem ai)ne/w
:prvb 				
:aug1 				
:stem ai)n				ew_pr,e_stem
:suff 				
:end ei=te	 pres imperat act 2nd pl	attic epic	contr	ew_pr

:raw *ai)nei=te

:workw ai)nei=te
:lem ai)ne/w
:prvb 				
:aug1 				
:stem ai)n				ew_pr,e_stem
:suff 				
:end ei=te	 pres opt act 2nd pl			ew_pr

:raw *ai)nei=te

:workw ai)nei=te
:lem ai)ne/w
:prvb 				
:aug1 				
:stem ai)n				ew_pr,e_stem
:suff 				
:end ei=te	 pres ind act 2nd pl	attic epic	contr	ew_pr

:raw *ai)nei=te

:workw ai)nei=te
:lem ai)ne/w
:prvb 				
:aug1 				
:stem ai)n			unaugmented	ew_pr,e_stem
:suff 				
:end ei=te	 imperf ind act 2nd pl	attic epic	contr	ew_pr
-----------------------------
```

# 2 - Web API

Using the [web API](https://services.perseids.org/bsp/morphologyservice/analysis/word?lang=grc&engine=morpheusgrc&word=%CE%91%E1%BC%B0%CE%BD%CE%B5%E1%BF%96%CF%84%CE%B5), with the same word returns an [XML file](word.xml) that presents essentially the same information—though slightly less complete—in a more easily readable format:

```xml
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <oac:Annotation xmlns:oac="http://www.openannotation.org/ns/" rdf:about="urn:TuftsMorphologyService:Αἰνεῖτε:morpheusgrc">
    <dcterms:creator xmlns:dcterms="http://purl.org/dc/terms/">
      <foaf:Agent xmlns:foaf="http://xmlns.com/foaf/0.1/" rdf:about="org.perseus:tools:morpheus.v1"/>
    </dcterms:creator>
    <dcterms:created xmlns:dcterms="http://purl.org/dc/terms/">2020-01-01T00:00:00.000000</dcterms:created>
    <oac:hasTarget>
      <rdf:Description rdf:about="urn:word:Αἰνεῖτε"/>
    </oac:hasTarget>
    <dc:title xmlns:dc="http://purl.org/dc/elements/1.1/"/>
    <oac:hasBody rdf:resource="urn:uuid:idmd262a33dea3e97a13ce384708b93ccc2f80f2da667103b796944a8596987aafa"/>
    <oac:Body rdf:about="urn:uuid:idmd262a33dea3e97a13ce384708b93ccc2f80f2da667103b796944a8596987aafa">
      <rdf:type rdf:resource="cnt:ContentAsXML"/>
      <cnt:rest xmlns:cnt="http://www.w3.org/2008/content#">
        <entry uri="">
          <dict>
            <hdwd xml:lang="grc">αἰνέω</hdwd>
            <pofs order="1">verb</pofs>
          </dict>
          <infl>
            <term xml:lang="grc">
              <stem>αἰν</stem>
              <suff>εῖτε</suff>
            </term>
            <pofs order="1">verb</pofs>
            <mood>imperative</mood>
            <num>plural</num>
            <pers>2nd</pers>
            <tense>present</tense>
            <voice>active</voice>
            <dial>Attic epic</dial>
            <stemtype>ew_pr</stemtype>
            <derivtype>e_stem</derivtype>
            <morph>contr</morph>
          </infl>
          <infl>
            <term xml:lang="grc">
              <stem>αἰν</stem>
              <suff>εῖτε</suff>
            </term>
            <pofs order="1">verb</pofs>
            <mood>optative</mood>
            <num>plural</num>
            <pers>2nd</pers>
            <tense>present</tense>
            <voice>active</voice>
            <stemtype>ew_pr</stemtype>
            <derivtype>e_stem</derivtype>
          </infl>
          <infl>
            <term xml:lang="grc">
              <stem>αἰν</stem>
              <suff>εῖτε</suff>
            </term>
            <pofs order="1">verb</pofs>
            <mood>indicative</mood>
            <num>plural</num>
            <pers>2nd</pers>
            <tense>present</tense>
            <voice>active</voice>
            <dial>Attic epic</dial>
            <stemtype>ew_pr</stemtype>
            <derivtype>e_stem</derivtype>
            <morph>contr</morph>
          </infl>
          <infl>
            <term xml:lang="grc">
              <stem>αἰν</stem>
              <suff>εῖτε</suff>
            </term>
            <pofs order="1">verb</pofs>
            <mood>indicative</mood>
            <num>plural</num>
            <pers>2nd</pers>
            <tense>imperfect</tense>
            <voice>active</voice>
            <dial>Attic epic</dial>
            <stemtype>ew_pr</stemtype>
            <derivtype>e_stem</derivtype>
            <morph>contr unaugmented</morph>
          </infl>
        </entry>
      </cnt:rest>
    </oac:Body>
  </oac:Annotation>
</rdf:RDF>

```

# 3 - NT occurrences

According to [BiblHub](https://biblehub.com/greek/aineite_134.htm), there are two occurrences of Αἰνεῖτε: [Romans 15:11](https://biblehub.com/text/romans/15-11.htm) and [Revelation 19:5](https://biblehub.com/text/revelation/19-5.htm). In both cases, it is [morphologically tagged](https://biblehub.com/grammar/greek.htm) as V-PMA-2P, which matches the first of the four records produced by Morpheus in the examples above. The other morphological alternative tags (V-P<b>O</b>A-2P, V-P<b>I</b>A-2P, and V-<b>II</b>A-2P) did not occur, since they were not considered the proper interpretation of the morpheme *in these specific contexts*.

# 4 - Version

<div style="float: left;">
  <table>
    <tr>
      <td><strong>Author</strong></td>
      <td>Tony Jurg</td>
    </tr>
    <tr>
      <td><strong>Version</strong></td>
      <td>1.2</td>
    </tr>
    <tr>
      <td><strong>Date</strong></td>
      <td>28 April 2025</td>
    </tr>
  </table>
</div>
