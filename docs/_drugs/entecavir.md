---
layout: default
title: Entecavir
parent: Nur Modellvorhersage (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: Von chronischer Hepatitis B zur chronischen Hepatitis-C-Virus-Infektion

## Zusammenfassung in einem Satz

> Entecavir ist ein Nukleosid-Analogon, das für chronische Hepatitis B (HBV) zugelassen ist, wo es die HBV-Reverse-Transkriptase hemmt.
> Das TxGNN-Modell signalisiert als Top-Ranking-Signal eine mögliche Aktivität gegen **chronische Hepatitis-C-Virus-Infektion**,
> aber bei Überprüfung testen keiner der **40 klinischen Studien** oder **20 Publikationen**, die für diese Paarung abgerufen wurden, Entecavir gegen HCV — sie befassen sich mit HBV-Behandlung oder HBV/HCV-Koinfektionsmanagement, und das Evidenzniveau ist **L5 (nur Modellvorhersage)**.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Chronische Hepatitis B (etablierte Indikation, in unterstützenden Beweisen referenziert — es war kein Eintrag zur offiziellen deutschen Marktzulassung verfügbar; siehe Informationen zum deutschen Markt) |
| Vorhergesagte neue Indikation | Chronische Hepatitis-C-Virus-Infektion |
| TxGNN-Vorhersage-Score | 99.98% |
| Evidenzniveau | L5 |
| Status auf dem deutschen Markt | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Daten zum Wirkmechanismus von Entecavir waren im Evidenzpaket nicht verfügbar. Basierend auf den vorhandenen Informationen ist Entecavir ein Desoxyguanosin-Nukleosid-Analogon, dessen etabliertes pharmakologisches Ziel die **Hepatitis-B-Virus-(HBV)-Reverse-Transkriptase** ist — es blockiert das Priming, die pgRNA-Reverse-Transkription und die Synthese des zweiten DNA-Strangs, und dies ist die Grundlage seiner genehmigten Verwendung bei chronischer Hepatitis B.

Das Hepatitis-C-Virus (HCV) ist dagegen ein *Flaviviridae*-RNA-Virus, das sich über eine **RNA-abhängige RNA-Polymerase (NS5B)** repliziert, ein strukturell und mechanistisch unterschiedliches Enzym, bei dem keine bekannte Kreuzreaktivität mit der HBV-gezielten Reverse-Transkriptase-Hemmung von Entecavir bekannt ist. Die eigene mechanistische Bewertung des Evidenzpakets kommt zu dem Schluss, dass es keine pharmakologische Grundlage für Queraktivität gibt.

Konsistent damit testen die klinischen Studien und die Literatur, die für die Abfrage „Entecavir + HCV" abgerufen wurden, nicht die Wirksamkeit von Entecavir gegen HCV. Es handelt sich um HBV-Behandlungsstudien oder Studien zum HBV/HCV-**Koinfektionsmanagement** (z. B. HBV-Reaktivierungsrisiko während der HCV-Therapie mit direkt wirkenden Antivirals), die nur deshalb auftauchten, weil „Hepatitis B und C" zusammen in denselben Abstracts erscheinen. Dieses Muster ist charakteristisch für ein TxGNN-Falsches-Positiv, das durch textliche/semantische Ähnlichkeit zwischen „virale Hepatitis"-Krankheitsknoten angetrieben wird, anstelle einer echten Wirkstoff-Ziel-Beziehung. Bemerkenswert ist, dass das Modell Entecavir separat und korrekt seiner **tatsächlichen bekannten Indikation, Hepatitis-B-Virus-Infektion** zuordnet (Score 99.85%, Evidenzniveau L1, angetrieben durch echte Phase-3-Registrierungsstudien wie NCT00036608, NCT00410202 und NCT01079806) — was validiert, dass das Modell wahre Beziehungen identifizieren kann, aber unterstreicht, dass das HCV-Signal keine ist.

---

## Evidenz aus klinischen Studien

Von den 40 klinischen Studien, die für die Abfrage „Entecavir + chronische HCV" abgerufen wurden, wurden nur einige auf Relevanz überprüft; alle überprüften Studien wurden als niedrig relevant (C) bewertet, weil sie Entecavir zur Behandlung von HBV, nicht HCV, betreffen. Keine Studie in der abgerufenen Menge testet die Wirksamkeit von Entecavir gegen HCV selbst.

| Studiennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---------|------|--------|----------|---------|
| [NCT01179594](https://clinicaltrials.gov/study/NCT01179594) | Phase 4 | Zurückgezogen | 0 | Peginterferon alfa-2a ± Entecavir bei HBeAg-negativer chronischer Hepatitis B — keine HCV-Studie; mit null Einschlussziffer zurückgezogen. |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Abgeschlossen | 120 | Entecavir vs. Lamivudin-Dosisfindung bei japanischen Patienten mit chronischer Hepatitis B — nur HBV, keine HCV-Gruppe. |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Abgeschlossen | 160 | Placebokontrollierte Sicherheits-/PK-Studie von RO7020531 bei chronischer Hepatitis B — die Relevanz von Entecavir/HCV konnte anhand der verfügbaren Details nicht bestätigt werden. |

Die verbleibenden ~37 Studien in der abgerufenen Menge sind nicht klassifiziert (Überprüfung steht an), folgen aber basierend auf ihren Titeln und Zusammenfassungen demselben Muster — Nukleos(t)id-Analog-Therapie bei chronischer Hepatitis B, HBV/HCV-Koinfektions-Reaktivierungsüberwachung oder unabhängige Hepatitis-B-Pharmakologie-Studien. Keine berichtet einen HCV-Wirksamkeits-Endpunkt für Entecavir.

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|--------|---------|
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Übersicht (Stufe 3) | Wiener medizinische Wochenschrift | Überprüft Behandlung von chronischer Hepatitis B und C als parallele, aber getrennte Krankheitspfade; testet Entecavir nicht gegen HCV. |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Übersicht (Stufe 3) | Expert Opinion on Pharmacotherapy | Fortschritte bei der Behandlung von HBV/HCV-**Koinfektionen**; Entecavir wird nur als die auf HBV gerichtete Komponente der Koinfektionsbehandlung erörtert. |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Übersicht (Stufe 3) | Clinics and Research in Hepatology and Gastroenterology | Erörtert die therapeutische Herausforderung von HBV/HCV-Doppelinfektion; keine Daten zur Aktivität von Entecavir gegen HCV selbst. |

Die verbleibenden Literatur-Treffer (z. B. PMID 28487602, 32173307, 24868325) folgen demselben Muster — HBV/HCV werden zusammen als gleichzeitig auftretende Lebererkrankungen oder Koinfektionsmanagement-Themen erörtert, nicht als Beweis für die Wirksamkeit von Entecavir gegen HCV.

---

## Informationen zum deutschen Markt

Entecavir wird derzeit **nicht vermarktet** im Quell-Regulierungsdatensatz (0 Zulassungen in den Aufzeichnungen). Keine Produktlizenz, Darreichungsform oder Text zur genehmigten Indikation war verfügbar zur Berichterstattung.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das chronische-HCV-Signal wird nicht durch Mechanismus (Entecavir zielt auf die HBV-Reverse-Transkriptase; HCV repliziert sich über eine nicht verwandte RNA-Polymerase) oder durch die abgerufenen Beweise gestützt — jede überprüfte klinische Studie und Publikation befasst sich mit der HBV-Behandlung oder dem HBV/HCV-Koinfektionsmanagement, nicht mit der Wirksamkeit von Entecavir gegen HCV. Dies wird am besten als TxGNN-Falsches-Positiv interpretiert, das aus semantischer Nähe zwischen Hepatitis-Virus-Krankheitsknoten entsteht, auf Evidenzniveau L5 (nur Modellvorhersage, keine bestätigenden Studien).

**Um fortzufahren, ist Folgendes erforderlich:**
- In-vitro-Beweise (z. B. HCV-Replikon-Assay), die eine direkte antivirale Aktivität von Entecavir gegen HCV zeigen, die derzeit fehlt
- Eine Überprüfung der TxGNN-Knowledge-Graph-Kanten, die dieser Vorhersage zugrunde liegen, um festzustellen, ob die Hepatitis-B/C-Knotenbeziehung ein Daten- oder Embedding-Artefakt widerspiegelt
- Vollständige Wirkmechanismus-Daten von DrugBank und TFDA/BfArM-Fachinformation für Entecavir, beide derzeit nicht verfügbar (Datenlücken DG001, DG002 in diesem Evidenzpaket), um eine zukünftige S1-Sicherheits-Vorprüfung zu unterstützen

**Zusätzlicher Hinweis zu anderen TxGNN-bewerteten Kandidaten für Entecavir:** Über die 10 in diesem Evidenzpaket bewerteten Krankheitsknoten hinweg zeigen nur zwei substanzielle Beweise — die unabhängige, hochkonfidente Wiederherstellung durch das Modell von Entecavirs **wahre Indikation, chronische Hepatitis B** (L1, Fortfahren mit Vorsichtsmaßnahmen — nützlich als Modell-Validitätsprüfung, nicht als neue Gelegenheit), und ein präklinisches Signal in **tierischem Hepadnavirus-Hepatitis** (L3, Woodchuck-Modell, PMID 11679911), das Entecavirs etablierten antiviralen Mechanismus in einem verwandten Hepadnavirus widerspiegelt. Alle anderen Kandidaten (HIV, felines/simianisches Immundefizienz-Virus, eine seltene neurodevelopmentale Störung, HEV, HAV) wurden als Halten mit L5-Evidenz und keinem plausiblen mechanistischen Zusammenhang bewertet.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

