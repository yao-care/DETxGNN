---
layout: default
title: Ceftolozane
parent: Nur Modellvorhersage (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Ceftolozane
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

# Ceftolozan: Von bakteriellen Infektionen zu Ureaplasma-Urethritis

## Zusammenfassung

Ceftolozan ist ein Cephalosporin-Antibiotikum, das ursprünglich zur Behandlung bakterieller Infektionen zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass es bei **Ureaplasma-Urethritis** wirksam sein könnte.
Dafür liegen jedoch **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Bakterielle Infektionen |
| Vorhergesagte neue Indikation | Ureaplasma-Urethritis |
| TxGNN-Vorhersagewert | 99,89 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung (keine gültige Zulassung) |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Ceftolozan gehört zu den Beta-Lactam-Antibiotika (Cephalosporine) und hemmt die bakterielle Zellwandsynthese. Seine Wirksamkeit bei bakteriellen Infektionen ist belegt, vor allem gegen *Pseudomonas aeruginosa* und Enterobacterales.

Für Ureaplasma-Urethritis ist die Vorhersage **mechanistisch nicht gestützt**: Ureaplasmen besitzen keine Zellwand, daher ist von Beta-Lactamen keine Wirkung zu erwarten. Der hohe Score spiegelt wahrscheinlich nur die allgemeine Assoziation mit „bakterieller Infektion“ wider.

Etwas plausiblere, aber ebenfalls unbelegte Kandidaten unter den weiteren Vorhersagen sind:
- **Gonokokken-Urethritis** (Score 99,89 %): Cephalosporine sind eine etablierte Klasse gegen *Neisseria gonorrhoeae*, Ceftolozan ist jedoch hauptsächlich gegen Pseudomonaden und Enterobacterales aktiv; Daten fehlen.
- **Entzündliche Uteruserkrankung** (99,88 %): Infektionen sind oft polymikrobiell, Ceftolozan (mit Tazobactam) wirkt gegen gramnegative Erreger und einige Anaerobier; Belege fehlen.
- **Xanthogranulomatöse Pyelonephritis** (99,88 %): Die Erreger (z. B. *Proteus*, *E. coli*) liegen im Wirkspektrum, die Erkrankung wird aber meist chirurgisch behandelt.

Die übrigen Vorhersagen (z. B. polyklonales Hyperviskositätssyndrom, Hyperamylasämie, kongenitale Analbuminämie, Blutgruppeninkompatibilität, prämaligne hämatologische Erkrankungen) haben keinen erkennbaren infektiösen Mechanismus und sind vermutlich Artefakte des Wissensgraphen. Bei der urogenitalen Tuberkulose ist die mechanistische Basis wegen der intrinsischen Beta-Lactam-Resistenz von *M. tuberculosis* schwach.

---

## Klinische Evidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Für die Top-Vorhersage (Ureaplasma-Urethritis) liegt keine Literatur vor. Für die viertplatzierte Vorhersage wurde lediglich eine allgemeine Übersichtsarbeit gefunden:

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Review | Current Opinion in Infectious Diseases | Allgemeiner Überblick über febrile Harnwegsinfektionen, Pyelonephritis und Urosepsis; kein spezifischer Beleg für Ceftolozan oder xanthogranulomatöse Pyelonephritis |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/003772 (erloschen) | Zerbaxa | – | Bakterielle Infektionen |

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: Insgesamt 11 Wechselwirkungen mit mittlerem Schweregrad (Moderate) wurden identifiziert:
  - Aminoglykoside: Kanamycin, Neomycin, Streptomycin, Amikacin (auch liposomal), Gentamicin
  - Antikoagulanzien: Warfarin, Dicoumarol
  - Weitere: Chloramphenicol, Ethinylestradiol, Mycophenolsäure

Für Warnhinweise und Gegenanzeigen liegen keine Daten vor; bitte die Fachinformation heranziehen.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage beruht ausschließlich auf dem Modell (Evidenzniveau L5), es gibt weder Studien noch Literatur. Zudem fehlt Ureaplasmen die Zellwand, sodass ein Beta-Lactam mechanistisch nicht wirksam sein dürfte. Hinzu kommt, dass die einzige Zulassung in Deutschland erloschen ist.

**Für ein Weiterkommen wäre erforderlich:**
- Daten zu Warnhinweisen und Gegenanzeigen aus der Fachinformation (derzeit blockierend für das Sicherheits-Screening)
- Detaillierte Wirkmechanismus-Daten (MOA)
- Prüfung alternativer Kandidaten mit plausiblerem Mechanismus (z. B. Gonokokken-Urethritis, entzündliche Uteruserkrankung) inklusive In-vitro-Empfindlichkeitsdaten
- Klärung der Zulassungs- und Verfügbarkeitssituation in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

