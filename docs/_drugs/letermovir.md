---
layout: default
title: Letermovir
parent: Nur Modellvorhersage (L5)
nav_order: 228
evidence_level: L5
indication_count: 1
---

# Letermovir
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

# Letermovir: Von unspezifischer ursprünglicher Indikation zu vulvovaginaler Candidiasis

## Zusammenfassung in einem Satz

Die ursprüngliche zugelassene Indikation von Letermovir ist im aktuellen Evidenzpaket nicht verfügbar. Das TxGNN-Modell sagt potenzielle Wirksamkeit bei **vulvovaginaler Candidiasis** voraus, diese Vorhersage wird jedoch derzeit durch **0 klinische Versuche** und **0 Publikationen** unterstützt, und die eigene mechanistische Rationale des Modells markiert die Verbindung als biologisch implausibel.

---

## Schnelübersicht

| Artikel | Inhalt |
|---|---|
| Ursprüngliche Indikation | Nicht verfügbar in aktuellen Daten (keine Lizenzdatensätze) |
| Vorhergesagte neue Indikation | Vulvovaginale Candidiasis |
| TxGNN-Vorhersagepunktzahl | 99.88% (Rang 1959) |
| Evidenzebene | L5 |
| Taiwan-Marktstatus | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhaltung |

---

## Warum ist diese Vorhersage angemessen?

Derzeit sind detaillierte Wirkmechanismus-Daten für Letermovir in diesem Evidenzpaket nicht verfügbar (Datenlücke DG002, markiert als hoher Schweregrad – Behebung ausstehend über DrugBank-API-Abfrage).

Die eigene Umwidmungsrationale des Modells bietet jedoch bereits eine mechanistische Bewertung, und diese ist negativ: Letermovir hemmt spezifisch den CMV-DNA-Terminase-Komplex (human herpesvirus 5) (pUL56/pUL89/pUL51-Untereinheiten), ein virusspezifisches Ziel ohne Entsprechung in Pilzpathogenen wie *Candida* spp. Vulvovaginale Candidiasis ist eine Pilzinfektion, die typischerweise durch Targeting der Ergosterolsynthese (z. B. Azole, die CYP51/Lanosterol-Demethylase hemmen) oder der Synthese der Pilzzellwand (Echinocandine) behandelt wird – Wege, die mit Letermovirs antiviraler Wirkungsweise nichts zu tun haben.

Der hohe TxGNN-Score (99.88%) spiegelt höchstwahrscheinlich eine indirekte Knowledge-Graph-Assoziation wider – zum Beispiel treten beide Entitäten häufig zusammen mit immungeschwächten/Transplantations-Patientenpopulationen in den zugrunde liegenden Daten auf – eher als echte pharmakologische Ähnlichkeit. Diese Vorhersage sollte als Graph-Embedding-Artefakt behandelt werden, bis unabhängige mechanistische oder klinische Beweise entstehen.

---

## Klinische Studienbelege

Derzeit sind keine damit zusammenhängenden klinischen Studien registriert.

---

## Literaturbelege

Derzeit ist keine damit zusammenhängende Literatur verfügbar.

---

## Taiwan-Marktinformationen

Letermovir wird derzeit in Taiwan **nicht vermarktet** (0 Lizenzen auf Datensatz), daher sind keine Zulassungsdetails verfügbar.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhaltung**

**Begründung:**
Die Vorhersage wird nur durch einen rohen TxGNN-Score (L5, S0) unterstützt, ohne klinische Studien, ohne Literatur und ohne vermarktetes Produkt in Taiwan, worauf man sich stützen könnte. Noch wichtiger ist, dass die eigene mechanistische Rationale des Modells explizit keine plausible pharmakologische Verbindung zwischen einem antiviralen DNA-Terminase-Inhibitor und einer antimykotischen Indikation findet – dies ist ein starkes Signal, dass die Assoziation spurios ist, anstatt ein echter Umwidmungsansatz zu sein.

**Zum Fortfahren ist Folgendes erforderlich:**
- Lösen Sie DG001 (TFDA/Herstellerkennzeichnung – Warnungen und Kontraindikationen) auf, bevor eine Überprüfung in der Sicherheitsphase (S1) beginnen kann
- Lösen Sie DG002 (bestätigter Wirkmechanismus über DrugBank) auf, um mechanistische Plausibilität angemessen zu bewerten oder auszuschließen
- Unabhängige präklinische oder In-vitro-Antimykotika-Aktivitätsdaten für Letermovir, da derzeit keine biologische Rationale diese Indikation unterstützt
- Bewerten Sie die Kandidatenpriorität neu – angesichts der mechanistischen Nichtübereinstimmung könnten Ressourcen besser auf andere vorhergesagte Indikationen mit stärkerer biologischer Plausibilität gerichtet werden

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

