---
layout: default
title: Elvitegravir
parent: Nur Modellvorhersage (L5)
nav_order: 142
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

# Elvitegravir: Von der HIV-1-Infektion zur Infektion mit dem Felinen Immundefizienzvirus (Felines AIDS)

## Zusammenfassung in einem Satz

Elvitegravir ist ein HIV-1-Integrase-Strang-Transfer-Inhibitor (INSTI) und die Rationale des Evidence Pack beschreibt seine ursprüngliche klinische Verwendung als Behandlung der HIV-1-Infektion beim Menschen; es ist derzeit **nicht in Deutschland zugelassen** (0 Zulassungen). Die Top-Vorhersage des TxGNN-Modells ist **feliner erworbener Immunmangel (FIV)** – eine veterinärmedizinische, keine menschliche Indikation – mit einem sehr hohen rohen Vorhersagescore (**99,89%**), aber **null klinische Studien und null Publikationen**, was bedeutet, dass dies ein reines Modellvorhersagesignal (L5) ohne translationalen Hintergrund ist.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|--------|
| Ursprüngliche Indikation | Nicht verfügbar im Evidence Pack — `original_indications` ist leer und `original_moa` ist als Datenlücke gekennzeichnet (DG002). Der Rationaltext im Pack deutet darauf hin, dass Elvitegravir als HIV-1-Integrase-Strang-Transfer-Inhibitor wirkt, was auf die ursprüngliche menschliche Indikation HIV-1-Infektion hindeutet, dies wird aber durch kein separates Feld unabhängig bestätigt. |
| Vorhergesagte neue Indikation | Feliner erworbener Immunmangel (FIV) |
| TxGNN-Vorhersagescore | 99,89% (Rang 1781) |
| Evidenzstufe | L5 (nur Modellvorhersage, keine klinischen Studien oder Literatur) |
| MarktStatus Deutschland | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halt** |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht als separates Feld verfügbar (DG002, hoher Schweregrad). Basierend auf den Informationen in der Repurposing-Rationale dieses Evidence Pack ist Elvitegravir ein HIV-1-Integrase-Strang-Transfer-Inhibitor (INSTI) – seine Wirksamkeit bei HIV-1-Infektion ist gut etabliert, und mechanistisch zielt diese Klasse von Inhibitoren auf das virale Integrase-Enzym ab, das für die Insertion der proviralen DNA in das Wirtsgenom verantwortlich ist.

Die Top-Vorhersage, FIV (Infektion mit dem Felinen Immundefizienzvirus), ist mechanistisch plausibel: FIV ist ein Lentivirus, der eng mit HIV-1 verwandt ist, und seine Integrase teilt strukturelle und katalytische Homologie mit HIV-1-Integrase. Theoretisch könnte die Strang-Transfer-Inhibition von Elvitegravir mit FIV-Integrase kreuzreagieren. Allerdings handelt es sich um eine **reine mechanistische Inferenz ohne in-vitro- oder in-vivo-Daten**, und – kritisch – FIV ist eine veterinärmedizinische Krankheit. Sie liegt völlig außerhalb des Evaluierungspfades für Arzneimittel-Repurposing beim Menschen (keine menschliche PK/PD, kein menschlicher Sicherheitspfad, keine regulatorische Route), weshalb sie unabhängig vom Modellscore keine praktikable Kandidatin für menschliche Indikationserweiterung darstellt.

Die anderen beiden Rangplatzierungen in diesem Pack verstärken eher eine „Halt"-Position als die Eskalation zu unterstützen. Rang 2 (Infektion mit Simianem Immundefizienzvirus) ist ein bekanntes *Krankheitsmodell bei Primaten ohne Menschen*, das zur Untersuchung von HIV-Antiretroviralen verwendet wird – nicht eine unabhängige menschliche oder auch nur eigenständige veterinärmedizinische Indikation – und es existieren keine elvitegravir-spezifischen SIV-Daten in diesem Pack. Rang 3 (eine seltene genetische neurodevelopmentale Störung) hat keine identifizierbare mechanistische Verbindung zur Integrase-Inhibition und ist in der Rationale des Pack selbst explizit als wahrscheinlich falsch-positiv gekennzeichnet, das aus Wissens-Graph-Embedding-Nähe statt echten biologischen Zusammenhängen stammt. Insgesamt deuten keine der drei Top-TxGNN-Vorhersagen für Elvitegravir derzeit auf eine praktikable menschliche Repurposing-Möglichkeit hin.

---

## Klinische Studienevidenz

Derzeit sind keine damit verbundenen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine damit verbundene Literatur verfügbar.

---

## Marktinformation Deutschland

Elvitegravir ist nicht in Deutschland zugelassen — `taiwan_regulatory.market_status` meldet „Not marketed" (Nicht zugelassen) mit 0 Gesamtlizenzen und keine Lizenzeinträge verfügbar im Evidence Pack.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

*(Hinweis: `key_warnings`, `contraindications` und DDI-Abfrage haben alle keine Daten in diesem Evidence Pack zurückgegeben. Dies ist im Pack als DG001 gekennzeichnet — eine Datenlücke mit **blockierendem** Schweregrad — was bedeutet, dass TFDA/Fachinformations-Warnungen und Kontraindikationen vor der Möglichkeit beschafft werden müssen, dass dieser Kandidat zu einer S1-Sicherheits-Vorabprüfung übergehen kann.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halt**

**Rationale:**
- Die Top-Vorhersage (FIV) ist eine veterinärmedizinische Erkrankung ohne menschlichen translationalen Pfad, trotz eines hohen rohen TxGNN-Scores; die verbleibenden zwei Vorhersagen sind entweder ein Tierforschungsmodell (SIV) oder eine wahrscheinlich falsch-positive genetische Störungsassoziation – keine stellt ein praktikables menschliches Repurposing-Signal dar.
- Die Evidenzstufe ist L5 über alle drei Vorhersagen hinweg (keine klinischen Studien, keine Literatur), und eine **blockierende** Datenlücke (DG001: TFDA-Warnungen/Kontraindikationen) hindert diesen Kandidaten überhaupt daran, eine Sicherheits-Vorabprüfung (S1) zu durchlaufen.

**Um voranzuschreiten, wird folgendes benötigt:**
- TFDA/Fachinformations-Quellen für Warnungen und Kontraindikationen (DG001 lösen), bevor eine Sicherheits-Vorabprüfung durchgeführt werden kann
- Bestätigte ursprüngliche Indikation und MOA-Daten für Elvitegravir (DG002 lösen), vorzugsweise direkt aus DrugBank/regulatorischer Fachinformation stammen, statt aus dem Rationaltext abgeleitet werden
- Neuprüfung der TxGNN-Ausgaben für Elvitegravir, um menschlich relevante Kandidatenindikationen zu identifizieren, da die aktuellen Top-3-Vorhersagen nicht klinisch praktikabel sind
- Falls FIV- oder SIV-Signale für einen Explorationszweck beibehalten werden, sollten sie zu einem veterinärmedizinischen/translationalen Forschungspfad geleitet werden statt zum Evaluierungspfad für menschliches Arzneimittel-Repurposing

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

