---
layout: default
title: Riluzole
parent: Nur Modellvorhersage (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzol: Von Amyotropher Lateralsklerose zu bilateraler parasagittaler parieto-okzipitaler Polymikrogyrie

## Zusammenfassung

Riluzol ist ein Wirkstoff, der ursprünglich zur Behandlung der Amyotrophen Lateralsklerose (ALS) zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **bilateraler parasagittaler parieto-okzipitaler Polymikrogyrie** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht ausschließlich auf dem Modell.

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Amyotrophe Lateralsklerose |
| Vorhergesagte neue Indikation | Bilaterale parasagittale parieto-okzipitale Polymikrogyrie |
| TxGNN-Vorhersagewert | 99,99 % |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen |
| Anzahl der Zulassungen | 2 (beide aufgehoben) |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage plausibel?

Für diesen Wirkstoff liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben zum Wirkmechanismus vor. Aus der Literatur ist bekannt, dass Riluzol die glutamaterge Neurotransmission dämpft und damit exzitotoxische Schäden an Motoneuronen verringern soll. Seine Wirksamkeit bei ALS ist belegt, aber nur moderat (Überlebensverlängerung von etwa 2–3 Monaten laut den Übersichtsarbeiten).

Ob sich dieser Mechanismus auf die Polymikrogyrie übertragen lässt, ist spekulativ. Man könnte vermuten, dass eine Hyperexzitabilität im Zusammenhang mit kortikalen Malformationen eine Rolle spielt. Die vorliegenden Daten stützen diese Annahme jedoch nicht. Der sehr hohe Modellwert (0,9999) ist eine rein rechnerische Vorhersage ohne klinische oder literaturbasierte Absicherung.

Auch die übrigen Top-10-Vorhersagen sind überwiegend reine Modellvorhersagen. Einige Motoneuron-Erkrankungen (z. B. spätadulte Erkrankung des unteren Motoneurons, monomelische Amyotrophie, genetische ALS-Subtypen) liegen mechanistisch näher an der ursprünglichen Indikation, sind aber ebenfalls ohne Studien- oder Literaturbelege.

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur zur vorhergesagten Indikation (Rang 1) vor.

Hinweis: Die umfangreichere Literatur im Datensatz betrifft den Vorhersageeintrag „ALS, Suszeptibilität", also die bereits zugelassene Indikation und keine echte Neuindikation. Sie besteht überwiegend aus Übersichtsarbeiten und mechanistischen Arbeiten, etwa zur Glutamat-Exzitotoxizität (PMID 9178165), sowie einer Assoziationsstudie zu CYP2D6-Varianten bei ALS (PMID 42161327, 2026).

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002622 | Riluzole Zentiva | – | Amyotrophe Lateralsklerose |
| EMEA/H/C/000109 | Rilutek | – | Amyotrophe Lateralsklerose |

Beide Zulassungen sind aufgehoben; aktuell gibt es keine gültige Zulassung.

## Sicherheitsaspekte

- **Kontraindikationen/Risikokonstellationen aus dem Wissensgraphen (PrimeKG, keine Packungsbeilagen-Angaben):** Neutropenie, Agranulozytose, Substanzmissbrauch/-abhängigkeit, Hyperbilirubinämie (auch hereditär), Gilbert-Syndrom, interstitielle Lungenerkrankung, arzneimittelbedingte Leberschädigung.
- **Leberwerte:** Laut Literatur zeigen etwa 50 % der ALS-Patienten unter oralem Riluzol erhöhte ALT-Werte (ca. 8 % über dem Dreifachen, ca. 2 % über dem Fünffachen der Obergrenze).
- **Arzneimittelwechselwirkungen:** Insgesamt 44 Wechselwirkungen erfasst. Auszug:
  - Moderat: Obeticholsäure, Naltrexon, Deferasirox, Osilodrostat, Anagrelid, Asparaginase, Brentuximab vedotin, Clofarabin, Methotrexat, Epirubicin
  - Gering: Omeprazol, Koffein, Theophyllin, Aminophyllin
  - Einstufung unbekannt: Metformin, Simvastatin, Ranitidin, Cyanocobalamin, Salbutamol, Ibuprofen

Für Warnhinweise und Kontraindikationen aus der Fachinformation liegen keine Daten vor; bitte die Packungsbeilage bzw. Fachinformation konsultieren.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage zur Polymikrogyrie beruht allein auf dem Modell (Evidenzlevel L5), ohne Studien, Literatur oder belegbaren mechanistischen Zusammenhang. Zudem besteht derzeit keine gültige Zulassung in Deutschland.

**Für ein Weiterkommen sind erforderlich:**
- Fachinformation (Warnhinweise, Kontraindikationen) aus BfArM bzw. EMA beschaffen, da die Sicherheitsprüfung sonst nicht fortgesetzt werden kann
- Detaillierte Wirkmechanismus-Daten (z. B. aus DrugBank) ergänzen
- Systematische Literatur- und Studienrecherche zu Riluzol bei kortikalen Malformationen
- Prüfung, ob die näher an ALS liegenden Vorhersagen (z. B. Erkrankung des unteren Motoneurons, monomelische Amyotrophie) als Kandidaten sinnvoller sind
- Prüfung der Schreibweise des Krankheitsnamens „amyotrohpic lateral sclerosis type 22" in der Krankheitszuordnung
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

