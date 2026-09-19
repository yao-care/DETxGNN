---
layout: default
title: Idebenone
parent: Nur Modellvorhersage (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Idebenone
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

# Idebenone: Investigative Neuanwendung auf Hepatische Porphyrie

## Zusammenfassung in einem Satz

> Das Evidenzpaket dokumentiert nicht Idebenones ursprüngliche zugelassene Indikation oder seinen Wirkmechanismus (beide werden als Datenlücken gekennzeichnet).
> Das TxGNN-Modell sagt voraus, dass es möglicherweise für **Hepatische Porphyrie** wirksam sein könnte,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — sie beruht allein auf topologischer Modellsimilarität.

## Schnelle Übersicht

| Punkt | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Nicht im Evidenzpaket dokumentiert |
| Vorhergesagte neue Indikation | Hepatische Porphyrie |
| TxGNN-Vorhersage-Score | 99.92% |
| Evidenzstufe | L5 (nur Modellvorhersage) |
| Marktstatus Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Ausstehend |

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten für Idebenone nicht im strukturierten Evidenzpaket verfügbar (gekennzeichnet als Datenlücke mit hohem Schweregrad, DG002). Basierend auf den mechanistischen Notizen, die den TxGNN-Vorhersagen beigefügt sind, wird Idebenone als **Coenzym-Q10-Analog** mit mitochondrialer Elektronentransport- und antioxidativer Aktivität beschrieben — diese Charakterisierung stammt aus dem Begründungstext des Modells statt aus einem bestätigten Wirkmechanismus-Datensatz, daher sollte sie als vorläufig behandelt werden.

Die ursprüngliche zugelassene Indikation ist ebenfalls nicht dokumentiert (`original_indications` ist leer, und es gibt keine Deutschland-Marktzulassungen, um sie daraus abzuleiten). Ohne eine bestätigte ursprüngliche Indikation ist es nicht möglich, die mechanistische Kontinuität zwischen „ursprünglicher Verwendung" und „hepatischer Porphyrie" auf die Weise zu bewerten, wie dieser Bericht es normalerweise tun würde.

Das Modell-Rationale selbst ist explizit über die Schwäche dieser Verbindung: Hepatische Porphyrie beinhaltet gestörte Häm-Biosynthese und mögliche sekundäre oxidative Belastung, und während Idebenones antioxidative/mitochondriale Unterstützungseigenschaften theoretisch mit der Verminderung oxidativer Schäden kompatibel sind, **es gibt keinen direkten Beweis, der Idebenone mit Porphyrin-Metabolismus oder ALA/PBG-Regulation verbindet**. Der hohe TxGNN-Score (99.92%) widerspiegelt Netzwerk-/topologische Ähnlichkeit im Wissensgraph des Modells, nicht bestätigte pharmakologische oder klinische Relevanz.

## Klinische Studienevidenz

Derzeit sind keine verwandten klinischen Studien registriert.

## Literaturbeweise

Derzeit ist keine verwandte Literatur verfügbar.

## Informationen zum Deutschland-Markt

Für Idebenone liegen derzeit keine Marktzulassungen in Deutschland vor (0 Lizenzen vorhanden).

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

## Fazit und nächste Schritte

**Entscheidung: Ausstehend**

**Begründung:**
Die Evidenzstufe ist L5 — die Vorhersage der hepatischen Porphyrie basiert ausschließlich auf TxGNN-Modell-Topologie, ohne klinische Studien oder Literaturstütze, und das Modell-Rationale selbst beschreibt die mechanistische Verbindung als indirekt/theoretisch. Daten zur ursprünglichen Indikation und zum Wirkmechanismus fehlen beide, und das Arzneimittel hat derzeit keine Marktpräsenz in Deutschland.

**Um fortzufahren, ist folgendes erforderlich:**
- TFDA/BfArM-Kennzeichnungsdaten (Warnungen, Kontraindikationen) — derzeit eine **blockierende** Datenlücke (DG001); erforderlich vor jeder S1-Sicherheitsbeurteilung
- Bestätigter Wirkmechanismus aus DrugBank oder Primärliteratur (DG002)
- Dokumentation von Idebenones ursprünglicher zugelassener Indikation(en), um eine mechanistische Kontinuitätsanalyse zu ermöglichen
- Präklinische oder mechanistische Studien, die mitochondriale/antioxidative Aktivität speziell mit Porphyrin-Metabolismus oder Häm-Biosynthese-Regulation verbinden
- Jegliche klinische oder fallbasierte Evidenz der Idebenone-Anwendung bei Porphyrie-Patienten, falls sie außerhalb registrierter Studien existiert

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

