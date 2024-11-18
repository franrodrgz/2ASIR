cls
do {

    Clear-Host
    Write-Host "1. Listado de puertos UDP abiertos." 
    Write-Host "2. Deshabilitar elementos del adaptador de red."
    Write-Host "3. Ver los bytes enviados y recibidos por la interfaz Ethernet."
    Write-Host "4. Obtener dirección IP del adaptador Ethernet."
    Write-Host "5. Ver la tabla de enrutamiento de IPv4."
    Write-Host "6. Realizar un apagado programado de otra máquina."
    Write-Host "7. Crear una barra de progreso."
    Write-Host "8. Salir."
    $x=Read-Host "Selecciona una opción"

if ($x -eq 1)
{
    cls
    Get-NetUDPEndpoint
}
if ($x -eq 2)
{
    cls
    Get-NetAdapter
    $nombreA=Read-Host "Introduce que adaptador quieres usar: "
    Get-NetAdapterBinding -Name $nombreA
    $nombreD=Read-Host "Que elementos quieres deshabilitar: "
    Disable-NetAdapterBinding -Name $nombreA -ComponentID $nombreD
    Write-Host "Hecho!"
}
if ($x -eq 3)
{
    cls
    Get-NetAdapterStatistics -Name "Ethernet"
}
if ($x -eq 4)
{
    cls
    Get-NetIPAddress -InterfaceAlias "Ethernet" | Where-Object {$_.AddressFamily -eq "IPv4"} | Select-Object IPAddress
}
if ($x -eq 5)
{
    cls
    Get-NetRoute -AddressFamily IPv4
}
if ($x -eq 6)
{
    cls
    $nombrePC=Read-Host "Introduce el nombre del ordenador al que quieres realizarle un apagado: "
    Stop-Computer -ComputerName $nombrePC -Credential (Get-Credential) -Force -Timeout 60
}
if ($x -eq 7)
{
    cls
    $progress = 0
    $totalSteps = 100

    # Bucle While que simula el progreso
    while ($progress -le $totalSteps) {
        # Mostrar la barra de progreso
        Write-Progress -Activity "Procesando..." `
                   -Status "Progreso: $progress%" `
                   -PercentComplete $progress

        # Incrementar el progreso
        $progress += 1

    # Pausa para simular trabajo (0.1 segundos)
    Start-Sleep -Milliseconds 100
}
}
if ($x -ne 8)
{
    Read-Host "Pulsa para continuar..."
}
} while ($x -ne 8)
