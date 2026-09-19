---
layout: default
title: Tecovirimat
parent: Nur Modellvorhersage (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Tecovirimat
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

# Tecovirimat: Von Pockenvirus-/Orthopoxvirus-Infektion zu Hordeolum

## Zusammenfassung in einem Satz

Tecovirimat ist ein VP37-Hüllprotein-Inhibitor, der ursprünglich entwickelt und von der FDA für Pockenerkrankungen und Orthopoxvirus-Infektionen (einschließlich Mpox) zugelassen wurde und über einen Mechanismus wirkt, der spezifisch für das *Orthopoxvirus*-Genus ist. Die Top-Vorhersage von TxGNN ist **Hordeolum**, aber die eigene mechanistische Überprüfung des Modells kennzeichnet dies als **hohen Embedding-Score ohne biologische Plausibilität**, da Hordeolum eine bakterielle (typischerweise staphylokokkenbedingte) Augenliddrüsen-Infektion ist, die mit der Pockenvirus-Replikation oder dem Budding nichts zu tun hat. **Keine klinischen Studien oder Fachliteratur unterstützen diese spezifische Kombination.**

---

## Schnellübersicht

| Element | Inhalt |
|------|------|
| Ursprüngliche Indikation | Pockenerkrankung / Orthopoxvirus-Infektion (einschl. Mpox), nach Literaturkontext im Evidenzpaket |
| Prognostizierte neue Indikation | Hordeolum |
| TxGNN-Vorhersage-Score | 99.66% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus in Deutschland | ✗ Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Zurückhalten** |

---

## Warum ist diese Vorhersage sinnvoll?

Tecovirimat hemmt das VP37-Hüllprotein, einen Mechanismus, der spezifisch für das *Orthopoxvirus*-Genus ist (Variola/Pockenerkrankung, Mpox, Vaccinia). Dieser Mechanismus hat keine bekannte Relevanz für Augenliddrüsen-Infektionen wie Hordeolum, die durch Bakterien (typischerweise *Staphylococcus aureus*) verursacht werden, die die Meibom- oder Zeis-Drüsen infizieren — eine völlig andere Pathogen-Klasse und Krankheitsprozess.

Das Evidenzpaket selbst weist diese Vorhersage in seiner mechanistischen Bewertung explizit zurück: **„Der hohe Score von TxGNN spiegelt eine Embedding-Space-Koinzidenz wider, ohne biologische Plausibilität."** Das gleiche Muster wiederholt sich bei den Rängen 2–10 (Vibrio-Infektion, Klebsiella-Infektion, Noma, Arbovirus-Infektion, Equine Infectious Anemia, idiopathisches Herpes, Astroviridae-Infektion, Arterivirus-Infektion) — alle sind bakterielle Infektionen, unverwandte RNA-/DNA-Virus-Familien oder nur veterinärmedizinische Erreger ohne mechanistischen Bezug zur VP37-Hemmung.

Die eine Ausnahme in diesem Kandidatensatz ist **Rang 5, „Koinfektion"** (L3, S1, die Evidenz umfasst 20 echte Veröffentlichungen). Bei genauerer Lektüre stellt dieses Literaturcluster jedoch kein echtes neues Indikationssignal dar — es besteht aus Fallberichten und Reviews, die die **existierende, bereits zugelassene Anwendung von Tecovirimat für Mpox** bei Patienten mit HIV oder anderen Koinfektion beschreiben (z.B. Neurosyphilis, VZV). Dies scheint ein **Datenkennzeichnungsartefakt** zu sein: die korrekte Krankheitskennzeichnung sollte „Mpox bei immunogeschwächten/koinfizierten Patienten" lauten, nicht ein neuartiges Repurposing-Ziel. Sie sollte nicht als neue Indikationsevidenz gezählt werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Fachliteratur

Derzeit ist keine zugehörige Fachliteratur für Hordeolum verfügbar.

*Anmerkung: 20 Veröffentlichungen existieren für Rang 5 („Koinfektion"), aber diese beschreiben die bereits zugelassene Mpox-Indikation von Tecovirimat bei HIV-/koinfizierten Populationen statt einer neuartigen Repurposing-Hypothese — siehe Begründung oben.*

---

## Marktinformationen für Deutschland

Tecovirimat ist **derzeit nicht auf dem Markt in Deutschland** (0 Zulassungen registriert), daher ist keine Zulassungstabelle verfügbar.

---

## Sicherheitserwägungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. Wichtige Warnhinweise, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind in diesem Evidenzpaket noch nicht verfügbar (gekennzeichnet als **Blocking**-Datenlücke, DG001 — TFDA/BfArM-Etikett-Warnhinweise und Kontraindikationen müssen abgerufen werden, bevor ein S1-Sicherheits-Screening durchgeführt werden kann).

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Alle zehn Top-Vorhersagen von TxGNN für Tecovirimat mangelt es an mechanistischer Plausibilität oder unterstützender klinischer/Fachliteratur-Evidenz. Neun von zehn (Hordeolum, Vibrio-Infektion, Klebsiella-Infektion, Noma, Arbovirus-Infektion, Equine Infectious Anemia, idiopathisches Herpes, Astroviridae-Infektion, Arterivirus-Infektion) sind bakterielle, unverwandte Virus- oder tiermedizinische Zustände ohne Bezug zum VP37-Orthopoxvirus-Mechanismus. Der eine Kandidat mit Literaturunterstützung („Koinfektion") ist sehr wahrscheinlich eine falsch gekennzeichnete Instanz der existierenden Mpox-Indikation von Tecovirimat bei HIV-koinfizierten Patienten, nicht ein echtes Repurposing-Signal.

**Um fortzufahren, ist Folgendes erforderlich:**
- **DG001 (Blocking)** beheben: TFDA/BfArM-Etikett-Warnhinweise und Kontraindikationen abrufen, bevor eine Sicherheitsstufen-Bewertung (S1) durchgeführt wird
- **DG002 (High)** beheben: formale DrugBank-/FDA-Etikett-MOA-Dokumentation abrufen, um zukünftige mechanistische Bewertungen ordnungsgemäß zu verankern
- „Koinfektion" in der TxGNN-Indikations-Ontologie als „Mpox bei HIV/immunogeschwächten Patienten" umkennzeichnen, um eine Vermischung von existierender Indikationsevidenz mit neuartigen Repurposing-Signalen zu vermeiden
- TxGNN-Bewertung erneut durchführen und dabei bekannte Off-Target-Embedding-Cluster (bakterielle/tiermedizinische Erkrankungen) ausschließen, falls dieses Muster bei anderen Orthopoxvirus-spezifischen Antiviralen erneut auftritt

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

