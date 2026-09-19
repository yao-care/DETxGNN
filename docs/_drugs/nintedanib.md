---
layout: default
title: Nintedanib
parent: Nur Modellvorhersage (L5)
nav_order: 270
evidence_level: L5
indication_count: 3
---

# Nintedanib
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

# Nintedanib: Von einer nicht dokumentierten Ursprungsindikation zur Dermatofibrosarkom Protuberans

## Zusammenfassung in einem Satz

> Die ursprüngliche zugelassene Indikation von Nintedanib ist in diesem Evidenzpaket nicht dokumentiert (Datenlücke).
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam sein könnte gegen **Dermatofibrosarkom Protuberans (DFSP)**,
> wobei derzeit **0 klinische Studien** und **1 unterstützende Publikation** identifiziert wurden — die Evidenz bleibt auf mechanistischer/präklinischer Ebene.

## Schneller Überblick

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar (Datenlücke — keine Aufzeichnungen im Evidenzpaket) |
| Vorhergesagte neue Indikation | Dermatofibrosarkom Protuberans |
| TxGNN-Vorhersage-Score | 99.15% |
| Evidenzlevel | L4 (präklinisch / nur mechanistischer Ebene) |
| Taiwan-Marktstatus | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

## Warum ist diese Vorhersage begründet?

Derzeit sind detaillierte Daten zum Wirkmechanismus von Nintedanib in diesem Evidenzpaket nicht verfügbar (DG002, hoher Schweregrad). Basierend auf dem verfügbaren mechanistischen Ansatz wird Nintedanib als PDGFR-α/β-Inhibitor unter seinen Zielen beschrieben.

DFSP-Tumoren werden durch eine COL1A1-PDGFB-Fusionsmutation angetrieben, die zur konstituktiven PDGFRB-Aktivierung führt. Dies überlappt mechanistisch mit Imatinib, der derzeitigen Standardbehandlung für DFSP. Die PDGFR-inhibitorische Aktivität von Nintedanib bietet eine plausible zielgerichtete Begründung für diese Vorhersage, und der sehr hohe TxGNN-Score (0.9915) spiegelt starke Unterstützung auf Netzwerkebene wider. Die einzige identifizierte unterstützende Literatur (PMID 29408302) ist jedoch eine allgemeine Übersicht über PDGFR-Inhibitoren als Arzneimittelklasse — sie berichtet nicht über Nintedanib-spezifische Daten bei DFSP, und es existieren derzeit keine klinischen Studien für diese Indikation.

Die anderen beiden vorhergesagten Indikationen (Liposarkom, ovarielles myxoides Liposarkom) sind erheblich schwächer: beide sind reine TxGNN-Score-basierte Extrapolationen aus der gleichen PDGFR/FGFR-Pfad-Logik, ohne unterstützende Literatur oder Studien überhaupt (Evidenzlevel L5, Empfehlung „Zurückhalten" für beide), und werden hier nicht weiter diskutiert.

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

## Literatur-Evidenz

| PMID | Jahr | Typ | Journal | Wesentliche Erkenntnisse |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Übersicht | Pharmacological Research | Überprüft die Rolle von Kleinmolekül-PDGFR-Inhibitoren (als Arzneimittelklasse) bei der Behandlung von neoplastischen Erkrankungen; etabliert PDGFR-Signalisierung als therapeutisches Ziel, berichtet aber nicht über Nintedanib-spezifische DFSP-Daten. |

## Taiwan-Marktinformationen

Nintedanib wird derzeit nicht in Taiwan vermarktet (0 Zulassungen in den Aufzeichnungen). Für dieses Evidenzpaket sind keine Lizenz- oder zugelassenen Indikationsdaten verfügbar.

## Sicherheitsüberlegungen

Bitte lesen Sie die Packungsbeilage für Sicherheitsinformationen.

*Hinweis: TFDA-Etiketten-/Warnungsdaten (DG001) sind als eine **blockierende** Datenlücke gekennzeichnet — deren Fehlen verhindert direkt den Eintritt in die S1-Sicherheitsvorbewertungsphase.*

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die DFSP-Vorhersage basiert auf einem plausiblen, aber indirekten mechanistischen Argument (PDGFR-Weg-Überlappung mit Imatinib), das durch eine einzelne Arzneimittelklassen-Übersichtspublikation unterstützt wird, ohne Nintedanib-spezifische Studien oder präklinische Daten, und ohne bestätigte ursprüngliche Indikation oder MOA auf der Akte. Eine blockierende Sicherheitsdatenlücke (TFDA-Etikett nicht verfügbar) verhindert auch eine formale S1-Sicherheitsbewertung.

**Um fortzufahren, ist folgendes erforderlich:**
- TFDA-/Packungsbeilage-Daten, um die blockierende Datenlücke DG001 zu beheben
- Bestätigte MOA und ursprüngliche zugelassene Indikation(en) für Nintedanib aus DrugBank (DG002)
- Nintedanib-spezifische präklinische (z. B. PDGFRB-Fusionszellinie/Xenotransplantat) oder fallbezogene klinische Daten bei DFSP
- Neubewertung der Liposarkom- und ovariellen myxoiden Liposarkom-Vorhersagen, falls unterstützende Literatur auftaucht (derzeit keine Grundlage zum Fortfahren)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

