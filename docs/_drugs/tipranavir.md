---
layout: default
title: Tipranavir
parent: Nur Modellvorhersage (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: Von der HIV-1-Infektion zum Felinen Immundefekt-Syndrom

## Zusammenfassung in einem Satz

Tipranavir ist ein nicht-peptidischer HIV-1-Proteasehemmer, der klinisch (in Kombination mit Ritonavir) zur Behandlung therapieerfahrener HIV-1-Infektionen eingesetzt wird. Die Top-Vorhersage des TxGNN-Modells ist das **Feline Immundefekt-Syndrom (FIV)**, eine veterinärmedizinische Retrovirus-Erkrankung bei Katzen – **ohne klinische Studien und ohne Literatur**, die dies derzeit als Gelegenheit zur Wiederverwendung beim Menschen stützt. Das Modell scheint eher strukturelle Homologien zwischen tierartübergreifenden Retroviralen Proteasen zu erfassen, als ein verwertbares klinisches Signal zu identifizieren.

---

## Schnellübersicht

| Eintrag | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Nicht im Evidenzpaket angegeben (klinisch bekannt: HIV-1-Infektion, therapieerfahrene Erwachsene, verwendet mit Ritonavir-Verstärkung) |
| Vorhergesagte neue Indikation | Felines Immundefekt-Syndrom (veterinärmedizinisch) |
| TxGNN-Vorhersage-Score | 99.99% (Rang 215 von der vollständigen Krankheitsliste) |
| Evidenzstufe | L5 (nur Modellvorhersage, keine stützenden Studien oder Literatur) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Abwartend |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad). Basierend auf bekannten Informationen ist Tipranavir ein nicht-peptidischer HIV-1-Proteasehemmer, der mit Ritonavir verabreicht wird; seine Wirksamkeit bei therapieerfahrenen HIV-1-Infektionen ist gut etabliert.

Die Top-bewertete vorhergesagte Indikation, das Feline Immundefekt-Syndrom (FIV), ist eine **veterinärmedizinische Retrovirus-Erkrankung**, keine menschliche Erkrankung. Die Begründung des Modells vermerkt explizit, dass die hohe Punktzahl wahrscheinlich die strukturelle Homologie zwischen den FIV- und HIV-Proteasen (ein tierartübergreifender Retrovirus-Mechanismus) widerspiegelt, eher als eine tatsächliche therapeutische Gelegenheit beim Menschen – die Quelldaten selbst besagen, dass dies „keinen praktischen Wert für die Wiederverwendung von Arzneimitteln hat".

Dasselbe Muster gilt für die meisten anderen Top-10-Vorhersagen: Simiane Immunodefekt-Virus-Infektion (Forschungstiermodell), eine seltene neuronale Entwicklungsstörung, familiäre Hyperlipidämie (wahrscheinlich eine bekannte Nebenwirkung des Proteasehemmers widerspiegelnd, eher als eine behandelbare Indikation), und mehrere nicht verwandte benigne Neoplasien (Prostatafibrom, Brenner-Tumor, Phyllodes-Tumor) – alle intern als Rauscheinbettung ohne biologische Plausibilität gekennzeichnet. Zwei Ausnahmen stechen hervor: **AIDS-assoziierter Komplex** (Rang 6, Evidenzstufe L4) ist mechanistisch kohärent, da er sich im gleichen HIV/AIDS-Krankheitsspektrum befindet, das Tipranavir bereits behandelt, obwohl keine Studien zu diesem älteren Begriff gefunden wurden; und **kongenitale HIV-Infektion** (Rang 5) ist mit 9 klinischen Studien verbunden, aber diese befassen sich alle mit anderen antiretroviralen Therapieschema (cabotegravir/rilpivirine, dolutegravir, Maraviroc-Klasse-CCR5-Antagonisten), eher als mit Tipranavir selbst, daher unterstützen sie nicht direkt eine neue Indikation für dieses Arzneimittel.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien für die vorhergesagte Indikation registriert (Felines Immundefekt-Syndrom).

---

## Literaturenevidenz

Derzeit ist keine zugehörige Literatur für die vorhergesagte Indikation verfügbar (Felines Immundefekt-Syndrom).

---

## Marktstatus Deutschland

Derzeit sind keine Marktgenehmigungen für Tipranavir registriert (0 Lizenzen erfasst; Marktstatus: nicht vermarktet).

---

## Sicherheitsüberlegungen

Bitte konsultieren Sie die Gebrauchsinformation für Sicherheitsinformationen. *(Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind derzeit nicht verfügbar – Das Abrufen des TFDA-Labels ist als Blockierungsdatenlücke gekennzeichnet.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwartend**

**Begründung:**
Die Top-bewertete vorhergesagte Indikation (Feliner AIDS) ist eine veterinärmedizinische Erkrankung ohne klinische Studien, ohne Literatur und mit einem ausdrücklichen mechanistischen Vorbehalt, dass sie keinen praktischen Wiederverwendungswert beim Menschen hat. Aus der aktuellen Vorhersage-Reihe geht keine klinisch verwertbare, ausreichend belegte menschliche Indikation hervor.

**Um fortzufahren, ist Folgendes erforderlich:**
- Abrufen des TFDA-genehmigten Labels (Warnhinweise/Kontraindikationen) – derzeit eine Blockierungslücke (DG001)
- Bestätigung der Wirkmechanismus-Daten von DrugBank beschaffen – derzeit eine Datenlücke mit hohem Schweregrad (DG002)
- Bei weiterer Verfolgung der Wiederverwendung sollte die Bewertung auf die mechanistisch kohärenteren Kandidaten im gleichen Krankheitsspektrum umgeleitet werden (z. B. „AIDS-assoziierter Komplex"), eher als die Top-TxGNN-bewerteten, aber biologisch implausiblen/tierartübergreifenden Vorhersagen
- Unabhängig überprüfen, ob tipranavir-spezifische Studien für HIV-Spektrum-Subindikationen existieren, da die derzeit mit „kongenitaler HIV-Infektion" verknüpften Studien andere antiretrovirale Mittel betreffen, nicht Tipranavir selbst

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

