rem 実行ディレクトリに遷移
cd %~dp0
echo %~dp0
rem ツールを実行
python NormaExporter.py

pause