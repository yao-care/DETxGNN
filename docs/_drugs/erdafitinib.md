---
layout: default
title: Erdafitinib
parent: Nur Modellvorhersage (L5)
nav_order: 153
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Erdafitinib: Von unspezifischer ursprünglicher Indikation zur Pulmonalen Hypertonie

## Zusammenfassung in einem Satz

> Erdafitinib ist ein Pan-FGFR-(FGFR1-4-)Kinase-Inhibitor; seine ursprüngliche zugelassene Indikation ist jedoch nicht im aktuellen Evidence Pack erfasst (Datenlücke).
> Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **Pulmonale Hypertonie** ist,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt – es handelt sich um eine reine Modell-Ebenen-Hypothese.

---

## Schnellübersicht

| Punkt | Inhalt |
|---|---|
| Ursprüngliche Indikation | Nicht verfügbar – keine ursprünglichen Indikationen im Evidence Pack erfasst (siehe DG001/DG002) |
| Vorhergesagte neue Indikation | Pulmonale Hypertonie |
| TxGNN-Vorhersage-Score | 99.38% |
| Evidence Level | L5 (reine Modellvorhersage, keine Studien oder Literatur) |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellung |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind strukturierte Wirkmechanismus-Daten für Erdafitinib nicht verfügbar (`original_moa`: Datenlücke), und es sind keine ursprünglichen Indikationen im Evidence Pack erfasst. Basierend auf der mechanistischen Rationale, die der TxGNN-Vorhersage beiliegt, wird Erdafitinib als **Pan-FGFR-(FGFR1-4-)Inhibitor** verstanden. FGF2/FGFR1-Signalisierung spielt eine bekannte Rolle bei der Proliferation glatter Muskelzellen der Lungengefäße und bei der vaskulären Remodellierung, was die biologische Grundlage bildet, auf die sich das Modell bei der Verknüpfung von Erdafitinib mit Pulmonaler Hypertonie stützt.

Diese Verknüpfung wird jedoch durch die Quellrationale selbst ausdrücklich als aus **ausschließlich mechanistischen Überlegungen auf in-vitro- und Tiermodell-Ebene** abgeleitet gekennzeichnet – es gibt keine klinische Studie, keine Beobachtungsstudie und keine veröffentlichten Fallberichte, die Erdafitinib mit Pulmonaler Hypertonie beim Menschen verbinden. Der hohe TxGNN-Score spiegelt eine starke Embedding-Space-Ähnlichkeit im Wissensgraph des Modells wider, nicht validierte pharmakologische Evidenz.

Ohne bestätigte Daten zu Erdafitinib's ursprünglichen zugelassenen Indikationen ist es zudem nicht möglich, die mechanistische Kontinuität zwischen der ursprünglichen und der vorhergesagten Verwendung zu bewerten – dies bleibt eine echte Datenlücke, anstatt einer gestützten Hypothese.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen für Deutschland

Erdafitinib hält derzeit **keine Marktgenehmigung** in dieser Rechtsordnung (`market_status`: Nicht vermarktet, `total_licenses`: 0). Es sind keine Produkt-/Lizenzeinträge verfügbar, die zusammengefasst werden könnten.

---

## Sicherheitsaspekte

Keine strukturierten Sicherheitsdaten (wichtige Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungen) sind derzeit für Erdafitinib in diesem Evidence Pack verfügbar, und die entsprechenden lokalen Verschreibungsinformationen konnten nicht beschafft werden (DG001, blockierendem Schweregrad). Da das Arzneimittel noch nicht in dieser Rechtsordnung vermarktet wird, sollte die Sicherheitsbewertung auf international veröffentlichte Verschreibungsinformationen (z. B. FDA-Etikett) gestützt werden, bis die Bestätigung lokaler Regulierungsdaten erfolgt ist.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Die vorhergesagte Indikation (Pulmonale Hypertonie) wird ausschließlich durch theoretische mechanistische Überlegungen gestützt, mit null klinischen Studien und null Literatur – dies ist eine L5, S0-stufige Vorhersage. In Kombination mit einer Lücke mit blockierendem Schweregrad bei lokalen Sicherheits-/Etiketten-Daten (DG001) und einer Lücke mit hohem Schweregrad bei MOA-Daten (DG002) kann der Kandidat nicht über das anfängliche Screening hinausgehen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM-Etikettendaten – Packungsbeilage-Warnungen, Kontraindikationen und Wechselwirkungsprofil (behebt DG001)
- Strukturierte MOA- und ursprüngliche Indikations-Referenzdaten (behebt DG002)
- Präklinische (Tiermodell-) oder Beobachtungsevidenz, die Erdafitinib speziell mit der Remodellierung der Lungengefäße/Pulmonaler Hypertonie verknüpft
- DrugBank-Kategorie-/Klassifizierungsdaten zur Bestimmung des antineoplastischen/Zytotoxizitäts-Risikoprofils, das derzeit aus verfügbaren Daten nicht bestimmbar ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

