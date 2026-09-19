---
layout: default
title: Sofosbuvir
parent: Mittlere Evidenz (L3-L4)
nav_order: 369
evidence_level: L4
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **8** 
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

# Sofosbuvir: Von der Hepatitis-C-Virus-Infektion zur Hepatitis-B-Virus-Infektion

## Zusammenfassung in einem Satz

Sofosbuvir ist ein Nukleotidanalogon-Inhibitor der Hepatitis-C-Virus (HCV)-NS5B-RNA-abhängigen RNA-Polymerase, und seine etablierte Wirksamkeit liegt bei der chronischen HCV-Infektion. Das TxGNN-Modell sagt voraus, dass es auch bei der **Hepatitis-B-Virus-Infektion** wirksam sein könnte, mit **50 klinischen Studien** und **19 Veröffentlichungen**, die mit diesem Label gekennzeichnet sind – aber bei genauerer Überprüfung befasst sich die große Mehrheit dieser Evidenz mit der HCV-Behandlung bei Patienten, die auch HBV tragen (Ko-Infektions-/Reaktivierungskontexte), nicht mit direkter Anti-HBV-Wirksamkeit.

---

## Schnellübersicht

| Item | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Hepatitis-C-Virus (HCV)-Infektion *(abgeleitet von Wirkmechanismus-Aussagen, die in der Evidenzbeschaffung eingebettet sind; es wurden keine formalen `original_indications`/Label-Daten bereitgestellt)* |
| Vorhergesagte neue Indikation | Hepatitis-B-Virus-Infektion |
| TxGNN-Vorhersage-Score | 99,77% |
| Evidenzstufe | L4 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind detaillierte Wirkmechanismus-Daten (`original_moa`) im strukturierten Arzneimitteldatensatz nicht verfügbar. Die Evidenzbeschaffung selbst identifiziert jedoch konsequent Sofosbuvir als ein Nukleotidanalogon, das die HCV-NS5B-RNA-abhängige RNA-Polymerase (RdRp) hemmt – das Enzym, das HCV (ein Mitglied der Familie *Flaviviridae*) zur Replikation seines Genoms nutzt. Dies ist ein gut etablierter, klinisch bewiesener Wirkmechanismus gegen HCV.

HBV ist dagegen ein *Hepadnavirus*, das sich über eine Reverse-Transkriptase (RT)-Domäne in seinem eigenen Polymerase repliziert – ein strukturell und mechanistisch unterschiedliches Enzym von HCVs NS5B-RdRp. Es ist kein bekannter direkter inhibitorischer Effekt von Sofosbuvir gegen das HBV-Polymerase bekannt. Die eigene mechanistische Bewertung der Evidenzbeschaffung besagt dies explizit: Die beiden Enzyme haben „völlig unterschiedliche" aktive Zentren und Substratspezifität, und kein direkter HBV-Polymerase-Hemmmechanismus ist bekannt.

Dies ist konsistent mit der Beobachtung, dass die meisten der zugrunde liegenden klinischen Studien und Literaturbefunde **nicht** die Wirksamkeit von Sofosbuvir gegen HBV testen. Stattdessen fällt es in zwei Kategorien: (1) Studien zu Sofosbuvir-basierten HCV-Regimen, die in Patientenpopulationen durchgeführt werden, die zufällig HCV/HBV-ko-infiziert sind, wobei das Behandlungsziel HCV bleibt; und (2) Fallberichte und Kohortenstudien, die die **HBV-Reaktivierung** als nachteilige Folge der HCV-Clearance mit direkt wirkenden Antiviralen (DAA) beschreiben, was ein Sicherheitssignal ist und nicht als Beweis für Anti-HBV-Wirksamkeit. Die einzige unmittelbar relevante Studie – eine kleine, einarmige Phase-2-Studie mit Ledipasvir/Sofosbuvir bei HBV-monoinfizierten Subjekten (NCT03312023, n=21) – war auf der Grundlage einer bescheidenen, zuvor beobachteten Reduktion von HBsAg bei HCV/HBV-Ko-Infektionsbehandlung konzipiert und stellt eher eine Hypothesen-generierende Pilotstudie dar als bestätigte Wirksamkeit. Insgesamt scheint der TxGNN-Score stark durch Label-Ko-Vorkommen (HCV/HBV-Ko-Infektions- und Reaktivierungsliteratur) angetrieben zu sein, eher als durch einen validierten antiviralen Mechanismus gegen HBV selbst.

