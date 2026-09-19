---
layout: default
title: Irbesartan
parent: Nur Modellvorhersage (L5)
nav_order: 212
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **4** 
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

# Irbesartan: Vom Bluthochdruck zur malignen hypertensiven Nierenkrankheit

## Zusammenfassung in einem Satz

Irbesartan ist ein Angiotensin-II-Rezeptorblocker (ARB), dessen etablierte Pharmakologie sich auf die Behandlung von Hypertonie durch Blockade des AT1-Rezeptors und Unterdrückung der RAAS-Aktivität konzentriert. Das TxGNN-Modell sagt eine mögliche neue Anwendung bei **maligner hypertensiver Nierenkrankheit** voraus, aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt, was sie in diesem Stadium zu einer reinen modellgestützten Hypothese macht.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Hypertonie (basierend auf Irbesartans bekannter ARB-Klassifizierung; nicht explizit erfasst im Feld `original_indications` dieses Evidence-Pakets) |
| Vorhergesagte neue Indikation | Maligne hypertensive Nierenkrankheit |
| TxGNN-Vorhersage-Score | 99.31% |
| Evidenzebene | L5 |
| Taiwan-Marktstatus | Nicht zugelassen (Nicht zugelassen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage begründet?

Formale Daten zum Wirkmechanismus von DrugBank stellen derzeit eine Datenlücke (DG002) in diesem Evidence-Paket dar. Basierend auf der mechanistischen Begründung, die die Vorhersage begleitet, ist Irbesartan ein AT1-Rezeptor-Antagonist (ARB), der den intraglomerulären Druck senkt und die Proteinurie reduziert, indem die Angiotensin-II-Aktivität blockiert wird – ein Wirkmechanismus mit etablierter pharmakologischer Grundlage bei allgemeiner hypertensiver Nephropathie (z. B. diabetische Nephropathie).

Die maligne hypertensive Nierenkrankheit ist jedoch eine akute Notfallerkrankung, die eine schnelle Blutdruckkontrolle neben oft steil abfallenden Nierenfunktion erfordert. ARBs haben einen relativ langsamen Wirkeintritt, und angesichts einer akut sich verschlechternden Nierenfunktion birgt die RAAS-Blockade das Risiko von Hyperkaliämie und weiterem GFR-Rückgang. Der TxGNN-Score scheint daher eher eine allgemeine RAAS-Pfad-Assoziation widerzuspiegeln als eine validierte klinische Möglichkeit, und – bemerkenswert – die begleitende Begründung für verwandte Vorhersagen (z. B. maligne renovaskuläre Hypertonie) kennzeichnet die ARB-Anwendung in diesem Kontext explizit als potentielle **Sicherheitsbedenken** statt als therapeutisches Signal, da die ARB/ACEi-Blockade der kompensatorischen efferenten arteriellen Konstriktion bei renovaskulärer Erkrankung akutes Nierenversagen auslösen kann.

Angesichts der völligen Abwesenheit von klinischen Studien oder Literatur, die speziell Irbesartan in dieser Indikation bewerten, sollte diese Vorhersage als eine vom Modell generierte Pathway-Hypothese interpretiert werden, nicht als Hinweis auf therapeutischen Nutzen.

---

## Evidence aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert.

---

## Literaturgestützte Evidenz

Derzeit keine verwandte Literatur verfügbar.

---

## Taiwan-Marktinformation

Irbesartan ist derzeit **nicht zugelassen** in Taiwan (0 Zulassungen im Datensatz). Keine Lizenz- oder produktbezogenen Daten sind in diesem Evidence-Paket verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen. Eine blockierende Datenlücke (DG001) wurde identifiziert: TFDA-Fachinformations-Warnungen/Kontraindikationen wurden noch nicht abgerufen, was den Eintritt in die S1-Sicherheits-Vorprüfungsphase verhindert. Es wurden keine Arzneimittel-Wechselwirkungs-Datensätze gefunden (`query_status: not_found`).

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die vorhergesagte Indikation wird nur durch L5 (nur modellgestützte Vorhersage) mit null unterstützenden klinischen Studien oder Literatur gestützt, das Arzneimittel ist derzeit in Taiwan nicht zugelassen, und eine blockierende Sicherheits-Datenlücke (TFDA-Kennzeichnung) verhindert eine formale Sicherheits-Vorprüfung. Darüber hinaus wirft die mechanistische Begründung selbst eher Vorsicht als Zuversicht auf, angesichts bekannter Risiken der RAAS-Blockade bei akutem/renovaskulärem Nierenkompromiss.

**Um fortzufahren, ist folgendes erforderlich:**
- TFDA-Fachinformation (Warnungen, Kontraindikationen) abrufen, um die blockierende Datenlücke DG001 zu beheben
- Formalen DrugBank-MOA-Datensatz bestätigen, um die Datenlücke DG002 zu beheben
- Gezielt Literatur-/klinische Studien-Suche speziell zu Irbesartan (oder ARB-Klasse) bei maligner hypertensiver Nierenkrankheit und renovaskulärer Hypertonie-Populationen
- Nierenfunktions- und Kalium-Überwachungsprotokoll, angesichts des mechanistischen Risikos der RAAS-Blockade bei akutem Nierenkompromiss
- Routenkompatibilitäts-Bewertung (derzeit als „pending" im Evidence-Paket markiert)

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

