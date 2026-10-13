---
layout: default
title: Tenecteplase
parent: Nur Modellvorhersage (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: Vom Myokardinfarkt zum posterolateralen Myokardinfarkt

## Zusammenfassung

Tenecteplase ist ein fibrinspezifischer Gewebeplasminogenaktivator (Thrombolytikum), der ursprünglich zur Behandlung des Myokardinfarkts zugelassen wurde.
Das TxGNN-Modell sagt voraus, dass er bei **posterolateralem Myokardinfarkt** wirksam sein könnte. Hierfür liegen jedoch **keine klinischen Studien** und **keine spezifischen Publikationen** vor. Es handelt sich um einen Untertyp der bereits zugelassenen Indikation und nicht um ein echtes Repurposing-Signal.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Myokardinfarkt |
| Vorhergesagte neue Indikation | Posterolateraler Myokardinfarkt |
| TxGNN-Vorhersagewert | 99,87 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Tenecteplase ist ein fibrinspezifischer Plasminogenaktivator, der Koronarthromben auflöst. Seine Wirksamkeit beim Myokardinfarkt ist etabliert, und mechanistisch ist er auf thrombotische Koronarverschlüsse übertragbar.

Der posterolaterale Myokardinfarkt ist ein anatomischer Untertyp des bereits zugelassenen Myokardinfarkts. Der hohe TxGNN-Wert spiegelt vor allem die Nähe zur ursprünglichen Indikation wider und stellt kein eigenständiges Repurposing-Signal dar.

Auch die weiteren Vorhersagen (posteroinferiorer und septaler Infarkt) sind Untertypen der Zulassungsindikation. Für Krankheiten wie Chromosom-16-Deletion, Beta-Thalassämie, Pyruvatkinase-Mangel oder hereditäre Pyropoikilozytose besteht kein plausibler Mechanismus; diese Werte sind vermutlich Artefakte des Wissensgraphen. Beim Koronarstenosen-Kandidaten (Rang 5) ist die Evidenz auf Stufe L3 klein und heterogen. Hier ist am ehesten eine intrakoronare Anwendung bei PCI oder Stentthrombose denkbar, nicht aber bei fixierter Stenose.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literatur

Für den posterolateralen Myokardinfarkt liegen derzeit keine zugehörigen Publikationen vor.

Zur Einordnung: Für den septalen Myokardinfarkt (Rang 3) und die Koronarstenose (Rang 5) wurden nur indirekte Arbeiten gefunden. Die relevantesten sind:

| PMID | Jahr | Typ | Journal | Kernaussage |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Randomisierte Machbarkeitsstudie (n=40) | Am J Cardiol | Niedrig dosiertes intrakoronares Tenecteplase während primärer PCI bei STEMI: Machbarkeit und Sicherheit (ICE T-TIMI 49) |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | Klinische Studie | J Am Coll Cardiol | CAPITAL AMI: Tenecteplase-gestützte Angioplastie vs. alleinige Thrombolyse bei Hochrisiko-STEMI |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | Kleine klinische Studie | J Am Coll Cardiol | Intrakoronare fibrinspezifische Lyse zur Erleichterung der Rekanalisation chronischer Totalverschlüsse |
| [23975441](https://pubmed.ncbi.nlm.nih.gov/23975441/) | 2014 | Fallserie | J Thromb Thrombolysis | Wirksamkeit und Sicherheit von Tenecteplase bei Lungenembolie (30 Patienten, indirekt) |
| [42220791](https://pubmed.ncbi.nlm.nih.gov/42220791/) | 2026 | Fallbericht | Cureus | Ventrikelseptumruptur trotz früher pharmako-invasiver Reperfusion bei Vorderwand-STEMI (Sicherheitssignal) |

---

## Marktinformationen Deutschland

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000306 | Metalyse | – | Myokardinfarkt |

Die Zulassung ist erloschen (Status: cancelled). Hersteller: Boehringer Ingelheim International GmbH.

---

## Sicherheitsaspekte

- **Arzneimittelwechselwirkungen**: In den Daten sind 100 Wechselwirkungen erfasst. Wichtige Beispiele:
  - **Schwerwiegend (Major)**: Abciximab, Apixaban, Betrixaban, Acalabrutinib, Avapritinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab. Meist handelt es sich um Substanzen mit erhöhtem Blutungsrisiko.
  - **Moderat**: Acetylsalicylsäure, Ibuprofen, Ketorolac, Celecoxib, Aminocapronsäure, Omega-3-Fettsäuren, Fenfluramin, Dexfenfluramin, Sibutramin.
- **Sicherheitssignal aus der Literatur**: Ein Fallbericht (2026) beschreibt eine mechanische Komplikation (Ventrikelseptumruptur) nach Reperfusion.

Angaben zu Warnhinweisen und Gegenanzeigen aus der Fachinformation liegen nicht vor; bitte die Fachinformation konsultieren.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Der posterolaterale Myokardinfarkt ist ein Untertyp der bereits zugelassenen Indikation. Es gibt weder Studien noch spezifische Literatur, und der hohe Vorhersagewert ist kein echtes Repurposing-Signal. Zudem ist die deutsche Zulassung erloschen. Die Evidenz beschränkt sich auf eine reine Modellvorhersage (L5).

**Für ein Weiterkommen sind erforderlich:**
- Auswertung der Fachinformation (Warnhinweise, Gegenanzeigen), da dies derzeit die Sicherheitsprüfung blockiert
- Daten zum Wirkmechanismus (z. B. aus DrugBank)
- Klärung, ob der Fokus eher auf Kandidaten mit echtem Repurposing-Potenzial liegen sollte, etwa der intrakoronaren Anwendung bei Koronarverschluss durch Thrombus (Evidenzstufe L3), und gezielte Recherche dazu
- Klärung des Zulassungs- und Marktstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