---

## Evidenz aus klinischen Studien

| Studienkennummer | Phase | Status | Einschluss | Wichtigste Ergebnisse |
|---------|------|--------|----------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Abgeschlossen | 21 | Offene Pilotstudie mit Ledipasvir/Sofosbuvir 12 Wochen bei **HBV-monoinfizierten** Subjekten; primäre/sekundäre Endpunkte waren Rückgang von HBsAg und HBV-DNA, basierend auf früherer Beobachtung eines bescheidenen HBsAg-Rückgangs bei HCV/HBV-ko-infizierten Patienten. Unmittelbar relevanteste Studie im Datensatz. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Abgeschlossen | 111 | Ledipasvir/Sofosbuvir-FDC 12 Wochen bei taiwanesischen Erwachsenen mit chronischem Genotyp 1/2 HCV **und HBV-Ko-Infektion**; HCV-antivirale Wirksamkeit/Sicherheit bewertet, HBV-Ergebnisse sekundär. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Abgeschlossen | 23 | Prospektive Studie zur Häufigkeit/Risikofaktoren der HBV-Reaktivierung während DAA-Behandlung von HCV/HBV-ko-infizierten Patienten – eine Sicherheits-/Reaktivierungsstudie, keine HBV-Wirksamkeitsstudie. |
| [NCT02349048](https://clinicaltrials.gov/study/NCT02349048) | Phase 2 | Abgeschlossen | 68 | Simeprevir + Daclatasvir + Sofosbuvir für chronisches HCV Genotyp 1 (6–8 Wochen); **bewertet mit niedriger Relevanz (C)** – nur HCV-Behandlung, kein HBV-Endpunkt. |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Abgeschlossen | 228 | Generischer Velpatasvir/Sofosbuvir ± Ribavirin für HCV bei HIV-ko-infizierten Patienten; **bewertet mit niedriger Relevanz (C)** – keine HBV-Verbindung. |
| [NCT02717949](https://clinicaltrials.gov/study/NCT02717949) | Phase 4 | Beendet | 1 | Orale HCV-Therapie bei Patienten mit indolentem Lymphom; **bewertet mit niedriger Relevanz (C)**, beendet mit minimalem Einschluss. |

*Hinweis: Die zugrunde liegende Evidenzbeschaffung listet ~50 Studien unter diesem Indikationslabel auf; die verbleibenden ~44 sind überwiegend konventionelle HCV-Direktviral-Studien (Wirksamkeit, Sicherheit, Arzneimittelwechselwirkungen, Spezialgruppen) ohne direkten Bezug zur HBV-Wirksamkeit – sie erscheinen in diesem Label hauptsächlich über HCV/HBV-Ko-Infektionskohorten oder Populationsüberlappung, nicht weil Sofosbuvir gegen HBV getestet wurde.*

---

## Evidenz aus der Literatur

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|---------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase-2-offene Studie | J Med Virol | Ledipasvir/Sofosbuvir 12 Wochen bei HBV-monoinfizierten Subjekten; Hypothese war, dass der HBsAg-Rückgang bei HCV/HBV-Ko-Infektion wiederkehren würde – die einzige prospektive interventionelle Evidenz für direkte Anti-HBV-Aktivität. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Kohorte (HCV/HBV-Ko-Infektion) | Trans R Soc Trop Med Hyg | Sofosbuvir/Daclatasvir-basierte Therapie bei ägyptischen HCV- und HCV/HBV-ko-infizierten Patienten; Wirksamkeitsendpunkt konzentriert sich auf HCV-Clearance. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Fallbericht | Medicine | HBV-Reaktivierung nach erfolgreicher HCV-Behandlung mit Sofosbuvir + Ribavirin – ein Sicherheitssignal, keine Wirksamkeitsevidenz. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Kohorte/Register | J Clin Gastroenterol | Risiko der HBV-Reaktivierung bei Patienten, die mit Ledipasvir-Sofosbuvir für HCV behandelt werden. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Kohorte | Infect Drug Resist | Management der HBV-Reaktivierung nach DAA-Behandlung von HCV bei HCV/HBV-ko-infizierten Patienten. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Fallbericht | J Med Case Rep | HBV-Reaktivierung mittels einer Oberflächenantigen-Immunflucht-Mutante während Sofosbuvir/Velpatasvir-Behandlung für HCV. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospektive Beobachtungsstudie | J Viral Hepat | HBV-Reaktivierung bei Krebspatienten, die DAAs für HCV/HBV-Ko-Infektion erhalten. |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | ADR-Bericht | Hospital Pharmacy | Notiert einen Fall von Hepatitis-B-Reaktivierung während HCV-Behandlung mit Simeprevir und Sofosbuvir. |

*Hinweis: Der Großteil dieser Literatur dokumentiert das Risiko der HBV-Reaktivierung während der HCV-Behandlung mit Sofosbuvir-basierten Regimen – ein Sicherheitsanliegen, das für HCV/HBV-ko-infizierte Patienten relevant ist – eher als Beweis dafür, dass Sofosbuvir HBV-Infektion behandelt.*

---

## Marktinformationen für Deutschland

Sofosbuvir ist gemäß dieser Evidenzaufzeichnung (`market_status`: Not marketed / Nicht vermarktet) derzeit **nicht vermarktet** in Deutschland, mit **0 eingetragenen Genehmigungen**. Keine Lizenz- oder Produktinformationen sind verfügbar zur Tabellarisierung.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

*(In dieser Evidenzbeschaffung waren keine strukturierten Warnungen, Kontraindikationen oder DDI-Daten verfügbar. Beachten Sie jedoch, dass die obige Literaturrecherche ein wiederkehrendes Signal des **HBV-Reaktivierungsrisikos** bei HCV/HBV-ko-infizierten Patienten, die mit Sofosbuvir-basierten Regimen behandelt werden, zutage brachte – dies sollte ein spezifischer Fokus jeder zukünftigen formalen Sicherheitsbewertung für diese Indikation sein.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die vorhergesagte Verbindung zwischen Sofosbuvir und HBV-Infektion wird nicht durch einen validierten Mechanismus gestützt – HBVs Reverse-Transkriptase-basierte Replikation ist strukturell unabhängig von der HCV-NS5B-RdRp, die Sofosbuvir hemmt. Der hohe TxGNN-Score scheint stark durch Label-Ko-Vorkommen in HCV/HBV-Ko-Infektions- und Reaktivierungsliteratur angetrieben zu sein, eher als durch genuine Anti-HBV-Aktivität, und die einzige direkte interventionelle Evidenz ist eine einzelne kleine Phase-2-Pilotstudie (n=21) ohne bestätigende Nachverfolgung.

**Um fortzufahren, wird Folgendes benötigt:**
- Auflösung der blockierenden Datenlücke bei TFDA/BfArM-Label-Warnungen und Kontraindikationen (DG001), bevor eine Sicherheitsbewertung durchgeführt werden kann
- Bestätigte Wirkmechanismus-Daten (DG002), um einen plausiblen Anti-HBV-Weg zu validieren oder zu widerlegen
- Ergebnisdaten (nicht nur Studiendesign) von NCT03312023, um zu bestimmen, ob das beobachtete HBsAg/HBV-DNA-Signal klinisch bedeutsam war
- Eine angemessen gepowerte, HBV-Monoinfektion-spezifische kontrollierte Studie mit virologischen Endpunkten, eher als Abhängigkeit von Ko-Infektions-/Reaktivierungskohorten
- Eine spezielle Überprüfung des in der Literatur identifizierten HBV-Reaktivierungsrisikosignals, bevor diese Indikation weiter in Betracht gezogen wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

