---
layout: default
title: Albutrepenonacog Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **6** 
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

# Albutrepenonacog Alfa: Von Hämophilie B (Faktor-IX-Ersatztherapie) zu Pseudo-von-Willebrand-Syndrom

## Zusammenfassung in einem Satz

> Albutrepenonacog alfa (rIX-FP, DrugBank DB13884) ist ein rekombinantes Gerinnungs-Faktor-IX-Fc-Fusionsersatzprodukt, das zur Behandlung von Hämophilie B verwendet wird.
> Das TxGNN-Modell prognostiziert, dass es möglicherweise wirksam für das **Pseudo-von-Willebrand-Syndrom** ist, mit einem sehr hohen Prognosewert (**99.94%**),
> aber diese Richtung wird derzeit durch **0 klinische Studien** und **0 Veröffentlichungen** gestützt – es handelt sich um eine reine Modellvorhersage ohne praktische Belege.

---

## Kurzübersicht

| Element | Inhalt |
|---------|---------|
| Ursprüngliche Indikation | Hämophilie B (Faktor-IX-Ersatztherapie) – aus Arzneistoffklasse abgeleitet; deutsche Zulassungsdaten sind nicht verfügbar (0 Zulassungen dokumentiert) |
| Vorhergesagte neue Indikation | Pseudo-von-Willebrand-Syndrom |
| TxGNN-Prognosewert | 99.94% |
| Evidenzebene | L5 (reine Modellvorhersage, keine klinischen Studien oder Literatur) |
| Marktstatus Deutschland | ✗ Nicht am Markt |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Aufschub |

---

## Warum ist diese Vorhersage begründet?

Gegenwärtig sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (Datenlücke). Nach verfügbaren Informationen ist Albutrepenonacog alfa ein rekombinantes Gerinnungs-Faktor-IX-Fc-Fusionsprotein (rIX-FP) – ein Faktor-Ersatzprodukt mit verlängerter Halbwertszeit, dessen Wirksamkeit bei Hämophilie B (Faktor-IX-Mangel) gut etabliert ist. Mechanistisch wäre zu erwarten, dass es auf Blutgerinnungsstörungen anwendbar ist, die die Rolle von Faktor IX in der Gerinnungskaskade teilen.

Die ursprüngliche Indikation (Faktor-IX-Mangel) und die vorhergesagte neue Indikation (Pseudo-von-Willebrand-Syndrom) fallen beide unter die breite Kategorie der „vererbten Blutgerinnungsstörungen", was wahrscheinlich erklärt, warum der TxGNN-Knowledge-Graph einen hohen Ähnlichkeitswert zuweist – das Modell könnte gemeinsame phänotypische Merkmale (Blutungsneigung, Muster des gemeinsamen Auftretens von Krankheiten) erfassen, anstatt eines echten gemeinsamen pharmakologischen Wirkmechanismus.

Wichtig ist, dass die eigene mechanistische Analyse des Evidenzpakets erhebliche Zweifel an dieser spezifischen Vorhersage aufwirft. Das Pseudo-von-Willebrand-Syndrom wird durch einen Funktionsgewinnndefekt des Thrombozyten-GPIb-Rezeptors verursacht (erhöhte Affinität für den von-Willebrand-Faktor) – eine **primäre Hämostase-/Thrombozyten-Adhäsions**-Störung. Dies ist mechanistisch unterschiedlich von der Faktor-IX-Ersatztherapie, die auf die **sekundäre Hämostase/Thrombinbildungskaskade** einwirkt. Es wurde keine direkte kausale pharmakologische Verbindung hergestellt, und die gleiche Warnung gilt für die anderen fünf nächstbesten Vorhersagen in diesem Paket (Primäre Thrombozytensekretionstörung, Glanzmann-Thrombasthenie, Scott-Syndrom, Blutungsstörung bei Kollagenrezeptordefekt und konstitutionelle Thrombozytopenie) – alle sind Thrombozyten-Funktions- oder Thrombozytenzahl-Störungen, die mechanistisch von der Faktor-IX-Ersatztherapie unterscheidbar sind, und keine haben unterstützende klinische oder literarische Belege. Dieses Muster ist konsistent mit **phänotypischer Verwirrung** (das Modell clustert vielfältige „Blutgerinnungsstörungen" zusammen) statt echter mechanistischer Überlappung.

---

## Belege aus klinischen Studien

Gegenwärtig sind keine verwandten klinischen Studien registriert.

---

## Literaturbelege

Derzeit liegt keine einschlägige Literatur vor.

---

## Marktsituation in Deutschland

Für Albutrepenonacog alfa wurde keine deutsche Marktzulassung gefunden. Das Produkt ist derzeit als **Nicht am Markt** in Deutschland klassifiziert, mit 0 registrierten Zulassungen.

---

## Sicherheitsaspekte

Bitte beachten Sie die Gebrauchsinformation für Sicherheitsinformationen.

*(Wichtige Warnhinweise, Gegenanzeigen und Daten zu Arzneimittelwechselwirkungen sind derzeit nicht verfügbar – Daten zur TFDA-Gebrauchsinformation sind als blockierende Datenlücke (DG001) gekennzeichnet, die die S1-Sicherheitsvorbewertungsphase verhindert.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Aufschub**

**Begründung:**
- Der TxGNN-Prognosewert ist sehr hoch (99.94%), wird aber durch null klinische Studien und null Literatur unterstützt – die Evidenzebene ist L5, die niedrigste Stufe.
- Die mechanistische Begründung selbst kennzeichnet diese Vorhersage (und alle 5 nächstbesten Vorhersagen) als wahrscheinlich angetrieben durch phänotypische Ähnlichkeit zwischen „Blutgerinnungsstörungen" statt einem echten gemeinsamen pharmakologischen Wirkmechanismus zwischen Faktor-IX-Ersatztherapie und Thrombozyten-Funktions-/Thrombozytenzahl-Störungen.
- Zwei Datenlücken blockieren derzeit eine rigorose Bewertung: TFDA/EMA-Gebrauchsinformation-/Warnhinweise-Daten (DG001, blockierend) und Wirkmechanismus-Daten (DG002, hohe Priorität).

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/EMA-Gebrauchsinformation und Sicherheitsdaten (DG001 beheben – erforderlich vor jeder S1-Sicherheitsvorbewertung)
- Bestätigter Wirkmechanismus für Albutrepenonacog alfa (DG002 beheben)
- Präklinische oder mechanistische Studien zur Etablierung einer plausiblen kausalen Verbindung zwischen Faktor-IX-Ersatztherapie und Thrombozyten-Funktionsstörungen (Pseudo-von-Willebrand-Syndrom, Glanzmann-Thrombasthenie, Scott-Syndrom usw.)
- Belege aus der klinischen Praxis oder Fallberichte über Off-Label-Einsatz bei Thrombozytenstörungen
- Klärung des deutschen/EU-Zulassungsstatus, da das Produkt derzeit 0 Marktzulassungen aufweist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

