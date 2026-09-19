---
layout: default
title: Diroximel Fumarate
parent: Nur Modellvorhersage (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Diroximel Fumarate
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

# DIROXIMEL FUMARATE: Von unbekannter Originalindikation zu Diabetischer Katarakt

## Zusammenfassung in einem Satz

Diroximel fumarate ist ein Fumarsäureester-Prodrug, dessen Originalindikation und Wirkmechanismus derzeit in diesem Evidence Pack nicht dokumentiert sind (Datenlücke). TxGNN sagt eine mögliche Assoziation mit **Diabetischer Katarakt** voraus, aber diese Vorhersage wird durch **0 klinische Studien** und **0 Publikationen** gestützt, was sie derzeit zu einem reinen Modellsignal macht.

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Originalindikation | Nicht verfügbar (keine zugelassene Indikation dokumentiert) |
| Vorhergesagte neue Indikation | Diabetische Katarakt |
| TxGNN-Vorhersage-Score | 99.9993% |
| Evidenzstufe | L5 |
| Markt-Status in Deutschland | Nicht vermarktet (Not marketed) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Pausieren |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar. Basierend auf bekannten Informationen gehört diroximel fumarate zur Fumarsäureester-Klasse von Prodrugs, aber seine Originalindikation und pharmakologische Begründung sind in diesem Evidence Pack nicht dokumentiert, daher kann keine mechanistische Verbindung zur diabetischen Katarakt hergestellt werden.

Bemerkenswert ist, dass die top 10 vorhergesagten Indikationen für dieses Arzneimittel alle diabetes-bezogene okulare Erkrankungen sind (diabetische Katarakt, diabetische Retinopathie, verschiedene Katarakttypen) mit nahezu identischen TxGNN-Werten (0.999990–0.999992). Dieses Muster homogener, nicht differenzierter Werte über eine ganze Krankheitsgruppe ist eine bekannte Signatur von Modellen, die Vorhersagen durch einen gemeinsamen Knoten verknüpfen (z. B. „Diabetes" oder „Katarakt"), anstatt arzneimittelspezifische Signale zu erzeugen. Ohne unabhängige klinische oder Literaturbelege sollte dieses Muster als Flagge für potenzielle Modellüber-Generalisierung anstelle einer echten Umwidmungshypothese behandelt werden.

---

## Evidenz klinischer Studien

Derzeit keine zugehörigen klinischen Studien registriert

---

## Literaturbeweise

Derzeit keine zugehörige Literatur verfügbar

---

## Marktinformationen für Deutschland

Diroximel fumarate wird derzeit nicht in Deutschland vermarktet (Not marketed), und keine Zulassungsunterlagen sind verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind alle als Datenlücken im aktuellen Evidence Pack gekennzeichnet. Gemäß DG001 müssen TFDA/BfArM-Etikettenwarnungen und Kontraindikationen vor jeder Sicherheits-Vorbewertung (S1) eingeholt werden.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Pausieren**

**Begründung:**
Dieser Kandidat hat null klinische Studien, null Literaturunterstützung und keine Wirkmechanismus-Daten — kombiniert mit einem verdächtigen Muster von nahezu identischen TxGNN-Werten über alle 10 vorhergesagten Diabetes-/Augen-Indikationen hinweg, was darauf hindeutet, dass die Vorhersage eher das Shared-Node-Clustering widerspiegelt als ein spezifisches Arzneimittel-Krankheits-Signal. Es gibt keine Evidenzbasis, um über S0 hinaus voranzugehen.

**Um voranzugehen, ist Folgendes erforderlich:**
- DG001 (Blockierend) lösen: TFDA/offizielle Etikettenwarnungen und Kontraindikationen vor jeder Sicherheitsbewertung einholen
- DG002 (Hoch) lösen: MOA von DrugBank abrufen, um Bewertung der mechanistischen Plausibilität zu ermöglichen
- Bestätigung der ursprünglich zugelassenen Indikation(en) für diroximel fumarate, da derzeit keine dokumentiert sind
- Unabhängige Literatur-/klinische Studiensuche speziell zu diabetischer Katarakt und diroximel fumarate (oder ihrer Mutterverbindung Monomethylfumarat), um echtes Signal von Modell-Artefakt zu unterscheiden
- Manuelle Überprüfung der Krankheits-Embedding-Struktur von TxGNN für dieses Arzneimittel, um zu bewerten, ob das Diabetes-/Kataraktcluster eine Trainings-Daten- oder Überanpassungsproblematik widerspiegelt, bevor eine Indikation in diesem Cluster weiter vorangetrieben wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

