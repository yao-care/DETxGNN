---
layout: default
title: Relebactam Monohydrate
parent: Nur Modellvorhersage (L5)
nav_order: 333
evidence_level: L5
indication_count: 0
---

# Relebactam Monohydrate
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **0** 
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

# Relebactam-Monohydrat: β-Lactamase-Inhibitor — Repurposing-Analyse kann nicht fortgesetzt werden

## Zusammenfassung in einem Satz

Relebactam-Monohydrat ist ein β-Lactamase-Inhibitor, der in Kombination mit Imipenem-Cilastatin verabreicht wird und von der FDA 2019 für schwere nosokomiale Gram-negative Bakterieninfektionen zugelassen wurde.
Das aktuelle Evidence Pack enthält **keine TxGNN-vorhergesagten Indikationen** und Angaben zu kritischen Eingaben — Wirkmechanismus und behördliche Kennzeichnung — die erforderlich sind, um die Repurposing-Pipeline voranzutreiben.
Ohne vorhergesagte Indikationen kann eine standardmäßige Repurposing-Bewertung nicht abgeschlossen werden; **Hold** ist die einzig vertretbare Empfehlung, bis Datenlücken geschlossen sind.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nosokomiale / beatmungsassoziierte Bakterienpneumonie; komplizierte intra-abdominale und Harnwegsinfektionen (mit Imipenem-Cilastatin) |
| Vorhergesagte neue Indikation | — (Keine TxGNN-Vorhersage generiert) |
| TxGNN-Vorhersagenwert | — |
| Evidence Level | L5 |
| Status auf dem Taiwan-Markt | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Arzneimittelhintergrund

Für Relebactam-Monohydrat wurde keine TxGNN-Vorhersage generiert, daher kann die standardmäßige Analyse „Warum ist diese Vorhersage sinnvoll?" nicht abgeschlossen werden. Der folgende Hintergrund wird aus veröffentlichter Literatur bereitgestellt, um zukünftige Pipeline-Durchläufe zu unterstützen.

Relebactam ist ein bicyclisches Piperidin-basierter Inhibitor von Serin-β-Lactamasen der Klasse A und C (einschließlich KPC-Carbapenemase und AmpC-Enzyme). Es besitzt keine intrinsische antibakterielle Aktivität; seine Funktion besteht darin, Imipenem vor enzymatischem Abbau zu schützen und dadurch die Wirksamkeit von Imipenem gegen ansonsten resistente Organismen wie KPC-produzierende *Klebsiella pneumoniae* und Imipenem-resistente *Pseudomonas aeruginosa* wiederherzustellen. Das Kombinationspräparat mit fester Dosierung (Imipenem 500 mg / Cilastatin 500 mg / Relebactam 250 mg, Handelsname RECARBRIO™, Merck) wurde im Juli 2019 von der FDA zugelassen.

Mechanistische MOA-Daten konnten in diesem Evidence Pack nicht abgerufen werden (DG002). Bis der MOA formal codiert ist, kann der TxGNN-Knowledge-Graph keine Vorhersagen für Arzneimittel-Krankheits-Verbindungen für diese Substanz generieren.

---

## Taiwan-Marktinformationen

Relebactam-Monohydrat hat **keine von der TFDA zugelassenen Produkte** in Taiwan zum Zeitpunkt der Abfrage. Es sind keine Lizenzunterlagen oder Darreichungsformen vorhanden.

---

## Sicherheitsaspekte

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Keine Warnungen, Kontraindikationen oder Arzneimittelwechselwirkungsdaten konnten aus diesem Evidence Pack abgerufen werden.

> **Hinweis für Analytiker:** Die TFDA-Abfrage zur Packungsbeilage hat einen Treffer ergeben (Abfrage-ID 4, Ergebnisanzahl = 1), was darauf hindeutet, dass der Labeltext analysierbar sein könnte. Das direkte Extrahieren dieses Inhalts würde DG001 auflösen und den Sicherheitsabschnitt freigeben.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die TxGNN-Pipeline hat keine vorhergesagten Indikationen generiert, da kritische Eingaben — Wirkmechanismus (DG002, Schweregrad: Hoch) und TFDA-Warnkennzeichnung (DG001, Schweregrad: Blockierend) — nicht erfolgreich aufgenommen wurden. Eine auf einem leeren Vorhersagensatz basierende Repurposing-Bewertung würde keine wissenschaftliche Gültigkeit haben.

**Folgende Maßnahmen sind erforderlich, um fortzufahren:**

1. **Auflösen von DG001 — Sicherheitskennzeichnung (Blockierend):** Die TFDA-Abfrage zur Packungsbeilage hat ein Ergebnis ergeben; analysieren Sie dieses PDF, um Warnungen, Kontraindikationen und Dosierungsinformationen zu extrahieren.
2. **Auflösen von DG002 — MOA (Hoch):** Fragen Sie DrugBank ab (Abfrage-ID 3 ergab 1 Ergebnis), um den pharmakologischen Mechanismus zu extrahieren und in den TxGNN-Knowledge-Graph zu codieren.
3. **TxGNN-Pipeline erneut ausführen:** Sobald MOA- und Kennzeichnungseingaben vollständig sind, `predicted_indications` neu generieren.
4. **Verbesserung der Datenbankabfragekohärenz:** Erwägen Sie, als Plain-Text `"relebactam"` (ohne das Salzsuffix „monohydrat") in DrugBank, PubChem und klinischen Versuchsregistern abzufragen, um die Abrufquote zu maximieren.
5. **DDI-Abfrage:** Wiederholen Sie die Arzneimittelwechselwirkungsabfrage nach Auflösung des INN-Suffix-Problems; aktuelles Ergebnis ist `not_found` mit 0 Wechselwirkungen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

