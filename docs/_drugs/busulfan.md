---
layout: default
title: Busulfan
parent: Nur Modellvorhersage (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: Neubewertung für Umwidmung — Ausstehende prognostizierte Indikation

## Zusammenfassung in einem Satz

Busulfan ist ein bifunktionelles Alkylierungsmittel mit etabliertem Einsatz bei chronischer myeloischer Leukämie (CML) und Konditionierungsregimen vor Stammzelltransplantation (HSCT). Das aktuelle Beweispaket enthält **keine durch TxGNN prognostizierten neuen Indikationen**, und kritische Daten einschließlich Wirkmechanismus und Sicherheitsinformationen bleiben ungeklärt. Dieser Bericht dokumentiert den aktuellen Datenstatus und definiert die erforderlichen Abhilfemaßnahmen, bevor die Bewertung der Umwidmung fortgesetzt werden kann.

---

## Schnelläbersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Chronische myeloische Leukämie / Konditionierung vor Transplantation (basierend auf etabliertem pharmakologischem Wissen; Packungsbeilage für Taiwan nicht abgerufen) |
| Prognostizierte neue Indikation | Keine im aktuellen Beweispaket generiert |
| TxGNN-Prognosescore | Nicht verfügbar |
| Evidenzstufe | Kann nicht bestimmt werden |
| Marktstatus in Taiwan | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage angemessen?

Da die TxGNN-Pipeline in diesem Beweispaket keine prognostizierten Indikationen zurückgegeben hat, kann zu diesem Zeitpunkt keine formelle mechanistische Brückenanalyse durchgeführt werden.

Basierend auf etabliertem pharmakologischem Wissen ist Busulfan ein bifunktionelles Alkylierungsmittel, das DNA-Stränge quervernetzt und die Replikation in schnell teilenden Zellen unterbricht. Dieser Mechanismus liegt seiner langjährigen Verwendung bei CML (Knochenmarksuppression als therapeutische Absicht) und seiner Rolle als myeloablativer Konditionierungsstoff vor HSCT zugrunde, um verbleibende hämatopoetische Zellen vor dem Engraftment des Spenders zu beseitigen.

Um zu bewerten, ob dieser Mechanismus auf eine neue Indikation anwendbar ist, müssen zunächst TxGNN-Vorhersagen generiert und überprüft werden. Sobald Kandidatenkrankheitszuordnungen verfügbar sind, kann die mechanistische Plausibilität im Kontext gemeinsamer biologischer Pfade bewertet werden.

---

## Zytotoxizität

Busulfan ist ein antineoplastisches Alkylierungsmittel; eine Zytotoxizitätsbewertung ist erforderlich.

| Artikel | Inhalt |
|---------|--------|
| Zytotoxizitätsklassifizierung | Konventionell zytotoxisch — Alkylierungsmittel (bifunktionelles Alkylsulfon) |
| Myelosuppressionsrisiko | Hoch — schwere, anhaltende Knochenmarksuppression ist die primäre dosislimitierende Toxizität; Tiefstwert typischerweise bei 11–30 Tagen |
| Emetogenitätsklassifizierung | Moderat (Standard-Dosis-Mundregimen); Hoch (hochdosierte IV-Konditionierung) |
| Überwachungselemente | Blutbild mit Differenzierung (täglich während Konditionierung), Leberfunktionstests, Nierenfunktion, Busulfan-Plasmaspiegel (therapeutisches Arzneimittelmonitoring für IV-Konditionierung), Serumelektrolyte |
| Handhabungsschutz | Muss Handhabungsvorschriften für zytotoxische Arzneimittel befolgen; IV-Formulierung erfordert spezielles Arzneimittel-Transfergerät für geschlossene Systeme |

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

> Hinweis: Der Abruf der Packungsbeilage für Taiwan ergab ein positives Ergebnis im Abfrageprotokoll (Abfrage-ID 4, Status: erfolgreich), aber der analysierte Inhalt war nicht in diesem Beweispaket enthalten. Warnungen und Kontraindikationen sollten aus dieser Quelle als nächster Abhilfeschritt entnommen werden.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Das Beweispaket ist völlig ohne TxGNN-Vorhersagen, und sowohl der Wirkmechanismus als auch Sicherheitsdaten bleiben ungeklärt — was es zu diesem Zeitpunkt unmöglich macht, eine Umwidmungshypothese zu bewerten oder ein Sicherheits-Vor-Screening durchzuführen.

**Um fortzufahren, wird folgendes benötigt:**

- **TxGNN-Vorhersage-Pipeline erneut ausführen** — Kandidatenkrankheitszuordnungen für Busulfan (DB01008) generieren, damit eine Umwidmungshypothese identifiziert werden kann
- **Inhalt der Packungsbeilage für Taiwan extrahieren** — das Abfrageprotokoll bestätigt einen erfolgreichen Abruf (Abfrage-ID 4); Warnungen, Kontraindikationen und Dosierungsinformationen aus dem abgerufenen Dokument extrahieren
- **DrugBank-API für vollständige Wirkmechanismus-Daten abfragen** — Wirkmechanismus ausfüllen, um Target-Pathway-Analyse zu ermöglichen
- **DDI-Daten abrufen** — Arzneimittel-Interaktionsdatenbanken abfragen (DDI-Abfrage gab not_found zurück; Suchbereich erweitern oder alternative Quellen verwenden)
- **Beweispaket erneut einreichen** — sobald die oben genannten vier Punkte gelöst sind, das Beweispaket erneut generieren und zur vollständigen Umwidmungsbewertung übergehen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

