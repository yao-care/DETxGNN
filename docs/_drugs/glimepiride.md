---
layout: default
title: Glimepiride
parent: Nur Modellvorhersage (L5)
nav_order: 181
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **9** 
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

# Glimepirid: Von Typ-2-Diabetes mellitus zu Focal Stiff Limb Syndrome

## Zusammenfassung in einem Satz

Glimepirid ist ein Sulfonylurea der zweiten Generation, pharmakologisch als Insulinsekretagogum zur Behandlung des Typ-2-Diabetes mellitus eingestuft. Das TxGNN-Modell weist einen hohen Vorhersagescore für **Focal Stiff Limb Syndrome** zu, eine autoimmune, GABAerge neurologische Erkrankung, aber diese Richtung wird derzeit von **0 klinischen Studien** und **0 Publikationen** gestützt, und das Evidenzpaket kennzeichnet die mechanistische Verbindung ausdrücklich als nicht gestützt.

---

## Schnellabriss

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Typ-2-Diabetes mellitus (basierend auf bekannter pharmakologischer Klassifizierung als Sulfonylurea; kein formaler regulatorischer Indikationstext in diesem Datensatz verfügbar) |
| Vorhergesagte neue Indikation | Focal Stiff Limb Syndrome |
| TxGNN-Vorhersagescore | 99.75% |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | ✗ Nicht auf dem Markt |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage angemessen?

Detaillierte Wirkmechanismuskaten für Glimepirid waren im strukturierten Evidenzpaket nicht direkt verfügbar (`original_moa` = Datenlücke). Basierend auf bekannter pharmakologischer Klassifizierung ist Glimepirid jedoch ein Sulfonylurea der zweiten Generation, das an SUR1-Untereinheiten bindet, um ATP-sensitive K⁺-Kanäle auf pankreatischen β-Zellen zu schließen und Insulinsekretion zu fördern.

Focal Stiff Limb Syndrome (eine lokalisierte Variante des Stiff Person Syndrome) ist eine autoimmune neurologische Erkrankung, die durch Anti-GAD65-Antikörper und beeinträchtigte GABAerge Neurotransmission getrieben wird. Obwohl ATP-sensitive K⁺-Kanäle auch in zentralen Neuronen exprimiert werden, gibt es derzeit keinen Hinweis darauf, dass Sulfonylurea-Klasse-Arzneistoffe die GABAerge Signalisierung oder die autoimmune GAD65-vermittelte Pathologie modulieren. Das Evidenzpaket selbst charakterisiert dies als „hohen TxGNN-Score ohne mechanistische Grundlage" – d. h. die vorhergesagte Verbindung scheint eher ein Graph-Embedding-Artefakt als eine biologisch fundierte Hypothese zu sein.

Angesichts der fehlenden mechanistischen Plausibilität, klinischen Studiendaten und Literaturstützung sollte dieser Kandidat als eine Modellausgabe mit geringerem Vertrauen und nicht als ein wissenschaftlich gestütztes Umpositionierungssignal interpretiert werden.

---

## Klinische Studienevidenz

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturnachweis

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Marktinformationen für Deutschland

Glimepirid ist derzeit nicht in der durch diesen regulatorischen Datensatz abgedeckten Gerichtsbarkeit auf dem Markt (Marktstatus: Nicht auf dem Markt / Not Marketed; 0 Zulassungen in den Aufzeichnungen). Es sind keine Lizenz- oder Produktinformationen verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die am höchsten bewertete Vorhersage (Focal Stiff Limb Syndrome) trägt eine L5-Evidenzstufe – einen TxGNN-Score ohne unterstützende klinische Studien, Literatur oder plausible mechanistische Verbindung zu Glimeprids bekannter Sulfonylurea-Pharmakologie. In Kombination mit dem Nicht-Markt-Status des Arzneistoffs in dieser Gerichtsbarkeit und den blockierenden Sicherheitsdatenlücken gibt es derzeit keine Grundlage, diesen Kandidaten voranzutreiben.

**Um fortzufahren, ist Folgendes erforderlich:**
- Bestätigte Arzneimitteletikette / Warnungen und Kontraindikationen von der zuständigen Behörde (derzeit eine blockierende Datenlücke – erforderlich vor jeder S1-Sicherheitsbewertung)
- Verifizierten Wirkmechanismuskaten von DrugBank oder primärer Literatur (Datenlücke mit hoher Schwere)
- Unabhängige mechanistische oder präklinische Hinweise, die die Sulfonylurea-Pharmakologie mit der GABAergen/autoimmunen neurologischen Pathologie verbinden, falls diese Indikation weiter verfolgt werden soll
- Überwachung von niedriger bewerteten Kandidaten (z. B. Thiamin-responsive Dysfunktionssyndrom, Rang 4), die einen etwas plausibleren – obwohl immer noch unverifizierten – Link zu Insulinsekretion-Wegen zeigen, und eine Literaturrecherche mit niedrigerer Priorität rechtfertigen können

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

