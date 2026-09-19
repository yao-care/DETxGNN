---
layout: default
title: Omalizumab
parent: Mittlere Evidenz (L3-L4)
nav_order: 280
evidence_level: L4
indication_count: 10
---

# Omalizumab
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **10** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmazeutischer Bewertungsbericht

</div>

# Omalizumab: Von allergischem Asthma zu Bronchitis

## Zusammenfassung in einem Satz

Omalizumab (Xolair) ist ein rekombinanter humanisierter monoklonaler Anti-IgE-Antikörper, der international zur Behandlung von mittel- bis schwerem allergischem Asthma und chronischer spontaner Urtikaria (CSU) zugelassen ist; er wird in Deutschland nicht vermarktet, sodass kein lokaler Zulassungstext verfügbar ist, um die ursprüngliche Indikationsformulierung zu bestätigen. Das TxGNN-Modell prognostiziert als höchstrangige neue Indikation für dieses Arzneimittel **Bronchitis**, gestützt durch **2 klinische Studien** und **8 Publikationen** — aber bei näherer Überprüfung ist im Grunde keine dieser Evidenzen bei Patienten mit tatsächlich diagnostizierter Bronchitis durchgeführt worden, daher sollte das Signal mit Vorsicht statt als umsetzbarer Repurposing-Kandidat behandelt werden.

---

## Schnellübersicht

| Element | Inhalt |
|---|---|
| Ursprüngliche Indikation | Nicht in der deutschen Zulassungsdatenbank vorhanden (Arzneimittel wird dort nicht vermarktet); international zugelassen für allergisches Asthma und chronische spontane Urtikaria (CSU) |
| Prognostizierte neue Indikation | Bronchitis |
| TxGNN-Vorhersage-Score | 99.9992% (interner Rang 30 unter allen Kandidatenkrankheiten) |
| Evidenzebene | L4 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Prognose begründet?

Das DrugBank-gestützte Wirkmechanismus-Feld für Omalizumab ist derzeit eine Datenlücke. Basierend auf Informationen, die in den klinischen Studien und Literatursummaries dieses Evidenzpakets verteilt sind, ist Omalizumab ein rekombinanter humanisierter monoklonaler Antikörper, der freies Serum-IgE bindet und seine Wechselwirkung mit dem hochaffinen FcεRI-Rezeptor auf Mastzellen und Basophilen blockiert. Dies unterbricht die IgE-vermittelte allergische Entzündungskaskade und ist der etablierte Mechanismus, der seiner zugelassenen Anwendung bei allergischem Asthma und CSU zugrunde liegt — beide Erkrankungen werden in den klinischen Studiennachweisen in diesem Paket wiederholt erwähnt, obwohl sie nicht im Feld `taiwan_regulatory.licenses` erscheinen, da das Arzneimittel in Deutschland nicht vermarktet wird.

Bronchitis und allergisches Asthma teilen sich anatomische Gebiete (die Bronchien) und einige überlappende Symptome (Husten, Atemwegsentzündung), weshalb das TxGNN-Einbettungsmodell sie wahrscheinlich nahe beieinander platziert. Jedoch ist die Atemwegsentzündung bei Bronchitis typischerweise durch Infektion oder Reizstoffexposition statt durch IgE-vermittelte Typ-I-Überempfindlichkeit bedingt, daher ist die Begründung zur Ausweitung eines Anti-IgE-Antikörpers speziell auf Bronchitis (im Gegensatz zu allergischem Asthma, das Omalizumab bereits behandelt) schwach.

