---
layout: default
title: Cerliponase Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Cerliponase Alfa: Von CLN2-Erkrankung (Batten-Krankheit) bis Scheie-Syndrom

## Zusammenfassung in einem Satz

> Cerliponase Alfa ist eine rekombinante TPP1-Enzymersatztherapie (Tripeptidylpeptidase 1), ursprünglich entwickelt für **CLN2-Erkrankung** (eine Form der neuronalen Ceroid-Lipofuszinose / Batten-Krankheit).
> Die Top-Vorhersage des TxGNN-Modells ist **Scheie-Syndrom** (ein Untertyp der Mukopolysaccharidose I) mit einer **99,98%**-Vorhersagepunktzahl,
> aber es gibt derzeit **0 klinische Studien** und **0 Publikationen**, die diesen spezifischen Zusammenhang unterstützen, und die mechanistische Begründung deutet darauf hin, dass das Signal wahrscheinlich ein Modellartefakt und nicht genuine biologische Plausibilität ist.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | CLN2-Erkrankung (Neuronale Ceroid-Lipofuszinose Typ 2 / Batten-Krankheit) — aus dem Arzneimittelumwidmungs-Texttext abgeleitet; nicht unabhängig über deutsche Zulassungsdaten bestätigt, da das Produkt dort nicht vermarktet wird |
| Vorhergesagte neue Indikation | Scheie-Syndrom |
| TxGNN-Vorhersagepunktzahl | 99,98% (Rang 468 in der Gesamtmodellausgabe) |
| Evidenzstufe | L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhaltung |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismus-Daten (`original_moa`) sind als Datenlücke in diesem Evidence Pack gekennzeichnet. Basierend auf den Arzneimittelumwidmungs-Textnotizen, die jeder vorhergesagten Indikation beigefügt sind, wird verstanden, dass Cerliponase Alfa eine rekombinante Enzymersatztherapie ist, die **TPP1** bereitstellt und auf die CLN2-Erkrankung abzielt, eine lysosomale Speicherkrankheit, die durch TPP1-Mangel verursacht wird.

Das Scheie-Syndrom hingegen ist eine lysosomale Speicherkrankheit, die durch einen Mangel an **Alpha-L-Iduronidasе** (Mukopolysaccharidose I) verursacht wird, einem völlig anderen Enzym und metabolischen Weg. Es gibt kein gemeinsames Substrat, keinen gemeinsamen Enzymzielstoff und keinen überlappenden Behandlungsmechanismus zwischen den beiden Bedingungen.

Der Begründungstext kennzeichnet dies deutlich: Das hohe TxGNN-Ergebnis wird höchstwahrscheinlich durch die Clusterung von Krankheiten des Modells im breiten semantischen Kategorien „lysosomale Speicherkrankheit" erklärt, anstatt durch eine echte pharmakologische Verbindung. Dieses Muster wiederholt sich in fast allen Top-10-Vorhersagen für dieses Arzneimittel — Hurler-Syndrom, Cholesterylester-Speicherkrankheit, Wolman-Krankheit und Gaucher-Krankheit sind alle lysosomale Speicherkrankheiten, die durch *unterschiedliche* Enzymmängel verursacht werden (Alpha-L-Iduronidasе, lysosomale saure Lipase, Glucocerebrosidase), von denen keiner TPP1 beteiligt. Nach den aktuellen Erkenntnissen sollte dieser Kandidat als wahrscheinlich **falsch positiv** und nicht als vielversprechender Arzneimittelumwidmungs-Lead behandelt werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert.

---

## Literaturbeweise

Derzeit sind keine verwandten Literaturbeweise verfügbar.

---

## Marktstatus in Deutschland

Cerliponase Alfa hat derzeit keine deutsche Marktgenehmigung auf Datei (`market_status`: Nicht vermarktet / Nicht vermarktet; `total_licenses`: 0). Es kann keine Produkttabelle erstellt werden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

*(Hinweis: TFDA-äquivalente Kennzeichnung/Warnungen und Kontraindikationsdaten sind als Blocking-Datenlücken in diesem Evidence Pack gekennzeichnet — siehe `DG001`. Dies muss behoben werden, bevor eine S1-Sicherheits-Vorbewertung durchgeführt werden kann.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhaltung**

**Begründung:**
Die top-bewertete Vorhersage (Scheie-Syndrom) und im Wesentlichen alle anderen Top-10-Kandidaten haben sowohl keine Evidenz aus klinischen Studien als auch keine Literaturunterstützung (Evidenzstufe L5), und der bekannte Enzymersatz-Wirkmechanismus des Arzneimittels (TPP1 für CLN2-Erkrankung) überlappt sich nicht mechanistisch mit den Enzymmängeln, die den vorhergesagten Indikationen zugrunde liegen (Alpha-L-Iduronidasе, lysosomale saure Lipase, Glucocerebrosidase usw.). Das Muster deutet stark darauf hin, dass die TxGNN-Ergebnisse die semantische Clusterung von „lysosomale Speicherkrankheits"-Labels widerspiegeln, anstatt ein echtes Arzneimittelumwidmungs-Signal zu sein.

**Um fortzufahren, wird folgendes benötigt:**
- Bestätigte Wirkmechanismus- und ursprüngliche Indikationsdaten aus DrugBank/Zulassungsquelle (derzeit `[Datenlücke]`)
- TFDA/EMA-äquivalente Kennzeichnung, Warnungen und Kontraindikationen (Blocking-Lücke `DG001`)
- Bei weiterer Verfolgung: unabhängige mechanistische Überprüfung, warum TPP1-Ersatz nicht-TPP1-lysosomale Wege plausibel beeinflussen könnte, da derzeit keine solche Begründung existiert
- Angesichts des Fehlens von Evidenz aus Studien oder Literatur bei allen 10 Kandidaten wird empfohlen, die aktive Bewertung dieses Arzneimittels zur Arzneimittelumwidmung zu deprioritieren, es sei denn, neue Erkenntnisse kommen zutage

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

