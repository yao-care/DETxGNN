---
layout: default
title: Insulin Human
parent: Nur Modellvorhersage (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# INSULIN HUMAN: Von Diabetes mellitus bis zur Autoimmun-Oophoritis

## Zusammenfassung in einem Satz

Insulin human ist die Standard-Ersatztherapie für Diabetes mellitus (endogener Insulinmangel).
Die vom TxGNN-Modell als ranghöchste neue Indikation vorhergesagte **Autoimmun-Oophoritis** (Score 99.84 %),
verfügt jedoch über **keine klinischen Studien, keine unterstützende Literatur und keine mechanistische Begründung für therapeutischen Nutzen** –
die Evidenzbewertung selbst kennzeichnet dies als wahrscheinliches Wissensgraph-Komorbiditätsartefakt anstelle eines echten Umwidmungssignals.

---

## Schnellübersicht

| Element | Inhalt |
|---------|--------|
| Ursprüngliche Indikation | Diabetes mellitus (Insulinersatztherapie) – nicht einzeln in diesem Evidenzpaket aufgeführt; Daten zu Deutschland/Zulassungen nicht verfügbar |
| Vorhergesagte neue Indikation | Autoimmun-Oophoritis |
| TxGNN-Vorhersagescore | 99.84 % |
| Evidenzebene | L5 (nur Modellvorhersage, keine unterstützenden Studien) |
| Marktstatus Deutschland | ✗ Nicht im Handel (Nicht im Handel) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | Hold |

---

## Warum ist diese Vorhersage vernünftig?

Derzeit sind detaillierte Daten zum Wirkmechanismus nicht verfügbar (gekennzeichnet als hochschwerwiegender Datenlücke in diesem Evidenzpaket). Nach allgemeinem pharmakologischen Wissen ersetzt oder ergänzt Insulin human das körpereigene Insulin zur Regulierung des Glucosestoffwechsels; seine Wirksamkeit bei Diabetes mellitus ist gut etabliert.

Der vorgeschlagene mechanistische Zusammenhang mit Autoimmun-Oophoritis besteht darin, dass beide Erkrankungen innerhalb eines autoimmunen polyglandulären Syndroms koexistieren können (Typ-1-Diabetes plus autoimmune Ovarialinsuffizienz teilen eine autoimmune Veranlagung). Dies ist jedoch eine **Komorbiditätsassoziation**, nicht ein Beweis dafür, dass Insulin eine direkte therapeutische Wirkung auf die autoimmune Zerstörung des Ovarialgewebes hat. Die Evidenzbewertung kennzeichnet diese Vorhersage explizit als „Relationsrauschen im Wissensgraphen" anstelle einer plausiblen pharmakologischen Hypothese – der Glucosesenkungsmechanismus von Insulin verfügt über keinen etablierten Wirkungsweg, der für die Beendigung oder Umkehrung einer Autoimmun-Oophoritis relevant ist.

Die Überprüfung des vollständigen Satzes von 10 TxGNN-Vorhersagen für dieses Arzneimittel bestärkt diese Schlussfolgerung: Die meisten (Ränge 1, 2, 3, 5, 6, 7, 8, 10) werden von der Evidenzschicht explizit als Komorbiditätsartefakte oder sogar **richtungsumgekehrte Assoziationen** gekennzeichnet (z. B. ist Insulininjektion eine bekannte *Ursache* lokalisierter Lipodystrophie, nicht eine Behandlung dafür). Die zwei Ausnahmen – Thiamin-responsives Dysfunktionssyndrom (Rang 4) und Bauchspeicheldrüsenagenese (Rang 9) – spiegeln die gut etablierte Rolle von Insulin bei der Behandlung von *sekundärem Diabetes* wider, der aus diesen genetischen Syndromen entsteht, was bereits bestehende klinische Standardpraxis ist anstelle einer neuartigen Umwidmungsentdeckung.

---

## Klinische Studienevidenz

Derzeit sind keine damit verbundenen klinischen Studien registriert.

---

## Literaturevidenz

Derzeit ist keine damit verbundene Literatur verfügbar.

---

## Informationen zum deutschen Markt

In diesem Evidenzpaket sind keine Zulassungsunterlagen verfügbar. Der Marktstatus wird als **Nicht im Handel (Nicht im Handel)** mit **0 Gesamtlizenzen** aufgezeichnet, daher kann keine Tabelle mit Produkten/Darreichungsformen erstellt werden.

---

## Sicherheitsüberlegungen

Bitte beachten Sie die Packungsbeilage für Sicherheitsinformationen. (Wichtige Warnungen, Kontraindikationen und Arzneimittelwechselwirkungsdaten sind alle in diesem Evidenzpaket nicht verfügbar; TFDA-Etikettenwarnungen/Kontraindikationen sind als **blockierende** Datenlücke gekennzeichnet, die eine formale S1-Sicherheitsbewertung verhindert.)

---

## Schlussfolgerung und nächste Schritte

**Entscheidung: Hold**

**Begründung:**
Die ranghöchste Vorhersage (Autoimmun-Oophoritis) verfügt über keine klinische, literaturgestützte oder mechanistische Unterstützung und wird von der Evidenzbewertung explizit als wahrscheinliches Wissensgraph-Artefakt identifiziert, das durch gemeinsame autoimmune Komorbiditäten angetrieben wird, anstelle eines echten pharmakologischen Signals. In Kombination mit einer blockierenden Datenlücke in der TFDA-Sicherheitskennzeichnung und einer hochschwerwiegenden Datenlücke in den Wirkmechanismus-Daten gibt es keine ausreichende Grundlage, um diesen Kandidaten voranzubringen.

**Um fortzufahren, ist Folgendes erforderlich:**
- TFDA/EMA-Packungsbeilagendaten (Warnungen, Kontraindikationen) zur Beseitigung der blockierenden Datenlücke und zur Ermöglichung der S1-Sicherheitsprüfung
- Bestätigte Wirkmechanismus-Dokumentation für Insulin human (DrugBank-API-Abfrage)
- Falls Autoimmun-Oophoritis weiterhin verfolgt wird: Dedizierte mechanistische oder präklinische Studien, die Insulin/Insulin-Signalgebungswege im autoimmunen Ovarialgewebe evaluieren – derzeit existieren keine
- Neubewertung, ob die Ränge 4 (Thiamin-responsives Dysfunktionssyndrom) und 9 (Bauchspeicheldrüsenagenese) stattdessen als „bestehende klinische Standardpraxis" anstelle von neuartigen Umwidmungskandidaten neu klassifiziert werden sollten, da Insulin bereits klinisch für sekundären Diabetes in beiden Syndromen verwendet wird

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

