---
layout: default
title: Granisetron
parent: Nur Modellvorhersage (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Granisetron: vorhergesagte neue Indikation Manische bipolare affektive Störung (Evidenzstufe L5). Ursprüngliche Indikation: Erbrechen"
monitor_inn: "GRANISETRON"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **10** 
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

# Granisetron: Von Erbrechen bei Krebserkrankungen zu manischer bipolarer affektiver Störung

## Zusammenfassung

Granisetron ist ein selektiver 5-HT3-Rezeptor-Antagonist, der ursprünglich zur Behandlung von Erbrechen im Zusammenhang mit Krebserkrankungen zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **manischer bipolarer affektiver Störung** wirksam sein könnte.
Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor; die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Erbrechen; Krebserkrankung |
| Vorhergesagte neue Indikation | Manische bipolare affektive Störung |
| TxGNN-Vorhersagewert | 99,62 % |
| Evidenzniveau | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 (erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Detaillierte Daten zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten nicht vor. Bekannt ist, dass Granisetron ein selektiver 5-HT3-Rezeptor-Antagonist ist. Seine Wirksamkeit gegen Erbrechen ist etabliert; mechanistisch könnte er auch bei manischer bipolarer Störung eine Rolle spielen.

Bei Manie wird eine Dysregulation des serotonergen und dopaminergen Systems diskutiert. 5-HT3-Antagonisten wie Ondansetron wurden bereits als Zusatztherapie bei psychiatrischen Erkrankungen untersucht. Der Zusammenhang zur ursprünglichen Indikation (Übelkeit/Erbrechen) ist gering; er beschränkt sich auf den gemeinsamen Zielrezeptor.

Der hohe TxGNN-Wert (0,996) ist eine rein rechnerische Vorhersage. Klinische Belege fehlen, daher bleibt die Verbindung hypothetisch.

Weitere vorhergesagte Indikationen (jeweils L5, jeweils ohne Studien oder Literatur):

| Rang | Indikation | TxGNN-Wert | Plausibilität des Mechanismus |
|------|------|------|------|
| 2 | Tourette-Syndrom | 99,52 % | Plausibel, aber hypothetisch (dopaminerg/serotonerg) |
| 3 | Akute ansteckende Konjunktivitis | 99,49 % | Kein erkennbarer Mechanismus |
| 4 | Angioödem | 99,36 % | Spekulativ |
| 5 | Allergische Urtikaria | 99,32 % | Indirekt, spekulativ |
| 6 | Nephrogenes Syndrom der inadäquaten Antidiurese | 99,32 % | Schwach |
| 7 | Trichotillomanie | 99,23 % | Plausibel, aber indirekt |
| 8 | Bronchitis | 99,18 % | Schwach, indirekt |
| 9 | Kälteurtikaria | 99,10 % | Spekulativ |
| 10 | Konjunktivitis | 99,09 % | Kein etablierter Mechanismus |

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum Markt in Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/002296 | Sancuso (Grünenthal GmbH) | – | Erbrechen; Krebserkrankung (Status: erloschen) |

---

## Sicherheitsaspekte

- **Kontraindikationen aus dem Wissensgraphen** (aus Wissensgraph-Beziehungen, nicht aus dem Beipackzettel): Long-QT-Syndrom, familiäres Long-QT-Syndrom, Kaliummangel, plötzlicher Herzstillstand, Erregungsleitungsstörungen des Herzens. Es besteht damit ein Signal für kardiale Risiken (QT-Verlängerung).
- **Arzneimittelwechselwirkungen**: Abfrage abgeschlossen, 100 Wechselwirkungen erfasst (Auszug von 20 dargestellt). Als **schwerwiegend (Major)** eingestuft:
  - Opioide: Fentanyl, Alfentanil, Tramadol
  - Triptane: Almotriptan, Sumatriptan
  - Dextromethorphan
  - QT-relevante/Antiarrhythmika und Psychopharmaka: Amiodaron, Amisulprid, Amitriptylin, Anagrelid
  
  Als **moderat** eingestuft u. a.: Abametapir (topisch), Abirateron, Dihydrocodein, Codein, Famotidin, Formoterol, Adenosin, Salbutamol, Alfuzosin, Propofol.

Für weitere Sicherheitsinformationen (Warnhinweise, Gegenanzeigen) siehe die Fachinformation.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage stützt sich ausschließlich auf das Modell (L5), ohne klinische Studien oder Publikationen. Zudem ist die einzige deutsche Zulassung erloschen, und das kardiale Sicherheitssignal (QT-Verlängerung) sowie zahlreiche schwerwiegende Wechselwirkungen, insbesondere mit Psychopharmaka, erfordern Vorsicht.

**Für ein Weiterkommen sind erforderlich:**
- Systematische Literaturrecherche und Prüfung von Studienregistern zu Granisetron bei Manie
- Daten zum Wirkmechanismus (MOA)
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM)
- Bewertung des QT-Risikos und der Wechselwirkungen bei Kombination mit Stimmungsstabilisierern und Antipsychotika
- Klärung der Verfügbarkeit und Darreichungsform (Zulassung erloschen)
- Gegebenenfalls Priorisierung plausiblerer Indikationen (z. B. Tourette-Syndrom, Trichotillomanie) für eine erste Evidenzprüfung
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

