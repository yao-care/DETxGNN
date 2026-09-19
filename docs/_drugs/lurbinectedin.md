---
layout: default
title: Lurbinectedin
parent: Nur Modellvorhersage (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
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

# Lurbinectedin: Vom kleinzelligen Lungenkrebs zum Multiplen Endokrinen Neoplasie-Syndrom

## Zusammenfassung in einem Satz

Lurbinectedin ist ein zytotoxisches Chemotherapeutikum, das in der Evidenzdarlegung als aktuell bei kleinzelligem Lungenkrebs eingesetzt beschrieben wird.
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam für das **Multiple Endokrine Neoplasie-Syndrom** sein könnte,
aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — nur der Score, ohne unterstützende Evidenz.

---

## Schnelle Übersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Kleinzelliger Lungenkrebs (SCLC) — in der Modellbegründung erwähnt; nicht bestätigt durch formale Zulassungs-/Regulatorydaten (Datenlücke) |
| Vorhergesagte neue Indikation | Multiples Endokrines Neoplasie-Syndrom |
| TxGNN-Vorhersage-Score | 99.44% |
| Evidenzgrad | L5 (nur Modellvorhersage; keine unterstützenden Studien oder Literatur) |
| Marktstatus in Deutschland | Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkmechanismus-Daten sind im formalen Arzneimitteleintrag nicht verfügbar (Datenlücke DG002, hoher Schweregrad). Nach den Begründungsannotationen des Modells ist Lurbinectedin ein DNA-Minorrille-bindendes Transkriptionsinhibitor, das transkriptionsabhängige DNA-Schäden durch RNA Pol II-Hemmung hervorruft — ein konventioneller zytotoxischer Chemotherapie-Mechanismus, der derzeit bei kleinzelligem Lungenkrebs angewendet wird.

Für die höchstrangige Vorhersage wird im Evidenzpaket jedoch explizit festgehalten, dass es **keine bekannte mechanistische Beziehung** zwischen diesem Transkriptionshemmungs-/DNA-Schadmechanismus und dem Multiplen Endokrinen Neoplasie-Syndrom gibt (ein Keimbahn-RET/MEN1-assoziiertes endokrines Tumor-Syndrom). Die Vorhersage stützt sich ausschließlich auf TxGNN-Graph-Ähnlichkeits-Inferenzen, ohne klinische oder literarische Bestätigung.

Angesichts der zytotoxischen und immunsuppressiven Eigenschaften von Lurbinectedin ist eine Ausweitung auf ein nicht-onkologisches, genetisch bedingtes endokrines Syndrom auf dieser Stufe biologisch nicht plausibel. Der gleiche Vorbehalt gilt für alle neun weiteren eingestuften Vorhersagen in diesem Evidenzpaket — von denen mehrere nicht einmal menschliche Krankheiten sind (z. B. Felines Immundefizienzvirus-Syndrom, Infektiöse bovine Rhinotracheitis), was auf artübergreifendes Rauschen im zugrunde liegenden Wissensgraphen hindeutet, nicht auf echte Umwidmungssignale.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literarische Evidenz

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktstatus in Deutschland

Lurbinectedin hält derzeit keine Marktzulassung in Deutschland (0 Lizenzen registriert); Marktstatus ist **Nicht im Handel**.

---

## Zytotoxizität

| Punkt | Inhalt |
|------|------|
| Zytotoxizitätsklassifizierung | Konventionell zytotoxisch — DNA-Minorrille-bindendes Transkriptionsinhibitor (nach Begründungstext; nicht unabhängig über DrugBank-Kategoriendaten bestätigt) |
| Myelosuppressions-Risiko | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Emetogenitätsklassifizierung | Bitte beachten Sie die Warnhinweise und Vorsichtsmaßnahmen der Fachinformation |
| Überwachungselemente | Blutbild mit Differentialzählung, Leber- und Nierenfunktion (Standard bei zytotoxischer Chemotherapie; produktspezifische Daten nicht bestätigt) |
| Schutzmaßnahmen bei der Handhabung | Standardmaßnahmen zur sicheren Handhabung von zytotoxischen Substanzen sind erforderlich, da es sich um ein bestätigtes zytotoxisches Chemotherapeutikum handelt |

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. TFDA-Etikettenwarnungen und Kontraindikationen sind derzeit eine **Blockierende Datenlücke (DG001)**, die eine formale S1-Sicherheitsvorbewertung verhindert.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Alle 10 von TxGNN vorhergesagten Indikationen für Lurbinectedin sind Evidenzgrad L5 (nur Vorhersage, null klinische Studien, null Literatur). Der höchstrangige Kandidat — Multiples Endokrines Neoplasie-Syndrom — wird in seiner eigenen Begründung explizit als mangelhaft in mechanistischer, klinischer oder literarischer Unterstützung gekennzeichnet, und mehrere niedriger eingestufte Vorhersagen sind nicht einmal menschliche Krankheiten, was wahrscheinliches artübergreifendes Wissensgraph-Rauschen statt eines glaubwürdigen Umwidmungssignals andeutet.

**Zum Fortfahren ist Folgendes erforderlich:**
- TFDA-Etikettenwarnungen/Kontraindikationen (DG001, blockierend) — erforderlich vor jeder S1-Sicherheitsvorbewertung
- Bestätigter Wirkmechanismus über DrugBank oder Primärliteratur (DG002, Hoch)
- Unabhängige Überprüfung der ursprünglichen Indikation und der Zulassungshistorie
- Präklinische oder mechanistische Evidenz, die die biologische Plausibilität des Zusammenhangs mit dem Multiplen Endokrinen Neoplasie-Syndrom belegt, bevor weitere Investitionen erfolgen
- Erneutes Screening der niedriger eingestuften Vorhersagen zur Filterung von Nicht-Humanerkrankungseinträgen (artübergreifendes Wissensgraph-Rauschen)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

