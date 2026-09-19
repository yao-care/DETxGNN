---
layout: default
title: Imiglucerase
parent: Nur Modellvorhersage (L5)
nav_order: 199
evidence_level: L5
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Imiglucerase: Von der Gaucher-Krankheit zum Hurler-Syndrom

## Zusammenfassung in einem Satz

> Imiglucerase ist eine rekombinante humane Glukozerebrosidasen, die als Enzymersatztherapie bei der Gaucher-Krankheit eingesetzt wird.
> TxGNN sagt eine mögliche neue Indikation für **Hurler-Syndrom** (MPS I) mit einer Punktzahl von **99.52%** voraus,
> aber dies wird derzeit nur durch **0 klinische Studien** und **2 allgemeine (nicht medikamentenspezifische) Übersichtsartikel** unterstützt – die eigene Begründung des Modells kennzeichnet dies als ein wahrscheinliches Falschpositiv, das durch semantisches Clustering von „lysosomale Speicherkrankheit" angetrieben wird, nicht durch echte mechanistische Überlappung.

---

## Schnellübersicht

| Posten | Inhalt |
|--------|--------|
| Ursprüngliche Indikation | Gaucher-Krankheit (aus Literaturbelegen ermittelt; es existiert kein strukturiertes Taiwan-/deutsches Regulierungsregister) |
| Vorhergesagte neue Indikation | Hurler-Syndrom |
| TxGNN-Vorhersage-Score | 99.52% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nicht vermarktet (Nicht vermarktet) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aussetzen |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Daten zum Wirkmechanismus sind nicht im Evidence Pack vorhanden (gekennzeichnet als Datenlücke mit hohem Schweregrad). Basierend auf bekannter Pharmakologie ist Imiglucerase ein rekombinantes Analogon der humanen **Glukozerebrosidasen**, und seine etablierte Rolle ist die substratspezifische Enzymersatztherapie bei der Gaucher-Krankheit, die durch Glukozerebrosidasen-Mangel verursacht wird.

Das Hurler-Syndrom (Mukopolysaccharidose Typ I) wird durch Mangel eines **anderen Enzyms, Alpha-L-Iduronidase**, verursacht, das auf ein anderes Substrat wirkt (Glykosaminoglykane, nicht Glukocerebroside). Beide Erkrankungen gehören zur breiteren Kategorie der „lysosomalen Speicherkrankheiten", was fast sicherlich der Grund ist, warum TxGNN beide hoch zusammen bewertete – aber dies ist eine Ähnlichkeit auf Kategorien-Ebene (semantisch), keine mechanistische Verbindung auf Enzym-/Substrat-Ebene. Die zwei unterstützenden Literaturpunkte sind allgemeine Übersichten über Enzymersatztherapie bei mehreren lysosomalen Speicherkrankheiten; keiner berichtet, dass Imiglucerase speziell beim Hurler-Syndrom getestet oder wirksam ist.

**Gesamtbewertung: Die mechanistische Grundlage für diese Vorhersage ist schwach.** Im Gegensatz zu echten Repurposing-Kandidaten, bei denen ein gemeinsamer Signalweg plausibel die Wirksamkeit über mehrere Indikationen hinweg erklärt, unterscheiden sich hier die Zielenzyme und Substrate völlig, und Imiglucerase würde nicht von katalytischer Aktivität relevant für MPS I erwartet.

---

## Klinische Studienbelege

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturbelege

| PMID | Jahr | Typ | Zeitschrift | Wichtigste Erkenntnisse |
|------|------|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Übersicht (Bildgebungsmethodik) | PNAS | Allgemeine Übersicht der PET-Bildgebung für Enzymersatztherapie bei lysosomalen Speicherkrankheiten (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); nicht spezifisch für die Wirksamkeit von Imiglucerase beim Hurler-Syndrom |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Übersicht | La Revue de médecine interne | Allgemeine Übersicht der ERT-Geschichte (Alglucerase → Imiglucerase bei Gaucher-Krankheit) und deren Erweiterung auf andere LSDs; berichtet nicht über die Verwendung von Imiglucerase beim Hurler-Syndrom |

---

## Marktstatus in Deutschland

Imiglucerase hält derzeit keine Zulassung in Deutschland (0 Lizenzen auf Rekord).

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aussetzen**

**Begründung:**
- Die vorhergesagte Indikation (Hurler-Syndrom) und die anderen vier Kandidaten in diesem Evidence Pack (Scheie-Syndrom, benigne Neoplasie der Nebenniere, autosomal rezessive Ichthyose, Cholesterylester-Speicherkrankheit) sind alle mit L5 bewertet und mit einer „Aussetzen"-Empfehlung. Die medikamentenspezifische mechanistische Begründung für jeden kennzeichnet explizit Enzym-/Substrat-Nichtübereinstimmungen mit der bekannten Glukozerebrosidasen-Aktivität von Imiglucerase, was nahelegt, dass diese hohen TxGNN-Bewertungen Erkrankungs-Kategorien-Clustering („lysosomale Speicherkrankheit") widerspiegeln, eher als echte Zielüberlappung.
- Grundlegende medikamentenspezifische Daten (MOA, TFDA/Deutsche Kennzeichnungs-Warnungen und Kontraindikationen) fehlen und blockieren (DG001, DG002), daher kann dieser Kandidat nicht einmal zu einem grundlegenden Sicherheitsscreening (S1) fortschreiten, unabhängig von der Repurposing-Hypothese.

**Um fortzufahren, wird Folgendes benötigt:**
- Bestätigen Sie den vollständigen Wirkmechanismus über DrugBank (DG002 auflösen)
- Besorgen Sie sich amtliche Kennzeichnungs-Warnungen/Kontraindikationen, z. B. von einem EU/FDA-zugelassenen Produkt (DG001 auflösen, blockierend)
- Suchen Sie nach präklinischen oder biochemischen Belegen dafür, dass Imiglucerase katalytische oder Off-Target-Aktivität relevant für Alpha-L-Iduronidase-Mangel-Erkrankungen besitzt (derzeit existieren keine solchen Belege)
- Falls keine medikamentenspezifischen mechanistischen oder präklinischen Belege auftauchen, sollte dieser Kandidat als wahrscheinliches Modell-Falschpositiv herabgestuft werden, anstatt weiter vorangetrieben zu werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

