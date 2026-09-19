---
layout: default
title: Idelalisib
parent: Mittlere Evidenz (L3-L4)
nav_order: 194
evidence_level: L3
indication_count: 10
---

# Idelalisib
{: .fs-9 }

Evidenzniveau: **L3** | Vorhergesagte Indikationen: **10** 
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

# IDELALISIB: Von B-Zell-Lymphoiden Malignomen zum Mantelzell-Lymphom

## Zusammenfassung in einem Satz

Idelalisib ist ein selektiver PI3Kδ-Inhibitor, der ursprünglich für B-Zell-Lymphoide Malignome entwickelt wurde (chronische lymphatische Leukämie, follikuläres Lymphom, kleines lymphozytäres Lymphom).
Das TxGNN-Modell prognostiziert, dass es auch bei **Mantelzell-Lymphom (MCL)** wirksam sein könnte,
mit **9 klinischen Studien** und **20 Publikationen**, die derzeit diese Richtung unterstützen — obwohl bestätigende Phase-2/3-Evidenz spezifisch für MCL noch fehlt.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht in Evidenz-Paket angegeben (Datenlücke — `drug.original_indications` ist leer). Basierend auf der bekannten Identität des Arzneistoffs (idelalisib/Zydelig®), auf die sich die Begründung des Evidenz-Pakets bezieht, sind die etablierten Indikationen rezidiviertes CLL, follikuläres Lymphom und kleines lymphozytäres Lymphom. |
| Vorhergesagte neue Indikation | Mantelzell-Lymphom |
| TxGNN-Prognose-Score | 99,84% (Rang 2395) |
| Evidenzstufe | L3 |
| Status auf dem deutschen Markt | Nicht im Handel (Nicht im Handel) — intern gekennzeichnet als wahrscheinliche Datenlücke statt wahre Abwesenheit einer Zulassung (siehe Begründung unten) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Prognose vernünftig?

Derzeit sind detaillierte Wirkmechanismus-Daten im strukturierten Feld `drug.original_moa` nicht verfügbar (Datenlücke, Element DG002). Auf Grundlage von Informationen, die an anderer Stelle in diesem Evidenz-Paket enthalten sind, ist Idelalisib ein selektiver, oral bioverfügbarer Inhibitor der δ-Isoform der Phosphatidylinositol-3-Kinase (PI3Kδ). PI3Kδ-Signalisierung ist eine Kernkomponente des B-Zell-Rezeptor (BCR)-Signalwegs, der das Überleben und die Proliferation bei mehreren B-Zell-Malignomen antreibt.

Mantelzell-Lymphom ist wie die etablierten Indikationen von Idelalisib (CLL, FL, SLL) ein BCR-Signalisierungs-abhängiges B-Zell-Lymphom. Diese gemeinsame molekulare Abhängigkeit bildet die biologische Grundlage für die TxGNN-Prognose: Ein gegen ein BCR-getriebenes Malignom validierter Arzneistoff ist mechanistisch plausibel gegen ein anderes. In-vitro-Studien in diesem Evidenz-Paket unterstützen dies direkt — Idelalisib hemmt das Wachstum und induziert Apoptose in MCL-Zelllinien (PMID 27342398, PMID 33850273, PMID 40466505), und eine frühe klinische Studie berichtete über messbare Einzelwirkstoff-Aktivität bei Patienten mit rezidiviertem/refraktärem MCL (PMID 24795031, PMID 24615778).

