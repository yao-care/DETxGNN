---
layout: default
title: Lopinavir
parent: Nur Modellvorhersage (L5)
nav_order: 238
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir: Von HIV-1-Infektion zu Simian Immunodeficiency Virus Infection

## Eine-Satz-Zusammenfassung

> Lopinavir ist ein HIV-1-Proteasehemmstoff, der typischerweise mit Ritonavir kombiniert wird zur antiretroviralen Therapie der HIV-1-Infektion.
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **Simian Immunodeficiency Virus Infection** sein könnte,
> derzeit wird dies nur durch **3 präklinische Studien im Tiermodell** gestützt, **ohne klinische Studien**, und die „Indikation" ist grundsätzlich eine Infektion in Primaten und keine menschliche Krankheit.

---

## Schnellübersicht

| Punkt | Inhalt |
|-------|--------|
| Ursprüngliche Indikation | HIV-1-Infektion (basierend auf Wirkmechanismus-Inferenz-Text in Evidenzpaket; formale MOA-Daten fehlen) |
| Vorhergesagte neue Indikation | Simian Immunodeficiency Virus Infection |
| TxGNN-Vorhersage-Score | 99,90% |
| Evidenzgrad | L4 (präklinische Tierstudien) |
| Marktstatus in Taiwan | Not marketed |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage sinnvoll?

Die formalen Wirkmechanismus-Daten (MOA) sind derzeit noch nicht vollständig (Datenlücke). Basierend auf dem Wirkmechanismus-Inferenztext im Evidenzpaket ist Lopinavir ein **HIV-1-Proteasehemmstoff**, dessen ursprüngliche Verwendung die HIV-1-Protease hemmt, um die virale Reifung und Replikation zu blockieren, typischerweise kombiniert mit Ritonavir (Lopinavir/Ritonavir-Fixkombination) zur Behandlung der menschlichen HIV-1-Infektion.

SIV (Simian Immunodeficiency Virus) gehört wie HIV zur Gattung der Lentiviren bei Primaten (Lentivirus). Beide haben hochgradig homologe Proteasestrukturen und -funktionen. Theoretisch könnte Lopinavir daher auch gegen die SIV-Protease inhibitorische Aktivität zeigen. Dies ist die biologische Grundlage dieser Vorhersage.

Allerdings ist besonders hervorzuheben: Die Studiendesigns der 3 vorhandenen Arbeiten verwenden SIV/SHIV-infizierte Makaken meistens **als präklinisches Tiermodell zum Testen der Wirksamkeit von HIV-Proteasehemmern**, nicht als Entwicklung einer unabhängigen Arzneimittel-Indikation zur „Behandlung von SIV-Infektionen bei Affen". Mit anderen Worten: Die Assoziation, die TxGNN erfasst, könnte einfach widerspiegeln, dass „dieses Arzneimittel häufig in diesem Tiermodell zum Testen verwendet wird", anstatt eine echte neue menschliche Indikation zu sein. Dieser Punkt sollte bei der späteren Bewertung besonders beachtet werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine relevanten registrierten klinischen Studien verfügbar.

---

## Literaturbeweise

| PMID | Jahr | Studientyp | Fachzeitschrift | Wichtigste Erkenntnisse |
|------|------|-----------|-----------------|------------------------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Präklinische Tierstudie | Journal of Virology | 4 mit SIVmac251 infizierte Makaken erhielten eine vierfach kombinierte antivirale Therapie. Schnelle Viruslastabnahme wurde beobachtet und als Vergleichsgrundlage für die Erstellung eines mathematischen Modells der HIV-1-Virodynamik verwendet. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Präklinische Tierstudie | Microbes and Infection | Konstruktion eines neuen SHIV-pr-Virusstamms mit HIV-1-Proteasegen als Werkzeug zum In-vivo-Testen der Wirksamkeit von Proteasehemmern |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Präklinische Tierstudie | Journal of Virological Methods | Chronisch mit SHIV(89.6P) infizierte Makaken erhielten 28 Tage lang orale AZT+3TC+Lopinavir/Ritonavir-Therapie; Auswirkungen auf CD8-Subgruppen wurden bewertet |

---

## Arzneimittelzulassungsinformationen Taiwan

Lopinavir hat derzeit in Taiwan **keine Arzneimittelzulassung erhalten** (Anzahl der Zulassungen: 0), daher können keine Produktnamen, Darreichungsformen und zugelassenen Indikationen bereitgestellt werden.

---

## Sicherheitsaspekte

Bitte konsultieren Sie die Fachinformation für Sicherheitsinformationen.

> Zusätzliche Anmerkung: Diese Bewertung ergab eine **Datenlücke auf Blocking-Ebene** – die Warnung/Kontraindikation-Daten aus der BfArM-Fachinformation wurden noch nicht beschafft, weshalb dieser Fall **nicht zur S1-Sicherheitsscreening-Phase übergehen kann**. Bevor diese Lücke geschlossen ist, werden keine klinischen oder regulatorischen Folgemaßnahmen empfohlen.

---

## Weitere sekundäre Vorhersagen (niedrigeres Vertrauen, nur zur Information)

In der gleichen Vorhersage-Serie gibt es zwei weitere Kandidaten mit ähnlichem Ranking, aber extrem niedriger Evidenzstärke, beide werden als Hold empfohlen:

| Rang | Vorhergesagte Indikation | TxGNN-Score | Evidenzgrad | Erklärung |
|------|-------------------------|------------|------------|-----------|
| 2 | Feline acquired immunodeficiency syndrome | 99,90% | L5 | FIV-Protease hat begrenzte Homologie zu HIV-1, keine Literatur- oder Studienbelege, fehlende biologische Wirkmechanismus-Unterstützung |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (seltene genetische neurodevelopmentale Erkrankung) | 99,90% | L5 | Keine bekannte biologische Assoziation zum HIV-Proteasehemmungs-Wirkmechanismus, stark verdächtig auf Modell-Rauschen (false positive) |

---

## Schlussfolgerung und nächste Schritte

**Empfehlung: Hold**

**Begründung:**
- Verfügbare Evidenz beschränkt sich auf präklinische Tiermodelle, und die meisten Studien zielen darauf ab, die Wirksamkeit zu testen, nicht auf die Entwicklung einer unabhängigen Indikation für SIV-Infektion. SIV/FIV-Infektionen sind grundsätzlich Tierkrankheiten mit begrenztem klinischem Wert für Menschen.
- Sicherheitsdaten zeigen eine **Blocking-Ebene-Datenlücke** (BfArM-Fachinformation Warnung/Kontraindikationen nicht beschafft). Nach Vorschrift kann die S1-Sicherheits-Erstbewertung nicht voranschreiten.

**Für eine Weiterverfolgung erforderlich:**
- Vollständige Warnungen und Kontraindikationen aus der TFDA-Fachinformation, um die Blocking-Lücke der S1-Sicherheits-Erstbewertung zu schließen (DG001)
- Formale Wirkmechanismus-Daten (MOA) für Lopinavir zur Stärkung der Wirkmechanismus-Assoziationsanalyse (DG002)
- Klärung, ob SIV/FIV-Infektion eine entsprechende menschliche klinische Bedeutung hat oder ob diese Vorhersagerichtung als Tierarzneimittel/präklinisches Forschungswerkzeug und nicht als Kandidat für alte Arzneimittel mit neuer Anwendung in der Humanmedizin neu positioniert werden sollte
- Falls eine Verfolgung der humanmedizinischen Indikation gewünscht ist, sind echte klinische Studien erforderlich, nicht nur tierexperimentelle Literatur

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

