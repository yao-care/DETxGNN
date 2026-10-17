---
layout: default
title: Belimumab
parent: Nur Modellvorhersage (L5)
nav_order: 55
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Belimumab: vorhergesagte neue Indikation Primäre Thrombozyten-Freisetzungsstörung (Evidenzstufe L5). Ursprüngliche Indikation: Systemischer Lupus erythematodes"
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
---

# Belimumab
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Belimumab: Von systemischem Lupus erythematodes zu primärer Thrombozyten-Freisetzungsstörung

## Zusammenfassung

Belimumab ist ein Antikörper, der ursprünglich zur Behandlung des **systemischen Lupus erythematodes** zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei der **primären Thrombozyten-Freisetzungsstörung** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Systemischer Lupus erythematodes |
| Vorhergesagte neue Indikation | Primäre Thrombozyten-Freisetzungsstörung |
| TxGNN-Vorhersagewert | 99,96 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine Angaben vor. Nach allgemeinem Wissen neutralisiert Belimumab den B-Lymphozyten-Stimulator (BLyS bzw. BAFF), verringert dadurch das Überleben von B-Zellen und senkt die Autoantikörperbildung. Beim systemischen Lupus erythematodes, einer autoantikörpervermittelten Erkrankung, ist dieser Mechanismus nachvollziehbar.

Die primäre Thrombozyten-Freisetzungsstörung ist dagegen ein angeborener oder erworbener qualitativer Funktionsdefekt der Thrombozyten und in der Regel nicht durch B-Zellen oder Autoantikörper getrieben. Ein plausibler mechanistischer Zusammenhang ist derzeit nicht erkennbar. Der hohe Vorhersagewert ist eine rein graphbasierte Modellvorhersage und wird weder durch Studien noch durch Literatur gestützt.

Auch die weiteren Vorhersagen sind überwiegend mechanistisch schwach begründet:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Pseudo-von-Willebrand-Erkrankung | 99,96 % | Genetischer Defekt des Thrombozytenrezeptors GPIbα; kein bekannter Bezug zur BAFF-Hemmung |
| 3 | Glanzmann-Thrombasthenie | 99,88 % | Angeborener Defekt von αIIbβ3; allenfalls theoretischer Bezug über Alloantikörper nach Transfusionen |
| 4 | Fetale und neonatale Alloimmunthrombozytopenie | 99,59 % | Antikörpervermittelt, daher konzeptionell denkbar; Sicherheitsbedenken in der Schwangerschaft |
| 5 | Schwere nichtproliferative diabetische Retinopathie | 99,05 % | Kein etablierter Bezug von BAFF zur Pathogenese |
| 6 | Autosomal-dominante Makrothrombozytopenie | 99,04 % | Angeborene Bildungsstörung, nicht immunvermittelt |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002015 | Benlysta (GlaxoSmithKline Trading Services Limited) | – | Systemischer Lupus erythematodes |

Diese Zulassung ist erloschen; es besteht aktuell keine gültige Zulassung.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt wurden 69 Wechselwirkungen erfasst. Davon eine Auswahl:
  - **Schwerwiegend (Major)**: Adalimumab, Baricitinib, Certolizumab pegol, BCG-Lebendimpfstoff (Stamm Tice)
  - **Mäßig (Moderate)**: Roflumilast, Azathioprin, Alemtuzumab, Anakinra, Canakinumab, Alefacept, Tetanus-Toxoid sowie weitere Impfstoffe
  - **Gering (Minor)**: Zinkacetat, Zinkgluconat, Zinksulfat, Zinkchlorid

  Die schwerwiegenden Wechselwirkungen betreffen vor allem andere Immunsuppressiva und Lebendimpfstoffe.

- Für die vorhergesagte Indikation fetale und neonatale Alloimmunthrombozytopenie bestehen zusätzlich Bedenken zur Anwendung in der Schwangerschaft (begrenzte Datenlage, Plazentagängigkeit von IgG).

Angaben zu Warnhinweisen und Gegenanzeigen liegen nicht vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf ein Graphmodell. Es gibt weder klinische Studien noch Publikationen, und ein plausibler Wirkmechanismus fehlt. Zudem besteht in Deutschland derzeit keine gültige Zulassung.

**Für ein Weiterverfolgen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Ergänzung der Wirkmechanismus-Daten (MOA) aus DrugBank
- Systematische Literatur- und Studienrecherche zu Belimumab bei Thrombozytenerkrankungen
- Prüfung der Indikationen mit immunologischem Bezug (z. B. fetale und neonatale Alloimmunthrombozytopenie) auf mechanistische Plausibilität und Sicherheit
- Klärung des Zulassungs- und Marktstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

