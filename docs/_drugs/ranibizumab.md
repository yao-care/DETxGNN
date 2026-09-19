---
layout: default
title: Ranibizumab
parent: Nur Modellvorhersage (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: Neuanwendungsbewertung — Keine TxGNN-Vorhersage verfügbar

## Zusammenfassung in einem Satz

Ranibizumab ist ein monoklonales Anti-VEGF-Antikörperfragment, das international unter dem Handelsnamen Lucentis bekannt ist und hauptsächlich zur Behandlung okulärer neovaskulärer Erkrankungen wie feuchter altersbedingter Makuladegeneration verwendet wird.
Das TxGNN-Modell hat für dieses Medikament **keine vorhergesagten neuen Indikationen generiert**,
und **keine klinischen Studien oder Literaturbeweise** sind in diesem Evidence Pack enthalten.
Dieser Bericht spiegelt die aktuelle Datenverfügbarkeit wider und zeigt auf, was erforderlich ist, bevor die Bewertung fortgesetzt werden kann.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in diesem Evidence Pack aufgezeichnet |
| Vorhergesagte neue Indikation | Keine — TxGNN-Ausgabe nicht verfügbar |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzgrad | L5 (Nur Modellvorhersage — keine tatsächlichen Studien verlinkt) |
| Marktstand | Nicht auf dem Markt (0 Zulassungen verzeichnet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückstellung** |

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
Diesem Evidence Pack fehlen die vier wesentlichen Eingaben, die für eine Neuanwendungsbewertung erforderlich sind — vorhergesagte Indikationen, Text der ursprünglichen Indikation, Wirkmechanismus und Sicherheitsprofil. Ohne diese können weder die klinische Plausibilität noch die Risikobewertung durchgeführt werden.

**Um fortzufahren, ist Folgendes erforderlich:**

- **TxGNN-Vorhersage-Ausgabe** — `predicted_indications` ist derzeit eine leere Liste; führen Sie die TxGNN-Pipeline für DB01270 erneut aus und überprüfen Sie, dass der Zuordnungsschritt Ranibizumab erfolgreich mit Krankheitsknoten verknüpft hat
- **Originalindikationsdaten** — `original_indications` ist leer; rufen Sie den genehmigten Indikationstext aus dem DrugBank-Eintrag oder der Gebrauchsinformation ab
- **Wirkmechanismus (MOA)** — gekennzeichnet als hochgradige Datenlücke; fragen Sie die DrugBank-API für DB01270 ab, um den pharmakologischen Mechanismus zu erhalten
- **Sicherheitsdaten** — wichtige Warnhinweise und Kontraindikationen fehlen; laden Sie die PDF der Gebrauchsinformation herunter und analysieren Sie diese, um diese Felder auszufüllen
- **Überprüfung des Regulierungsstatus** — bestätigen Sie, ob das Ergebnis „0 Lizenzen" den tatsächlichen Marktstand widerspiegelt oder eine Abfrageabdeckungsbeschränkung darstellt

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

