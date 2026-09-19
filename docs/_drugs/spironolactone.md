---
layout: default
title: Spironolactone
parent: Nur Modellvorhersage (L5)
nav_order: 372
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **2** 
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

# Spironolakton: Von Aldosteron-assoziierter Flüssigkeitsretention bis Hypotrichosis simplex der Kopfhaut

## Zusammenfassung in einem Satz

> Spironolakton ist ein Mineralokortikoid-(Aldosteron-)Rezeptor-Antagonist, der historisch für Zustände wie Ödeme und Hypertonie verwendet wird, und off-label für androgenische Alopezie wegen seiner antiandrogenen Aktivität.
> Das TxGNN-Modell sagt voraus, dass es wirksam sein könnte für **Hypotrichosis simplex der Kopfhaut**, eine erbliche Haarausfallstörung,
> aber diese Vorhersage wird derzeit durch **0 klinische Studien** und **0 Publikationen** gestützt — Beweisniveau L5 (nur Modellvorhersage).

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht in Evidenzpaket dokumentiert (Datenlücke); Spironolakton ist allgemein bekannt als Aldosteron-Antagonist zur Behandlung von Ödemen/Flüssigkeitsretention und Hypertonie |
| Vorhergesagte neue Indikation | Hypotrichosis simplex der Kopfhaut |
| TxGNN-Vorhersage-Score | 99.26% |
| Beweisniveau | L5 |
| Marktstatus in Deutschland | Nicht im Handel |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Halten |

---

## Warum ist diese Vorhersage plausibel?

Derzeit sind keine detaillierten Wirkmechanismus-Daten in diesem Evidenzpaket verfügbar. Auf der Grundlage allgemein bekannter Pharmakologie ist Spironolakton ein Mineralokortikoid-Rezeptor-Antagonist, der auch antiandrogene Aktivität aufweist, weshalb es off-label für androgenische Alopezie (eine hormon-/androgen-bedingte Haarausfallerkrankung) verwendet wird.

Hypotrichosis simplex der Kopfhaut ist jedoch eine erbliche, autosomale Erkrankung, die am häufigsten mit **APCDD1**-Mutationen verbunden ist, die den für die normale Haarfollikelentwicklung erforderlichen **Wnt-Signalweg** stören. Dieser Mechanismus steht in keinem Zusammenhang mit Androgen- oder Mineralokortikoid-Signalwegen. Folglich gibt es keinen etablierten biologischen Weg, der die bekannte Pharmakologie von Spironolakton mit dieser spezifischen genetischen Störung verbindet — der hohe TxGNN-Score (0.99) spiegelt wahrscheinlich eher die Embedding-Ähnlichkeit zwischen „Haarausfall"-Phänotypen im Wissensgraph des Modells wider, als dass er einen echten kausalen oder mechanistischen Zusammenhang zeigt.

Ein zweiter Kandidat in diesem Evidenzpaket, **kongenitale Hypotrichose mit Milien** (Score 0.99, Rang 9732), zeigt das gleiche Muster: Es ist eine seltene ektodermale Dysplasie, die durch Gene der Keratinozyten-Differenzierung und Haarfollikelentwicklung bedingt ist, ohne bekannten Zusammenhang zu Mineralokortikoid- oder Androgen-Signalwegen. Beide Vorhersagen sollten nur als hypothesengenerierend behandelt werden, nicht als Beweis für therapeutische Plausibilität.

---

## Evidenz aus klinischen Studien

Derzeit keine verwandten klinischen Studien registriert

---

## Evidenz aus der Literatur

Derzeit keine verwandte Literatur verfügbar

---

## Marktsituation in Deutschland

Spironolakton wird derzeit laut diesem Evidenzpaket nicht in Deutschland vermarktet (0 Zulassungen in der Akte), daher kann keine Lizenztabelle erstellt werden.

---

## Sicherheitsüberlegungen

Bitte lesen Sie die Packungsbeilage für Sicherheitsinformationen.

*(Hinweis: TFDA-/Etiketten-Warnungen, Gegenanzeigen und Arzneimittel-Wechselwirkungsdaten sind derzeit nicht verfügbar — dies ist eine blockierende Datenlücke (DG001), die vor jeder Sicherheitsbewertung (S1) behoben werden muss.)*

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Die vorhergesagte Indikation hat keine Unterstützung durch klinische Studien oder Literatur (L5, Entscheidungsstufe S0), und der vorgeschlagene mechanistische Zusammenhang zwischen der bekannten Pharmakologie von Spironolakton und dieser erblichen Haarfollikelstörung des Wnt-Signalwegs ist biologisch nicht gestützt. Darüber hinaus fehlen Sicherheitsdaten (Warnungen/Gegenanzeigen), was eine vorläufige Sicherheitsbewertung blockiert.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA-/EMA-Etiketten-Warnungen und Gegenanzeigen (DG001, blockierend — erforderlich vor S1-Sicherheits-Screening)
- Verifizierte ursprüngliche Indikation und Wirkmechanismus-Daten aus DrugBank (DG002)
- Beliebige präklinische oder genetische Evidenz für eine Verbindung zwischen Mineralokortikoid-/antiandrogener Aktivität und APCDD1/Wnt-Signalweg-Haarfollikelstörungen
- Falls keine solche mechanistische oder empirische Evidenz gefunden werden kann, sollte dieser Kandidat indefinit bei S0/Halten verbleiben, anstatt allein aufgrund des TxGNN-Scores voranzugehen

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

