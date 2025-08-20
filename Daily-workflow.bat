@echo off
SET REPO_PATH=C:\Users\SER5 PRO\bpr-integration
SET LOGS_PATH=%REPO_PATH%\logs

echo ================================
echo BPR Integration Daily Workflow (Advanced)
echo ================================

cd /d "%REPO_PATH%"

:: Pilih langkah
echo Select steps to run:
echo 1. Run demo transactions
echo 2. Run daily maintenance
echo 3. Git commit & push
echo 4. All steps
set /p STEPS=Enter number (1-4): 

:: Jumlah transaksi dummy
if "%STEPS%"=="1" set /p NUMTXN=Enter number of demo transactions: 
if "%STEPS%"=="4" set /p NUMTXN=Enter number of demo transactions: 

:: Step 1: Run demo
if "%STEPS%"=="1" (
    echo Running demo transactions...
    python src\tests\run_demo_full.py %NUMTXN%
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Demo transactions failed
        pause
        exit /b %ERRORLEVEL%
    )
)
if "%STEPS%"=="4" (
    echo Running demo transactions...
    python src\tests\run_demo_full.py %NUMTXN%
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Demo transactions failed
        pause
        exit /b %ERRORLEVEL%
    )
)

:: Step 2: Maintenance
if "%STEPS%"=="2" (
    echo Running daily maintenance...
    python maintenance.py
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Maintenance failed
        pause
        exit /b %ERRORLEVEL%
    )
)
if "%STEPS%"=="4" (
    echo Running daily maintenance...
    python maintenance.py
    if %ERRORLEVEL% NEQ 0 (
        echo ERROR: Maintenance failed
        pause
        exit /b %ERRORLEVEL%
    )
)

:: Step 3: Git commit & push
if "%STEPS%"=="3" (
    echo Adding changes to git...
    git add .
    git commit -m "Daily update: demo transactions & maintenance"
    echo Pushing to GitHub...
    git push
)
if "%STEPS%"=="4" (
    echo Adding changes to git...
    git add .
    git commit -m "Daily update: demo transactions & maintenance"
    echo Pushing to GitHub...
    git push
)

echo.
echo Workflow completed successfully!
pause

