---
layout: default
title: Ritonavir
parent: Nur Modellvorhersage (L5)
nav_order: 349
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: Evaluierungsbericht — Unzureichende TxGNN-Vorhersagedaten

## Zusammenfassung in einem Satz

Ritonavir ist ein HIV-Proteaseinhibitor, der häufig als pharmakokinetischer Booster in kombinierten antiviralen Regimen verwendet wird (z. B. Paxlovid, Lopinavir/Ritonavir).
Das aktuelle Evidence Pack enthält **keine TxGNN-vorhergesagten neuen Indikationen** und das Arzneimittel ist **nicht in Taiwan registriert**.
Aufgrund kritischer Datenlücken in den Dimensionen Vorhersage, Regulierung, Wirkmechanismus und Sicherheit **kann eine vollständige Umwidmungsbewertung in diesem Stadium nicht abgeschlossen werden**.

---

## Schnellübersicht

| Eintrag | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | HIV-Infektion (allgemeines pharmazeutisches Wissen; nicht in behördlichen Daten vorhanden) |
| Vorhergesagte neue Indikation | Nicht verfügbar |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzstufe | Undefiniert – keine Vorhersagedaten vorhanden |
| Taiwan-Marktstatus | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Sicherheitsaspekte

Für dieses Evidence Pack sind keine Sicherheitsdaten verfügbar. Alle Felder für Warnungen, Kontraindikationen und Arzneimittelwechselwirkungen wurden als leer oder fehlend zurückgegeben.

> Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Das Evidence Pack für Ritonavir ist in allen vier Evaluierungsdimensionen kritisch unvollständig – TxGNN-Vorhersage, behördlicher Status, Wirkmechanismus und Sicherheitsprofil. Ohne eine vorherzusagende Indikation zur Bewertung kann kein Umwidmungsfall konstruiert oder bewertet werden.

**Um fortzufahren, ist Folgendes erforderlich:**

- **TxGNN-Vorhersageergebnisse** — `predicted_indications` müssen mit mindestens einer Kandidatenindikation und zugehörigen Daten gefüllt werden (klinische Studien, Literatur)
- **Wirkmechanismus (MOA)** — abrufen von DrugBank-API (DG002: Lücke mit hohem Schweregrad)
- **Packungsbeilage Sicherheitsdaten** — Hauptwarnungen, Kontraindikationen und Arzneimittelwechselwirkungen aus TFDA oder gleichwertiger Quelle (DG001: Blockierende Lücke)
- **Bestätigung der ursprünglichen Indikation** — Überprüfung genehmigter Indikationen aus Taiwan TFDA oder internationalen behördlichen Quellen (EMA/FDA)
- **Arzneimittelwechselwirkungsprofil** — DDI-Abfrage gab `not_found` zurück; erneute Abfrage mit alternativen Quellen (z. B. DrugBank DDI, klinisch-pharmakologische Datenbanken)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

