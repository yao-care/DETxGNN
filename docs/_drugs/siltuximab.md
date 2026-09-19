---
layout: default
title: Siltuximab
parent: Nur Modellvorhersage (L5)
nav_order: 364
evidence_level: L5
indication_count: 8
---

# Siltuximab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **8** 
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

# Siltuximab: Von der multizentrische Castleman-Krankheit zum extrakutanen Mastozytom

## Zusammenfassung in einem Satz

Siltuximab ist ein monoklonaler Anti-IL-6-Antikörper, dessen etablierte Anwendung die multizentrische Castleman-Krankheit (MCK) ist, eine seltene lymphoproliferative Störung, die durch IL-6-Dysregulation angetrieben wird. Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam für **extrakutanes Mastozytom** ist, aber diese Einstufung basiert rein auf Netzwerk-Vorhersage — **keine klinischen Studien und keine Literatur** unterstützen derzeit diese spezifische Richtung.

---

## Schnellübersicht

| Merkmal | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Multizentrische Castleman-Krankheit (MCK) *(hergeleitet aus dem Begründungstext des Evidenzpakets; nicht separat bestätigt im strukturierten `original_indications`-Feld)* |
| Vorhergesagte neue Indikation | Extrakutanes Mastozytom |
| TxGNN-Vorhersage-Score | 99.64% |
| Evidenzgrad | L5 (rein Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage vernünftig?

Strukturierte Wirkmechanismus-Daten sind für dieses Arzneimittel nicht verfügbar (`original_moa` = Datenlücke). Basierend auf dem Begründungstext des Evidenzpakets ist Siltuximab ein rekombinanter chimärer monoklonaler Anti-IL-6-Antikörper, und seine etablierte Wirksamkeit liegt bei der IL-6-gesteuerten multizentrische Castleman-Krankheit.

Für die am höchsten bewertete Vorhersage, extrakutanes Mastozytom, ist der mechanistische Fall schwach. Einige Literatur hat hypothesiert, dass IL-6 die Mastzellproliferation und -aktivierung fördern kann, was eine vage biologische Begründung für die IL-6-Blockade bei Mastzellstörungen bietet. Es gibt jedoch **keine direkten Belege**, die Siltuximab speziell mit dieser seltenen Mastozytom-Variante verbinden — das Evidenzpaket stellt ausdrücklich fest, dass dies „rein eine TxGNN-Netzwerk-Vorhersage ist, der mechanistische Validierungsdaten fehlen."

Da es keinerlei klinische Studien oder Literatur für diese Indikation gibt, sollte die mechanistische Verbindung nur als Forschungshypothese behandelt werden, nicht als validiertes Repurposing-Signal.

---

## Evidenz klinischer Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturbelege

Derzeit sind keine zugehörigen Literaturquellen verfügbar.

---

## Marktstatus Deutschland

Siltuximab wird derzeit nicht in Deutschland vermarktet (0 erfasste Genehmigungen); keine Produktlizenzinformationen sind in diesem Evidenzpaket verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: `key_warnings`, `contraindications` und Arzneimittel-Wechselwirkungsdaten sind alle in diesem Evidenzpaket als Datenlücken gekennzeichnet. TFDA/BfArM-Etikettwarnungen — gekennzeichnet als `DG001`, Blocking-Schweregrad — müssen vor jeder S1-Sicherheitsbewertung eingeholt werden.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Diese Vorhersage wird nur durch den TxGNN-Modellscore (L5-Evidenzgrad) unterstützt, ohne klinische Studien und ohne Literatur. Der vorgeschlagene Mastzell-Wirkmechanismus ist spekulativ und wird im Evidenzpaket ausdrücklich als mangelnde mechanistische Validierungsdaten gekennzeichnet. Dies erfüllt derzeit nicht die Anforderungen für weitere Entwicklung.

**Um fortzufahren, ist Folgendes erforderlich:**
- Detaillierte Wirkmechanismus-Daten (MOA) für Siltuximab (`DG002`)
- TFDA/BfArM-Packungsbeilage — Warnhinweise und Kontraindikationen (`DG001`, Blocking — erforderlich vor jeder S1-Sicherheitsbewertung)
- Gezielte Literatur- und klinische Studiensuche speziell für IL-6-Blockade bei Mastzellstörungen (aktuelles Paket hat null Treffer)
- Bestätigung der ursprünglichen genehmigten Indikation(en) des Arzneimittels, da das strukturierte `original_indications`-Feld derzeit leer ist

**Zusätzlicher Hinweis:** Unter den anderen Kandidaten in diesem Evidenzpaket hat **Kaposi-Sarkom** (Rang 5) eine stärkere evidenzielle Grundlage (L4, Entscheidungsstufe S1) über seine biologische Verbindung zur HHV-8-assoziierten multizentrische Castleman-Krankheit, und könnte eine separate, dedizierte Bewertung vor diesem Spitzenkandidat rechtfertigen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

