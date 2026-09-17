@echo off
setlocal enabledelayedexpansion
REM Creates a venv in the current folder and installs requirements.txt.
REM Usage 1) If requirements.txt already exists here:  ..\..\scripts\setup.bat
REM Usage 2) Pass template names directly (no need to remember them - see menu below):
REM          ..\..\scripts\setup.bat jupyter langchain
REM          ..\..\scripts\setup.bat jupyter rag
REM Usage 3) Run with no arguments and pick from a numbered menu instead.
REM          Works even if requirements.txt already exists - selected templates
REM          are installed on top of what's already there, then re-frozen.

set SCRIPT_DIR=%~dp0
set REQ_DIR_WIN=%SCRIPT_DIR%requirements
set REQ_DIR=%REQ_DIR_WIN%
REM pip's requirements-file parser mangles backslashes in -r paths, so use forward slashes
set REQ_DIR=%REQ_DIR:\=/%
set TEMPLATE_ARGS=%*

echo ==================================
echo      Environment Setup
echo ==================================
echo Target folder: %cd%

REM 0a. If no templates were given on the command line, offer a numbered menu
REM     so you don't have to remember template names.
if "%TEMPLATE_ARGS%"=="" (
    echo.
    echo Available templates:
    set /a IDX=0
    for %%F in ("%REQ_DIR_WIN%\*.txt") do (
        set /a IDX+=1
        set "TPL_!IDX!=%%~nF"
        echo   !IDX!. %%~nF
    )
    echo.
    set /p TPL_CHOICE=Select template numbers, comma-separated e.g. 1,3 - press Enter to skip:
    if not "!TPL_CHOICE!"=="" (
        set "TPL_CHOICE=!TPL_CHOICE:,= !"
        for %%N in (!TPL_CHOICE!) do (
            call set TEMPLATE_ARGS=%%TEMPLATE_ARGS%% %%TPL_%%N%%
        )
    )
)

REM 0b. Copy .env template if missing
if not exist ".env" (
    if exist "%SCRIPT_DIR%.env.example" (
        copy "%SCRIPT_DIR%.env.example" ".env" >nul
        echo .env template copied
    )
)

REM 0c. Copy a starter notebook matching the requested templates, if this folder has none yet
set HAS_NOTEBOOK=
for %%F in (*.ipynb) do set HAS_NOTEBOOK=1

if not "!TEMPLATE_ARGS!"=="" if not defined HAS_NOTEBOOK (
    set STARTER_NB=
    echo !TEMPLATE_ARGS! | findstr /i "langchain rag" >nul
    if !errorlevel! equ 0 set STARTER_NB=langchain_starter.ipynb
    if defined STARTER_NB (
        copy "%SCRIPT_DIR%templates\!STARTER_NB!" ".\!STARTER_NB!" >nul
        echo Starter notebook copied: !STARTER_NB!
    )
)

REM 0d. Copy the LangChain import cheatsheet matching the requested templates, if missing here
if not "!TEMPLATE_ARGS!"=="" if not exist "langchain_import_cheatsheet.md" (
    echo !TEMPLATE_ARGS! | findstr /i "langchain rag" >nul
    if !errorlevel! equ 0 (
        copy "%SCRIPT_DIR%templates\langchain_import_cheatsheet.md" ".\langchain_import_cheatsheet.md" >nul
        echo Import cheatsheet copied: langchain_import_cheatsheet.md
    )
)

REM 1. Create venv if missing
if not exist ".venv" (
    echo.
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 goto :error
) else (
    echo.
    echo Virtual environment already exists, skipping creation.
)

REM 2. Activate venv
call .venv\Scripts\activate.bat
if errorlevel 1 goto :error

REM 3. Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 goto :error

REM 4. If templates were given (via args or the menu above), install them on top
REM    of whatever's already in the venv, then freeze the full result into
REM    requirements.txt (so it stays a real, reproducible record).
if not "!TEMPLATE_ARGS!"=="" (
    echo.
    echo Installing from templates: !TEMPLATE_ARGS!
    > requirements.in (
        for %%T in (!TEMPLATE_ARGS!) do (
            echo -r %REQ_DIR%/%%T.txt
        )
    )
    pip install -r requirements.in
    if errorlevel 1 goto :error
    del requirements.in

    echo.
    echo Freezing installed versions into requirements.txt...
    pip freeze > requirements.txt
    goto :done
)

REM 5. No templates selected - just install whatever requirements.txt already has
if exist "requirements.txt" (
    echo.
    echo Installing libraries from requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 goto :error
    goto :done
)

echo.
echo [WARN] No requirements.txt and no template selected, skipping install.
echo Usage: setup.bat [template1] [template2] ...   e.g. setup.bat langchain rag
echo    or run with no arguments to pick from a menu.

:done
echo.
echo ==================================
echo     Setup complete!
echo ==================================
goto :eof

:error
echo.
echo [ERROR] Something went wrong during setup.
exit /b 1
