---
layout: default
title: Vilanterol
parent: Nur Modellvorhersage (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Vilanterol
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

# Vilanterol: Datenlücken-gesteuerte Bestätigung der Verwendung bei obstruktiven Atemwegserkrankungen (COPD/Asthma)

## Zusammenfassung in einem Satz

> Diese Evidenzbasis zeigt keine dokumentierte ursprüngliche Indikation oder keinen bekannten Wirkmechanismus für Vilanterol — beide sind als Datenlücken in der Quelldatenbank gekennzeichnet, und das Arzneimittel ist derzeit nicht auf dem taiwanesischen Markt zugelassen.
> Das TxGNN-Modell prognostiziert die höchste Wahrscheinlichkeit für **obstruktive Atemwegserkrankungen**, und die unterstützenden Beweise — **über 80 klinische Studien (viele haben Phase 3 abgeschlossen) und 20 Veröffentlichungen**, einschließlich der wegweisenden IMPACT- und FULFIL-Studien — zeigen, dass dies kein neues Repurposing-Signal ist, sondern Vilanterols bereits gut etablierte, weltweit zugelassene Rolle als langwirksamer β2-Agonist (LABA) in COPD/Asthma-Kombinationsinhalatoren (z. B. Breo/Relvar Ellipta, Anoro Ellipta, Trelegy Ellipta).
> Dieser Fall sollte als **Datenlücken-Sanierung und Bestätigung** gelesen werden, nicht als Entdeckung einer neuen Indikation.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar — keine genehmigte Indikation dokumentiert (Arzneimittel nicht auf dem taiwanesischen Markt zugelassen; Feld original_indications in den Quelldaten leer) |
| Vorhergesagte neue Indikation | Obstruktive Atemwegserkrankung (COPD / Asthma) |
| TxGNN-Vorhersagepunktzahl | 99,97% |
| Evidenzstufe | L1 (≥2 abgeschlossene Phase-3-RCTs) |
| Status auf dem taiwanesischen Markt | Nicht zugelassen (Nicht zugelassen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Mit Schutzmaßnahmen fortfahren |

---

## Warum ist diese Vorhersage angemessen?

Das strukturierte Feld `original_moa` des Evidenzpakets ist eine Datenlücke, aber die zugrunde liegenden Studien- und Literaturbeweise beschreiben durchweg die Pharmakologie von Vilanterol: Es ist ein selektiver langwirksamer β2-adrenerger Rezeptor-Agonist (LABA), der β2-Rezeptoren auf der Bronchialmuskulatur aktiviert, den intrazellulären cAMP-Spiegel erhöht und eine anhaltende Bronchodilation (~24-Stunden-Dauer) bewirkt. Dies ist eine direkte, mechanismusbasierte pharmakologische Wirkung auf eine Atemwegsverengung — nicht eine spekulative netzwerkgestützte Assoziation.

Entscheidend ist, dass „obstruktive Atemwegserkrankung" keine neue therapeutische Richtung für Vilanterol ist — sie ist die Kern-, bereits zugelassene Indikation des Arzneimittels international, die als Bestandteil von Fixkombinations-Inhalatoren mit Fluticasonfuroat (Breo/Relvar Ellipta), Umeclidinium (Anoro Ellipta) oder beiden (Trelegy Ellipta, Triple-ICS/LAMA/LABA-Therapie) angeboten wird. Die leeren Felder `original_indications` und `original_moa: [Data Gap]` in dieser Evidenzbasis sollten als **Datenbankpopulations-Lücke** verstanden werden, nicht als Beweis, dass das Arzneimittel keine etablierte Indikation hat.

Da der Wirkmechanismus-Erkrankung-Zusammenhang direkt und nicht abgeleitet ist, und da die Evidenzbasis große, hochwertige bestätigende Studien enthält (z. B. die 10,355-Patienten umfassende IMPACT-Studie und die FULFIL-Studie), wird dieser Kandidat mit der höchsten Evidenzstufe (L1) bewertet, trotz der zugrunde liegenden Datenlücken in den Arzneimittel-Metadaten.

---

## Klinische Studienevidenz

| Studiennummer | Phase | Status | Einschreibung | Wichtigste Ergebnisse |
|---------|------|------|------|---------|
| [NCT02164513](https://clinicaltrials.gov/study/NCT02164513) | Phase 3 | Abgeschlossen | 10,355 | IMPACT-Studie — FF/UMEC/VI-Triple-Therapie reduziert die jährliche Exazerbationsrate vs. FF/VI oder UMEC/VI Dual-Therapie bei COPD |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Abgeschlossen | 4,233 | 12-Monats-Wirksamkeit von FF/VI einmal täglich vs. übliche Asthma-Erhaltungstherapie |
| [NCT01313650](https://clinicaltrials.gov/study/NCT01313650) | Phase 3 | Abgeschlossen | 1,538 | Zentrale 24-Wochen-Effektivitäts-/Sicherheitsstudie von UMEC/VI und einzelnen Komponenten vs. Placebo bei COPD |
| [NCT02467452](https://clinicaltrials.gov/study/NCT02467452) | Phase 3 | Abgeschlossen | 1,479 | Nichtunterlegenheit von Triple-pMDI-Therapie vs. FF/VI plus Tiotropium bei COPD |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | Abgeschlossen | 1,055 | Geschlossene Triple-Therapie (FF/UMEC/VI) vs. offene Triple (FF/VI + UMEC) — Lungenfunktionsvergleich bei COPD |
| [NCT03248128](https://clinicaltrials.gov/study/NCT03248128) | Phase 3 | Abgeschlossen | 906 | FF/VI vs. FF allein bei pädiatrischen/jugendlichen Asthma (5–17 Jahre) unkontrolliert auf ICS |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Phase 3 | Abgeschlossen | 717 | UMEC/VI vs. Fluticason/Salmeterol über 12 Wochen bei COPD (Relevanz Grad A) |
| [NCT01817764](https://clinicaltrials.gov/study/NCT01817764) | Phase 3 | Abgeschlossen | 707 | UMEC/VI vs. Fluticason/Salmeterol über 12 Wochen bei COPD (Relevanz Grad A) |
| [NCT05757102](https://clinicaltrials.gov/study/NCT05757102) | Phase 3 | Rekrutierung läuft | 292 | FF/UMEC/VI vs. FF/VI bei Jugendlichen (12–17 Jahre) mit unzureichend kontrolliertem Asthma; Bayessches dynamisches Borrowing-Design |
| [NCT03378648](https://clinicaltrials.gov/study/NCT03378648) | Phase 1/2 | Abgeschlossen | 118 | First-in-human-Sicherheits-/PK/PD-Studie einer bifunktionalen muscarinergen Antagonisten-/β2-Agonisten-Verbindung (MABA) Bronchodilator-Verbindung |

---

## Literaturevidenz

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Ergebnisse |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | NEJM | IMPACT-Studie — Triple-ICS/LAMA/LABA-Therapie vs. Dual-Therapie bei COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (Mortalitätsanalyse) | Am J Respir Crit Care Med | FF/UMEC/VI reduziert signifikant die Gesamtmortalität vs. UMEC/VI bei COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL-Studie — tägliche Triple-Therapie einmal täglich überlegen gegenüber ICS/LABA-Dual-Therapie bei COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT (Phase 3A) | Lancet Respir Med | CAPTAIN-Studie — FF/UMEC/VI vs. FF/VI bei unzureichend kontrolliertem Asthma |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | RCT-Subgruppenanalyse | Eur Respir J | IMPACT-Studie — Auswirkung der Exazerbationsvorgeschichte auf Behandlungsergebnisse |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Netzwerk-Metaanalyse | Adv Ther | FF/UMEC/VI vs. andere COPD-Therapien — comparative Wirksamkeit |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematische Übersicht & Metaanalyse | BMC Pulm Med | UMEC/VI vs. andere Bronchodilatatoren bei COPD-Management |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematische Übersicht | Clin Respir J | Fixdosis-UMEC/VI-Kombination für COPD — systematische Übersicht |
| [30463451](https://pubmed.ncbi.nlm.nih.gov/30463451/) | 2018 | Übersicht | Expert Rev Respir Med | FF/UMEC/VI-Kombinationstherapie für COPD |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Übersicht | Expert Rev Respir Med | Fluticasonfuroat und Vilanterol für COPD-Behandlung |

---

## Informationen zum taiwanesischen Markt

Keine Zulassungen dokumentiert. Vilanterol-haltige Produkte sind derzeit nicht auf dem taiwanesischen Markt zugelassen, entsprechend dieser Evidenzbasis (`total_licenses: 0`, `licenses: []`).

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Dieses Evidenzpaket enthält keine wesentlichen Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungsdaten (alle sind als Datenlücken gekennzeichnet; die DDI-Abfrage gab keine Ergebnisse zurück), und dies ist als blockierende Datenlücke (DG001) aufgezeichnet, die eine formale Sicherheitsvorbewertung verhindert.

---

## Fazit und nächste Schritte

**Entscheidung: Mit Schutzmaßnahmen fortfahren**

**Begründung:**
Der Zusammenhang zwischen Vilanterol und obstruktiver Atemwegserkrankung wird durch L1-Evidenz unterstützt — mehrere abgeschlossene Phase-3-RCTs einschließlich der großangelegten IMPACT- und FULFIL-Studien — und spiegelt einen direkten, etablierten pharmakologischen Wirkmechanismus (LABA-Bronchodilation) wider, keine spekulative Vorhersage. Jedoch fehlen in dieser Evidenzbasis die Arzneimittel-Metadaten (ursprüngliche Indikation, MOA) und alle Sicherheits-/Regulierungsdaten (TFDA-Kennzeichnung, Kontraindikationen, DDI), und das Arzneimittel ist derzeit nicht auf dem taiwanesischen Markt zugelassen, daher kann es noch nicht über das erste Sicherheits-Screening (S1/S3-Gate) hinausgehen.

**Um fortzufahren, ist Folgendes erforderlich:**
- Lösen Sie DG001 (blockierend): Beschaffen Sie TFDA-Kennzeichnungswarnungen/Kontraindikationen, oder bestätigen Sie dies über die ursprüngliche Herstellerkennzeichnung (Breo/Anoro/Trelegy Ellipta), falls Vilanterol als Kombinationsprodukt importiert wird
- Lösen Sie DG002 (Hoch): Ergänzen Sie die MOA- und ursprünglichen Indikationsfelder mithilfe von DrugBank, um die scheinbare „Datenlücke" zu korrigieren, die diesen Kandidaten als neue Vorhersage statt einer bestätigten bestehenden Verwendung erscheinen lässt
- Bestätigen Sie den Regulierungs-/Importstatus in Taiwan für Vilanterol-haltige Kombinationsprodukte
- Klassifizieren Sie diesen Kandidaten intern als **Datenbestätigung**, nicht als Neuentdeckung einer Indikation, um zu vermeiden, dass eine bereits genehmigte globale Indikation fälschlicherweise als Repurposing-Befund präsentiert wird

**Anmerkung zu anderen vorhergesagten Indikationen (Ränge 2–10):** Die verbleibenden Kandidaten in dieser Evidenzbasis (hyperluzente Lunge, interstitiales Emphysem, kompensatorisches Emphysem, Trachealstenose, Tracheale Verkalkung, Laryngotracheitis, kongenitales Lappemphysem, Bronchialneoplasma, Respiratorische Fehlbildung) sind entweder reine TxGNN-Modellpunkte ohne unterstützende klinische Studien- oder Literaturbeweise (L5, Hold), oder zeigen Evidenz-/Thema-Diskrepanzen, bei denen die zugrunde liegenden Studien und Arbeiten generische COPD/Asthma-Studien sind, die sich nicht auf die spezifische vorhergesagte Erkrankung beziehen (wahrscheinlich Ontologie-Label-Mismatch). Keiner dieser Kandidaten ist ohne zusätzliche gezielte Evidenzen zur weiteren Bewertung bereit.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

