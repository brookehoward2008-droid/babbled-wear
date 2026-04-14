@echo off
setlocal
cd /d "%~dp0"

echo.
echo ============================================
echo   baBBled wear — publish site
echo ============================================
echo.
echo   1) Personal  (brookehoward2008/babbled-wear)
echo      -- https://brookehoward2008.github.io/babbled-wear/
echo.
echo   2) Business  (babbledllc/babbledllc.github.io)
echo      -- https://babbledllc.github.io/
echo.
echo   3) BOTH
echo.
echo   0) Cancel
echo.

set /p CHOICE="Pick [1/2/3/0]: "

if "%CHOICE%"=="0" goto :end
if "%CHOICE%"=="1" goto :personal
if "%CHOICE%"=="2" goto :business
if "%CHOICE%"=="3" goto :both
echo Invalid choice.
goto :end

:personal
echo.
echo Staging + committing any changes...
git add -A
git diff --cached --quiet || git commit -m "update site"
echo Pushing to PERSONAL...
git push -u personal main
goto :end

:business
echo.
echo Staging + committing any changes...
git add -A
git diff --cached --quiet || git commit -m "update site"
echo Pushing to BUSINESS...
git push -u business main
goto :end

:both
echo.
echo Staging + committing any changes...
git add -A
git diff --cached --quiet || git commit -m "update site"
echo Pushing to PERSONAL...
git push -u personal main
echo Pushing to BUSINESS...
git push -u business main
goto :end

:end
echo.
pause
endlocal