Kritischerweise: Wenn die abgerufenen Evidenzen überprüft werden, unterstützen sie tatsächlich nicht einen bronchitis-spezifischen Effekt: beide klinischen Studien rekrutierten Asthma- oder CSU-Populationen statt Bronchitis-Patienten, und von den 8 Literatureinträgen erörtert nur einer ausdrücklich Bronchitis (PMID 31478531), und das ist ein Fallbericht von *plastischer Bronchitis als Komplikation der Bronchialthermoplastie* — ein prozedurales Nebenereignis, keine therapeutische Evidenz für Omalizumab bei der Behandlung von Bronchitis. Dieses Muster ist konsistent mit einem Krankheits-Ontologie-Nähe-Artefakt statt eines echten pharmakologischen Signals.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---|---|---|---|---|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Abgeschlossen | 11 | Kortikoid-sparende Wirkung von Omalizumab bei Patienten mit **Asthma und persistierender eosinophiler Bronchitis** (Zusatz zu Prednison). *Relevanzgrad C — Studienpopulation ist primär Asthma, nicht Bronchitis als eigenständige Diagnose.* |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | Abgeschlossen | 382 | Dosisfindungsstudie von QGE031 (Ligelizumab) vs. Placebo als Zusatztherapie bei **chronischer spontaner Urtikaria (CSU)**. *Relevanzgrad C — keine Bronchitis-Population; erfasst nur über Arzneimittelklasse/Mechanismus-Nähe.* |

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|---|---|---|---|---|
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Übersichtsarbeit | Expert Opinion on Pharmacotherapy | Erörtert durch Rauchen induzierte Atemwegserkrankungen (chronische Bronchitis, Emphysem, Asthma-COPD-Überschneidung) und vermerkt, dass Patienten mit diesen Erkrankungen typischerweise von Asthma-Biologika-Studien ausgeschlossen werden. |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Sicherheits-Kohorte | Current Medical Research and Opinion | Gepoolte Sicherheitsanalyse von Omalizumab bei **Kindern mit allergischem Asthma**; keine bronchitis-spezifischen Daten. |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Übersichtsarbeit | Clinical Reviews in Allergy & Immunology | Erfahrung nach der Zulassung von Omalizumab bei **mittel- bis schwerem persistentem Asthma**; etabliert den zugelassenen Anwendungskontext des Arzneimittels, nicht Bronchitis. |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Kohorte | Postępy Dermatologii i Alergologii | Omalizumab bei älteren Patienten mit schwerem **allergischem Asthma-COPD-Überschneidung**; Atemwegsverengungskontext, aber nicht spezifisch Bronchitis. |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Narrative Übersicht | Masui (Japanese J. Anesthesiology) | Präoperatives Managementleitfaden für Patienten mit Bronchialasthma **oder** chronischer Bronchitis; erwähnt Omalizumab nur im Asthma-Behandlungskontext. |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Übersichtsarbeit | Revue des Maladies Respiratoires | Französische Fachexpertenübersicht über Asthma-Exazerbationen bei Erwachsenen; allgemeine Krankheitsmanagement-Übersicht, keine bronchitis-spezifischen Wirksamkeitsdaten. |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Übersichtsarbeit | Allergologia et Immunopathologia | Allgemeine pädiatrische Übersicht über monoklonale Antikörper (einschließlich Anti-IgE) bei allergischen und neoplastischen Erkrankungen; nicht bronchitis-fokussiert. |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Fallbericht | J. Investigational Allergology & Clinical Immunology | Berichtet einen seltenen Fall von **plastischer Bronchitis als Komplikation nach Bronchialthermoplastie** — ein prozedurales Nebenereignis, keine Evidenz der Omalizumab-Wirksamkeit gegen Bronchitis. |

---

## Informationen zum Marktstatus in Deutschland

Omalizumab wird derzeit **nicht in Deutschland vermarktet** nach diesem Evidenzpaket (`market_status: Not marketed`, `total_licenses: 0`). Keine BfArM-Zulassungsdatensätze sind verfügbar, um Produktnamen, Darreichungsformen oder zugelassene Indikationsformulierungen zusammenzufassen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Keine wichtigen Warnungen, Gegenanzeigen oder Arzneimittel-Wechselwirkungsdaten waren zu diesem Zeitpunkt abrufbar (DDI-Abfragestatus: nicht gefunden). Beachten Sie, dass die zugrunde liegenden TFDA/BfArM-Fachinformationswarnungen und Gegenanzeigen in diesem Evidenzpaket als **Blocking**-Severity-Datenlücke gekennzeichnet sind (DG001), was bedeutet, dass ein formales Sicherheits-Vorscreening (S1) für diesen Kandidaten noch nicht abgeschlossen werden kann.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
- Die von TxGNN höchstrangig prognostizierte neue Indikation für Omalizumab, Bronchitis (Score 99.9992%), wird durch ihre unterstützende Evidenz nicht belegt: beide abgerufenen klinischen Studien rekrutierten Asthma/CSU-Populationen (Relevanzgrad C, nicht Bronchitis), und 7 von 8 Literatureinträgen sind allgemeine Asthma/Atemwegserkrankungs-Übersichten ohne bronchitis-spezifische Wirksamkeitsdaten — der eine Eintrag, der Bronchitis direkt nennt, ist ein Fallbericht eines behandlungsbezogenen Nebenereignisses, keine therapeutische Erkenntnis.
- Evidenzebene ist L4 (Mechanismus/präklinische Ebene) mit Entscheidungsphase S0, was darauf hinweist, dass das Signal wahrscheinlich die Krankheits-Ontologie-Nähe im Einbettungsraum des Modells widerspiegelt (Bronchitis teilt anatomische/Symptom-Überschneidung mit Asthma) statt eines echten pharmakologischen Effekts, der spezifisch für Bronchitis ist.

