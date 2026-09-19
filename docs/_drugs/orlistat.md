---
layout: default
title: Orlistat
parent: Nur Modellvorhersage (L5)
nav_order: 284
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **1** 
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

# Orlistat: Von unspezifischer ursprünglicher Indikation zu Hypervitaminose

## Zusammenfassung in einem Satz

Die ursprüngliche genehmigte Indikation von Orlistat ist im aktuellen Evidenzpaket nicht dokumentiert, und sein Wirkmechanismus (MOA) ist als Datenlücke hohen Schweregrades gekennzeichnet, die ausstehend zur DrugBank-Verifikation ist. Das TxGNN-Modell sagt eine mögliche Anwendung in **Hypervitaminose** voraus, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** unterstützt – sie beruht vollständig auf einer theoretischen, inversen Wirkmechanismus-Rationale.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | **Nicht im Evidenzpaket dokumentiert (Datenlücke)** |
| Vorhergesagte neue Indikation | **Hypervitaminose** |
| TxGNN-Vorhersage-Score | 99.42% (Rang #6553) |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | **Nicht vermarktet** |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Abwarten** |

---

## Warum ist diese Vorhersage begründet?

Der formale Wirkmechanismus von Orlistat ist in diesem Evidenzpaket noch nicht bestätigt (gekennzeichnet als Datenlücke hohen Schweregrades, DG002, ausstehend DrugBank-API-Verifikation). Die dieser Vorhersage zugeordnete Umpositionierungsrationale beschreibt Orlistat jedoch als einen gastrointestinalen Lipase-Hemmer, der die Hydrolyse von Nahrungstriglyceriden blockiert und dadurch die Fettaufnahme im Darm verringert.

Eine bekannte Folge dieses Wirkmechanismus – klinisch als Nebenwirkung behandelt, die Supplementierung erfordert – ist die verminderte Aufnahme fettlöslicher Vitamine (A, D, E, K). Die TxGNN-Vorhersage kehrt im Wesentlichen diesen bekannten Effekt um: Wenn Orlistat die Aufnahme fettlöslicher Vitamine verringert, könnte es theoretisch zur Senkung der übermäßigen Aufnahme bei Hypervitaminose A/D/E/K umpositioniert werden.

Dies ist eine wirkmechanistisch plausible Hypothese, keine evidenzgestützte therapeutische Anwendung. Sie wurde in keiner klinischen Studie geprüft und wird durch keine Literatur bis heute unterstützt, und die zugrunde liegenden MOA-Daten selbst erfordern noch formale Verifikation, bevor diese Rationale als zuverlässig angesehen werden kann.

---

## Klinische Studienevidenz

Derzeit keine verwandten klinischen Studien registriert

---

## Literaturevidenz

Derzeit keine verwandte Literatur verfügbar

---

## Deutschland-Marktinformationen

Orlistat hat derzeit in Deutschland keine Marktzulassung – der Marktstatus ist **nicht vermarktet**, mit 0 registrierten Lizenzen. Keine Einträge für Produkte, Darreichungsformen oder genehmigte Indikationen sind verfügbar.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Abwarten**

**Begründung:**
Diese Vorhersage wird nur durch eine theoretische Umkehrung des Wirkmechanismus unterstützt (L5, Entscheidungsstadium S0), ohne klinische Studien oder Literaturbelege. Eine blockierende Datenlücke bezüglich TFDA-Kennzeichnungshinweisen/Kontraindikationen (DG001) verhindert eine Vorab-Sicherheitsbewertung, und der Wirkmechanismus des Arzneimittels selbst (DG002) ist nicht verifiziert.

**Um fortzufahren, wird Folgendes benötigt:**
- Bestätigung des Wirkmechanismus von Orlistat über DrugBank-API (DG002 auflösen)
- Erwerb und Analyse der TFDA-Kennzeichnungs-PDF auf Hinweise/Kontraindikationen (DG001 auflösen – blockierend)
- Identifikation mindestens präklinischer oder beobachtender Evidenz, die Orlistat direkt mit der Hypervitaminose-Therapie verknüpft, bevor das Stadium S0 überschritten wird
- Neubewertung des regulatorischen Weges in Deutschland, da das Arzneimittel derzeit dort nicht vermarktet ist

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

