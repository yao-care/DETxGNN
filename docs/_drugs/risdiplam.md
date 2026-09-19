---
layout: default
title: Risdiplam
parent: Nur Modellvorhersage (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
---

# Risdiplam
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# RISDIPLAM: Bewertung ausstehend — Kritische Datenlücken verhindern vollständige Bewertung

## Zusammenfassung in einem Satz

Risdiplam (DrugBank ID: DB15305) ist derzeit nicht in Taiwan im Handel erhältlich, und das TxGNN-Modell hat in diesem Evidenzpaket **keine vorhergesagten Indikationen** zurückgegeben.
Ursprüngliche Indikationen, Wirkmechanismus und Sicherheitsdaten fehlen vollständig, was eine aussagekräftige Umwidmungsbewertung in dieser Phase unmöglich macht.
Dieser Bericht dokumentiert den aktuellen Zustand und gibt die erforderlichen Daten für die Fortsetzung an.

---

## Schneller Überblick

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in diesem Evidenzpaket ausgefüllt |
| Vorhergesagte neue Indikation | Keine TxGNN-Vorhersagen zurückgegeben |
| TxGNN-Vorhersage-Score | N/A |
| Evidenzstufe | L5 — Nur Modellvorhersage (keine verknüpften tatsächlichen Studien) |
| Taiwan-Marktstatus | Nicht im Handel erhältlich |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum keine Vorhersage verfügbar ist

Das `predicted_indications`-Array in diesem Evidenzpaket ist leer. Ohne eine TxGNN-vorhergesagte Zielindikation kann die standardmäßige Umwidmungs-Pipeline nicht fortgesetzt werden.

Darüber hinaus ist auch das Feld `original_indications` leer und der Wirkmechanismus ist als Datenlücke gekennzeichnet. Bei der Erstellung des Evidenzpakets wurden zwei vorgelagerte Datenlücken (DG001: Packungsbeilage-Warnungen/Kontraindikationen; DG002: MOA) identifiziert, beide bewertet mit **Blocking**- oder **High**-Schweregrad. Diese Lücken müssen behoben werden, bevor eine mechanistische Ähnlichkeitsanalyse verfasst werden kann.

Basierend auf allgemeinem Wissen ist Risdiplam ein gut charakterisierter oraler Kleinmolekül-SMN2-pre-mRNA-Splicing-Modulator, der in mehreren Märkten für Spinale Muskelatrophie (SMA) zugelassen ist. Diese Informationen sind jedoch **im eingereichten Evidenzpaket nicht vorhanden** und können daher nicht als Grundlage für eine Bewertungsempfehlung verwendet werden. Die Daten-Pipeline muss mit den folgenden Abhilfemaßnahmen erneut ausgeführt werden.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die erforderlichen Mindestdaten zur Durchführung einer Umwidmungsbewertung fehlen — `predicted_indications` ist leer und die zwei vorgelagerten Datenlücken (DG001, DG002) wurden vor der Finalisierung dieses Evidenzpakets nicht behoben.

**Um fortzufahren, ist Folgendes erforderlich:**

- **[DG001 — Blocking]** TFDA-Packungsbeilage-PDF herunterladen und analysieren, um Schlüsselwarnungen und Kontraindikationen zu extrahieren; Sicherheitsmodul erneut ausführen
- **[DG002 — High]** DrugBank-API für Risdiplam (DB15305) abfragen, um MOA-, Wirkstoffklassen- und Toxizitätsdaten abzurufen; `original_moa` ausfüllen
- **TxGNN-Inferenz erneut ausführen** nachdem `original_indications` und `original_moa` ausgefüllt wurden, damit `predicted_indications` mindestens einen Kandidaten zurückgibt
- **Ursprüngliche Indikationsliste überprüfen** — bestätigen, dass die genehmigte(n) Indikation(en) (z. B. SMA) korrekt in die Pipeline geladen sind, bevor die Neubewertung durchgeführt wird
- Sobald das oben Genannte abgeschlossen ist, Evidenzpaket neu generieren und erneut für einen umfassenden Bewertungsbericht einreichen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

