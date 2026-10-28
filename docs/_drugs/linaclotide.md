---
layout: default
title: Linaclotide
parent: Nur Modellvorhersage (L5)
nav_order: 272
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Linaclotide: vorhergesagte neue Indikation Cauda-equina-Syndrom (Evidenzstufe L5). Ursprüngliche Indikation: Reizdarmsyndrom"
monitor_inn: "LINACLOTIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
---

# Linaclotide
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

## Linaclotid: Vom Reizdarmsyndrom zum Cauda-equina-Syndrom
{: .text-alpha }

## Zusammenfassung in einem Satz

Linaclotid ist ein lokal im Darm wirkender Guanylatcyclase-C-Agonist (GC-C), der ursprünglich zur Behandlung des Reizdarmsyndroms zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **Cauda-equina-Syndrom** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor. Die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Reizdarmsyndrom |
| Vorhergesagte neue Indikation | Cauda-equina-Syndrom |
| TxGNN-Vorhersagewert | 0,9996 |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Im Handel (gültige Zulassungen: 1 von 1) |
| Anzahl der Zulassungen | 1 (gültig: 1) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel (oder nicht)?

Detaillierte Wirkmechanismus-Daten liegen in den für diesen Bericht zusammengestellten Daten nicht vor. Nach allgemeinem Wissen ist Linaclotid ein GC-C-Agonist, der im Darmepithel den intrazellulären cGMP-Spiegel erhöht. Die systemische Resorption ist minimal, die Wirkung bleibt daher weitgehend auf den Darm beschränkt.

Das Cauda-equina-Syndrom ist eine neurologische Kompressionsschädigung der lumbosakralen Nervenwurzeln. Ein plausibler Mechanismus, wie eine lokale GC-C-Agonisierung diese Erkrankung behandeln könnte, ist nicht erkennbar. Der sehr hohe TxGNN-Wert (0,9996) spiegelt vermutlich die Nähe im Netzwerk zu Darm- und Blasenfunktionsstörungen wider (Obstipation, neurogener Darm) und keinen krankheitsmodifizierenden Effekt.

Allenfalls ließe sich eine sekundäre Obstipation lindern. Das wäre Symptomkontrolle und keine Behandlung des Syndroms selbst.

**Weitere vorhergesagte Indikationen** (ebenfalls ohne Studien oder Literatur, jeweils L5 und Hold):

| Rang | Erkrankung | TxGNN-Wert | Einschätzung |
|------|------|------|------|
| 2 | Neurogene Blase (in der Ontologie als veraltet markiert) | 0,9989 | Kein belegter Mechanismus. Mögliche Verbindung über das gemeinsame Auftreten von neurogener Blase und neurogenem Darm. Der veraltete Begriff deutet zudem auf ein überholtes oder doppeltes Konzept hin. |
| 3 | Insomnie | 0,9951 | Kein glaubwürdiger Mechanismus. Wegen der vernachlässigbaren systemischen Exposition sind keine zentralen Effekte zu erwarten. Ein indirekter Nutzen durch weniger Bauchbeschwerden wäre spekulativ. |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002490 (erloschen) | Constella | – | Reizdarmsyndrom |

Hersteller: AbbVie Deutschland GmbH & Co. Es besteht eine gültige Zulassung in Deutschland (1 von 1 Zulassung gültig).

---

## Sicherheitsaspekte

**Arzneimittelwechselwirkungen:** In der Abfrage wurden insgesamt 56 Wechselwirkungen gefunden. Die Liste der übermittelten Daten enthält 20 davon.

- **Moderat:** Levonorgestrel, Ethinylestradiol, Norethisteron, Levothyroxin, Schilddrüsenextrakt (Schwein)
- **Gering:** u. a. Rabeprazol, Esomeprazol, Dexlansoprazol, Ketorolac, Ibuprofen, Diclofenac, Oxaprozin, Bromfenac, Bisacodyl, Picosulfat, Docusat, Macrogol (3350 mit Elektrolyten), Rizinusöl, Cascararinde, mikrokristalline Cellulose

Für Warnhinweise und Gegenanzeigen bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für alle drei vorhergesagten Indikationen gibt es ausschließlich Modellvorhersagen (L5) ohne Studien oder Literatur, und ein plausibler Wirkmechanismus fehlt. Das Arzneimittel ist in Deutschland mit einer gültigen Zulassung (1 von 1) im Handel.

**Für ein Weiterkommen erforderlich:**
- Fachinformation (Warnhinweise, Gegenanzeigen) beim BfArM beschaffen, da dies derzeit die Sicherheitsprüfung blockiert
- Wirkmechanismus-Daten (MOA) aus DrugBank ergänzen
- Prüfen, ob für die Vorhersagen präklinische oder klinische Hinweise existieren, etwa zu neurogener Obstipation als Symptomkontrolle
- Den veralteten Ontologiebegriff „neurogene Blase" auf ein aktuelles Konzept abbilden und die Vorhersage neu bewerten
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

