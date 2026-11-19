---
layout: default
title: Belimumab
parent: Nur Modellvorhersage (L5)
nav_order: 55
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-20
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

## Belimumab: Von systemischem Lupus erythematodes zu Primäre Thrombozyten-Freisetzungsstörung
{: .text-alpha }

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
| TxGNN-Vorhersagewert | 0,9996 |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Laut dem Abschnitt „Mechanism of Action“ der von der US-amerikanischen FDA genehmigten Fachinformation (Prescribing Information) für Belimumab (inoffizielle Übersetzung): „BENLYSTA ist ein BLyS-spezifischer Inhibitor, der die Bindung von löslichem BLyS, einem B-Zell-Überlebensfaktor, an seine Rezeptoren auf B-Zellen blockiert. BENLYSTA bindet nicht direkt an B-Zellen, sondern hemmt durch die Bindung von BLyS das Überleben von B-Zellen, einschließlich autoreaktiver B-Zellen, und verringert die Differenzierung von B-Zellen in Immunglobulin-produzierende Plasmazellen.“ Englischer Originalwortlaut: "BENLYSTA is a BLyS-specific inhibitor that blocks the binding of soluble BLyS, a B-cell survival factor, to its receptors on B cells. BENLYSTA does not bind B cells directly, but by binding BLyS, BENLYSTA inhibits the survival of B cells, including autoreactive B cells, and reduces the differentiation of B cells into immunoglobulin-producing plasma cells." ([DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3), Fassung vom 2026-10-30; abgerufen am 2026-11-19). Nach allgemeinem Wissen neutralisiert Belimumab den B-Lymphozyten-Stimulator (BLyS bzw. BAFF), verringert dadurch das Überleben von B-Zellen und senkt die Autoantikörperbildung. Beim systemischen Lupus erythematodes, einer autoantikörpervermittelten Erkrankung, ist dieser Mechanismus nachvollziehbar.

Die primäre Thrombozyten-Freisetzungsstörung ist dagegen ein angeborener oder erworbener qualitativer Funktionsdefekt der Thrombozyten und in der Regel nicht durch B-Zellen oder Autoantikörper getrieben. Ein plausibler mechanistischer Zusammenhang ist derzeit nicht erkennbar. Der hohe Vorhersagewert ist eine rein graphbasierte Modellvorhersage und wird weder durch Studien noch durch Literatur gestützt.

Auch die weiteren Vorhersagen sind überwiegend mechanistisch schwach begründet:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Pseudo-von-Willebrand-Erkrankung | 0,9996 | Genetischer Defekt des Thrombozytenrezeptors GPIbα; kein bekannter Bezug zur BAFF-Hemmung |
| 3 | Glanzmann-Thrombasthenie | 0,9988 | Angeborener Defekt von αIIbβ3; allenfalls theoretischer Bezug über Alloantikörper nach Transfusionen |
| 4 | Fetale und neonatale Alloimmunthrombozytopenie | 0,9959 | Antikörpervermittelt, daher konzeptionell denkbar; Sicherheitsbedenken in der Schwangerschaft |
| 5 | Schwere nichtproliferative diabetische Retinopathie | 0,9905 | Kein etablierter Bezug von BAFF zur Pathogenese |
| 6 | Autosomal-dominante Makrothrombozytopenie | 0,9904 | Angeborene Bildungsstörung, nicht immunvermittelt |

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

Diese Zulassung ist gültig; das Arzneimittel ist aktuell im Handel.

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
Die Vorhersage stammt vom TxGNN-Modell (Deep Learning) und kann Ähnlichkeiten widerspiegeln, die das Modell zwischen verwandten Erkrankungen gelernt hat, nicht biologische Evidenz. Es gibt weder klinische Studien noch Publikationen, und ein plausibler Wirkmechanismus fehlt. Das Arzneimittel ist in Deutschland mit einer gültigen Zulassung im Handel.

**Für ein Weiterverfolgen sind folgende Schritte nötig:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Ergänzung der Wirkmechanismus-Daten (MOA) aus DrugBank
- Systematische Literatur- und Studienrecherche zu Belimumab bei Thrombozytenerkrankungen
- Prüfung der Indikationen mit immunologischem Bezug (z. B. fetale und neonatale Alloimmunthrombozytopenie) auf mechanistische Plausibilität und Sicherheit
- Klärung des Zulassungs- und Marktstatus in Deutschland

<!-- review:begin log -->

## Prüfprotokoll

Nachfolgend das Prüfprotokoll dieser Seite. Die Aussage, dass keine Daten zum Wirkmechanismus vorliegen, wurde durch einen Auszug aus der angegebenen amtlichen Fachinformation (mit inoffizieller Übersetzung) ersetzt; Modellvorhersagen, Evidenzstufen und Schlussfolgerungen wurden nicht umgeschrieben.

| Prüfdatum | Punkt | Maßnahme | Quelle |
|------|------|------|------|
| 2026-11-19 | Aussage „keine Daten zum Wirkmechanismus“ durch Auszug aus der US-Fachinformation ersetzt | Aussage, dass keine Daten zum Wirkmechanismus vorliegen, durch einen belegten Auszug ersetzt | [DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3) |

<!-- review:end log -->

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

