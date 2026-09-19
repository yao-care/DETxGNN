---
layout: default
title: Midazolam
parent: Nur Modellvorhersage (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Midazolam: Hin zu einer vorhergesagten Indikation für Schlaflosigkeit

## Zusammenfassung in einem Satz

Midazolam ist ein kurzwirksames Benzodiazepin; die ursprüngliche genehmigte Indikation ist im aktuellen Evidenzpaket nicht dokumentiert (behördliche Daten zeigen keine aktive Marktzulassung). Das TxGNN-Modell sagt eine Wirksamkeit für **Schlaflosigkeit** voraus, eine Anwendung, die bereits durch mehrere ältere klinische Studien gut unterstützt wird, anstatt ein echtes neues Repurposing-Signal zu sein, mit **31 klinischen Studien** und **11 Publikationen**, die in der Evidenzsuche zurückgegeben werden — obwohl die meisten Studien Midazolam nur als Vergleichsarm verwenden, anstatt als primäre Intervention bei Schlaflosigkeit.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Nicht im Evidenzpaket dokumentiert — `taiwan_regulatory.licenses` ist leer und kein Text zur ursprünglichen Indikation wird bereitgestellt (Datenlücke) |
| Vorhergesagte neue Indikation | Schlaflosigkeit (Erkrankung) |
| TxGNN-Vorhersage-Score | 99.74 % |
| Evidenzgrad | L2 (mehrere historische doppelblinde RCTs, die Midazolam direkt bei Schlaflosigkeit testen; keine modernen Phase-2/3-registrierten Studien für diese Indikation spezifisch) |
| Status auf dem deutschen Markt | Nicht im Handel (Nicht im Handel) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus im Evidenzpaket nicht verfügbar. Basierend auf etabliertem pharmakologischem Wissen ist Midazolam ein kurzwirksames Benzodiazepin, das als positiver allosterischer Modulator an GABA-A-Rezeptoren wirkt und die hemmende GABAerge Neurotransmission verstärkt. Dieser Mechanismus liegt seinen etablierten klinischen Rollen in Sedation, Anxiolyse, Narkoseeinleitung und — direkt relevant hier — Schlafeinleitung zugrunde.

Da das Evidenzpaket keinen Text zur ursprünglichen Indikation enthält (Lizenz-Array ist leer; Marktstatus ist „Nicht im Handel"), können wir nicht mit Sicherheit sagen, was die ursprünglich genehmigte Indikation des Arzneistoffs in dieser Rechtsordnung war. Jedoch ist die sedativ-hypnotische Pharmakologie von Midazolam inhärent mit der Schlafeinleitung verbunden, was mit der TxGNN-vorhergesagten Indikation Schlaflosigkeit übereinstimmt.

Es ist erwähnenswert, dass diese Vorhersage weitgehend eine bereits bekannte pharmakologische Anwendung von Benzodiazepinen (kurzfristige hypnotische Therapie) bestätigt, anstatt eine echte neue mechanistische Repurposing-Gelegenheit zu erkennen — mehrere der unterstützenden Publikationen stammen aus den 1980er–1990er Jahren und testeten Midazolam direkt als Schlafmittel. Die klinische Bedeutung liegt daher weniger in der wissenschaftlichen Neuheit und mehr in der Frage, ob eine lokale behördliche/Marktrückkehr für diese spezifische Indikation gerechtfertigt ist.

---

## Klinische Studienevidenz

Die meisten Studien in der rohen Evidenzbasis verwenden Midazolam nur als Sedations-Vergleich für unabhängige primäre Endpunkte (z. B. Delir-Prävention, Kopfschmerzen, Onkologie). Die folgenden sind die Studien, die am direktesten relevant für Midazolam und schlafbezogene/Schlaflosigkeits-Ergebnisse sind:

| Studiinnummer | Phase | Status | Rekrutierung | Wichtige Ergebnisse |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Abgeschlossen | 111 | Vergleich der postoperativen Schlafqualität von IV Dexmedetomidin vs. Midazolam kombiniert mit Spinalanästhesie bei TURP-Patienten |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | NA | Wird durchgeführt | 280 | Wirkung von präoperativem oralem Midazolam auf postoperative Schmerzen bei Patienten mit vorbestehender Schlafstörung/Angst, die sich einer laparoskopischen Kolorektalkrebsresektion unterziehen |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | NA | Abgeschlossen | 23 | Randomisierte doppelblinde Studie zum Übergang von Benzodiazepin-(Midazolam-)Sedation zu Dexmedetomidin zur Erleichterung der Entwöhnung von der Beatmung auf der Intensivstation |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Beendet | 5 | 24-Stunden-Polysomnographie-Vergleich der Schlafqualität/-menge und Delir-Inzidenz: Dexmedetomidin vs. Midazolam bei mechanisch beatmeten Intensivstations-Patienten |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Beendet | 6 | Polysomnographischer Vergleich von α2-Agonisten vs. GABA-Agonisten (einschließlich Midazolam) auf Schlafstadien und Gesamtschlafzeit |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unbekannt | 120 | Sedations-Wirksamkeit von Dexmedetomidin vs. Midazolam bei kritisch kranken beatmeten Kindern |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Phase 4 | Unbekannt | 285 | Remimazolam (Benzodiazepin-Klasse) vs. Standard-Sedation für mechanische Beatmung auf der Intensivstation nach Mund-/Kieferchirurgie |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | NA | Abgeschlossen | 131 | RCT zum Vergleich von Remimazolam-Allgemeinnarkose vs. Propofol + Midazolam-Kontrollgruppe |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Phase 2 | Wird durchgeführt | 110 | Midazolam-kontrollierte RCT von internetgestützter KVT + IV Ketamin bei Suizidalität in therapieresistenter Depression |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | NA | Abgeschlossen | 178 | Wirkung von Ketamin (zusätzlich zu Midazolam-basierter Sedation) auf Schlafqualität bei Koloskopie-Patienten |

*Hinweis: Diese Studien sind indirekte Evidenz (Midazolam hauptsächlich als aktiver Vergleich/Sedations-Hintergrund verwendet), keine Studien zur Testung von Midazolam als primäre Behandlung für diagnostizierte Schlaflosigkeit.*

---

## Literaturevidenz

| PMID | Jahr | Typ | Zeitschrift | Wichtige Ergebnisse |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | Br J Clin Pharmacol | Doppelblinde Studie: Midazolam 15 mg vs. Vesparax bei sekundärer Schlaflosigkeit bei neuromuskulärer Erkrankung; beide wirksam, Midazolam besser verträglich ohne Hangover-Effekt |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | J Clin Psychopharmacol | Multizentrische randomisierte doppelblinde Parallelgruppenstudie: 14-Tage-Midazolam vs. Flurazepam bei chronischer Schlaflosigkeit, Bewertung von Schlaf, Leistung und Plasmakonzentrationen |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | J Clin Psychopharmacol | Zusammenfassung der oben genannten 14-Tage-multizentrischen Midazolam-vs.-Flurazepam-Studie bei chronischer Schlaflosigkeit |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT (Dosisfindung) | Arzneimittelforschung | Multizentrische Pilotstudie mit oralem Midazolam (10–30 mg) bei 75 Patienten mit leichter bis mittelschwerer Schlaflosigkeit, sekundär zu muskuloskelettalen/neurologischen/allergischen Erkrankungen |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Übersicht | Acta Psychiatr Scand Suppl | Übersicht der klinischen Anwendung von Schlafmitteln (einschließlich Benzodiazepine) bei verschiedenen Schlaflosigkeits-Subtypen |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Übersicht | Orvosi Hetilap | Übersicht der Pathogenese von Schlaflosigkeit, einschließlich Hyperarousal- und zerebraler Hypoperfusions-Mechanismen |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Pilotstudie | J Clin Med | Bewertung von Lemborexant bei Schlaflosigkeit zur Verringerung des Delir-Risikos bei Hochrisiko-Endoskopie-Patienten; beachten Sie, dass die traditionelle Benzodiazepin-Anwendung bei Schlaflosigkeit das Delir verschlimmern kann |

---

## Informationen zum deutschen Markt

Midazolam verfügt derzeit über **keine aktive Marktzulassung** im vorliegenden Datensatz (`market_status`: Nicht im Handel / Nicht im Handel; `total_licenses`: 0). Es sind keine Produkt-/Lizenzaufzeichnungen verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Alle Felder in `safety.key_warnings`, `safety.contraindications` und `safety.ddi` sind als Datenlücken im Evidenzpaket gekennzeichnet. Beachten Sie auch, dass die Datenlücke DG001 — TFDA-Etikett-Warnhinweise/Kontraindikationen — als **Blockierender Schweregrad** klassifiziert ist, was bedeutet, dass die Sicherheitsbewertung (S1) derzeit nicht fortfahren kann.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
- Die vorhergesagte Indikation (Schlaflosigkeit) ist pharmakologisch plausibel und wird durch mehrere historische RCTs unterstützt, aber dieses Evidenzpaket weist eine **Blockierende**-Schweregrad-Datenlücke auf (fehlende TFDA-Etikett-/Sicherheitsdaten), die per Definition den Eintritt in die S1-Sicherheitsanfangsbewertung verhindert.
- Das Arzneimittel verfügt über keine aktive Marktzulassung in dieser Rechtsordnung (0 Zulassungen), und es ist kein Text zur ursprünglichen Indikation verfügbar.
- Die vorhergesagte „neue" Indikation überlappt sich erheblich mit der bereits bekannten hypnotischen Pharmakologie von Midazolam, anstatt einen neuartigen mechanistischen Fund darzustellen, was die Dringlichkeit/den Wert einer weiteren Repurposing-Investition im Vergleich zu den fehlenden Sicherheitsdaten verringert.

**Um fortzufahren, wird folgende Information benötigt:**
- Beschaffung von TFDA-(oder relevanter behördlicher) Packungsbeilage-Daten — Warnhinweise, Kontraindikationen, Arzneimittelwechselwirkungen (DG001, Blockierend)
- Bestätigung der aus DrugBank stammenden MOA und Arzneimittelkategorien direkt (DG002, Hoch)
- Klärung der ursprünglichen/derzeit genehmigten Indikation(en) des Arzneistoffs, falls vorhanden, auf dem Zielmarkt
- Falls weitere Verfolgung angestrebt wird, Ermittlung oder Beauftragung von klinischen Studien, die Midazolam als primäre Intervention bei diagnostizierter Schlaflosigkeit testen (aktuelle Studienevidenz ist indirekt/vergleichsbasiert)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

