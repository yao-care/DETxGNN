---
layout: default
title: Ibuprofen
parent: Nur Modellvorhersage (L5)
nav_order: 225
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Ibuprofen: vorhergesagte neue Indikation Akromesomele Dysplasie, Typ Hunter-Thompson (Evidenzstufe L5). Ursprüngliche Indikation: Persistierender Ductus arteriosus (Ductus Arteriosus, Patent)"
monitor_inn: "IBUPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Ibuprofen
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **7** 
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

## Ibuprofen: Akromesomele Dysplasie, Typ Hunter-Thompson
{: .text-alpha }

## Zusammenfassung in einem Satz

Ibuprofen ist ein nicht-selektiver COX-Hemmer, der in der EU zur Behandlung des persistierenden Ductus arteriosus (PDA) zugelassen war.
Das TxGNN-Modell sagt vorher, dass er bei der **akromesomelen Dysplasie, Typ Hunter-Thompson** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Persistierender Ductus arteriosus (Ductus Arteriosus, Patent) |
| Vorhergesagte neue Indikation | Akromesomele Dysplasie, Typ Hunter-Thompson |
| TxGNN-Vorhersagewert | 0,9974 |
| Evidenzlevel | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 2 von 2) |
| Anzahl der Zulassungen | 2 (gültig: 2) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Ibuprofen ein nicht-selektiver Hemmer von COX-1 und COX-2 ist und damit die Prostaglandinsynthese reduziert. Beim PDA nutzt man diesen Effekt, um den Verschluss des Ductus anzustoßen.

Die akromesomele Dysplasie vom Typ Hunter-Thompson ist eine Skelettdysplasie, die durch Funktionsverlust-Varianten im GDF5-Gen (BMP-Signalweg) verursacht wird. Ein etablierter mechanistischer Zusammenhang mit der COX-Hemmung besteht nicht, und die Daten stützen keine Beteiligung von Prostaglandinen an dieser Erkrankung. Ein möglicher Nutzen wäre allenfalls symptomatisch (Schmerzlinderung), nicht krankheitsmodifizierend.

Der hohe TxGNN-Wert (0,9974) ist daher eine reine Vorhersage des TxGNN-Modells (Deep Learning) und sollte nicht als Hinweis auf Wirksamkeit gewertet werden.

Weitere Vorhersagen des Modells (alle Evidenzlevel L5, alle ohne Studien oder Literatur, Empfehlung jeweils Hold):

| Rang | Erkrankung | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Brachyolmie-Amelogenesis-imperfecta-Syndrom | 0,9971 | Kein etablierter Mechanismus |
| 3 | Myosklerose | 0,9968 | Allenfalls symptomatisch (Schmerz/Entzündung) |
| 4 | Brachyolmie | 0,9967 | Kein etablierter Mechanismus |
| 5 | Brachydaktylie-Syndaktylie-Syndrom | 0,9966 | Kein plausibler Mechanismus; NSAR mit entwicklungs- und fetaltoxikologischen Vorbehalten |
| 6 | Pseudoachondroplasie | 0,9966 | Nur symptomatisch bei Gelenkschmerzen |
| 7 | Kolobomatöse Mikrophthalmie-rhizomele-Dysplasie-Syndrom | 0,9960 | Kein COX-bezogener Mechanismus |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/006129 | Ibuprofen Gen.Orph | – | Persistierender Ductus arteriosus |
| EMEA/H/C/000549 | Pedea | – | Persistierender Ductus arteriosus |

Beide Zulassungen sind gültig; das Arzneimittel ist in Deutschland im Handel.

---

## Sicherheitsaspekte

- **Wissensgraph-basierte Kontraindikationen** (aus Arzneimittel-Krankheits-Beziehungen, nicht aus Fachinformationstexten): u. a. Bluthochdruck, Leberversagen und Lebererkrankungen, Nierenerkrankungen, Epilepsie, COPD, Thrombozytopenie, Magengeschwür, chronisch-entzündliche Darmerkrankungen, systemischer Lupus erythematodes, Diabetes mellitus, Gerinnungsstörungen, Schlaganfall und zerebrovaskuläre Erkrankungen, Herzinfarkt, Hypothyreose, Kaliummangel, benigne Prostatahyperplasie sowie Substanzabhängigkeit.
- **Arzneimittelwechselwirkungen** (100 Einträge in der Abfrage, hier eine Auswahl):
  - **Schwerwiegend (Major):** Acetylsalicylsäure
  - **Moderat:** Kortikosteroide (Betamethason, Budesonid, Dexamethason, Hydrocortison), Sulfonylharnstoffe (Acetohexamid, Chlorpropamid, Glimepirid, Glipizid, Glyburid), Exenatid, Aprepitant, Balsalazid, Fenfluramin, Dexfenfluramin, Kanamycin, Levofloxacin
  - **Gering (Minor):** Famotidin, Ranitidin, Cimetidin
- **Hinweis zu Entwicklungsrisiken:** Für das Brachydaktylie-Syndaktylie-Syndrom gelten NSAR-bedingte Vorbehalte zur Entwicklungs- und Fetalsicherheit.

Angaben aus der Fachinformation (Warnhinweise, Gegenanzeigen) liegen nicht vor; bitte die Fachinformation zu Rate ziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert, ohne klinische Studien, Publikationen oder plausiblen Wirkmechanismus. Das Arzneimittel ist in Deutschland zwar im Handel (2 von 2 Zulassungen gültig), die Sicherheitsdaten sind jedoch unvollständig.

**Für ein Weiterverfolgen sind erforderlich:**
- Fachinformation (Warnhinweise und Gegenanzeigen) der zuständigen Behörde beschaffen und auswerten, da dies die Sicherheitsprüfung derzeit blockiert
- Daten zum Wirkmechanismus (MOA) ergänzen
- Präklinische oder mechanistische Belege für eine Rolle des Prostaglandin-/COX-Signalwegs bei der Zielerkrankung (GDF5/BMP-Signalweg) erarbeiten
- Prüfung der Routen- bzw. Darreichungsform-Kompatibilität und der Ähnlichkeit zur ursprünglichen Indikation (derzeit offen)
- Klärung des Zulassungsstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

