---
layout: default
title: Regorafenib
parent: Nur Modellvorhersage (L5)
nav_order: 332
evidence_level: L5
indication_count: 8
---

# Regorafenib
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

# REGORAFENIB: Umwidmungs-Bewertung — Unzureichende Daten zur Durchführung einer vollständigen Bewertung

---

## Zusammenfassung in einem Satz

REGORAFENIB (DrugBank-ID: DB08896) ist ein Arzneistoff, für den das aktuelle Evidence Pack keine Einträge zu zugelassenen Indikationen, keine Daten zum Wirkungsmechanismus und keine durch TxGNN vorhergesagten Indikationen enthält.
Eine vollständige Umwidmungs-Bewertung kann zu diesem Zeitpunkt nicht erstellt werden; der folgende Bericht dokumentiert, was verfügbar ist, und gibt die vor dem Fortschreiten erforderlichen Sanierungsschritte an.

---

## Schnellübersicht

| Artikel | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | In aktuellen Daten nicht verfügbar |
| Vorhergesagte neue Indikation | Keine Vorhersagen zurückgegeben |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidenzstufe | Unter L5 — keine Vorhersagen oder verknüpfte Studien |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum ist diese Vorhersage angemessen?

Für diesen Kandidaten wurden keine vorhergesagten Indikationen durch die TxGNN-Pipeline zurückgegeben (`predicted_indications: []`).
Ohne eine Zielindikation zur Bewertung kann keine mechanistische Begründung konstruiert werden.

Darüber hinaus ist das Feld Wirkungsmechanismus als Datenlücke gekennzeichnet (DG002, Schweregrad: Hoch).
Ohne Informationen zum Wirkungsmechanismus ist es nicht möglich, die pharmakologische Plausibilität zu bewerten, selbst wenn eine Kandidatenindikation vorgeschlagen würde.

**Was erforderlich ist, bevor dieser Abschnitt verfasst werden kann:**
1. Erneutes Ausführen des TxGNN-Modells, um zu bestätigen, ob die Vorhersageausgabe aufgrund eines Pipeline-Fehlers unterdrückt wurde oder tatsächlich keine Kandidaten über dem Schwellenwert zurückgegeben wurden.
2. Abrufen von Wirkungsmechanismus-Daten von DrugBank (DG002-Sanierung: DrugBank-API für DB08896 abfragen).

---

## Evidenz klinischer Studien

Derzeit sind keine verwandten klinischen Studien für die vorhergesagte Indikation registriert — keine Zielindikation ist verfügbar.

---

## Evidenz der Literatur

Derzeit ist keine verwandte Literatur verfügbar — keine Zielindikation ist verfügbar.

---

## Informationen zum deutschen Markt

REGORAFENIB hat **0 Zulassungen** im aktuellen regulatorischen Datensatz. Es sind keine Produktauflistungen zum Anzeigen verfügbar.

---

## Sicherheitserwägungen

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

> **Anmerkung:** Zwei blockierende Datenlücken verhindern eine Sicherheitsbewertung:
> - **DG001 (Blockierend):** Warnungen und Kontraindikationen der Fachinformation wurden nicht geparst. Sanierung: PDF von der offiziellen Behörde herunterladen und Text extrahieren.
> - **DG002 (Hoch):** Wirkungsmechanismus-Daten sind nicht vorhanden, was eine mechanistische DDI-Analyse verhindert. Sanierung: DrugBank-API für DB08896 abfragen.

Es wurden keine Arzneimittelwechselwirkungsdaten gefunden (DDI-Abfragestatus: `not_found`, 0 Wechselwirkungen).

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack für REGORAFENIB ist kritisch unvollständig — es gibt keine vorhergesagten Indikationen, keinen Text zu zugelassenen Indikationen, keinen Wirkungsmechanismus und keine Sicherheitsdaten für die Bewertung verfügbar. Eine Fortsetzung ohne diese Eingaben würde zu einer unzuverlässigen Bewertung führen.

**Zum Fortschreiten ist Folgendes erforderlich:**

- [ ] **TxGNN-Pipeline diagnostizieren** — Bestätigen Sie, ob das leere Array `predicted_indications` ein echtes Ergebnis unterhalb des Schwellenwerts widerspiegelt oder einen Pipeline-Fehler (z. B. fehlende Graph-Einbettung für DB08896).
- [ ] **Wirkungsmechanismus-Daten von DrugBank-API abrufen** — DB08896 abfragen, um Pharmakologie, Wirkungsmechanismus und Arzneimittelkategorien zu erhalten (behebt DG002).
- [ ] **Fachinformation parsen** — PDF von der Behörde herunterladen und Warnungen, Kontraindikationen und zugelassene Indikationen extrahieren (behebt DG001).
- [ ] **Evidence Pack erneut generieren** — Nach dem Ausfüllen von DG001 und DG002 das Evidence Pack (v5 oder später) erneut generieren und erneut zur Berichterstellung einreichen.
- [ ] **Zielindikation bestätigen** — Sobald TxGNN-Vorhersagen verfügbar sind, wählen Sie die höchstbewertete Indikation aus und rufen Sie verknüpfte klinische Studien und Literatur über die Evidence-Pipeline ab.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

