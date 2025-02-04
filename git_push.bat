@echo off

:: Check if commit message and branch name are provided
if "%~1"=="" (
    echo Error: Commit message is required.
    exit /b 1
)

if "%~2"=="" (
    echo Error: Branch name is required.
    exit /b 1
)

:: Assign parameters to variables
set COMMIT_MESSAGE=%~1
set BRANCH_NAME=%~2

:: Add all changes to git
git add .

:: Commit with the provided message
git commit -m "%COMMIT_MESSAGE%"

:: Push changes to the provided branch
git push origin %BRANCH_NAME%

echo Changes have been added, committed, and pushed to branch %BRANCH_NAME% successfully.
pause