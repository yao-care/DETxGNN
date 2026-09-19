---
layout: default
title: Fenbendazole
parent: Nur Modellvorhersage (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Fenbendazole
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

## Fenbendazol: Von der Anthelmintika-Anwendung zum Harnblasenkarzinom

## Zusammenfassung (Ein Satz)

Fenbendazol ist ein Benzimidazol-Anthelmintikum (Entwurmungsmittel), das derzeit nicht zur Anwendung beim Menschen in Deutschland zugelassen ist.
Das TxGNN-Modell sagt voraus, dass es möglicherweise wirksam gegen **Harnblasenkarzinom** sein könnte (und 9 weitere Harnblasenkrebssubtypen, alle mit ähnlich hohen Scores),
aber diese höchstrangierte Vorhersage hat derzeit **keine unterstützenden klinischen Studien oder Literatur** — Belege gibt es nur für eine eng verwandte Indikation (Neoplasma der Harnblase), und nur auf präklinischer Ebene.

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht angegeben im Nachweispaket; Fenbendazol ist ein Antiparasitikum (Anthelmintikum) der Benzimidazolklasse für Veterinär- und Humanmedizin, keine Onkologie-Indikation dokumentiert |
| Vorhergesagte neue Indikation | Harnblasenkarzinom |
| TxGNN-Vorhersage-Score | 99.99% |
| Evidenzlevel | L5 |
| Marktstatus Deutschland | ✗ Nicht zugelassen |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellen |

## Warum ist diese Vorhersage sinnvoll?

Derzeit sind detaillierte formale Wirkmechanismus-Daten (original_moa) für Fenbendazol nicht verfügbar. Basierend auf der Repurposing-Rationale des TxGNN-Modells gehört Fenbendazol zur Benzimidazol-Anthelmintikum-Klasse, und sein vorgeschlagener Antitumor-Wirkmechanismus besteht in der Bindung an die Colchicin-ähnliche Stelle auf β-tubulin, wobei die Mikrotubuluspolymerisation gehemmt wird. Dies stört die Bildung der mitotischen Spindel, verursacht einen G2/M-Phasen-Zellzyklus-Arrest, und kann zusätzlich GLUT-Glukose-Transporter herunterregulieren und Hexokinase hemmen, was den Tumorzellstoffwechsel beeinträchtigt — ein Wirkmechanismus, der konzeptionell Taxanen/Vinca-Alkaloiden ähnelt, aber an einer unterschiedlichen Bindungsstelle wirkt.

Es gibt keine etablierte Beziehung zwischen Fenbendazols ursprünglicher antiparasitärer Anwendung und Harnblasenkrebs; die Verbindung ist rein mechanistisch (Störung der Mikrotubuli, die sich auf schnell teilende Urothelialkarzinomzellen auswirkt), vom TxGNN-Netzwerk hergeleitet und nicht aus klinischen Präzedenzfällen abgeleitet.

Bemerkenswert ist, dass die höchstrangierte Vorhersage (Harnblasenkarzinom, Fokus dieses Berichts) **keine direkte Literatur- oder Studienevidenz** hat — ihre Rationale erklärt ausdrücklich, dass dies „rein eine TxGNN-Netzwerk-Vorhersage-Score" ist, die von der eng verwandten Indikation „Neoplasma der Harnblase" (Rang 2, Score 99.99%) extrapoliert ist, die zwei präklinische Literaturzitate aufweist: eines über Fenbendazol in Kombination mit CRISPR-Cas13a in einem intravesikalen Instillationsmodell für Harnblasenkrebs, und eines über einen nicht verwandten Karzinogenese-Wirkmechanismus-Weg (UBD-Aktivierung), der nicht spezifisch für die Fenbendazol-Behandlung ist. Acht weitere Harnblasenkrebssubtypen (Ränge 3–10) tragen die gleiche unbewiesene mechanistische Rationale ohne direkte Belege.

## Evidenz aus klinischen Studien

Derzeit sind keine verwandten klinischen Studien registriert

## Evidenz aus der Literatur

Derzeit ist keine verwandte Literatur verfügbar

## Informationen zum Markt Deutschland

Fenbendazol ist derzeit **nicht auf dem deutschen Markt verfügbar** (0 Zulassungen dokumentiert). Im Nachweispaket sind keine Produktlizenzen oder zugelassenen Humanindikationen vorhanden.

## Sicherheitserwägungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*Hinweis: Eine blockierende Datenlücke (DG001) wurde ermittelt — TFDA/Label-Warnungen und Kontraindikationen wurden noch nicht ermittelt, was eine vorläufige Sicherheitsbewertung (S1) verhindert.*

## Schlussfolgerung und nächste Schritte

**Entscheidung: Zurückstellen**

**Begründung:**
Die höchstrangierte Vorhersage (Harnblasenkarzinom) wird nur durch einen TxGNN-Netzwerk-Score unterstützt (L5, nur Modellvorhersage) ohne direkte klinische Studien oder Literatur. Selbst die am besten belegte verwandte Indikation (Neoplasma der Harnblase) erreicht nur L4 (präklinisch/mechanistisch), und das Arzneimittel ist nicht zur Anwendung beim Menschen in Deutschland zugelassen. In Kombination mit einer blockierenden Datenlücke zu Sicherheitswarnungen gibt es derzeit unzureichende Belege, um fortzufahren.

**Um fortzufahren, ist folgendes erforderlich:**
- Auflösung von DG001 (Blocking): Abruf/Bestätigung von Warnungen und Kontraindikationen für die Humananwendung, da Fenbendazol derzeit nur als Veterinär-/Antiparasitikum etabliert ist
- Auflösung von DG002 (High): Bestätigung der Wirkmechanismus-Daten von DrugBank zur Validierung der Mikrotubulus-Inhibitions-Hypothese
- In-vitro/in-vivo-Bestätigung der Antitumor-Aktivität speziell in Harnblasenkarzinom-Modellen (über die einzige für die verwandte Indikation „Neoplasma der Harnblase" gefundene Kombinationstherapie-Präklinik-Studie hinaus)
- Menschliche pharmakokinetische/Sicherheitsdaten, da es keine bestehende zugelassene menschliche Formulierung oder Dosierungsanwendung gibt
- Neubewertung, sobald Phase-1/2-Studien oder zusätzliche begutachtete Literatur für diese spezifische Indikation verfügbar wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

