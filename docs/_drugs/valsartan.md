---
layout: default
title: Valsartan
parent: Mittlere Evidenz (L3-L4)
nav_order: 419
evidence_level: L4
indication_count: 7
---

# Valsartan
{: .fs-9 }

Evidenzniveau: **L4** | Vorhergesagte Indikationen: **7** 
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

# Valsartan: Vom Bluthochdruck zur malignen hypertensiven Nierenkrankheit

## Zusammenfassung in einem Satz

> Valsartan ist ein etablierter Angiotensin-II-Rezeptorblocker (ARB); dieses Evidenzpaket enthält keine strukturierten Daten zu seinen ursprünglichen Indikationen, aber ARBs werden breit für die Behandlung von Bluthochdruck und Herzinsuffizienz verwendet.
> Das TxGNN-Modell sagt voraus, dass es wirksam sein könnte für **Maligne hypertensive Nierenkrankheit**,
> aber derzeit unterstützen nur **0 klinische Studien** und **1 indirekte Publikation** (Untersuchung eines anderen Medikaments, Avosentan) diese spezifische Richtung.

---

## Schneller Überblick

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Nicht verfügbar im Evidenzpaket (Valsartan ist ein ARB der Standardklasse, üblicherweise für Bluthochdruck/Herzinsuffizienz indiziert; es wurden keine strukturierten `original_indications` oder Lizenztexte bereitgestellt) |
| Vorhergesagte neue Indikation | Maligne hypertensive Nierenkrankheit |
| TxGNN-Vorhersagepunktzahl | 99.97% |
| Evidenzgrad | L4 |
| Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Mechanismus-der-Wirkung-Daten für diesen Datensatz nicht verfügbar (`original_moa: [Data Gap]`). Basierend auf der bekannten Pharmakologie ist Valsartan ein Angiotensin-II-Typ-1-(AT1)-Rezeptorblocker, der das Renin-Angiotensin-Aldosteron-System (RAAS) unterdrückt, den glomerulären Kapillardruck senkt und die Proteinurie reduziert — ein Mechanismus, der weit verbreitet mit Nierenschutz bei hypertensiver Nephropathie verbunden ist.

Die maligne Hypertonie mit Nierenbeteiligung ist durch deutlich erhöhte Angiotensin-II-Aktivität und RAAS-getriebene vaskuläre/glomeruläre Schädigung gekennzeichnet, was eine RAAS-Blockade mechanistisch plausibel macht. Allerdings ist maligne Hypertonie ein hypertensiver Notfall, der eine schnelle Blutdrucksenkung erfordert; orale ARBs haben einen langsamen Wirkungseintritt und sind nicht First-Line für die akute Phase, was die direkte Anwendbarkeit begrenzt.

Wichtig ist, dass die einzige Literaturzitierung, die diese Vorhersage unterstützt (PMID 24368192), **Avosentan** untersucht, einen Endothelin-Rezeptorblocker, nicht Valsartan — sie unterstützt nur indirekt das allgemeine Konzept, dass die Blockade von vasoaktiven/pressorischen Wegen gegen hypertensive Nephropathie in einem Tiermodell schützen kann. Es wurden keine Valsartan-spezifischen klinischen oder präklinischen Daten für diese Indikation ermittelt, daher sollte die mechanistische Verbindung eher als eine Klassenhypothese als als substanzspezifische Evidenz betrachtet werden.

*Anmerkung: Dieses Evidenzpaket enthält 7 TxGNN-vorhergesagte Indikationen für Valsartan. Zwei sind auf der Stufe "Forschungsfrage" markiert — diese (Rang 1, L4, hauptsächlich getrieben durch TxGNN-Punktzahl) und "chronische pulmonale Herzerkrankung" (Rang 6, L2, unterstützt durch mehrere abgeschlossene Phase-3/4-RCTs von Sacubitril/Valsartan bei HFrEF mit rechts-ventrikulärer/pulmonaler Komorbitidität). Der Rang-6-Kandidat hat eine wesentlich stärkere klinische Evidenzbasis und könnte eine separate Bewertung rechtfertigen.*

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|------|-----|---------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Präklinisch/Übersicht | Pharmacological Research | Endothelin-Rezeptorblocker (Avosentan) — nicht Valsartan — zeigte Nierenschutz in einem Tiermodell mit hypertensiver Nephropathie (doppelt transgene Ratten, die Renin/Angiotensinogen überexprimieren) bei Dosen, die Flüssigkeitsretention vermieden. Unterstützt das allgemeine RAAS/vasoaktive-Weg-Nephroprotektions-Konzept, liefert aber keine direkten Valsartan-Daten. |

---

## Marktinformation für Deutschland

Valsartan hat derzeit keine registrierte Marktgenehmigung in diesem Datensatz (Marktstatus: **Nicht vermarktet**, 0 Lizenzen).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Anmerkung: Eine Blockierungslücke besteht — Warnungen/Kontraindikationen auf Ebene des TFDA-äquivalenten Produktlabels für Valsartan konnten nicht ermittelt werden (DG001), was derzeit eine formale S1-Sicherheitsbewertung verhindert.)*

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die vorhergesagte Indikation wird nur durch eine TxGNN-Punktzahl mit null klinischen Studien und einem einzigen indirekten, nicht-Valsartan-spezifischen Literaturstück (L4-Evidenz) unterstützt. Zusammen mit dem Status "Nicht vermarktet" des Medikaments und einer Blockierungslücke in Sicherheitsdaten auf Labelebene gibt es derzeit unzureichende Evidenz, um zu diesem Zeitpunkt eine Sicherheitsbewertung einzuleiten.

**Um fortzufahren, ist Folgendes erforderlich:**
- Packungsbeilage / offizielle Sicherheitswarnungen und Kontraindikationen für Valsartan (DG001, Blockierend — erforderlich vor S1-Sicherheitsbewertung)
- Detaillierte Mechanismus-der-Wirkung-Dokumentation (DG002)
- Direkte präklinische oder klinische Evidenz mit Valsartan selbst (nicht Endothelin-Antagonisten) für hypertensive Nephropathie oder maligne Hypertonie
- Erwägen Sie ein separates Evaluierungsgleis für den Kandidaten "chronische pulmonale Herzerkrankung" (Rang 6), der bemerkenswert stärkere Evidenz aufweist (L2, mehrere abgeschlossene Phase-3/4-RCTs von Sacubitril/Valsartan)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

