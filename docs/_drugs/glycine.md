---
layout: default
title: Glycine
parent: Nur Modellvorhersage (L5)
nav_order: 216
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Glycin: Von der Ahornsirupkrankheit zur Erkrankung der Nasenhöhle

## Zusammenfassung

Glycin (Handelsname Maapliv) wurde ursprünglich zur Behandlung der Ahornsirupkrankheit (Maple Syrup Urine Disease) zugelassen.
Das TxGNN-Modell sagt voraus, dass es bei **Erkrankungen der Nasenhöhle** wirksam sein könnte.
Die Evidenz ist jedoch sehr schwach: Es liegt **1 klinische Studie** (ohne therapeutische Relevanz) und **2 Publikationen** (Grundlagenforschung ohne Bezug zu Glycin) vor.

## Kurzübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Ahornsirupkrankheit (Maple Syrup Urine Disease) |
| Vorhergesagte neue Indikation | Erkrankung der Nasenhöhle (nasal cavity disease) |
| TxGNN-Vorhersagewert | 99,85 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung (nicht mehr vermarktet) |
| Anzahl der Zulassungen | 1 (davon 0 gültig, 1 erloschen) |
| Empfohlene Entscheidung | Hold |

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus von Glycin liegen derzeit nicht vor. Glycin ist eine körpereigene Aminosäure und wurde bei der Ahornsirupkrankheit eingesetzt. Ein belastbarer mechanistischer Zusammenhang zu Erkrankungen der Nasenhöhle lässt sich aus den vorliegenden Daten nicht herleiten.

Der hohe Vorhersagewert (0,998) beruht ausschließlich auf einer modellbasierten Vorhersage. Allgemein wird Glycin eine entzündungshemmende bzw. zellschützende Wirkung zugeschrieben, doch für diese Indikation wird dies durch die vorliegenden Daten nicht gestützt. Die Ähnlichkeit zwischen ursprünglicher und neuer Indikation ist nicht bewertet.

Die zweitplatzierte Vorhersage, die akute Laryngopharyngitis (Wert 99,84 %), hat weder klinische Studien noch Literatur und ist ebenfalls nur modellbasiert.

## Klinische Evidenz

| Studiennummer | Phase | Status | Teilnehmerzahl | Kernaussagen |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Abgeschlossen | 25 | Bildgebungsstudie (PET/CT bzw. PET/MRI) mit dem Radiotracer 18F-FPPRGD2 zur Erfassung der αvβ3-Integrin-Expression als Angiogenese-Biomarker bei Krebspatienten. Glycin wird nicht als Therapie geprüft; kein Beleg für Repurposing. |

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Grundlagenforschung (Veterinärhistochemie) | Veterinary Pathology | Lektin-Histochemie der normalen und herpesvirus-infizierten Nasenschleimhaut beim Rind; kein Bezug zu Glycin. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Grundlagenforschung (Wirkstoffabgabe/Materialien) | Chemical & Pharmaceutical Bulletin | Oligoarginin-Polymere als mukosale Adjuvantien für die nasale Impfung bei Mäusen; kein Bezug zu Glycin. |

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/005557 (erloschen) | Maapliv | – | Ahornsirupkrankheit (Maple Syrup Urine Disease) |

## Sicherheitsaspekte

Aus der Wissensgraph-Analyse (TxGNN/PrimeKG, keine Packungsbeilagen-Angaben) ergeben sich Hinweise auf mögliche Kontraindikationen bei folgenden Erkrankungen:

- **Nieren- und Harnwege:** Nierenerkrankung, chronische Niereninsuffizienz, terminale Niereninsuffizienz, Nephrolithiasis, Nephrokalzinose, akute Uratnephropathie, Pyourether
- **Calcium-/Phosphat-/Knochenstoffwechsel:** Hyperkalzämie, humorale Hyperkalzämie bei Malignomen, Hyperparathyreoidismus, Osteitis fibrosa, Störungen des Phosphorstoffwechsels, Hyperphosphatämie, lytische Knochenmetastasen, Hypervitaminose
- **Herz-Kreislauf:** Herzerkrankung, Herz-Kreislauf-Erkrankung, Arteriosclerosis obliterans, Digitalisvergiftung, Kammerflimmern
- **Weitere:** Sarkoidose, Obstipation, Phenylketonurie, Störungen des Phenylalanin-Stoffwechsels

Diese Angaben stammen aus Modellbeziehungen und müssen anhand der Fachinformation überprüft werden.

Für Arzneimittelwechselwirkungen wurden keine Einträge gefunden. Für weitere Sicherheitsinformationen siehe die Packungsbeilage.

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das TxGNN-Modell (Evidenzgrad L5). Die einzige Studie und beide Publikationen haben keinen Bezug zu Glycin als Therapie, und die deutsche Zulassung ist erloschen.

**Für ein Weiterkommen sind folgende Schritte nötig:**
- Auswertung der Packungsbeilage (Warnhinweise und Gegenanzeigen) von der BfArM-Website, da dies derzeit den Sicherheits-Screening-Schritt blockiert
- Daten zum Wirkmechanismus (MOA), z. B. über die DrugBank-API
- Gezielte Literatur- und Studienrecherche zu Glycin bei Erkrankungen der Nasenhöhle bzw. Laryngopharyngitis
- Prüfung der Applikationswege (lokal/nasal), da die Routenkompatibilität noch nicht bewertet ist
- Klärung der Ähnlichkeit zwischen ursprünglicher und neuer Indikation
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