Gleichzeitig weist das Evidenz-Paket selbst darauf hin, dass Idelalisib in einer Untergruppe von MCL-Fällen *intrinsische Resistenz* zeigt (PMID 33850273), und mehrere Studien, die Idelalisib mit anderen Wirkstoffen bei MCL kombinierten, wurden frühzeitig beendet (z. B. NCT01796470, NCT02457598) — was darauf hindeutet, dass zwar die mechanistische Begründung sinnvoll ist, die klinische Umsetzung bei MCL spezifisch jedoch noch nicht auf definitivem Niveau bestätigt worden ist.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Abgeschlossen | 241 | Sicherheit von Idelalisib kombiniert mit Anti-CD20-mAk, Chemotherapie, mTOR/Protease/Antiangiogenese/Immunmodulatoren bei rezidiviertem/refraktärem iNHL, MCL oder CLL |
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 | Abgeschlossen | 106 | Idelalisib + Lenalidomid bei rezidiviertem/refraktärem MCL — dediziertes Phase-I/randomisiertes Phase-II-Design |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Abgeschlossen | 20 | BCL201 + Idelalisib bei follikulärem Lymphom und MCL; Sicherheit/Verträglichkeit primärer Endpunkt |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Beendet | 66 | Entospletinib + Idelalisib bei rezidiviertem/refraktärem hämatologischen Malignomen inkl. MCL |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Beendet | 203 | Tirabrutinib kombiniert mit zielgerichteten Krebstherapien (inkl. Idelalisib) bei B-Zell-Malignomen inkl. MCL |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Beendet | 16 | Idelalisib als postalloge HSZT-Erhaltungstherapie bei B-Zell-Malignomen |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Abgeschlossen | 121 | Reale-Welt-PK/Toxizitäts-Korrelation von Ibrutinib und Idelalisib bei hämatologischen Malignomen inkl. MCL |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unbekannt | 464 | Lebensqualität bei Lymphom-Patienten unter oralen Therapien, einschließlich Idelalisib für MCL |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Abgeschlossen | 803 | Pirtobrutinib bei CLL/SLL und NHL — Idelalisib erscheint nur als Hintergrund/Vorbehandlung, nicht als Studienarzneistoff |

---

## Evidenz aus Literatur

