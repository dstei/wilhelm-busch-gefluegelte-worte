# wilhelm-busch-gefluegelte-worte
Suchmethodik und -ergebnis von geflügelten Worten von Wilhelm Busch im GC4-Korpus.

## GC4-Korpus
Monatlich werden Milliarden von Internet-Seiten heruntergeladen und in einem Korpus namens Common Crawl 29 veröffentlicht. Einige dieser monatlichen Downloads hat die German NLP Group in Form von Philip May und Philipp Reißel für deutschsprachiger Anwender:innen aufbereitet, indem sie
- mithilfe von Facebook Researchs cc_net 32 Duplikate innerhalb des Downloads identifiziert und gelöscht sowie deutschsprachige Texte identifiziert und herausgefiltert haben;
- Duplikate aus der aktuellsten Korpusversion, die in vorherigen Versionen schon enthalten waren, gelöscht haben;
- Seiten nach der Textqualität sortiert haben in die drei Kategorien head (hohe Qualität: Zeitungsartikel, offizielle homepages), middle (informelle Texte wie Kommentare und Foreneinträge), tail (die dunkle Seite des Internets).
Die entstandenen Korpora haben sie unter dem Namen GC4 für German colossal, cleaned Common Crawl corpus veröffentlicht.

Für die vorliegende Arbeit wurde die head-Version der Oktober-2020-Ausgabe des GC4 verwendet, die aus 240 Terabyte Daten des Common Crawl von Februar 2020 destilliert wurde und 11 232 673 Seiten von 1 158 880 unterschiedlichen Domains enthält – insgesamt etwa 44 Gigabyte an Text. Für die häufigsten in dem Korpus vorkommenden Domains siehe folgende Tabelle.

| Domain | Seiten |
|--------|--------|
| de.m.wikipedia.org | 32292 |
| dejure.org | 18526 |
| www.gesetze-bayern.de | 17539 |
| de.wikipedia.org | 14847 |
| www.tt.com | 12923 |
| api.whatsapp.com | 12499 |
| www.zeit.de | 11683 |
| www.bpb.de | 10350 |
| www.welt.de | 9859 |
| www.ebay.de | 9796 |
| www.spiegel.de | 9342 |
| dewiki.academic.ru | 9238 |
| www.faz.net | 9192 |
| www.sueddeutsche.de | 9096 |
| www.abendblatt.de | 8861 |
| www.fr.de | 8762 |
| www.lr-online.de | 8042 |
| jobs.zeit.de | 8008 |
| www.ris.bka.gv.at | 8003 |
| www.tagesspiegel.de | 7785 |

## Methodik
Zur Datenverarbeitung und -darstellung wurde Python, insbesondere die Python-Bibliotheken Pandas 33 und Matplotlib, 34 genutzt.

### Google Books n-Gramm-Korpus
Die Aufbereitung der Daten für Abb. 4 basiert auf einem n-Gramm-Korpus von Google Books erfolgte folgendermaßen:
1. Herunterladen der relevanten Teile der 20200217-Version des deutschen Google-Books-n-Gramm-Korpus, 35
2. Extraktion der interessanten n-Gramm-Zeitreihen mit grep,
3. Normalisierung der n-Gramm-Datenpunkte mit der Gesamtanzahl des jeweiligen n-Gramms im jeweiligen Jahr,
4. Normalisierung der n-Gramm-Zeitreihen auf den Maximalwert der jeweiligen Zeitreihe für bessere Darstellung.

### GC4
Der oben vorgestellte Teil des GC4-Korpus wurde nach Vorkommen von Buschs geflügelten Worten durchsucht. Nach Ausschluss der Fehlalarme, Dopplungen, meta-Einträge und Treffer der Kategorie »Wörter« aus den vorerst 6234 Treffern bleiben 777 Busch-Zitate bzw. -Abwandlungen von 691 unterschiedlichen Domains übrig. Für Domains mit mehr als drei Treffern siehe Tab. 7. Die gesamte Datenverarbeitung verlief folgendermaßen:
1. Formulieren der regulären Ausdrücke, um Textstellen zu finden, vgl. Tab. 8.
2. Split der heruntergeladenen Textdateien mit flex 36 in ca. 800 Megabyte große Stücke, um sie handhabbar zu machen.
3. Erster Suchdurchgang mit Konkatenation aller regulären Ausdrücke und Extraktion aller Seiten mit einem Treffer.
4. Für jeden regulären Ausdruck (entspricht jedem geflügelten Wort) erneuter Suchdurchgang auf dem im vorigen Schritt vorgefilterten Datensatz mit Extraktion der Textstellen.
5. Für alle Funde der geflügelten Worte Klassifikation der Fundstelle nach Fehlalarm, Dopplung oder einer der Kategorien in Tab. 1.
6. Um die weit auseinandergehende Anzahl bei den Funden von einem bis mehreren Hundert je geflügeltes Wort einzudämmen, folgt die Gewichtung folgender Methode: Das geflügelte Wort wird mit der Quadratwurzel der Anzahl seiner Funde gewichtet, maximal jedoch mit 10.

| Domain | Funde |
| -------|-------|
| vaeternotruf.de | 9 |
| digital.zlb.de | 5 |
| www.thalia.de | 4 |
| www.tagesspiegel.de | 4 |
| de.linkfang.org | 3 |
| de.m.wikipedia.org | 3 |
| www.buecher-leben.de | 3 |
| kriminalakte.wordpress.com | 3 |
| drhelgawaess.blogspot.com | 3 |
| www.hochstetten-dhaun.info | 3 |
| 2012.comic-salon.de | 3 |
| de.wikipedia.org | 3 |
| www.skats.de | 3 |
| www.vaterfreuden.de | 3 |
| sgipt.org | 3 |

## Ergebnisse TODO
Siehe text + kritik
Tabelle 1
Tabelle 2
