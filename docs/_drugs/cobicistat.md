---
layout: default
title: Cobicistat
parent: Nur Modellvorhersage (L5)
nav_order: 106
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **3** 
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

# Cobicistat: Von fehlender ursprünglicher Indikation zum Feline Acquired Immunodeficiency Syndrome (Signal)

## Zusammenfassung in einem Satz

Das Evidenzpaket für Cobicistat (DB09065) enthält keine dokumentierte ursprüngliche Indikation oder keinen Wirkmechanismus, und das Arzneimittel ist derzeit **in Deutschland nicht vermarktet**. Die Top-Vorhersage des TxGNN-Modells ist **Feline Acquired Immunodeficiency Syndrome**, aber dieses Signal wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt, was es zu einer reinen Modellvorhersage ohne externe Validierung macht.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Nicht verfügbar – kein genehmigter Indikationstext im Evidenzpaket vorhanden |
| Vorhergesagte neue Indikation | Feline Acquired Immunodeficiency Syndrome |
| TxGNN-Vorhersage-Score | 99.92% |
| Evidenzgrad | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten für Cobicistat in diesem Evidenzpaket nicht verfügbar, und auch keine ursprüngliche Indikation dokumentiert. Dies macht es unmöglich, die mechanistische Plausibilität für die vorhergesagte Indikation zu diesem Zeitpunkt formal zu bewerten.

Trotzdem teilen die Top-zwei-Vorhersagen des TxGNN – Feline Acquired Immunodeficiency Syndrome (Rang 1) und Simian Immunodeficiency Virus-Infektion (Rang 2) – ein beachtenswertes Muster: beide sind Lentivirus-Immunmangelkrankheiten bei Tierarten, strukturell und pathophysiologisch analog zur menschlichen HIV/AIDS. Diese Häufung deutet darauf hin, dass das Modell möglicherweise ein echtes antivirales oder immunmangelassoziiertes Signal im Wissensgraph erfasst, anstelle von reinem Rauschen. Ohne MOA-Daten, ursprüngliche Indikationsdaten oder unterstützende Studien/Literatur bleibt dies jedoch eine unbestätigte Hypothese statt einer evidenzgestützten Begründung.

Eine dritte, niedriger bewertete Vorhersage im Paket (eine seltene neurodevelopmentale Störung, Evidenzgrad L5, Entscheidung S0/Halten) wurde explizit als keine identifizierbaren mechanistischen Verbindungen aufweisend gekennzeichnet und als wahrscheinlich Rauschen einbettend bewertet – was verstärkt, dass nicht alle TxGNN-Ausgaben für dieses Arzneimittel gleiche biologische Plausibilität tragen, und Rang 1/2 unabhängige Überprüfung verdienen statt automatisches Vertrauen.

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Literaturevidence

Derzeit keine verwandte Literatur verfügbar

---

## Marktstatus Deutschland

Cobicistat ist derzeit in Deutschland nicht vermarktet, und im Evidenzpaket sind keine Zulassungsunterlagen verfügbar.

---

## Sicherheitsaspekte

Weitere Sicherheitsinformationen finden Sie in der Fachinformation.

*Hinweis: Warnhinweise und Kontraindikationen in der Fachinformation für dieses Arzneimittel sind derzeit eine Blockierungsdatenlücke (DG001) – dies muss vor jeder Sicherheitsbewertung gelöst werden.*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Es gibt keine klinischen Studien, Literatur, Wirkmechanismus- oder ursprünglichen Indikationsdaten, die diese Vorhersage stützen, und das Arzneimittel ist in Deutschland nicht vermarktet. Die Sicherheitsdaten der Fachinformation sind eine Blockierungslücke. Die Evidenz ist unzureichend, um über ein reines Modellsignal hinaus voranzukommen.

**Erforderlich zum Fortschreiten:**
- Ursprüngliche Indikations- und MOA-Daten (z. B. über DrugBank-API-Abfrage)
- TFDA/BfArM-Fachinformation zu Warnhinweisen und Kontraindikationen (löst Blockierungslücke DG001)
- Gezielte Literatur-/Studiensuche zu Cobicistat in Kontexten der HIV/Lentivirus-bezogenen Umnutzung, um die FIV/SIV-Mechanismusthese zu testen
- Klarstellung darüber, warum eine felide-spezifische Veterinärerkrankung als die Top-bewertete Vorhersage erscheint, und ob eine menschlich-relevante analoge Indikation ersetzt werden sollte

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