| PMID | Jahr | Typ | Journal | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Kohorte | Cancer Discovery | Idelalisib zeigte messbare Einzelwirkstoff-Aktivität bei stark vorbehandelten Patienten mit rezidiviertem/refraktärem MCL |
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase-1-Klinische Studie | Blood | 48-Wochen-Phase-1-Studie von Idelalisib (50–350 mg) bei 40 Patienten mit rezidiviertem/refraktärem MCL; berichtete ORR, PFS, DOR |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Präklinisch | Clin Cancer Res | Idelalisib beeinträchtigt translationsregulierende Mechanismen zur Unterdrückung von MCL-Zellwachstum |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Präklinisch | Acta Pharmacol Sin | P300/CBP-Inhibitor A-485 überwindet intrinsische Idelalisib-Resistenz in MCL-Zellen in vitro/in vivo |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Präklinisch | Phytomedicine | CBX5-Verlust treibt PI3Kδ-Inhibitor-Resistenz in MCL an; Propolis stellt Idelalisib-Sensitivität via Ferroptose wieder her |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Präklinisch | Cancer Letters | Idelalisib verstärkt antitumorale Wirkung von CDK4/6-Inhibitor Palbociclib via PLK1 bei rezidiviertem/refraktärem MCL und DLBCL |
| [28295729](https://pubmed.ncbi.nlm.nih.gov/28295729/) | 2017 | Übersicht | J Intern Med | Überblick über BCR-Weg-gerichtete Wirkstoffe; vermerkt etablierte Rolle von Idelalisib bei CLL und MCL |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Übersicht | Br J Haematol | Überblick über aktuelle und neue Wirkstoffe (inkl. PI3K-Weg-Inhibitoren) für MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Übersicht | Expert Opin Pharmacother | Übersicht über Behandlungsoptionen für MCL, einschließlich zielgerichteter BCR-Weg-Wirkstoffe |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | Übersicht | Curr Treat Options Oncol | Aktuelle und neu entstehende Therapien bei MCL |

---

## Marktinformation Deutschland

Im Evidenz-Paket sind keine Marketingzulassungen aufgeführt (`total_licenses: 0`, `market_status: Not marketed`). Dies spiegelt höchstwahrscheinlich eine unvollständige Datenabfrage statt echte Abwesenheit vom Markt wider, da Idelalisib (Markenname Zydelig®) extern als EMA-zugelassen für CLL und rezidiviertes follikuläres Lymphom dokumentiert ist — eine Diskrepanz, auf die dieses Evidenz-Paket selbst in der Begründung für die Vorhersage „B-Zell-Neoplasma" hinweist. **Dieses Regulierungs-Status-Feld sollte unabhängig überprüft werden (siehe DG001), bevor eine abschließende Go/No-Go-Entscheidung getroffen wird.**

---

## Zytotoxizität

Idelalisib ist ein Antineoplastikum (zugelassene Onkologie-Indikation; Kinase-Inhibitor-Klasse), daher gilt dieser Abschnitt.

| Element | Inhalt |
|------|------|
| Zytotoxizitäts-Klassifizierung | Zielgerichtete Therapie (PI3Kδ-selektiver kleiner-Molekül-Kinase-Inhibitor; nicht-zytotoxischer Mechanismus) |
| Myelosuppressionsrisiko | Nicht quantifizierbar aus diesem Evidenz-Paket (Sicherheitsdaten gekennzeichnet als Datenlücke). Literatur in diesem Paket verweist auf Neutropenie- und Zytopenie-Überwachung bei Idelalisib-behandelten Patienten — bitte Packungsbeilage konsultieren |
| Emetogenitäts-Klassifizierung | Bitte Packungsbeilage Warnhinweise und Vorsichtsmaßnahmen konsultieren |
| Überwachungselemente | Bitte Packungsbeilage Warnhinweise und Vorsichtsmaßnahmen konsultieren |
| Handhabungsschutz | Bitte Packungsbeilage Warnhinweise und Vorsichtsmaßnahmen konsultieren |

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Packungsbeilage für Sicherheitsinformationen. Alle strukturierten Sicherheitsfelder in diesem Evidenz-Paket (`key_warnings`, `contraindications`, `ddi`) sind als Datenlücken gekennzeichnet, und dies wird als **Blocking**-Lücke (DG001) gekennzeichnet, die den Eintritt in die S1-Sicherheits-Vor-Bewertungsphase verhindert.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Evidenz spezifisch für Idelalisib bei MCL ist derzeit auf abgeschlossene Phase-1-Studien und präklinische mechanistische Studien beschränkt (Evidenzstufe L3, Entscheidungsphase S2, TxGNN's eigene Empfehlung ist „Research Question"), ohne abgeschlossene Phase-2/3-bestätigende Studie für diese Indikation. Kombiniert mit einer **Blocking**-Datenlücke in TFDA/Etikett-Sicherheitsinformationen (DG001), kann eine vollständige Sicherheits- und Wirksamkeitsbewertung derzeit nicht abgeschlossen werden.

**Um fortzufahren, ist folgendes erforderlich:**
- Beschaffung und Parsing des offiziellen Produktetiketts (TFDA/EMA) zur Behebung von DG001 und Ermöglichung der S1-Sicherheitsüberprüfung
- Bestätigung der Wirkmechanismus-Dokumentation via DrugBank zur Behebung von DG002
- Unabhängige Überprüfung des wahren deutschen/taiwanesischen Marktierungs- und Zulassungsstatus (derzeitiges „nicht im Handel / 0 Zulassungen" erscheint inkonsistent mit Idelalisib's bekannter globaler Zulassungsgeschichte)
- Überwachung auf Initiierung einer dedizierten Phase-2/3-Studie bei rezidiviertem/refraktärem MCL
- Etablierung eines Sicherheitsüberwachungsplans, der bekannte Klasseneffekt-Toxizitäten von PI3Kδ-Inhibitoren adressiert (Hepatotoxizität, Kolitis/Diarrhöe, Pneumonitis, opportunistische Infektionen) nach Verfügbarkeit von Etiketten-Daten

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

