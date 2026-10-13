---
layout: default
title: Mecasermin
parent: Nur Modellvorhersage (L5)
nav_order: 286
evidence_level: L5
indication_count: 5
---

# Mecasermin
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
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

# Mecasermin: Vom Laron-Syndrom zu Monosomie X (Turner-Syndrom)

## Zusammenfassung

Mecasermin ist rekombinanter humaner IGF-1 (insulinähnlicher Wachstumsfaktor 1) und wurde ursprünglich zur Behandlung des Laron-Syndroms eingesetzt. Das TxGNN-Modell sagt voraus, dass der Wirkstoff bei **Monosomie X (Turner-Syndrom)** wirksam sein könnte. Dafür liegen derzeit **keine klinischen Studien** und **keine Publikationen** vor, die Vorhersage beruht allein auf dem Modell.

---

## Kurzüberblick

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Laron-Syndrom |
| Vorhergesagte neue Indikation | Monosomie X |
| TxGNN-Vorhersagewert | 99,59 % |
| Evidenzgrad | L5 |
| Marktstatus in Deutschland | Nur erloschene Zulassung |
| Anzahl der Zulassungen | 1 |
| Empfohlene Entscheidung | Hold (zurückstellen) |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist: Mecasermin ersetzt IGF-1 direkt und wirkt unterhalb der Wachstumshormon-Achse (GH). Beim Laron-Syndrom, einer schweren primären IGF-1-Defizienz, ist diese Substitution der therapeutische Ansatz.

Das Turner-Syndrom (Monosomie X) ist durch Kleinwuchs gekennzeichnet, und Wachstumshormon ist die etablierte Standardtherapie. Über die IGF-1-Achse besteht daher ein denkbarer Zusammenhang. Allerdings ist das Turner-Syndrom in der Regel nicht durch einen primären IGF-1-Mangel definiert, und GH bleibt der Behandlungsstandard. Die Verbindung ist eine reine Vorhersage. Der TxGNN-Wert (0,996) ist eine rechnerische Schätzung und kein klinischer Beleg.

---

## Klinische Studien

Derzeit sind keine zugehörigen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit liegt keine zugehörige Literatur vor.

---

## Informationen zum deutschen Markt

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000704 | Increlex | – | Laron-Syndrom |

Diese Zulassung ist erloschen; aktuell besteht keine gültige Zulassung in Deutschland.

---

## Sicherheitshinweise

- **Arzneimittelwechselwirkungen:** Insgesamt wurden 24 Wechselwirkungen erfasst, die in der verfügbaren Datenbasis als **moderat** eingestuft sind. Sie betreffen blutzuckersenkende Wirkstoffe, da IGF-1 selbst blutzuckersenkend wirkt und das Hypoglykämierisiko steigen kann:
  - **Sulfonylharnstoffe:** Chlorpropamid, Acetohexamid, Glimepirid, Glipizid, Glibenclamid
  - **Glinid:** Nateglinid
  - **Insuline:** Humaninsulin (u. a. Normal-, Isophan-, Zink- und Zink-Depot-Formen, inhalatives Humaninsulin), Insulin aspart (auch Protamin-Form), Insulin degludec, Insulin detemir, Insulin glargin, Insulin glulisin, Insulin lispro (auch Protamin-Form)

Zu Warnhinweisen und Gegenanzeigen liegen keine Daten vor. Bitte die Fachinformation zu Rate ziehen.

---

## Weitere vorhergesagte Indikationen (zur Einordnung)

| Rang | Indikation | TxGNN-Wert | Einschätzung |
|---|---|---|---|
| 2 | Wolman-Krankheit mit Hypolipoproteinämie und Akanthozytose | 99,09 % | Kein erkennbarer mechanistischer Zusammenhang; vermutlich Artefakt des Graphen. Hold |
| 3 | Wachstumshormon-Insensitivitätssyndrom mit Immundysregulation 2, autosomal-dominant | 99,06 % | Biologisch plausibelster Kandidat (IGF-1-Mangel trotz normalem/hohem GH, analog zum Laron-Syndrom); adressiert jedoch nicht die Immundysregulation. Forschungsfrage |
| 4 | Ösophagusvarizen mit Blutung | 99,03 % | Kein mechanistischer Zusammenhang; theoretisches Risiko durch mitogene Wirkung. Hold |
| 5 | Ösophagusvarizen ohne Blutung | 99,03 % | Wie Rang 4; identischer Wert deutet auf gemeinsame Graph-Assoziation hin. Hold |

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Für Monosomie X liegen weder klinische Studien noch Literatur vor (Evidenzgrad L5). Der Standard (Wachstumshormon) ist etabliert, und ein primärer IGF-1-Mangel ist beim Turner-Syndrom nicht typisch. Zudem besteht in Deutschland keine gültige Zulassung.

**Für ein Fortschreiten sind folgende Schritte nötig:**
- Gezielte Literaturrecherche zu IGF-1 beim Turner-Syndrom; vorrangig außerdem zur STAT5B-Defizienz bzw. zum GH-Insensitivitätssyndrom (Rang 3), da dieser Kandidat plausibler ist
- Daten zum Wirkmechanismus (MOA) aus DrugBank
- Warnhinweise und Gegenanzeigen aus der Fachinformation (BfArM); dies ist eine blockierende Datenlücke für das Sicherheits-Screening
- Klärung des Zulassungsstatus und der Verfügbarkeit des Präparats in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

