---
layout: default
title: Ocrelizumab
parent: Nur Modellvorhersage (L5)
nav_order: 276
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
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

# Ocrelizumab: Von Multiple Sklerose zum HER2-positiven Mammakarzinom

## Zusammenfassung in einem Satz

> Ocrelizumab ist ein Anti-CD20-Monoklonalantikörper, dessen etablierte Anwendung die B-Zell-Depletion bei Multipler Sklerose ist; formaler Indikationstext ist in diesem Evidenzpaket nicht verfügbar, da das Arzneimittel **derzeit nicht in Deutschland vermarktet wird**.
> Das TxGNN-Modell prognostiziert, dass es für **HER2-positives Mammakarzinom** wirksam sein könnte, mit einem sehr hohen Rohergebnis (**99.89%**), aber diese Vorhersage wird derzeit durch **null klinische Studien** und **null Literaturverweise** gestützt, und die vom Reviewer verfasste mechanistische Begründung verweist explizit auf keine bekannte biologische Verbindung zwischen B-Zell-Depletion und HER2/ERBB2-getriebenem Tumorsignaling.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Multiple Sklerose (basierend auf bekannter Arzneimittelklasse/Hintergrund; kein formaler deutscher Regulierungsindikationstext liegt vor – Arzneimittel ist unvermarktet) |
| Vorhergesagte neue Indikation | HER2-positives Mammakarzinom |
| TxGNN-Vorhersage-Score | 99.89% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden klinischen oder Literaturdaten) |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Genehmigungen | 0 |
| Empfohlene Entscheidung | **Zurückstellen** |

---

## Warum ist diese Vorhersage sinnvoll?

Detaillierte Wirkmechanismus-Daten sind als Datenlücke in diesem Evidenzpaket gekennzeichnet (DG002). Basierend auf bekannten Hintergrundinformationen ist Ocrelizumab ein Anti-CD20-Monoklonalantikörper, der CD20-positive B-Lymphozyten abbaut, um eine Immunmodulation zu erreichen, und ist für Multiple Sklerose zugelassen. Dieser Wirkmechanismus ist grundsätzlich eine Immunzell-zielgerichtete Therapie, nicht eine Tumor-Signalweg-Therapie.

HER2-positives Mammakarzinom wird hingegen durch Überexpression/Amplifikation der HER2 (ERBB2) Rezeptor-Tyrosinkinase angetrieben, die nachgelagerte proliferative Signalisierung (PI3K/AKT, MAPK) unabhängig von B-Zell-Biologie aktiviert. Es gibt keine Überlappung zwischen dem CD20/B-Zell-Depletion-Weg und dem HER2/ERBB2-Signalweg, und keine veröffentlichten Beweise, dass eine B-Zell-depletive Therapie HER2-getriebenes Tumorwachstum verändert.

Angesichts des Fehlens einer mechanistischen Brücke, klinischer Studien oder Literaturunterstützung kommt die Reviewer-Bewertung in diesem Evidenzpaket zu dem Ergebnis, dass der hohe TxGNN-Score höchstwahrscheinlich **modellseitiges Vorhersage-Rauschen** widerspiegelt, anstelle eines biologisch begründeten Repurposing-Signals. Dies ist ein wichtiger Vorbehalt, der stark gegen das Handeln nach dem Score allein wiegen sollte.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine zugehörige Literatur verfügbar.

**Anmerkung zur Datenqualität (aus demselben Evidenzpaket, andere Kandidatenindikationen):** Ein verwandter Kandidat, *„Brusttumorluminal A oder B,"* erbrachte 19 PubMed-Treffer während der automatisierten Suche. Bei manueller Überprüfung sind alle 19 nicht mit Brustkrebs verwandt – sie betreffen B-Zell-Entwicklung/Reifung, Hepatitis-B-Impfstoffe und HLA-B-Allel-Typisierung. Dies deutet stark darauf hin, dass die Literatursuche auf dem eigenständigen Buchstaben „B" (von „luminal B") statt auf dem Krankheitskonzept abgestimmt war, und sollte als **falsch-positives Artefakt der Such-Pipeline** behandelt werden, nicht als unterstützender Beweis. Die übrigen drei Kandidatenindikationen (normaler brustähnlicher Subtyp, PR-positives Mammakarzinom, PR-negatives Mammakarzinom) erbrachten null Studien und null Literatur. Keine der fünf vorhergesagten Indikationen in diesem Paket haben derzeit echte unterstützende Beweise.

---

## Marktinformationen für Deutschland

Ocrelizumab hat derzeit **keine Zulassung in der Akte in Deutschland** (0 Lizenzen registriert). Keine Produktbezeichnung, Darreichungsform oder genehmigter Indikationstext ist aus den Zulassungsdaten für dieses Arzneimittel in diesem Markt verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Wichtige Warnhinweise, Kontraindikationen und Arzneimittel-Arzneimittel-Wechselwirkungsdaten sind alle als Datenlücken in diesem Evidenzpaket gekennzeichnet – insbesondere DG001, eine *Blocking*-Schweregrad-Lücke für TFDA/Etikettenwarnungen und Kontraindikationen, die verhindert, dass dieser Kandidat das S1-Sicherheitspre-Screening besteht.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die Evidenzstufe ist L5 (nur Modellvorhersage) ohne klinische Studien und ohne echte Literaturunterstützung für HER2-positives Mammakarzinom oder eine der anderen vier vorhergesagten brustkrebsbezogenen Indikationen in diesem Paket. Der vorgeschlagene Wirkmechanismus (CD20-vermittelte B-Zell-Depletion) hat keine etablierte biologische Verbindung zu HER2/ERBB2-getriebenem Tumorsignaling, und die scheinbare Literaturunterstützung eines benachbarten Kandidaten stellte sich als falsch-positives Artefakt der Such-Pipeline heraus. In Kombination mit einer Blocking-Schweregrad-Sicherheitsdatenlücke (DG001) und einer High-Schweregrad-MOA-Datenlücke (DG002) kann dieser Kandidat derzeit nicht einmal das anfängliche Sicherheits- und Evidenz-Screening-Stadium bestehen.

**Zur Fortsetzung ist Folgendes erforderlich:**
- Bestätigte Wirkmechanismus-Daten für Ocrelizumab aus DrugBank/Primärliteratur (behebt DG002)
- TFDA/BfArM Packungsbeilage-Warnhinweise und Kontraindikationen (behebt DG001, Blocking)
- Eine korrigierte, indikationsspezifische Literatur- und klinische Studiensuche, die Einzelbuchstaben-/Schlüsselwort-Falschentsprechungen herausfiltert (z.B. erneute Ausführung der „luminal B"-Abfrage mit krankheitsspezifischen MeSH-Begriffen)
- Falls weiter verfolgt: dedizierte präklinische oder mechanistische Studien, die einen plausiblen Zusammenhang zwischen B-Zell-Depletion und HER2-getriebener Tumorbiologie etablieren, bevor eine klinische Hypothese berücksichtigt wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

