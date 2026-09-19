---
layout: default
title: Icatibant
parent: Hohe Evidenz (L1-L2)
nav_order: 191
evidence_level: L1
indication_count: 7
---

# Icatibant
{: .fs-9 }

Evidenzniveau: **L1** | Vorhergesagte Indikationen: **7** 
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

# Icatibant: Von hereditärem Angioödem zu C1-Inhibitor-Mangel

## Zusammenfassung in einem Satz

> Icatibant (vermarktet als Firazyr) ist ein synthetischer Bradykinin-B2-Rezeptor-Antagonist, der zur Behandlung akuter Anfälle von hereditärem Angioödem (HAE) aufgrund von C1-Inhibitor-Mangel etabliert ist.
> Die Top-Vorhersage des TxGNN-Modells — **C1-Inhibitor-Mangel** — ist keine echte neue Indikation, sondern beschreibt im Wesentlichen die Krankheit, die icatibant bereits behandelt; das Modell hat die bekannte Anwendung des Arzneistoffs korrekt neu identifiziert, anstatt eine neuartige Umwidmungsmöglichkeit aufzudecken.
> Diese höchste bewertete „Vorhersage" wird durch **23 klinische Studien** (viele abgeschlossene Phase-3-RCTs) und **20 Publikationen** gestützt, doch dies spiegelt bestehende, gut etablierte Evidenz wider, nicht neue Erkenntnisse. Sechs niedriger bewertete Vorhersagen (Serpinopathie, Pseudo-von-Willebrand-Erkrankung, Thrombozytenstörungen, Immunmyopathien) wurden ebenfalls überprüft und als mechanistisch nicht unterstützt befunden.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | Hereditäres Angioödem (HAE) aufgrund von C1-Inhibitor-Mangel *(aus klinischen Studiendaten hergeleitet; in strukturierten behördlichen Daten nicht erfasst — Datenlücke)* |
| Vorhergesagte neue Indikation | C1-Inhibitor-Mangel *(im Wesentlichen die gleiche Krankheit wie die oben etablierte Indikation — siehe Caveat unten)* |
| TxGNN-Vorhersage-Score | 99,99 % |
| Evidenzgrad | L1 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Daten zum Wirkmechanismus von icatibant nicht über dieses Evidenzpaket in DrugBank verfügbar. Basierend auf Informationen, die in den klinischen Studienunterlagen selbst eingebettet sind (z. B. NCT00097695), wird icatibant als „ein Bradykinin-Antagonist" beschrieben — insbesondere ein selektiver Bradykinin-B2-Rezeptor-Antagonist, der die vasodilatativen und permeabilitätssteigernden Wirkungen von überschüssigem Bradykinin blockiert, dem Mediator, der für Angioödem-Anfälle bei Patienten mit C1-Inhibitor-Mangel verantwortlich ist.

**Wichtiger Hinweis:** Die höchste bewertete TxGNN-Vorhersage, „C1-Inhibitor-Mangel", ist keine eigenständige neue Indikation — sie ist die zugrunde liegende Krankheitskategorie für hereditäres Angioödem, das icatibant bereits als seine primäre zugelassene Verwendung weltweit behandelt (z. B. unter dem Markennamen Firazyr). Die überwältigende Anzahl von klinischen Studien und Literaturbelegen, die dieser Vorhersage beigefügt sind, bestätigt eine *bestehende*, Jahrzehnte alte Arzneistoff-Krankheits-Beziehung, anstatt einen neuartigen Umwidmungskandidaten zu identifizieren. Dies sollte als **Modellvalidierungssignal** (TxGNN stellt eine bekannte echte positive Erkenntnis korrekt wieder her) interpretiert werden, nicht als geschäftliche Gelegenheit zur Umwidmung.

