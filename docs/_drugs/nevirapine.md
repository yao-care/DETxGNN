---
layout: default
title: Nevirapine
parent: Nur Modellvorhersage (L5)
nav_order: 268
evidence_level: L5
indication_count: 3
---

# Nevirapine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Nevirapine: Von der HIV-1-Infektion zum erworbenen Immundefizienzsyndrom der Katzen

## Zusammenfassung in einem Satz

> Nevirapine (DB00238) ist ein Nicht-Nukleosid-Reverse-Transkriptase-Inhibitor (NNRTI), dessen etablierte klinische Anwendung die Behandlung der HIV-1-Infektion beim Menschen ist.
> Die Top-Vorhersage des TxGNN-Modells deutet auf das **erworbene Immundefizienzsyndrom der Katzen** – eine tierärztliche Erkrankung bei Katzen, verursacht durch FIV, keine Humanerkrankung –
> derzeit gestützt durch **0 klinische Studien** und nur **1 präklinische/mechanistische Publikation**.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | HIV-1-Infektion (gemäß Literaturbelegen in diesem Paket; nicht bestätigt durch deutsche Zulassungsdaten – Arzneistoff ist nicht im Handel) |
| Vorhergesagte neue Indikation | Erworbenes Immundefizienzsyndrom der Katzen (FIV-Infektion bei Katzen) |
| TxGNN-Vorhersage-Score | 99.85% |
| Evidenzlevel | L4 (einzelne präklinische/In-vitro-mechanistische Studie, keine klinischen Studien) |
| Marktverfügbarkeit in Deutschland | ✗ Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Wartestellung |

---

## Warum ist diese Vorhersage begründet?

Derzeit sind detaillierte Angaben zum Wirkmechanismus von Nevirapine in diesem Evidenzpaket nicht verfügbar (gekennzeichnet als hochgradig schwerwiegende Datenlücke). Basierend auf bekannten Informationen, die in der unterstützenden Literatur referenziert sind, ist Nevirapine ein NNRTI der ersten Generation, der direkt an die HIV-1-Reverse-Transkriptase bindet, und seine Wirksamkeit bei der HIV-1-Infektion ist in der klinischen Praxis gut etabliert.

Die vorhergesagte Indikation, das erworbene Immundefizienzsyndrom der Katzen, wird durch das Feline-Immundefizienzvirus (FIV) verursacht – ein Lentivirus, der strukturell und funktionell dem HIV verwandt ist. Die Begründung für die TxGNN-Vorhersage liegt in der mechanistischen Nähe: Beide Viren sind auf ein Reverse-Transkriptase-Enzym für die Replikation angewiesen, und Forscher haben direkt untersucht, ob HIV-1-spezifische NNRTIs (Nevirapine, Efavirenz, Rilpivirin) die FIV-Reverse-Transkriptase hemmen könnten.

Ein wichtiger Vorbehalt ist jedoch: Es handelt sich um eine **tierärztliche Indikation (Katzen), nicht um eine Humanerkrankung**. NNRTIs sind aufgrund von Unterschieden in der Reverse-Transkriptase-Bindungstasche zwischen Lentivirus-Arten hochspezifisch (eine Limitation, die auch für Nevirapine gegen SIV/HIV-2 in der Rang-2-Vorhersage dieses Pakets dokumentiert ist). Keine Daten in diesem Paket zeigen, dass Nevirapine die FIV-RT in vitro oder in vivo effektiv hemmt – die zitierte Studie untersuchte nur das *Potenzial* von NNRTIs für diesen Zweck. Diese Vorhersage sollte daher eher als schwaches Signal für eine nicht-humane Anwendung als als Kandidat für die Humanmedikation angesehen werden.

---

## Klinische Studienevidenz

Derzeit sind keine damit verbundenen klinischen Studien registriert.

---

## Literaturische Evidenz

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|------|-----|-------------|------------------------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Präklinische / In-vitro-biochemisch-strukturelle Studie | Journal of Veterinary Science | Vergleich von Nevirapine, Efavirenz und Rilpivirin (HIV-NNRTIs) gegen Reverse-Transkriptase des felinen und humanen Immundefizienzvirus zur Beurteilung der möglichen Nützlichkeit von NNRTIs für die Behandlung von FIV-infizierten Katzen; es existiert derzeit keine wirksame FIV-Therapie. |

---

## Marktverfügbarkeit in Deutschland

Nevirapine ist derzeit nicht im Handel in Deutschland; keine Zulassungsunterlagen sind in diesem Evidenzpaket verfügbar.

---

## Sicherheitsaspekte

Bitte siehe Fachinformation für Sicherheitsinformationen.

> Hinweis: TFDA/BfArM-Kennzeichnungswarnungen und Kontraindikationen sind in diesem Evidenzpaket als eine **blockierende** Datenlücke (DG001) erfasst, was bedeutet, dass dieser Kandidat unabhängig von der Wirksamkeitsevidenz noch nicht zur S1-Sicherheits-Vorbewertung übergehen kann.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Wartestellung**

**Begründung:**
Die Top-Vorhersage von TxGNN zielt auf eine tierärztliche Erkrankung (felines AIDS) ab und nicht auf eine Humanindikation, und wird durch nur eine einzelne präklinische/mechanistische Publikation ohne klinische Studien gestützt. Dies wird weiter durch eine blockierende Datenlücke bei TFDA/BfArM-Sicherheitsangaben verstärkt, die eine Sicherheits-Vorbewertung verhindert. Nevirapines weitere TxGNN-Vorhersagen in diesem Paket (Infektion mit dem Simian-Immundefizienzvirus – ein Tierforschungsmodell; und eine seltene Neurentwicklungsstörung ohne Belege überhaupt) sind gleichermaßen nicht umsetzbar für die Humanmedikation, was eine Wartestellung über die gesamte Kandidatengruppe hinweg verstärkt.

**Um fortzufahren, ist das Folgende erforderlich:**
- TFDA/BfArM-Fachinformationsdaten (Warnungen, Kontraindikationen) zur Beseitigung der blockierenden Datenlücke (DG001)
- Bestätigter Wirkmechanismus (MOA) und ursprünglich genehmigte Humanindikation aus DrugBank (DG002)
- Klarstellung der klinischen Relevanz – die aktuelle Top-Vorhersage ist eine nicht-humane/tierärztliche Erkrankung und erfordert eine Neubewertung gegen echte humane Erkrankungsziele
- Falls die FIV-Signalverfolgung nur zu Translationszwecken/tierärztlichen Zwecken angestrebt wird, In-vitro-Wirksamkeitsdaten (IC50/Bindungsaffinität von Nevirapine gegen FIV-Reverse-Transkriptase) über die einzelne explorative Publikation hinaus

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

