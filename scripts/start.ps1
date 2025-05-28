Write-Host "Starting backend..."
Set-Location -Path "app/backend"
.\venv\Scripts\Activate.ps1
Start-Process -FilePath "uvicorn" -ArgumentList "main:app --host 0.0.0.0 --port 8000"
Write-Host "Starting frontend..."
Set-Location -Path "../frontend"
Start-Process -FilePath "npm" -ArgumentList "start"