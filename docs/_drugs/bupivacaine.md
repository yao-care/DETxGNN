---
layout: default
title: Bupivacaine
parent: Nur Modellvorhersage (L5)
nav_order: 72
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Bupivacain: Lokalanästhetikum — Keine Umwidmungsvorhersagen verfügbar

## Zusammenfassung in einem Satz

Bupivacain ist ein lang wirkendes Lokalanästhetikum vom Amidtyp, das häufig für Regional- und Neuraxialanästhesie verwendet wird. Das aktuelle Evidenzpaket enthält **keine neuen von TxGNN vorhergesagten Indikationen** für dieses Arzneimittel, und das Arzneimittel ist **in Taiwan nicht registriert**. Ohne vorhergesagte Indikationen oder Daten zur behördlichen Genehmigung kann eine formale Umwidmungsbewertung in diesem Stadium nicht durchgeführt werden.

---

## Schnelle Übersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Lokal-/Regionalanästhesie (aus allgemeinem pharmakologischem Wissen; nicht im Evidenzpaket vorhanden) |
| Vorhergesagte neue Indikation | — Keine Vorhersage verfügbar |
| TxGNN Vorhersage-Score | — |
| Evidenzstufe | — (Keine Vorhersagen zur Bewertung) |
| Marktstatus Taiwan | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

---

## Warum ist diese Vorhersage sinnvoll?

Keine Umwidmungsvorhersage ist in diesem Evidenzpaket verfügbar, daher kann eine mechanistische Begründung für eine neue Indikation zu diesem Zeitpunkt nicht bewertet werden.

Zu Ihrer Information ist Bupivacain ein spannungsabhängiger Natriumkanal-Blocker (Nav1.x). Er hemmt die Membrandepolarisation in sensorischen und motorischen Neuronen und erzeugt eine reversible Leitungsblockade. Dieser Mechanismus ist pharmakologisch relevant für mehrere nicht-anästhetische Anwendungen (z. B. chronische Schmerzen, antiarrhythmische Effekte bei niedrigen Dosen), aber ohne ein spezifisches von TxGNN vorhergesagtes Krankheitsziel kann keine Aussage gemacht werden.

Das Evidenzpaket dokumentiert auch zwei Datenlücken: Daten zum Wirkmechanismus (MOA) fehlen in dem strukturierten Arzneimitteldatensatz, und es wurden keine Taiwan-Packungsbeilage-Warnungen in die Sicherheitsfelder eingegeben. Diese Lücken sollten behoben werden, bevor ein Umwidmungspfad bewertet wird.

---

## Nachweis aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien für eine Umwidmungsindikation registriert (`predicted_indications` ist leer).

---

## Nachweis aus Literatur

Derzeit ist keine verwandte Literatur für eine Umwidmungsindikation verfügbar (`predicted_indications` ist leer).

---

## Taiwan-Marktinformationen

Bupivacain ist derzeit **nicht bei der Taiwan Food and Drug Administration (TFDA) registriert**. Es sind keine Genehmigungsunterlagen verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> **Hinweis:** Die TFDA-Packungsbeilage-Abfrage (query_log ID 4) hat ein Ergebnis zurückgegeben, aber die strukturierten Sicherheitsfelder wurden nicht ausgefüllt. Eine manuelle Überprüfung des Packungsbeilage-PDFs ist erforderlich, um Warnungen und Kontraindikationen zu extrahieren.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Das Evidenzpaket enthält keine von TxGNN vorhergesagten Indikationen, keine strukturierten Sicherheitsdaten und keine Taiwan-behördlichen Genehmigungen. Es gibt zu diesem Zeitpunkt keinen Umwidmungskandidaten zu bewerten.

**Um fortfahren zu können, wird Folgendes benötigt:**

- **TxGNN-Vorhersage-Pipeline erneut ausführen** für DB00297 (Bupivacain), um Scores auf Erkrankungsebene und Kandidatenindikationen zu erhalten
- **DG001 beheben** — Extrahieren Sie Schlüsselwarnungen, Kontraindikationen und Dosierungsgrenzen aus dem TFDA-Packungsbeilage-PDF
- **DG002 beheben** — Fragen Sie die DrugBank-API nach strukturierten MOA- und pharmakologischen Kategoriedaten ab
- **DDI-Daten überprüfen** — DDI-Abfrage gab `not_found` zurück; vergleichen Sie mit alternativen Interaktionsdatenbanken (z. B. DrugBank-Interaktionen, Taiwan-NHI-Formularium)
- Sobald vorhergesagte Indikationen verfügbar sind, erneut einen vollständigen Bewertungsbericht mit klinischen Studien- und Literaturbelegen ausstellen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

