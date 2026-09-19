---
layout: default
title: Cabazitaxel
parent: Nur Modellvorhersage (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: Von Prostatakrebs – Umwidmungsbewertung (Vorhersagen ausstehend)

## Zusammenfassung in einem Satz

Cabazitaxel (Jevtana®) ist ein halbsynthetisches Taxan-Derivat, das international zur Behandlung von metastasiertem kastrationsresistentem Prostatakrebs (mCRPC) nach vorheriger Docetaxel-basierter Therapie zugelassen ist.
Dieses Evidence-Paket **enthält noch keine TxGNN-Umwidmungsvorhersagen** – die Vorhersage-Pipeline wurde aufgrund ungeklärter Datenlücken (MOA und behördliches Fachinformationsblatt) nicht abgeschlossen.
Ohne Vorhersageergebnisse kann derzeit keine neue Indication bewertet werden.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indication | Metastasierter kastrationsresistenter Prostatakrebs (mCRPC), Zweitlinienbehandlung nach Docetaxel |
| Vorhergesagte neue Indication | Nicht verfügbar – TxGNN-Vorhersagen noch nicht erstellt |
| TxGNN-Vorhersage-Score | Nicht verfügbar |
| Evidence Level | L5 (Modellvorhersagen noch nicht durchgeführt) |
| Marktstatus | In dieser Jurisdiktion nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückhalten** – Datenpipeline vor Bewertung abschließen |

---

## Arzneimittel-Hintergrund

Cabazitaxel ist ein Mikrotubuli-stabilisierendes Mittel aus der Taxan-Klasse. Es wurde speziell entwickelt, um die Resistenz gegen Docetaxel zu überwinden, da es eine geringe Affinität für P-Glykoprotein aufweist – die Efflusspumpe, die für die Taxan-Resistenz in vielen Tumorzelllinien verantwortlich ist.

Der primäre Wirkmechanismus beinhaltet die Bindung an Tubulin und die Hemmung der Mikrotubuli-Depolymerisierung, wodurch die Zellen in der G2/M-Phase arretiert werden. Dieser Mechanismus ist breit auf Tumortypen anwendbar, die auf schnelle Zellteilung angewiesen sind, was ihn zu einem interessanten Kandidaten für die Umwidmung über Prostatakrebs hinaus macht.

Cabazitaxel ist von der FDA (2010) und der EMA (2011) unter dem Markennamen Jevtana® für mCRPC zugelassen. Es ist derzeit in dieser Jurisdiktion nicht vermarktet (0 lokale Zulassungen), was bedeutet, dass eine Einfuhr oder lokale Registrierung für jede klinische Anwendung erforderlich wäre.

> **Anmerkung zur MOA-Datenlücke:** Das Evidence-Paket führt MOA als Datenlücke mit hohem Schweregrad auf (DG002). Der obige Hintergrund basiert auf etablierter pharmakologischer Literatur und sollte formal über die DrugBank API bestätigt werden, bevor eine vollständige Umwidmungsanalyse durchgeführt wird.

---

## Warum derzeit keine Umwidmungsbewertung möglich ist

Das Evidence-Paket ist unvollständig:

| Datenlücke | Schweregrad | Auswirkung |
|------------|------------|-----------|
| TFDA-Fachinformationsblatt (Warnhinweise/Gegenanzeigen) | **Blockierend** | Kann S1-Sicherheits-Screening nicht abgeschlossen werden |
| Wirkmechanismus (MOA) | Hoch | Kann keine mechanistische Ähnlichkeitsanalyse durchführen |
| TxGNN-Vorhersageergebnis | Kritisch | Keine neue Indication vorhergesagt – `predicted_indications: []` |

Das `predicted_indications`-Array ist leer, was bedeutet, dass entweder:
1. Der TxGNN-Vorhersageschritt für dieses Arzneimittel noch nicht durchgeführt wurde, **oder**
2. Die Vorhersage-Pipeline durch die obigen vorgelagerten Datenlücken blockiert wurde.

Bis TxGNN eine priorisierte Liste von Kandidaten-Indikationen produziert, gibt es kein Umwidmungsziel zu bewerten.

---

## Zytotoxizität

Cabazitaxel ist ein zytotoxisches Chemotherapeutikum. Das Folgende gilt unabhängig vom Umwidmungsziel.

| Element | Inhalt |
|---------|--------|
| Klassifizierung der Zytotoxizität | Konventionelles Zytotoxikum – Taxan-Klasse |
| Myelosuppressionsrisiko | **Hoch** – Fieberhafte Neutropenie ist das häufigste schwerwiegende Nebenereignis; G-CSF-Prophylaxe ist Standard der Praxis |
| Emetogenitäts-Klassifizierung | Niedrig bis moderat |
| Überwachungspunkte | CBC mit Differenzierung (wöchentlich während des ersten Zyklus), Leberfunktion, Nierenfunktion, Elektrolyte |
| Handhabungsschutz | Muss den Bestimmungen zur Handhabung zytotoxischer Arzneimittel entsprechen – Geschlossene Transfersysteme erforderlich |

---

## Sicherheitserwägungen

Das Evidence-Paket enthält keine umsetzbaren Sicherheitsdaten für dieses Arzneimittel in dieser Jurisdiktion. Vor der Durchführung klinischer oder behördlicher Arbeiten:

> Bitte beachten Sie die EMA SmPC (Jevtana®) und das aktuelle TFDA-Fachinformationsblatt für vollständige Warnhinweise, Gegenanzeigen und Informationen zu Arzneimittelwechselwirkungen. Die kritischsten bekannten Risiken sind fieberhafte Neutropenie, schwere Überempfindlichkeitsreaktionen und Gastrointestinaltoxizität.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Das Evidence-Paket für Cabazitaxel fehlen sowohl die TxGNN-Umwidmungsvorhersagen als auch die blockierenden Sicherheitsdaten, die für das S1-Screening erforderlich sind. Es gibt keine neue Indication zu bewerten und keine Sicherheitsgrundlage für die Bewertung.

**Um fortzufahren, ist Folgendes erforderlich:**

1. **DG001 auflösen (Blockierend):** Das TFDA-Fachinformationsblatt als PDF herunterladen und analysieren, um Warnhinweise und Gegenanzeigen zu extrahieren – erforderlich zum Freischalten des S1-Sicherheits-Tors.
2. **DG002 auflösen (Hoch):** DrugBank API für formale MOA-Daten abfragen, um eine mechanistische Ähnlichkeitsanalyse zu ermöglichen.
3. **TxGNN-Vorhersage-Pipeline erneut ausführen** für DB06772 – das `predicted_indications`-Array muss vor jeder Umwidmungsbewertung gefüllt werden.
4. **EMA SmPC für Jevtana® überprüfen** als ergänzende Sicherheitsreferenz, da das Arzneimittel in Europa zugelassen ist, aber nicht in dieser Jurisdiktion.
5. Sobald Vorhersagen verfügbar sind, die Bewertung des Evidence Level und die Entscheidungsempfehlung nach standardmäßigen L1–L5-Kriterien erneut durchführen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

