---
layout: default
title: Albutrepenonacog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 22
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Albutrepenonacog Alfa: vorhergesagte neue Indikation Pseudo-von-Willebrand-Erkrankung (Evidenzstufe L5). Ursprüngliche Indikation: Hämophilie B"
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog alfa: Von Hämophilie B zu Pseudo-von-Willebrand-Erkrankung

## Zusammenfassung in einem Satz

Albutrepenonacog alfa ist ein rekombinanter Gerinnungsfaktor IX, der an Albumin fusioniert ist, und wurde ursprünglich zur Behandlung der Hämophilie B eingesetzt.
Das TxGNN-Modell sagt voraus, dass er bei der **Pseudo-von-Willebrand-Erkrankung** wirksam sein könnte, doch dafür gibt es bislang **keine klinischen Studien** und **keine Publikationen**; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie B |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Erkrankung |
| TxGNN-Vorhersagewert | 99,94 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zur Wirkungsweise liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Albutrepenonacog alfa ist ein rekombinanter Faktor IX mit Albumin-Fusion (rFIX-FP), der die Halbwertszeit bei Hämophilie B verlängert. Seine Wirksamkeit bei Hämophilie B, einem Mangel an Faktor IX, ist belegt.

Die Pseudo-von-Willebrand-Erkrankung (plättchentypische VWD) entsteht durch Gain-of-function-Varianten von GP1BA. Diese verstärken die Bindung der Blutplättchen an den von-Willebrand-Faktor (VWF), was zum Abbau der Plättchen und zum Verlust hochmolekularer VWF-Multimere führt. Eine Faktor-IX-Substitution behebt diesen Defekt des Plättchen-GPIb nicht, daher ist die biologische Verbindung **schwach**.

Der hohe TxGNN-Wert (0,9994) spiegelt wahrscheinlich die Nähe im Netzwerk der Gerinnungs- und Blutungserkrankungen wider und keine echte mechanistische Begründung.

Weitere vom Modell vorhergesagte Indikationen sind ähnlich schlecht begründet:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Mechanistische Einschätzung |
|------|------|------|------|
| 2 | Primäre Plättchen-Freisetzungsstörung | 99,94 % | Defekt der primären Hämostase; Faktor IX wirkt in der sekundären Hämostase |
| 3 | Glanzmann-Thrombasthenie | 99,92 % | Defekt von αIIbβ3; Faktor IX stellt die Plättchenaggregation nicht wieder her |
| 4 | Scott-Syndrom | 99,63 % | Fehlende Phosphatidylserin-Exposition; theoretischer Bezug zum Tenase-Komplex, aber spekulativ |
| 5 | Blutungsneigung durch Kollagenrezeptor-Defekt | 99,28 % | Primärer Plättchenfunktionsdefekt |
| 6 | Hämorrhagische Störung bei konstitutioneller Thrombozytopenie | 99,26 % | Faktor IX erhöht weder Plättchenzahl noch -funktion |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003955 | Idelvion (CSL Behring GmbH) | – | Hämophilie B |

Diese Zulassung ist als erloschen/zurückgezogen geführt; derzeit gibt es keine gültige Zulassung.

---

## Sicherheitsaspekte

Bitte die Fachinformation für Sicherheitsangaben heranziehen. In den zusammengestellten Daten liegen keine Warnhinweise oder Gegenanzeigen vor, und für Arzneimittelwechselwirkungen wurden keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (L5); es gibt weder Studien noch Publikationen, und die mechanistische Verbindung ist schwach, da Faktor IX den Plättchendefekt nicht korrigiert. Zudem besteht in Deutschland keine gültige Zulassung, und die Sicherheitsdaten fehlen.

**Für einen Fortschritt sind folgende Punkte erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) aus der BfArM-Quelle beschaffen, da dies die Sicherheitsprüfung blockiert
- Daten zum Wirkmechanismus ergänzen (z. B. über DrugBank)
- Präklinische oder mechanistische Belege prüfen, ob Faktor IX bei plättchenbedingten Blutungsstörungen eine Rolle spielen kann
- Klärung des Zulassungsstatus und der Verfügbarkeit in Deutschland
- Abgleich mit bestehenden Standardtherapien (z. B. Plättchentransfusion, rFVIIa, Antifibrinolytika)
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

