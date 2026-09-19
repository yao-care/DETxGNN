---
layout: default
title: Budesonide
parent: Nur Modellvorhersage (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Budesonide: Bewertung der Umwidmung unvollständig — Keine Vorhersagen verfügbar

## Zusammenfassung in einem Satz

Budesonide (DrugBank: DB01222) ist ein synthetisches Glukokortikoid mit etablierten entzündungshemmenden Eigenschaften.
Dieses Evidence Pack enthält **keine von TxGNN vorhergesagten neuen Indikationen**, und zwei kritische Datenpunkte — Wirkmechanismus und Sicherheitsdaten aus der TFDA-Packungsbeilage — wurden nicht erfolgreich extrahiert.
Eine vollständige Bewertung der Umwidmung kann nicht fortgesetzt werden, bis diese Lücken behoben sind.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|---------|
| Original-Indikation | Im Evidence Pack nicht verfügbar |
| Vorhergesagte neue Indikation | Keine — TxGNN-Vorhersagen nicht geladen |
| TxGNN-Vorhersageergebnis | N/A |
| Evidenzgrad | N/A |
| Taiwan-Marktstatus | Nicht vermarktet (0 TFDA-Genehmigungen gefunden) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Ausstehend** |

---

## Warum die Bewertung nicht fortgesetzt werden kann

Drei strukturelle Probleme verhindern, dass dieser Bericht in Standardformat abgeschlossen werden kann:

**1. Keine vorhergesagten Indikationen**
Das Feld `predicted_indications` ist leer. TxGNN hat keine Kandidaten-Indikationen für Budesonide in diesem Evidence Pack zurückgegeben. Ohne eine Umwidmungs-Hypothese gibt es keine klinischen Studiendaten zu erfassen, keine mechanistische Brücke zu erklären und kein Nutzen-Risiko-Verhältnis zu bewerten.

**2. Wirkmechanismus nicht verfügbar (DG002 — Hoher Schweregrad)**
DrugBank wurde erfolgreich abgefragt und gab einen Datensatz zurück, aber MOA-Daten wurden nicht in das Paket extrahiert. Ohne MOA kann die mechanistische Plausibilität für keine zukünftige vorhergesagte Indikation bewertet werden.

**3. TFDA-Sicherheitsdaten fehlen (DG001 — Blockierender Schweregrad)**
Die Abfrage der TFDA-Packungsbeilage gab ein Ergebnis zurück, aber Warnhinweise und Kontraindikationen wurden nicht in die Sicherheitsfelder geparst. Dies wird als blockierend klassifiziert — der Sicherheits-Vor-Screening-Schritt ist formal unvollständig, und kein Kandidat kann unter diesem Status zur Bewertung der klinischen Machbarkeit voranschreiten.

> **Hinweis zur Datenqualität:** Das Abfrageprotokoll zeigt sowohl die DrugBank-Abfrage (ID 3) als auch die TFDA-Packungsbeilage-Abfrage (ID 4) als `success` mit `result_count: 1`. Die Datenlücken spiegeln daher einen Extraktions- oder Parsingfehler wider, nicht ein Verfügbarkeitsproblem der Quelle. Das Wiederausführen der Extraktions-Pipeline sollte diese Informationen wiederherstellen, ohne dass die Quellen neu abgefragt werden müssen.

---

## Sicherheitserwägungen

Sicherheitsinformationen entnehmen Sie bitte der Packungsbeilage.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Ausstehend**

**Begründung:**
Keine TxGNN-Umwidmungsvorhersagen sind in diesem Evidence Pack vorhanden. Selbst wenn Vorhersagen hinzugefügt würden, würden zwei blockierende/hochgradig schwerwiegende Datenlücken — fehlende Sicherheitsextraktionen und fehlende MOA — verhindern, dass die Bewertung die obligatorischen Vor-Screening-Kontrollpunkte passiert.

**Zum Fortfahren wird Folgendes benötigt:**

- **Extraktions-Pipeline erneut ausführen** für den bereits abgerufenen DrugBank-Datensatz und das TFDA-Packungsbeilage-PDF, um MOA- und Sicherheitsfelder auszufüllen — die Quelldokumente sind als verfügbar bestätigt

- **TxGNN-Vorhersageergebnisse** für Budesonide in das Evidence Pack laden (`predicted_indications` muss ausgefüllt werden, bevor irgendwelche Bewertungsarbeiten beginnen)

- **Taiwan-Marktstatus erneut überprüfen**: Die TFDA-Lizenzierungsabfrage gab 0 Ergebnisse zurück, aber Budesonide hat international vermarktete Markenprodukte (z. B. Rhinocort®, Pulmicort®, Entocort®); eine erneute Abfrage unter Verwendung alternativer Handelsnamen oder ATC-Code R03BA02 / A07EA06 kann vorhandene Genehmigungen ans Licht bringen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