**Für den Fortschritt ist Folgendes erforderlich:**
- TFDA/BfArM-Fachinformation (Warnungen, Gegenanzeigen) — derzeit eine Blocking-Datenlücke (DG001), erforderlich vor jedem S1-Sicherheits-Vorscreening.
- Ein bestätigter, strukturierter ursprünglicher Wirkmechanismus-Datensatz (MOA) von DrugBank (DG002), statt der ergänzenden/abgeleiteten Beschreibung des Pakets.
- Klinische Evidenz unter Einschluss von Patienten mit bestätigter Bronchitis-Diagnose (im Gegensatz zu Asthma- oder CSU-Patienten, die über Schlüsselwort/Ontologie-Überschneidung erfasst werden), bevor dieser Kandidat neu bewertet werden kann.

---

### Zusätzliche Anmerkung: Andere TxGNN-prognostizierte Indikationen in diesem Evidenzpaket

Dieses Evidenzpaket evaluierte Omalizumab gegen 10 Kandidaten-Indikationen. Während Bronchitis den höchsten TxGNN-Modell-Score trägt, ist sie nicht der stärkste evidenzgestützte Kandidat in der Gruppe. Zum Kontext:

| Erkrankung | TxGNN-Score | Evidenzebene | Empfehlung | Anmerkung |
|---|---|---|---|---|
| Obstruktive Lungenerkrankung | 99.97% | L1 | Mit Vorsichtsmaßnahmen fortfahren | Umfangreiche Phase-3/4-RCT-Unterstützung (z. B. NCT00314574, n=850; NCT00401596, n=1899); mechanistisch spiegelt dies größtenteils Omalizumabs *bereits etablierte* allergische Asthma-Aktivität statt eine neuartige Repurposing-Gelegenheit wider. |
| Atopisches Ekzem | 99.97% | L2 | Forschungsfrage | Eine direkte Phase-4-RCT (NCT02300701, n=62) plus gemischte Literatur, einschließlich eines Fallberichts von Omalizumab-*induzierter* Dermatitis — das Wirksamkeitssignal ist inkonsistent. |
| Dermatitis | 99.97% | L2 | Forschungsfrage | Teilt nahezu denselben Evidenzbestand wie atopisches Ekzem; wahrscheinlich ein Duplikatsignal aus demselben Krankheitscluster statt eines unabhängigen Befunds. |
| Bronchiales Neoplasma | 99.95% | L5 | Zurückstellen | Keine mechanistische oder klinische Grundlage; beide abgerufenen Einträge sind nur Asthma-Kontext. |
| Akne Keloid / Acrodermatitis chronica atrophicans / Hydroa vacciniforme / neonatale Dermatomyositis / sekundäre Kinder-ILD | 99.9–99.94% | L5 | Zurückstellen | Null klinische Studien oder Literatur; keine mechanistische Begründung. |

Zur zukünftigen Priorisierung verdienen "Obstruktive Lungenerkrankung" und separat "Atopisches Ekzem"/"Dermatitis" (empfohlen, gemeinsam evaluiert zu werden, angesichts überlappender Evidenz) mehr Aufmerksamkeit als Bronchitis allein.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

