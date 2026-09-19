---
layout: default
title: Ramucirumab
parent: Nur Modellvorhersage (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: Bewertung der Arzneistoffrepositionierung — Unzureichende Daten für vollständige Evaluierung

## Zusammenfassung in einem Satz

Ramucirumab ist ein vollständig humaner IgG1-Monoklonalantikörper gegen VEGFR-2 und wurde als Antitumormittel für Magen-/GEJ-Adenokarzinom, NSCLC und kolorektales Karzinom entwickelt.
Das aktuelle Evidence Pack enthält **keine TxGNN-vorhergesagten neuen Indikationen**, und Zulassungsunterlagen für den deutschen Markt wurden nicht abgerufen (0 Genehmigungen in der Datei).
Eine vollständige Repositionierungs-Evaluierung kann zu diesem Zeitpunkt nicht durchgeführt werden; dieser Bericht dokumentiert verfügbare Ergebnisse und die Datenlücken, die behoben werden müssen, bevor die Bewertung fortgesetzt wird.

---

## Schnellübersicht

| Element | Angaben |
|---------|--------|
| Ursprüngliche Indikation | Nicht angegeben im Evidence Pack |
| Vorhergesagte neue Indikation | Keine — TxGNN-Vorhersagen nicht verfügbar |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzgrad | Nicht bewertbar |
| Marktstatus Deutschland | Nicht vermarktet (0 Genehmigungen in der Datei) |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Wirkungsmechanismus

Detaillierte Daten zum Wirkungsmechanismus sind derzeit nicht im Evidence Pack verfügbar. Basierend auf bekannten pharmakologischen Informationen ist Ramucirumab ein vollständig humaner IgG1-Monoklonalantikörper, der selektiv an die extrazelluläre Domäne von VEGFR-2 (Vaskulärer Endothelwachstumsfaktor-Rezeptor 2) bindet, die Bindung von VEGF-A-, VEGF-C- und VEGF-D-Liganden blockiert und ihre nachgelagerten pro-angiogenen Signalisierungskaskaden unterbricht.

Seine Antitumorwirksamkeit bei Magen- und GEJ-Adenokarzinomen wurde in pivotalen Phase-3-Studien etabliert (REGARD, RAINBOW). Durch die Ausrichtung auf Tumorvaskulatur statt auf Krebszellen direkt ist der Mechanismus theoretisch auf jeden soliden Tumor mit signifikanter VEGFR-2-abhängiger Angiogenese anwendbar — eine Begründung, die bereits Zulassungserweiterungen auf NSCLC, kolorektales Karzinom und hepatozelluläres Karzinom in mehreren Jurisdiktionen unterstützt hat.

Sobald TxGNN-Vorhersagedaten verfügbar werden, kann die Mechanismus-Krankheits-Übereinstimmung formal bewertet werden.

---

## Zytotoxizität

| Element | Angaben |
|---------|--------|
| Zytotoxizitäts-Klassifizierung | Gezielte Therapie — Anti-VEGFR-2-Monoklonalantikörper (antiangiogenetisch) |
| Myelosuppressions-Risiko | Niedrig bis moderat (Neutropenie wurde berichtet; erheblich weniger schwerwiegend als konventionelle zytotoxische Chemotherapie) |
| Emetogenitäts-Klassifizierung | Niedrig |
| Überwachungselemente | Blutdruck (Hypertonie ist ein Klasseneffekt von Anti-VEGF-Wirkstoffen), Urinalyse auf Proteinurie, Blutbild mit Differenzial, Leberfunktion, Wundheilungsstatus |
| Handhabungsschutz | Standard-Handhabungsprotokolle für Biologika gelten; nicht als konventioneller zytotoxischer Wirkstoff klassifiziert, der zytotoxische Verschüttungs-Kits oder HEPA-geschützte Zubereitungsbereiche erfordert |

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Dem Evidence Pack fehlen alle drei Voraussetzungen für eine Repositionierungs-Evaluierung — TxGNN-Vorhersage-Ausgabe, Sicherheits-/Kontraindikationsdaten und Zulassungsunterlagen für den deutschen Markt — so dass es unmöglich ist, sowohl therapeutische Chancen als auch Risikoprofil zu diesem Zeitpunkt zu bewerten.

**Um fortzufahren, wird folgendes benötigt:**

- **TxGNN-Vorhersagen** (`predicted_indications`) müssen für Ramucirumab generiert werden, bevor eine Indikationsbewertung durchgeführt werden kann
- **Packungsbeilage-Warnungen und Kontraindikationen** — TFDA-PDF-Analyse wurde erfolgreich protokolliert (Abfrage 4), es wurden jedoch keine Daten zurückgegeben; dieses Problem muss behoben werden
- **Arzneimittelwechselwirkungsdaten** — Die DDI-Abfrage gab `not_found` zurück; eine umfassendere Datenbanksuche (z. B. mit DrugBank, Lexicomp) wird empfohlen
- **Deutschland BfArM/EMA-Genehmigungsprüfung** — Ramucirumab kann eine EMA-Marktgenehmigung besitzen, die in dieser Abfrage nicht erfasst wurde; eine direkte Suche in der EMA-Produktdatenbank wird empfohlen, um den tatsächlichen Marktstatus vor einer Klassifizierung als „nicht vermarktet" zu bestätigen
- **MOA-Daten aus DrugBank** — Die DrugBank-Abfrage gab 1 Ergebnis zurück (Abfrage 3), aber `original_moa` wurde nicht ausgefüllt; der DrugBank-Datensatz sollte erneut analysiert werden, um Felder für Mechanismus, Kategorien und Toxizität zu extrahieren

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

