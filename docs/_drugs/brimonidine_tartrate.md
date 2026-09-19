---
layout: default
title: Brimonidine Tartrate
parent: Nur Modellvorhersage (L5)
nav_order: 66
evidence_level: L5
indication_count: 0
---

# Brimonidine Tartrate
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

# Brimonidine Tartrate: Repurposing-Bewertung — TxGNN-Vorhersagedaten nicht verfügbar

## Zusammenfassung in einem Satz

Brimonidine Tartrate ist ein Alpha-2-adrenerger Agonist, der klinisch zur Senkung des Augeninnendrucks bei Glaukom und okularer Hypertension etabliert ist. Das aktuelle Evidence Pack enthält **keine durch TxGNN vorhergesagten neuen Indikationen**, und kritische Datenfelder — einschließlich MOA-Detail, Sicherheitswarnungen und Kontraindikationen — fehlen. Eine vollständige Repurposing-Bewertung **kann zu diesem Zeitpunkt nicht abgeschlossen werden**; der folgende Bericht dokumentiert die abgerufenen Daten und bildet die verbleibenden Lücken ab.

---

## Überblick

| Punkt | Inhalt |
|------|---------|
| Ursprüngliche Indikation | Glaukom / Okulare Hypertension (etablierte pharmakologische Klasse; nicht in diesem Evidence Pack erfasst) |
| Vorhergesagte neue Indikation | Nicht verfügbar — TxGNN-Vorhersageliste ist leer |
| TxGNN-Vorhersageergebnis | Nicht verfügbar |
| Evidence Level | L5 — Modellvorhersage nicht vorhanden; keine unterstützenden Studien identifiziert |
| Taiwan-Marktstatus | Nicht vermarktet (0 Zulassungen) |
| Anzahl der Zulassungen | 0 |
| Empfohlene Entscheidung | **Halten** |

---

## Warum diese Vorhersage noch nicht bewertet werden kann

Brimonidine Tartrate gehört zur Klasse der Alpha-2-adrenergen Agonisten. Sein primärer Mechanismus — selektive Stimulation von präsynaptischen und postsynaptischen α₂-Rezeptoren — reduziert die Produktion von Kammerwasser und erhöht den uveoskleralen Abfluss, wodurch der Augeninnendruck gesenkt wird. Sekundärmechanismen, die für die Neupositionierung relevant sind (Neuroprotection durch Bcl-2-Hochregulation, entzündungshemmende Aktivität, Vasokonstriktion für dermatologische Anwendungen wie Rosacea), sind in der Literatur dokumentiert, fehlen aber im `original_moa`-Feld dieses Evidence Packs.

Ohne ein aus TxGNN mit Daten gefülltes `predicted_indications`-Array ist es nicht möglich, die mechanistische Plausibilität für eine neue Indikation zu bewerten, noch können unterstützende Studien oder Publikationen ausgewählt werden. Die Pipeline scheint einen DrugBank-Datensatz abgerufen zu haben (query_log ID 3, status: success) und einen TFDA-Packungsbeilage (query_log ID 4, status: success), aber keiner lieferte strukturierte Daten in die Evidence Pack-Felder. Dies deutet auf einen nachgelagerten Parsing- oder Mapping-Fehler hin, nicht auf ein echtes Fehlen von Arzneimittelinformationen.

---

## Evidenz aus klinischen Studien

Derzeit ist keine durch TxGNN vorhergesagte Indikation verfügbar, um eine Studiensuche abzugrenzen. Es können keine Evidenzen aus klinischen Studien präsentiert werden.

---

## Literaturgestützte Evidenz

Derzeit ist keine durch TxGNN vorhergesagte Indikation verfügbar, um eine Literatursuche abzugrenzen. Es können keine Publikationsevidenzen präsentiert werden.

---

## Taiwan-Marktinformationen

Brimonidine Tartrate hat **null TFDA-Zulassungen**. Das Arzneimittel ist **nicht auf dem Taiwan-Markt zugelassen**. Es kann keine Lizenztabelle generiert werden.

> Anmerkung: Brimonidine wird unter Handelsnamen wie Alphagan® und Mirvaso® in den USA, der EU und mehreren asiatischen Märkten vermarktet. Die TFDA-Abfrage ergab 0 Ergebnisse (query_log ID 1), was einen formulierungsspezifischen oder Handelsname-Fehler widerspiegeln kann, anstelle einer globalen Nicht-Zulassung. Eine Überprüfung mit alternativen Schreibweisen (z. B. "Brimonidine", "酒石酸溴莫尼定") wird empfohlen.

---

## Sicherheitsaspekte

Alle Sicherheitsfelder in diesem Evidence Pack fehlen:

- Wichtige Warnungen: nicht abgerufen
- Kontraindikationen: nicht abgerufen
- Arzneimittel-Wechselwirkungen: Abfrage ergab keine Ergebnisse (query_log ID 2, status: not_found)

Bitte konsultieren Sie den Packungsbeilage (erfolgreich abgerufen gemäß query_log ID 4) und den DrugBank-Datensatz (query_log ID 3) für Warnungen, Kontraindikationen und Wechselwirkungen. Diese Quellen müssen geparst und erneut aufgenommen werden, bevor eine Sicherheitsbewertung fortgesetzt werden kann.

Bekannte Klasse-Vorsichtsmaßnahmen für Alpha-2-Agonisten umfassen: kardiovaskuläre Depression, ZNS-Sedation, Rebound-Hypertonie bei abruptem Absetzen und Risiko schwerer Hypotonie in Kombination mit Antihypertensiva oder ZNS-Depressiva.

---

## Fazit und nächste Schritte

**Entscheidung: Halten**

**Begründung:**
Das Evidence Pack ist strukturell unvollständig — TxGNN-Vorhersagen fehlen und zwei blockierende Datenlücken (DG001: Sicherheit/Warnungen, DG002: MOA) bleiben ungelöst. Keine Repurposing-Hypothese kann bewertet werden, und keine Sicherheitsprüfung kann eingeleitet werden, bis diese gelöst sind.

**Für die Fortsetzung ist Folgendes erforderlich:**

1. **Erneutes Durchführen der TxGNN-Inferenz** für Brimonidine Tartrate und Befüllung von `predicted_indications` — Bestätigung, dass die DrugBank-Entitäts-ID korrekt zugeordnet ist (das DrugBank ID-Feld ist derzeit null).
2. **Parsing des TFDA-Packungsbeilagenblatts** (bereits abgerufen, query_log ID 4), um strukturierte Warnungen und Kontraindikationen in `safety.key_warnings` und `safety.contraindications` zu extrahieren.
3. **Parsing des DrugBank-Datensatzes** (bereits abgerufen, query_log ID 3), um `original_moa`, Kategorien und Toxizitätsdaten zu extrahieren.
4. **TFDA-Suchabdeckung überprüfen** — erneute Abfrage mit vereinfachtem Arzneimittelnamen ("Brimonidine") und chinesischer INN ("溴莫尼定"), um Null-Ergebnis-Artefakte auszuschließen.
5. **DDI-Abfrage erneut durchführen**, sobald die DrugBank ID bestätigt ist, da der aktuelle not_found-Status möglicherweise auf einen fehlenden Identifier zurückzuführen ist.
6. Nachdem die obigen Punkte gelöst sind, das Evidence Pack neu generieren und zur vollständigen Bewertung erneut einreichen.

## Haftungsausschluss

Diese Inhalte dienen ausschließlich Forschungszwecken und stellen keine medizinische Beratung dar.
Vor jeder klinischen Anwendung ist eine klinische Validierung erforderlich.

---

