@echo off

python ./src/lazyspaces.py

if %errorlevel% neq 0 (
    pause
)