Im Gegensatz dazu haben die niedriger bewerteten Vorhersagen des Modells (Ränge 2–7: Serpinopathie, Pseudo-von-Willebrand-Erkrankung, primäre Thrombozytensekreetionsstörung, immunvermittelte nekrotisierende Myopathie, Antisynthetase-Syndrom, Glanzmann-Thrombasthenie) keine klinischen Studien oder Literaturbelege, und die eigene mechanistische Begründung des Evidenzpakets für jede dieser Erkrankungen vermerkt ausdrücklich, dass diese wahrscheinlich Wissensgraph-Nähe-Artefakte sind, anstatt biologisch plausible Verbindungen zum Bradykinin-B2-Weg zu sein.

---

## Evidenz aus klinischen Studien

| Studiennummer | Phase | Status | Rekrutierung | Wichtigste Erkenntnisse |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Abgeschlossen | 84 | Pivotale randomisierte, doppelblinde, placebokontrollierte Studie mit SC icatibant für akute kutane/abdominale HAE-Anfälle |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Abgeschlossen | 98 | Randomisierte, doppelblinde, placebokontrollierte Studie (FAST-3), die die Überlegenheit gegenüber Placebos bei akuten HAE-Anfällen bestätigte |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Abgeschlossen | 85 | Randomisierter Vergleich von SC icatibant versus oralem Tranexamsäure bei akuten HAE-Anfällen |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Abgeschlossen | 151 | Offene Studie zur Sicherheit, Verträglichkeit und Wirksamkeit von selbstverabreichtem SC icatibant |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Abgeschlossen | 8 | Offene Studie zu Wirksamkeit/PK/Sicherheit von icatibant bei japanischen HAE-Patienten Typ I/II |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Abgeschlossen | 32 | PK, Verträglichkeit und Sicherheit einer einzelnen SC icatibant-Dosis bei pädiatrischen/adoleszenten HAE-Patienten |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Abgeschlossen | 2 | Sicherheit, Wirksamkeit und PK von icatibant bei japanischen pädiatrischen/adoleszenten HAE-Patienten |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Abgeschlossen | 1761 | Icatibant Outcome Survey (IOS) — großes prospektives Real-World-Register in zugelassenen Ländern |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Abgeschlossen | 5 | Real-World-Sicherheit/Wirksamkeit von icatibant für bradykinin-induziertes Angioödem (breiter als klassisches HAE) |
| [NCT06346899](https://clinicaltrials.gov/study/NCT06346899) | N/A | Abgeschlossen | 115 | Real-World-Beobachtungsstudie von Lanadelumab und icatibant bei chinesischen HAE-Patienten |

---

## Literaturevidenz

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|-----|------|------|---------|
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Übersicht | J Investig Allergol Clin Immunol | Umfassender Überblick über aktuelle und aufkommende Therapien für C1-INH-HAE, einschließlich icatibant |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Übersicht | J Allergy Clin Immunol | Krankheitslast von HAE aufgrund von C1-Inhibitor-Mangel in der Asien-Pazifik-Region |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Übersicht | Curr Opin Allergy Clin Immunol | Diagnostisches und therapeutisches Management von C1-INH-HAE — italienische klinische Erfahrung |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Übersicht | Expert Rev Clin Immunol | Wirksamkeit und Sicherheit von icatibant bei Jugendlichen und Kindern über 2 Jahren mit C1-INH-HAE |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Beobachtungsstudie | Allergy Asthma Clin Immunol | Real-World-Icatibant-Ergebnisse bei spanischen HAE-Patienten aus dem IOS-Register |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registeranalyse | Clin Exp Allergy | Icatibant- und C1-Inhibitor-Verwendung bei Behandlung von laryngealen HAE-Anfällen |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Beobachtungsstudie | Allergy | Real-World-Verwendung von icatibant bei erworbenem (nicht hereditärem) C1-Inhibitor-Mangel |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospektive Studie | J Clin Pharmacol | Hohe Rate der Off-Label-Verwendung von icatibant/C1-INH bei nicht-HAE-Bradykinin-vermitteltem Angioödem |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Fallserie | J Clin Immunol | Behandlung von HAE-Anfällen mit icatibant und rekombinantem C1-Inhibitor während der Schwangerschaft |
| [20496014](https://pubmed.ncbi.nlm.nih.gov/20496014/) | 2010 | Übersicht | Intern Emerg Med | Klassischer Überblick über Angioödem aufgrund von C1-Inhibitor-Mangel und Behandlungsansätze |

---

## Marktinformationen Deutschland

Derzeit sind für icatibant in diesem Markt keine Marketingzulassungen registriert (`taiwan_regulatory.market_status` = Nicht vermarktet / Not Marketed; `total_licenses` = 0).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Wichtigste Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind derzeit nicht im Quellenregister verfügbar (gekennzeichnet als eine **blockierende** Datenlücke — TFDA/BfArM-Etikett-Warnungen und Kontraindikationen müssen vor dieser Kandidatenbetrachtung beschafft werden, bevor dieser in die S1-Sicherheitsbewertung übergehen kann).

---

## Zusätzliche TxGNN-Vorhersagen (niedrige Konfidenz, nicht empfohlen)

Das Evidenzpaket untersuchte auch sechs niedriger bewertete Vorhersagen für icatibant. Alle wurden als **L5 / Zurückhalten** bewertet — keine klinischen Studien, keine Literatur, und nur schwache oder fehlende mechanistische Plausibilität im Vergleich zu icatibants Bradykinin-B2-Antagonisten-Pharmakologie:

| Rang | Krankheit | Score | Bewertung |
|------|---------|-------|---------|
| 2 | Serpinopathie mit toxischer Serpin-Polymerisierung | 99,99 % | Nur indirekte Graphverbindung (SERPING1-Familie); B2-Antagonismus beeinflusst keine Serpin-Fehlfaltung |
| 3 | Pseudo-von-Willebrand-Erkrankung | 99,21 % | Keine bekannte mechanistische Überlappung mit dem Bradykinin-Weg |
| 4 | Primäre Thrombozytensekreetionsstörung | 99,14 % | Keine bekannte biologische Verbindung |
| 5 | Immunvermittelte nekrotisierende Myopathie | 99,06 % | Komplement-/immungesteuert; keine Überlappung mit B2-Antagonismus |
| 6 | Antisynthetase-Syndrom | 99,02 % | Autoantikörper-gesteuert; keine bekannte Kinin-System-Verbindung |
| 7 | Glanzmann-Thrombasthenie | 99,00 % | Angeborener GPIIb/IIIa-Defekt; nicht verwandter Weg |

Diese sollten nicht ohne neue mechanistische oder präklinische Evidenz weiter verfolgt werden.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die am höchsten bewertete Indikation (C1-Inhibitor-Mangel) ist keine neuartige Umwidmungsmöglichkeit — sie ist die bereits etablierte Verwendung des Arzneistoffs, daher stellt sie keinen neuen kommerziellen oder klinischen Wert dar. In Kombination mit der Abwesenheit des Arzneistoffs in diesem Markt (0 Zulassungen) und einer **blockierenden** Datenlücke bei TFDA/BfArM-Etikett-Warnungen und Kontraindikationen kann der Kandidat unabhängig von seiner Wirksamkeitsevidenz nicht in eine Sicherheitsbewertungsphase übergehen.

**Um fortzufahren, wird Folgendes benötigt:**
- Beschaffung der offiziellen Produktkennzeichnung (Warnungen, Kontraindikationen) von TFDA/BfArM, um die blockierende Sicherheitsdatenlücke zu schließen
- Abruf von DrugBank-MOA-Daten zur formalen Dokumentation des Bradykinin-B2-Antagonisten-Mechanismus
- Neuausrichtung der Umwidmungssuche: Da die Rang-1-Vorhersage die bekannte Indikation dupliziert, sollte auf tiefere Untersuchung von Off-Label-Evidenz Priorität gelegt werden (z. B. ACE-Hemmer-induziertes Angioödem, erworbener C1-INH-Mangel — beide bereits im Literaturbestand vertreten) als authentischere Umwidmungskandidaten als die oben aufgeführten sechs Vorhersagen mit niedriger Konfidenz aus dem Graphen
- Falls Markteintritt (nicht Umwidmung) das tatsächliche Ziel ist, Einleitung der Standardregistrierungsdossier-Einreichung für die bestehende HAE-Indikation

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

