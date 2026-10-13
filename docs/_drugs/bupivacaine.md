---
layout: default
title: Bupivacaine
parent: Nur Modellvorhersage (L5)
nav_order: 81
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

# Bupivacain: Von akutem Schmerz zu Acrodermatitis chronica atrophicans

## Zusammenfassung in einem Satz

Bupivacain ist ein Lokalanästhetikum vom Amid-Typ und wurde ursprünglich zur Behandlung von **akutem Schmerz** eingesetzt. Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **Acrodermatitis chronica atrophicans** voraus. Für diese Vorhersage liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor, sie beruht ausschließlich auf der Modellvorhersage.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Akuter Schmerz |
| Vorhergesagte neue Indikation | Acrodermatitis chronica atrophicans |
| TxGNN-Vorhersagewert | 99,23 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung (keine gültige Zulassung) |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Derzeit liegen keine detaillierten Daten zum Wirkmechanismus vor. Bekannt ist, dass Bupivacain ein Amid-Lokalanästhetikum ist, das spannungsabhängige Natriumkanäle blockiert. Seine Wirksamkeit bei akutem Schmerz gilt als belegt.

Ein plausibler mechanistischer Zusammenhang mit der neuen Indikation lässt sich aus den vorliegenden Daten **nicht** ableiten. Die Acrodermatitis chronica atrophicans ist das späte Hautstadium der Lyme-Borreliose und erfordert eine antibiotische Behandlung. Ein Lokalanästhetikum hat bei der zugrunde liegenden Infektion keine plausible Rolle. Der hohe TxGNN-Wert (0,992) ist eine reine Modellvorhersage ohne klinische oder literarische Stützung.

Weitere vom Modell vorhergesagte Indikationen sind ebenfalls ohne belegten mechanistischen Zusammenhang und ohne Studien oder Publikationen:

| Rang | Vorhergesagte Indikation | TxGNN-Wert | Evidenzgrad | Einschätzung |
|------|------|------|------|------|
| 2 | Neonatale Dermatomyositis | 99,15 % | L5 | Hold. Immunvermittelte Erkrankung. Bupivacain ist in hohen lokalen Konzentrationen myotoxisch, zudem bestehen Sicherheitsbedenken bei Neugeborenen (systemische Toxizität von Lokalanästhetika). |
| 3 | Sekundäre interstitielle Lungenerkrankung des Kindesalters bei Bindegewebserkrankung | 99,11 % | L5 | Hold. Die Therapie beruht auf Immunsuppression. Der hohe Wert spiegelt vermutlich die Nähe im Netzwerk wider, nicht eine pharmakologische Begründung. |
| 4 | Amyopathische Dermatomyositis | 99,03 % | L5 | Hold. Allenfalls symptomatische Linderung lokaler Schmerzen oder von Juckreiz, keine Repurposing-Indikation. |

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/004586 | Exparel liposomal | – | Akuter Schmerz |

Diese Zulassung ist erloschen. Der Hersteller ist Pacira Ireland Limited.

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen (PrimeKG, keine Angaben aus Fachinformationen):** Für folgende Erkrankungen sind Kontraindikations-Verknüpfungen hinterlegt: Bluthochdruck und Hypotonie, Leberversagen und Lebererkrankung, Epilepsie, COPD, Nierenerkrankung, Gallenblasenerkrankung, Hypothyreose (einschließlich Myxödem und angeborener Hypothyreose), chronisch-entzündliche Darmerkrankung, Kaliummangel, Diabetes mellitus und diabetische Ketoazidose, benigne Prostatahyperplasie, Vorhofflimmern, koronare Herzkrankheit, Myokardinfarkt, Koronarthrombose, plötzlicher Herzstillstand, Erregungsleitungsstörungen des Herzens, Hämoglobinopathie, Atemversagen, Engwinkelglaukom, Substanzmissbrauch/-abhängigkeit sowie Pyoureter.
- **Arzneimittelwechselwirkungen:** Insgesamt wurden 56 Wechselwirkungen erfasst. Als moderat eingestuft sind:
  - Aprepitant
  - Morphin (liposomal)

  Weitere erfasste Wechselwirkungen ohne Schweregrad-Einstufung sind unter anderem Pantoprazol, Omeprazol, Lansoprazol, Vancomycin, Atropin, Prednison, Prednisolon, Dexamethason, Hydrocortison, Triamcinolon, Simvastatin, Kaliumchlorid, Ranitidin, Famotidin, Ondansetron, Metoclopramid, Metronidazol und Naloxon.

Hinweise und Gegenanzeigen aus der Fachinformation lagen nicht vor. Bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf einem Modellwert (Evidenzgrad L5) ohne Studien oder Publikationen. Ein mechanistischer Zusammenhang ist nicht erkennbar, da die Acrodermatitis chronica atrophicans eine antibiotisch zu behandelnde Infektion ist. In Deutschland besteht zudem keine gültige Zulassung.

**Für ein Weiterkommen sind erforderlich:**
- Auswertung der Fachinformation (Warnhinweise und Gegenanzeigen) für die Sicherheitsprüfung
- Daten zum Wirkmechanismus (MOA), z. B. aus DrugBank
- Präklinische oder klinische Belege für einen plausiblen Wirkzusammenhang
- Prüfung der Anwendungswege und der Verträglichkeit in der Zielpopulation
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

