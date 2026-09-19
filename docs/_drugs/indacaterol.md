---
layout: default
title: Indacaterol
parent: Nur Modellvorhersage (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: Von Bronchialerkrankung (COPD/Asthma) zu Nephrogenes Syndrom der Inadäquaten ADH-Sekretion

## Zusammenfassung in einem Satz

> Indacaterol ist ein langwirksamer β2-adrenergischer Agonist (LABA) mit bronchodilatorischer Wirkung, der aufgrund seiner Wirkstoffklasse vermutlich für COPD/Asthma-bezogene Bronchialerkrankungen entwickelt wurde – formale Daten zur Originalindikation sind eine bestätigte Datenlücke, da das Arzneimittel derzeit in Deutschland nicht zugelassen ist.
> Die Top-Vorhersage des TxGNN-Modells deutet auf mögliche Wirksamkeit beim **Nephrogenen Syndrom der Inadäquaten ADH-Sekretion (NSIAD)** hin,
> wird aber derzeit durch **null klinische Studien** und **null Publikationen** unterstützt, und die mechanistische Bewertung des Evidenzpakets selbst kennzeichnet die Vorhersage als biologisch implausibel.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Nicht formal registriert – Arzneimittel ist in Deutschland nicht zugelassen; pharmakologisch wird auf der Grundlage der Wirkstoffklasse (LABA) von COPD/Asthma-bezogener Bronchialerkrankung ausgegangen |
| Vorhergesagte neue Indikation | Nephrogenes Syndrom der Inadäquaten ADH-Sekretion (NSIAD) |
| TxGNN-Vorhersagescore | 99.54% |
| Beweisebene | L5 (nur Modellvorhersage, keine unterstützenden klinischen Studien oder Literatur) |
| Marktstatus Deutschland | Nicht zugelassen (Nicht zugelassen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Zurückhalten |

---

## Warum ist diese Vorhersage vertretbar?

Detaillierte Originaldaten zum Wirkmechanismus stellen derzeit eine bestätigte Datenlücke dar (DG002). Basierend auf bekannten Informationen zur pharmakologischen Klasse, die an anderer Stelle in diesem Evidenzpaket erwähnt werden, ist Indacaterol ein selektiver langwirksamer β2-adrenergischer Rezeptoragonist (LABA), der die Bronchialmuskulatur erschlafft – ein Wirkmechanismus, der mit COPD/Asthma-ähnlichen Bronchialerkrankungen assoziiert ist.

NSIAD hingegen wird durch persistierende, ligandenunabhängige Aktivierung des Vasopressin-V2-Rezeptors im renalen Sammelrohr angetrieben, wodurch es zu unangemessener Wasserbindung unabhängig von ADH-Spiegeln kommt. Es gibt keinen etablierten pharmakologischen Weg, der β2-adrenergische Agonisten mit V2-Rezeptoraktivität verbindet.

Das Evidenzpaket selbst weist darauf hin: *"與腎性抗利尿激素不當分泌症候群(NSIAD)之V2受體persistent activation機轉無已知關聯。TxGNN高分推測缺乏生物學合理性支持"* – mit anderen Worten, trotz des hohen Ähnlichkeitsscore des Modells wird die Top-Vorhersage des Modells nicht durch einen plausiblen biologischen Mechanismus unterstützt. Dies sollte eher als Vorsichtshinweis denn als echtes Repurposing-Signal behandelt werden.

---

## Evidenz aus klinischen Studien

Derzeit sind keine Registrierungen verwandter klinischer Studien vorhanden.

---

## Literaturbeweise

Derzeit ist keine verwandte Literatur verfügbar.

---

## Marktsituation Deutschland

Für Indacaterol sind derzeit keine Genehmigungen auf dem deutschen Markt registriert (gesamt_lizenzen = 0; Marktstatus: Nicht zugelassen). Diese Datenlücke auf Arzneimittel-Ebene (siehe DG001) verhindert auch eine formale Überprüfung der Sicherheit/Indikationen gemäß Fachinformation.

---

## Sicherheitsaspekte

Bitte beachten Sie die Fachinformation für Sicherheitsinformationen.

---

## Fazit und nächste Schritte

**Entscheidung: Zurückhalten**

**Begründung:**
Die Top-Vorhersage des TxGNN (NSIAD) hat keine Unterstützung durch klinische Studien oder Literatur (Beweisebene L5) und die mechanistische Rationale in demselben Evidenzpaket besagt, dass die Verbindung biologisch implausibel ist. In Kombination mit blockierenden Datenlücken bei BfArM-Fachinformation-Warnungen (DG001) und Wirkmechanismus (DG002) gibt es keine ausreichende Grundlage, diese Indikation voranzutreiben.

**Um Fortschritte zu erzielen, ist Folgendes erforderlich:**
- Behebung von DG001 (BfArM-Warnungen/Kontraindikationen) durch Abruf der Fachinformation
- Behebung von DG002 (bestätigter Wirkmechanismus) über DrugBank-API
- Falls noch immer ein Repurposing-Signal für dieses Arzneimittel gewünscht ist, ist zu beachten, dass **„Bronchialerkrankung"** (Rang 7 in diesem Paket) starke Evidenz trägt (L1, 30+ Studien, 20+ Publikationen, Entscheidungsstufe S3, „Mit Schutzmaßnahmen fortfahren") – allerdings weist die Rationale des Pakets selbst darauf hin, dass dies eine Bestätigung der *bekannten* Pharmakologie des Arzneimittels (COPD/Asthma) und keine echte Repurposing-Kandidaten darstellt, sodass dies separat von einem echten Neuentwicklungs-Standpunkt bewertet werden sollte.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

