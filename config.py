"""
config.py - postsmolt, MANUELT TIDSSTYRT (bruker-definert oppskrift, 3 kar)
------------------------------------------------------------------------------
Se scheduler_manuell.py sin docstring for hvordan denne varianten skiller seg
fra de to andre (postsmolt_kalender/ og postsmolt_individuell/).

Kort sagt: du definerer selv EN ELLER FLERE "mal-kohorter" i en rotasjon
(f.eks. 3, én per runde i året) - hver med sitt eget smoltantall og sin egen
varighet i tank 1 og vekstkar. Modellen gjentar deretter rotasjonen
automatisk (oppskrift 1, 2, 3, 1, 2, 3, ...). Leveringsvekten beregnes
fortsatt av samme vekstmotor (Skretting SGR/FCR + temperaturprofil + RGI)
som de to andre modellene - det er kun tidspunktene (og smoltantallet) som
er manuelle.
"""

# ----------------------------------------------------------------------
# 1. KAR / LOKALITET
# ----------------------------------------------------------------------
TANK_VOLUME_M3 = 20_500
N_GROWOUT_TANKS = 2
SPLIT_RATIOS = [0.5, 0.5]

# ----------------------------------------------------------------------
# 2. MANUELL OPPSKRIFT-ROTASJON (gjentas automatisk)
# ----------------------------------------------------------------------
START_WEIGHT_KG = 0.10             # smoltvekt ved utsett (100 g default), felles for alle oppskrifter

N_BATCHES_IN_ROTATION = 3          # antall ulike oppskrifter i rotasjonen (1-4)

# Ett tall per oppskrift/batch (indeks 0 = batch 1, osv.) - batch 1 far her
# flere smolt enn batch 2/3 for a kompensere for at den settes ut i en
# kaldere periode av aret.
BATCH_SMOLT_COUNTS = [3_000_000, 1_600_000, 2_000_000]
BATCH_TANK1_GROWTH_WEEKS = [14, 15, 15]   # uker i tank 1 for splitt, per batch
BATCH_GROWOUT_WEEKS = [14, 15, 15]        # uker i vekstkar for salg, per batch

# Vasketid tank 1 - individuell per oppskrift (1-5 uker), slik at du kan
# flekse rotasjonen til a treffe akkurat 52 uker og fa en "recurring" arlig
# produksjonsplan. Med tallene under gir (14+2) + (15+3) + (15+3) = 52 uker
# eksakt - rotasjonen gjentar seg pa de samme kalenderukene hvert ar.
BATCH_TANK1_CLEANING_WEEKS = [2, 3, 3]

# Vasketid vekstkar (tank 2/3) - ogsa individuell per oppskrift, slik at du
# kan dytte produksjon frem/tilbake i tid per oppskrift uten a miste
# fleksibilitet (i stedet for ett felles tall for alle tre).
#
# NB: vekstkarenes vasketid pavirker IKKE full_rotasjon_uker (den styres
# kun av tank 1 sin rytme over) - men den ma likevel henge sammen med
# tank 1-rytmen for a unnga "kollisjon" (at neste kohort ma inn i
# vekstkaret for forrige kohorts vask her rekker a bli ferdig). Med
# tallene over/under er oppskrift 3 sin vekstkar-vask (2 uker) akkurat
# stram nok til a bli ferdig i samme uke som oppskrift 1 sin neste kohort
# ankommer - null kollisjon, null "dod tid" i karet.
BATCH_GROWOUT_CLEANING_WEEKS = [2, 3, 2]

# ----------------------------------------------------------------------
# 3. TETTHET (kun et varselniva - modellen styrer ikke mot dette)
# ----------------------------------------------------------------------
MAX_DENSITY_KG_M3 = 60.0

# ----------------------------------------------------------------------
# 4. DODELIGHET
# ----------------------------------------------------------------------
ANNUAL_MORTALITY_PCT = 0.5

# ----------------------------------------------------------------------
# 5. VEKSTYTELSE / TEMPERATUR
# ----------------------------------------------------------------------
RGI_PCT = 100.0
TEMPERATURE_PROFILES = {
    "Konvensjonell dybde": [
        7.5, 6.2, 5.5, 6.3, 8.5, 12.0, 14.5, 15.0, 15.8, 13.5, 11.0, 9.0,
    ],
    "25 m under overflaten (lukket anlegg)": [
        7.10, 6.10, 5.50, 6.20, 8.50, 9.00, 10.00, 12.00, 12.00, 11.00, 9.00, 8.00,
    ],
}
DEFAULT_TEMPERATURE_PROFILE = "25 m under overflaten (lukket anlegg)"
MONTHLY_TEMPERATURES_C = TEMPERATURE_PROFILES[DEFAULT_TEMPERATURE_PROFILE]

# ----------------------------------------------------------------------
# 6. KALENDER
# ----------------------------------------------------------------------
START_ISO_YEAR = 2026
START_ISO_WEEK = 2
N_YEARS_TO_RUN = 3

# ----------------------------------------------------------------------
# 7. OUTPUT
# ----------------------------------------------------------------------
OUTPUT_DIR = "output"
