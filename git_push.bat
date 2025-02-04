@echo off

:: Check if commit message is provided
if "%~1" == "" (
    echo Error: No commit message provided.
    exit /b 1
)

:: Display commit message
echo Commit message is: "%~1"
set commit_message=%~1

:: Check if branch name is provided
if "%~2" == "" (
    echo Error: No branch provided.
    exit /b 1
)

:: Display branch name
echo Branch name is: "%~2"
set branch_name=%~2


git add .

git commit -m "%commit_message%"
git push ogigin %branch_name%

echo Changes have been added, committed, and pushed to branch %BRANCH_NAME% successfully.
pause
