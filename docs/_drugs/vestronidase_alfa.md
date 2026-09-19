---
layout: default
title: Vestronidase Alfa
parent: Nur Modellvorhersage (L5)
nav_order: 425
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
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

# Vestronidase Alfa: Von Mukopolysaccharidose Typ VII (Sly-Syndrom) zu Scheie-Syndrom

## Zusammenfassung in einem Satz

> Vestronidase alfa ist eine rekombinante humane β-Glucuronidase (GUS)-Enzymersatztherapie, die ursprünglich für **Mukopolysaccharidose Typ VII (Sly-Syndrom)** entwickelt wurde.
> Das TxGNN-Modell sagt voraus, dass sie möglicherweise wirksam für **Scheie-Syndrom (MPS I)** sein könnte,
> aber **es gibt derzeit keine klinischen Studien oder Literatur**, die diese spezifische Indikation direkt unterstützen, und die zugrundeliegende mechanistische Begründung deutet darauf hin, dass dies wahrscheinlich ein falsch-positives Ergebnis ist.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Mukopolysaccharidose Typ VII (Sly-Syndrom) *(nicht in deutschen Zulassungsdaten vorhanden — Arzneimittel nicht vermarktet; aus Sekundärliteratur gewonnen)* |
| Vorhergesagte neue Indikation | Scheie-Syndrom |
| TxGNN-Vorhersage-Score | 99.90% |
| Evidenzstufe | L5 (nur Modellvorhersage, keine unterstützenden Studien/Literatur) |
| Marktstatus in Deutschland | Nicht vermarktet |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückstellung |

---

## Warum ist diese Vorhersage plausibel?

Vestronidase alfa ist eine rekombinante humane β-Glucuronidase (GUS)-Enzymersatztherapie. Sein einziger validierter Mechanismus besteht darin, die enzymatische Defizienz, die durch **GUSB**-Genmutationen in MPS VII (Sly-Syndrom) verursacht wird, zu korrigieren und den Abbau von Glykosaminoglykanen (GAGs) wiederherzustellen, die sich sonst in Lysosomen ansammeln würden.

Das Scheie-Syndrom ist jedoch ein Subtyp von **MPS I**, der durch einen Mangel an **Alpha-L-Iduronidase (IDUA)** — einem anderen Enzym, das auf ein anderes (wenn auch verwandtes) Glykosaminoglykan-Substrat wirkt — verursacht wird. Es gibt keine bekannte biochemische Kreuzreaktivität oder Substituierbarkeit zwischen GUS und IDUA. Nach der mechanistischen Bewertung des Evidenzpakets selbst spiegelt dieser hohe TxGNN-Score höchstwahrscheinlich **ähnlichkeitsbasierte Einbettung im Wissensgraphen** zwischen phänotypisch verwandten lysosomalen Speicherkrankheiten wider, anstatt einen echten gemeinsamen Wirkstoff-Ziel-Mechanismus zu reflektieren.

Diese Besorgnis wird durch die breitere Vorhersageliste verstärkt: Acht der neun höchsten Kandidaten (Hurler-Syndrom, Sanfilippo-Syndrom und mehrere nicht verwandte angeborene Syndrome) zeigen das gleiche Muster — hohe Ähnlichkeitswerte, die durch die Clusterung von lysosomalen Speicherkrankheiten im Graphen getrieben werden, aber ohne Enzym-Level-Begründung und in mehreren Fällen mit Literatur, die bei genauerer Betrachtung tatsächlich auf die *ursprüngliche* zugelassene Indikation des Arzneimittels (MPS VII) anstelle der vorhergesagten Indikation verweist. Dies deutet auf ein mögliches Krankheitslabel-Mismatch-Problem in der zugrunde liegenden Evidenzdatenbank hin, das eine manuelle Überprüfung vor dem Voranbringen dieser Kandidaten rechtfertigt.

---

## Evidenz aus klinischen Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Evidenz aus der Literatur

Derzeit ist keine zugehörige Literatur verfügbar.

---

## Informationen zum deutschen Markt

Vestronidase alfa ist **derzeit nicht in Deutschland vermarktet**; es gibt keine BfArM-Zulassungseinträge für diese Bewertung.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: Eine blockierende Datenlücke besteht — das offizielle TFDA/BfArM-Label, Warnhinweise und Kontraindikationen wurden noch nicht abgerufen, was verhindert, dass dieser Kandidat die S1-Sicherheits-Vorbewertungsphase erreicht.)*

---

## Fazit und nächste Schritte

**Entscheidung: Zurückstellung**

**Begründung:**
- Es gibt keine klinischen Studien oder Literatur, die vestronidase alfa's Verwendung bei Scheie-Syndrom direkt unterstützen; die Vorhersage wird nur durch einen rohen TxGNN-Ähnlichkeitsscore (L5-Evidenz) unterstützt.
- Der vorgeschlagene Mechanismus (GUS-Ersatz) stimmt nicht mit dem enzymatischen Mangel überein, der dem Scheie-Syndrom zugrunde liegt (IDUA), was darauf hindeutet, dass dies wahrscheinlich ein falsch-positives Ergebnis ist, das durch strukturelle Ähnlichkeit zwischen lysosomalen Speicherkrankheiten im Wissensgraphen anstelle einer echten pharmakologischen Verbindung getrieben wird.
- Eine blockierende Datenlücke (fehlende offizielle Kennzeichnung/Warnhinweise/Kontraindikationen) verhindert unabhängig den Fortschritt zur Sicherheits-Vorbewertung (S1).

**Um voranzukommen, ist Folgendes erforderlich:**
- Abrufen der offiziellen TFDA/BfArM-Packungsbeilage (Warnhinweise, Kontraindikationen), um die blockierende Datenlücke zu schließen
- Beschaffung von bestätigten Wirkungsmechanismen und ursprünglichen Indikationsdaten aus DrugBank, um den aktuellen „[Data Gap]"-Datensatz zu ersetzen
- Manuelle Überprüfung der Literatur, die mit anderen Kandidaten in diesem Evidenzpaket verbunden ist (z. B. Sanfilippo-Syndrom), auf mögliche Krankheitslabel-Mismatches, bevor eine weitere Nutzung erfolgt
- Falls die Verfolgung dieses Kandidaten weitergeht, eine gezielte Literatur-/Präklinische Suche speziell nach GUS/IDUA-Kreuzreaktivität oder Fallberichten über die Verwendung von vestronidase alfa bei MPS I-Patienten in Auftrag geben

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

