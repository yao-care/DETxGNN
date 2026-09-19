---
layout: default
title: Insulin Lispro
parent: Nur Modellvorhersage (L5)
nav_order: 209
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
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

# Insulin Lispro: Von Diabetes mellitus zu Autoimmun-Oophoritis

## Zusammenfassung in einem Satz

Insulin lispro ist ein schnellwirkendes Insulinanalogon zur Blutglukosekontrolle bei Diabetes mellitus.
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam für **Autoimmun-Oophoritis** sein könnte,
doch derzeit unterstützen **0 klinische Studien** und **0 Publikationen** diese Richtung, und die zugrunde liegende Rationale kennzeichnet diese Vorhersage als wahrscheinlich Rauschen auf Graphen-Ebene statt als echtes mechanistisches Signal.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Diabetes mellitus (Blutglukosekontrolle; detaillierter regulatorischer Indikationstext nicht in diesem Evidence-Pack verfügbar) |
| Vorhergesagte neue Indikation | Autoimmun-Oophoritis |
| TxGNN-Vorhersage-Score | 99.78% |
| Evidenzstufe | L5 |
| Marktstatus Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte Wirkmechanismus-Daten nicht verfügbar (Data Gap DG002). Basierend auf allgemeinem pharmakologischem Wissen ist Insulin lispro ein schnellwirkendes Insulinanalogon, das an den Insulinrezeptor bindet, um die zelluläre Glukoseaufnahme zu fördern; seine Wirksamkeit bei Diabetes mellitus ist gut belegt.

Für die höchstrangig bewertete Vorhersage, Autoimmun-Oophoritis, fällt die mechanistische Bewertung des Evidence-Packs selbst explizit negativ aus: Es gibt **keine bekannte biologische Beziehung** zwischen Autoimmun-Oophoritis und dem Insulinrezeptor-/Glukosestoffwechsel-Signalweg. Der hohe TxGNN-Score entsteht höchstwahrscheinlich, weil beide Erkrankungen im Trainings-Wissensgraph als „Autoimmunerkrankung" getaggt sind und zusammen mit Typ-1-Diabetes auftreten – ein semantisches Co-Occurrenz-Artefakt statt ein echter mechanistischer Link. Das Evidence-Pack selbst klassifiziert dies als „Datenbank-Rauschen ohne mechanistische Unterstützung".

Mehrere niedriger bewertete Kandidaten in diesem Pack zeigen vergleichsweise plausiblere (wenn auch weiterhin schwache) Rationale – zum Beispiel Pankreasagenesie (Rang 7) und Thiamin-responsive Funktionsstörung (Rang 2) sind beide mit echten Diabetes-assoziierten Begleiterkrankungen verknüpft, bei denen Insulin als Supportivtherapie verwendet wird. Dies sind nach wie vor Erweiterungen der bekannten Diabetes-Indikation statt echte neue Indikationen, aber sie verdienen mehr Beachtung als der höchstrangig bewertete Kandidat. Mehrere andere Kandidaten (arzneimittelinduzierte lokalisierte Lipodystrophie, zentrifugale Lipodystrophie, druckinduzierte lokalisierte Lipoatrophie) werden als wahrscheinlich Darstellungen von Insulins bekannter **Nebenwirkung** (Injektionsstellen-Lipodystrophie), die fälschlicherweise als Behandlungsbeziehung kodiert wurden, gekennzeichnet und sollten als Sicherheitssignale behandelt werden, nicht als therapeutische Möglichkeiten.

## Klinische Studienevidenz

Derzeit keine verwandten klinischen Studien registriert

## Literaturevidenz

Derzeit keine verwandte Literatur verfügbar

## Marktinformation Deutschland

Für Insulin lispro sind derzeit keine Vermarktungszulassungen im Evidence-Pack dokumentiert (Marktstatus: Nicht vermarktet; Gesamtzulassungen: 0).

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die höchstrangig vorhergesagte Indikation (Autoimmun-Oophoritis) hat L5-Evidenz mit null unterstützenden klinischen Studien oder Literatur, und die mechanistische Bewertung des Evidence-Packs selbst kommt zu dem Ergebnis, dass sie höchstwahrscheinlich ein semantisches Co-Occurrenz-Artefakt im Trainings-Graph statt eine echte biologische Assoziation ist. Kein anderer Kandidat in diesem Pack erreicht über L4/S1 „Forschungsfrage"-Status hinaus, und diejenigen (Pankreasagenesie, Thiamin-responsive Funktionsstörung) sind im Wesentlichen Reformulierungen der bestehenden Diabetes-Indikation in seltenen genetischen Subtypen, keine echten neuen Indikationen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/BfArM Packungsbeilage (Warnhinweise, Kontraindikationen) – derzeit blockierend (DG001)
- Detaillierte Wirkmechanismus-Daten aus DrugBank – derzeit hochpriorisierte Datenlücke (DG002)
- Bei Verfolgung von Pankreasagenesie oder Thiamin-responsive Funktionsstörung als Forschungsfragen, Fallserien- oder Registerdaten zur Insulin-Verwendung in diesen seltenen genetischen Diabetes-Subtypen
- TxGNN-Scoring erneut durchführen, wobei Lipodystrophie-verwandte Kandidaten als Nebenwirkungssignale statt als Kandidaten-Indikationen klassifiziert sind, um zukünftig falsch-positive Ergebnisse aus demselben Graph-Muster zu vermeiden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

