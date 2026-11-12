---
layout: default
title: Fostamatinib
parent: Nur Modellvorhersage (L5)
nav_order: 202
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Fostamatinib: vorhergesagte neue Indikation Autosomale Thrombozytopenie mit normalen Thrombozyten (Evidenzstufe L5). Ursprüngliche Indikation: Thrombozytopenie"
monitor_inn: "Fostamatinib"
predicted_indications: ["autosomal thrombocytopenia with normal platelets", "non-syndromic esophageal malformation"]
---

# Fostamatinib
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

## Fostamatinib: Autosomale Thrombozytopenie mit normalen Thrombozyten
{: .text-alpha }

## Zusammenfassung

Fostamatinib wurde ursprünglich zur Behandlung der Thrombozytopenie zugelassen. Das TxGNN-Modell sagt voraus, dass es bei **autosomaler Thrombozytopenie mit normalen Thrombozyten** wirksam sein könnte. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; sie beruht ausschließlich auf einer Modellberechnung.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Thrombozytopenie |
| Vorhergesagte neue Indikation | Autosomale Thrombozytopenie mit normalen Thrombozyten |
| TxGNN-Vorhersagewert | 0,9945 |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Fostamatinib ist ein Inhibitor der Spleen-Tyrosinkinase (SYK); sein aktiver Metabolit ist R406. Substanzen dieser Art werden bei immunvermittelter Thrombozytopenie eingesetzt, indem sie den Abbau von Thrombozyten durch Immunzellen hemmen. Detaillierte Daten zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten nicht vor.

Die hohe Modellbewertung stammt vom TxGNN-Modell (Deep Learning) und spiegelt vermutlich vor allem Ähnlichkeiten wider, die das Modell zwischen verwandten Thrombozytopenie-Erkrankungen gelernt hat, nicht biologische Evidenz. Die autosomale Thrombozytopenie mit normalen Thrombozyten scheint eine seltene, erblich bedingte Erkrankung zu sein. Ein Mechanismus, der auf der Hemmung eines immunvermittelten Thrombozytenabbaus beruht, ist hier daher möglicherweise nicht anwendbar. Belege für eine mechanistische Verbindung liegen nicht vor, es handelt sich um eine rein rechnerische Vorhersage.

Als zweite Vorhersage nennt das TxGNN-Modell (Deep Learning) die **nicht-syndromale ösophageale Fehlbildung** (Score 0,9905). Zwischen einer SYK-Hemmung und einer angeborenen strukturellen Entwicklungsstörung der Speiseröhre lässt sich kein plausibler Zusammenhang herleiten. Der Score kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, und ist keine biologische Evidenz; ohne unabhängige biologische Validierung sollte er nicht als therapeutisches Signal gewertet werden. Auch hier gilt: Evidenzstufe L5, Empfehlung Hold.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

<!-- review:begin de-lic-20261106-fostamatinib-1 -->

> **Prüfkorrektur (2026-11-06)**: Ursprünglich stand hier: „Diese Zulassung ist erloschen (Hersteller: Instituto Grifols S.A.).“ Entfernt: Die Aussage, die Zulassungen seien erloschen, widerrufen oder ungültig, stimmte nicht mit den Zulassungsdaten überein (EMA-Daten zu zentral zugelassenen Arzneimitteln, Stand 2026-11-06). In den Daten (EMA-Daten zu zentral zugelassenen Arzneimitteln) sind für dieses Arzneimittel 1 Zulassungen erfasst, davon 1 gültig; die aktuellen Zahlen stehen in der Schnellübersicht und bei den Marktinformationen. Quelle: [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx).

<!-- review:end de-lic-20261106-fostamatinib-1 -->

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005012 | Tavlesse | – | Thrombozytopenie |

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** Im Rahmen der Abfrage wurden 100 Wechselwirkungen identifiziert. Die wichtigsten:

- **Schwerwiegend (Major):** Clarithromycin
- **Moderat:** Rabeprazol, Omeprazol, Dexlansoprazol, Cimetidin, Hydrocortison, Dexamethason, Betamethason, Budesonid, Triamcinolon, Alosetron, Alvimopan, Aprepitant, Dolasetron, Dronabinol, Eliglustat, Empagliflozin, Loperamid, Pioglitazon, Morphin

Weitere Hinweise zur Sicherheit entnehmen Sie bitte der Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der TxGNN-Wert ist sehr hoch, es gibt jedoch weder klinische Studien noch Publikationen, und ein plausibler Wirkmechanismus für die vorhergesagte Indikation ist nicht erkennbar. In Deutschland ist das Arzneimittel derzeit im Verkehr, mit 1 gültigen Zulassung von 1. Die Evidenz beschränkt sich auf eine reine Modellvorhersage (L5).

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Daten zum Wirkmechanismus (MOA) ergänzen, z. B. über DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation des BfArM einholen (derzeit blockierend für die Sicherheitsprüfung)
- Prüfen, ob die Pathophysiologie der autosomalen Thrombozytopenie mit normalen Thrombozyten überhaupt mit einer SYK-Hemmung vereinbar ist
- Präklinische oder mechanistische Studien sowie Literaturrecherche zur vorhergesagten Indikation
- Klärung des Zulassungs- und Verfügbarkeitsstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite: Aussagen, die mit den amtlichen Zulassungsdaten (EMA-Daten zu zentral zugelassenen Arzneimitteln) abgeglichen wurden. Korrekturen beschränken sich auf grundlegende Sachangaben; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-06 | Entfernt: „Diese Zulassung ist erloschen (Hersteller: Instituto Grifols S.A.)“ | Korrigiert | [EMA – Medicines output (European public assessment reports)](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

