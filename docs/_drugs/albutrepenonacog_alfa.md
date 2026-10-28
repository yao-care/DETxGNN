---
layout: default
title: Albutrepenonacog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 22
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Albutrepenonacog Alfa: vorhergesagte neue Indikation Pseudo-von-Willebrand-Erkrankung (Evidenzstufe L5). Ursprüngliche Indikation: Hämophilie B"
monitor_inn: "ALBUTREPENONACOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
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

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Albutrepenonacog alfa: Von Hämophilie B zu Pseudo-von-Willebrand-Erkrankung
{: .text-alpha }

## Zusammenfassung in einem Satz

Albutrepenonacog alfa ist ein rekombinanter Gerinnungsfaktor IX, der an Albumin fusioniert ist, und wurde ursprünglich zur Behandlung der Hämophilie B eingesetzt.
Das TxGNN-Modell sagt voraus, dass er bei der **Pseudo-von-Willebrand-Erkrankung** wirksam sein könnte, doch dafür gibt es bislang **keine klinischen Studien** und **keine Publikationen**; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie B |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Erkrankung |
| TxGNN-Vorhersagewert | 0,9994 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zur Wirkungsweise liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Albutrepenonacog alfa ist ein rekombinanter Faktor IX mit Albumin-Fusion (rFIX-FP), der die Halbwertszeit bei Hämophilie B verlängert. Seine Wirksamkeit bei Hämophilie B, einem Mangel an Faktor IX, ist belegt.

Die Pseudo-von-Willebrand-Erkrankung (plättchentypische VWD) entsteht durch Gain-of-function-Varianten von GP1BA. Diese verstärken die Bindung der Blutplättchen an den von-Willebrand-Faktor (VWF), was zum Abbau der Plättchen und zum Verlust hochmolekularer VWF-Multimere führt. Eine Faktor-IX-Substitution behebt diesen Defekt des Plättchen-GPIb nicht, daher ist die biologische Verbindung **schwach**.

Der hohe TxGNN-Wert (0,9994) spiegelt wahrscheinlich die Nähe im Netzwerk der Gerinnungs- und Blutungserkrankungen wider und keine echte mechanistische Begründung.

Weitere vom Modell vorhergesagte Indikationen sind ähnlich schlecht begründet:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Mechanistische Einschätzung |
|------|------|------|------|
| 2 | Primäre Plättchen-Freisetzungsstörung | 0,9994 | Defekt der primären Hämostase; Faktor IX wirkt in der sekundären Hämostase |
| 3 | Glanzmann-Thrombasthenie | 0,9992 | Defekt von αIIbβ3; Faktor IX stellt die Plättchenaggregation nicht wieder her |
| 4 | Scott-Syndrom | 0,9963 | Fehlende Phosphatidylserin-Exposition; theoretischer Bezug zum Tenase-Komplex, aber spekulativ |
| 5 | Blutungsneigung durch Kollagenrezeptor-Defekt | 0,9928 | Primärer Plättchenfunktionsdefekt |
| 6 | Hämorrhagische Störung bei konstitutioneller Thrombozytopenie | 0,9926 | Faktor IX erhöht weder Plättchenzahl noch -funktion |

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

Diese Zulassung ist gültig (1 von 1 Zulassungen gültig); das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

Bitte die Fachinformation für Sicherheitsangaben heranziehen. In den zusammengestellten Daten liegen keine Warnhinweise oder Gegenanzeigen vor, und für Arzneimittelwechselwirkungen wurden keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (L5); es gibt weder Studien noch Publikationen, und die mechanistische Verbindung ist schwach, da Faktor IX den Plättchendefekt nicht korrigiert. Zudem ist das Arzneimittel in Deutschland im Handel (1 von 1 Zulassungen gültig), und die Sicherheitsdaten fehlen.

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

