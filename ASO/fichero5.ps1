cls
do {

    Clear-Host 
    Write-Host "1. Muestre por pantalla los procesos del sistema."
    Write-Host "2. Pida por pantalla el nombre de un proceso y  Detenerlo. Realiza una espera hasta que se haya detenido por completo el proceso anterior."
    Write-Host "3. Pedir el nombre de un procesos y espera durante unos segundos (pedidos por pantalla) que se detenga el proceso indicado."
    Write-Host "4. Inicia el Notepad.exe proceso. Maximiza la ventana y la conserva hasta que se finalice el proceso."
    Write-Host "5. Inicia PowerShell mediante la opción Ejecutar como administrador"
    Write-Host "6 Salir"
    $x = Read-Host "Selecciona una opción"

if ($x -eq 1)
{
    cls
    Get-Process | Format-Table
}
if ($x -eq 2)
{
    cls
    $nombreProceso = Read-Host "Ingrese el nombre del proceso que desea detener"
    $procesos = Get-Process -Name $nombreProceso -ErrorAction SilentlyContinue

    if ($procesos) {
    foreach ($proceso in $procesos) {
        try {
            Write-Host "Deteniendo el proceso $($proceso.Name) (PID: $($proceso.Id))..." -ForegroundColor Yellow
            Stop-Process -Id $proceso.Id -Force
            
            while (Get-Process -Id $proceso.Id -ErrorAction SilentlyContinue) {
                Start-Sleep -Seconds 1
            }
            
            Write-Host "El proceso $($proceso.Name) ha sido detenido completamente." -ForegroundColor Green
        } catch {
            Write-Host "No se pudo detener el proceso $nombreProceso. Error: $_" -ForegroundColor Red
        }
    }
} else {
    Write-Host "No se encontró ningún proceso con el nombre $nombreProceso." -ForegroundColor Red
}
}
if ($x -eq 3)
{
    cls
    $nombreProceso2 = Read-Host "Ingrese el nombre del proceso que desea monitorear (ejemplo: notepad.exe)"
    $tiempoEspera = Read-Host "Ingrese el tiempo de espera (en segundos) para verificar si el proceso se detiene"
    $tiempoEspera = [int]$tiempoEspera

    $inicio = Get-Date
    Write-Host "Monitoreando el proceso $nombreProceso2 durante $tiempoEspera segundos..." -ForegroundColor Yellow

    while ((Get-Date) -lt $inicio.AddSeconds($tiempoEspera)) {
        $proceso = Get-Process -Name $nombreProceso2 -ErrorAction SilentlyContinue
            if (-not $proceso) {
                Write-Host "El proceso $nombreProceso2 se ha detenido." -ForegroundColor Green
    break
    }
    Start-Sleep -Seconds 1
}

if ($proceso) {
    Write-Host "El proceso $nombreProceso2 aún está en ejecución después de $tiempoEspera segundos." -ForegroundColor Red
}

}
if ($x -eq 4)
{
    cls
    $proceso = Start-Process -FilePath "notepad.exe" -PassThru -WindowStyle Maximized
}
if ($x -eq 5)
{
    cls
    Start-Process -FilePath "powershell.exe" 
}
if ($x -ne 6)
{
    Read-Host "Pulse para continuar..."
}
} while ($x -ne 6)
