@echo off
REM start.bat - starter Hexacage postsmolt-modellen (3x runder/aar) i denne mappen.
REM Dobbeltklikk denne filen i Utforsker for a starte appen direkte.

REM Ga alltid til mappen denne filen selv ligger i, uansett hvor den startes fra.
cd /d "%~dp0"

echo Starter postsmolt_manuell (3x runder/aar) paa http://localhost:8501 ...
echo Lukk dette vinduet, eller trykk Ctrl+C, for a stoppe appen.

python -m streamlit run streamlit_app.py --server.port 8501

echo.
echo Appen er stoppet.
pause
