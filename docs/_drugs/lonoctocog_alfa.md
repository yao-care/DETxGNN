---
layout: default
title: Lonoctocog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 276
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Lonoctocog Alfa: vorhergesagte neue Indikation Pseudo-von-Willebrand-Erkrankung (Evidenzstufe L5). Ursprüngliche Indikation: Hämophilie A"
monitor_inn: "LONOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome"]
---

# Lonoctocog Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

## Lonoctocog alfa: Von Hämophilie A zu Pseudo-von-Willebrand-Erkrankung
{: .text-alpha }

## Zusammenfassung in einem Satz

Lonoctocog alfa ist ein rekombinanter Einzelketten-Faktor-VIII (mit verkürzter B-Domäne), der ursprünglich zur Behandlung der **Hämophilie A** eingesetzt wurde. Das TxGNN-Modell sagt voraus, dass er bei der **Pseudo-von-Willebrand-Erkrankung** wirksam sein könnte. Dafür liegen bislang **keine klinischen Studien und keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Hämophilie A |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Erkrankung |
| TxGNN-Vorhersagewert | 0,9985 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut ChEMBL (EMBL-EBI) ist für Lonoctocog Alfa folgender Wirkmechanismus erfasst (inoffizielle Übersetzung): „Exogenes Gerinnungsfaktor-VIII-Protein“. Englischer Originalwortlaut: "Coagulation factor VIII exogenous protein" ([ChEMBL CHEMBL4594603 (lonoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594603), CC BY-SA 3.0; abgerufen am 2026-11-19). Bekannt ist: Lonoctocog alfa ist ein rekombinantes Einzelketten-Faktor-VIII-Präparat mit verkürzter B-Domäne und gesteigerter Affinität zum von-Willebrand-Faktor (VWF). Seine Wirksamkeit bei Hämophilie A ist belegt, und mechanistisch könnte es bei Erkrankungen mit gestörter VWF-/Gerinnungsachse von Interesse sein.

Die Pseudo-von-Willebrand-Erkrankung (plättchentypische VWD) wird durch Gain-of-function-Varianten von GP1BA verursacht. Diese erhöhen die Bindung der Thrombozyten an VWF und führen zum Verlust hochmolekularer VWF-Multimere. Ein Faktor-VIII-Konzentrat hat daher eine denkbare, aber unbewiesene Verbindung. Die FVIII-Spiegel sind meist normal oder nur leicht erniedrigt, und der Primärdefekt liegt in den Thrombozyten.

Der hohe TxGNN-Wert ist eine reine Modellvorhersage und wird durch keine klinische oder literaturbasierte Evidenz gestützt.

**Weitere vorhergesagte Indikationen (alle Evidenzgrad L5, Empfehlung Hold):**

| Rang | Erkrankung | TxGNN-Wert | Einschätzung des mechanistischen Zusammenhangs |
|------|------|------|------|
| 2 | Primäre Plättchen-Freisetzungsstörung | 0,9984 | Der Defekt betrifft Granula-Freisetzung bzw. Signalwege, nicht FVIII; allenfalls indirekter Nutzen über die Gerinnungskaskade |
| 3 | Glanzmann-Thrombasthenie | 0,9976 | Defekt des Integrins αIIbβ3; FVIII korrigiert die Aggregationsstörung nicht, Rationale schwach |
| 4 | Scott-Syndrom | 0,9944 | FVIII ist Kofaktor im Tenase-Komplex, ersetzt aber nicht die fehlende Phospholipid-Oberfläche; Nutzen spekulativ |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

<!-- licenses:begin -->

| Zulassungsnummer | Produktname | Wirkstoff(e) | Therapeutisches Gebiet (EMA, englisch) | Status |
|------|------|------|------|------|
| EMEA/H/C/004075 | Afstyla | lonoctocog alfa | Hemophilia A | Gültig |

Quelle: EMA – Medicines output (zentral zugelassene Humanarzneimittel); Produktname, Wirkstoffe und therapeutisches Gebiet im englischen Original. Nationale Zulassungen (BfArM) und Tierarzneimittel sind in diesen Daten nicht enthalten.

<!-- licenses:end -->

Diese Zulassung hat den Status „gültig“; es besteht derzeit 1 gültige Zulassung (von 1).

---

## Sicherheitsaspekte

Bitte entnehmen Sie die Sicherheitsinformationen der Fachinformation. Für Wechselwirkungen wurden in den für diesen Bericht zusammengestellten Daten keine Einträge gefunden.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzgrad L5) ohne Studien oder Publikationen. Der mechanistische Zusammenhang ist bei allen vier vorhergesagten Indikationen schwach bis spekulativ, da der Primärdefekt jeweils thrombozytär ist. Zudem ist das Arzneimittel in Deutschland derzeit im Handel; 1 von 1 Zulassung ist gültig.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen) als Voraussetzung für das Sicherheitsscreening
- Ergänzung der Wirkmechanismus-Daten (z. B. über DrugBank)
- Systematische Literatur- und Studienrecherche zur Pseudo-von-Willebrand-Erkrankung und FVIII-Substitution
- Präklinische oder mechanistische Studien, die einen Nutzen von FVIII bei plättchenbedingten Störungen belegen
- Klärung des Zulassungs- und Verfügbarkeitsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt (überarbeitet am 2026-11-20; frühere Fassung im Protokoll erhalten) | [ChEMBL CHEMBL4594603 (lonoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594603) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

