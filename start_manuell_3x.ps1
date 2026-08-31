# start.ps1 - starter Hexacage postsmolt-modellen (3x runder/aar) i denne mappen.
# Kjor ved a hoyreklikke denne filen i VS Code / Utforsker og velge
# "Run with PowerShell" (eller "Kjor med PowerShell").

# Ga alltid til mappen denne filen selv ligger i, uansett hvor du kjorer den fra.
Set-Location -Path $PSScriptRoot

Write-Host "Starter postsmolt_manuell (3x runder/aar) paa http://localhost:8501 ..." -ForegroundColor Cyan
Write-Host "Lukk dette vinduet, eller trykk Ctrl+C, for a stoppe appen." -ForegroundColor DarkGray

python -m streamlit run streamlit_app.py --server.port 8501

Read-Host "Appen er stoppet. Trykk Enter for a lukke dette vinduet"
