---
layout: default
title: Dabigatran Etexilate
parent: Nur Modellvorhersage (L5)
nav_order: 127
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Dabigatran Etexilate: vorhergesagte neue Indikation Sklerosierende Cholangitis (Evidenzstufe L5). Ursprüngliche Indikation: Venöse Thromboembolie"
monitor_inn: "dabigatran etexilate"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
{: .fs-9 }

Evidenzniveau: **L5** | Vorhergesagte Indikationen: **5** 
{: .fs-6 .fw-300 }

---

## Inhaltsverzeichnis
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmazeutischer Bewertungsbericht

</div>

## Dabigatranetexilat: Von venöser Thromboembolie zu sklerosierender Cholangitis
{: .text-alpha }

## Zusammenfassung

Dabigatranetexilat (Pradaxa) ist ein oraler direkter Thrombinhemmer. Er wurde ursprünglich zur Prophylaxe venöser Thromboembolien nach Gelenkersatzoperationen (Arthroplastik) eingesetzt.
Das TxGNN-Modell sagt eine mögliche Wirksamkeit bei **sklerosierender Cholangitis** voraus. Dafür liegen jedoch **keine klinischen Studien** und nur **eine Publikation** ohne Wirksamkeitsdaten vor (eine Arzneimittelinteraktionsstudie zu einem anderen Wirkstoff). Die Vorhersage beruht damit ausschließlich auf dem Modell.

---

## Schnellübersicht

| Punkt | Inhalt |
|------|------|
| Ursprüngliche Indikation | Venöse Thromboembolie; Arthroplastik (Gelenkersatz) |
| Vorhergesagte neue Indikation | Sklerosierende Cholangitis |
| TxGNN-Vorhersagewert | 99,82 % |
| Evidenzstufe | L5 |
| Marktstatus in Deutschland | Nur erloschene/zurückgezogene Zulassungen |
| Anzahl der Zulassungen | 3 (alle erloschen) |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage plausibel?

Zum Wirkmechanismus liegen in den für diesen Bericht zusammengestellten Daten keine detaillierten Angaben vor. Bekannt ist, dass Dabigatran ein direkter Thrombinhemmer ist. Seine Wirksamkeit bei venöser Thromboembolie ist belegt.

Ein möglicher Zusammenhang: Thrombin und die PAR-1-Signalübertragung tragen zu Leberfibrose und Entzündung bei. In einigen präklinischen Lebermodellen verringerte eine Thrombinhemmung die Fibrose. Für die sklerosierende Cholangitis ist dies jedoch spekulativ. Die einzige gefundene Publikation behandelt Wechselwirkungen von Cilofexor (einem FXR-Agonisten) und liefert keine Wirksamkeitsevidenz für Dabigatran. Der hohe Vorhersagewert ist eine rein rechnerische Aussage.

Die übrigen vorhergesagten Indikationen sind noch schwächer begründet:

- **Obsolete familiäre kombinierte Hyperlipidämie** (99,63 %): Kein erkennbarer Mechanismus; der Krankheitsbegriff ist in der Ontologie veraltet, die Vorhersage könnte ein Artefakt sein.
- **Hypoalphalipoproteinämie** (99,57 %): Kein etablierter Zusammenhang; die eine registrierte Phase-1-Studie betrifft offenbar einen anderen Wirkstoff.
- **Homozygote familiäre Hypercholesterinämie** (99,49 %): Die Erkrankung beruht auf Defekten des LDL-Rezeptor-Wegs, den eine Thrombinhemmung nicht beeinflusst.
- **Primäre Plättchen-Freisetzungsstörung** (99,06 %): Es handelt sich um eine Blutungsstörung; ein Antikoagulans würde das Blutungsrisiko eher erhöhen.

---

## Klinische Evidenz

Derzeit sind keine relevanten klinischen Studien für sklerosierende Cholangitis registriert.

---

## Literaturevidenz

| PMID | Jahr | Typ | Journal | Kernaussagen |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Pharmakokinetische Studie (DDI) | Clinical Pharmacokinetics | Bewertung des Potenzials für CYP450- und transportervermittelte Wechselwirkungen von Cilofexor, einem FXR-Agonisten in Entwicklung bei NASH und primär sklerosierender Cholangitis. Kein Bezug zu Dabigatran und keine Wirksamkeitsdaten. |

---

## Marktinformationen Deutschland

Alle drei Zulassungen sind erloschen; es besteht keine gültige Zulassung.

| Zulassungsnummer | Produktname | Darreichungsform | Zugelassene Indikation |
|---------|------|------|-----------|
| EMEA/H/C/000829 | Pradaxa | – | Arthroplastik; venöse Thromboembolie |
| EMEA/H/C/005639 | Dabigatran Etexilate Accord | – | Venöse Thromboembolie; Arthroplastik |
| EMEA/H/C/005922 | Dabigatran etexilate Teva (zuvor Dabigatran etexilate Leon Farma) | – | Venöse Thromboembolie; Arthroplastik |

---

## Sicherheitsaspekte

Für Warnhinweise, Gegenanzeigen und Wechselwirkungen liegen keine Angaben aus der Packungsbeilage vor; die Wechselwirkungsabfrage ergab keine Treffer.

Aus dem TxGNN-Wissensgraphen (keine Fachinformationstexte) sind folgende Erkrankungen als Kontraindikationen verknüpft:

- Blutgerinnungsstörung
- Anämie
- Makrozytäre Anämie
- Intrazerebrale Blutung

Bitte ziehen Sie für verbindliche Sicherheitsinformationen die Fachinformation heran.

---

## Fazit und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die Vorhersage für sklerosierende Cholangitis beruht allein auf dem Modell (Evidenzstufe L5). Es gibt weder klinische Studien noch Wirksamkeitsdaten, und der mechanistische Zusammenhang ist spekulativ. In Deutschland besteht zudem keine gültige Zulassung.

**Für ein Weiterkommen ist Folgendes erforderlich:**
- Präklinische Daten zur Thrombinhemmung/PAR-1-Signalübertragung in Modellen der sklerosierenden Cholangitis
- Detaillierte Wirkmechanismus-Daten (MOA)
- Fachinformation (Warnhinweise, Gegenanzeigen) des BfArM bzw. der EMA zur Sicherheitsbewertung, insbesondere im Hinblick auf das Blutungsrisiko bei Lebererkrankungen
- Klärung des Zulassungs- und Marktstatus in Deutschland
## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

