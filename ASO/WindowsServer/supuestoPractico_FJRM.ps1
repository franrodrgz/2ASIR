cls
do {

    Clear-Host
    Write-Host "1. Liste los usuarios inactivos del sistema."
    Write-Host "2. Liste las cuentas de usuarios bloqueados."
    Write-Host "3. Muestra las aplicaciones instaladas en nuestra máquina."
    Write-Host "4. Mostrar una barra de progreso antes de mostrar la información de nuestra máquina."
    Write-Host "5. Apagar otra máquina remotamente."
    Write-Host "6. Salir."
    $x = Read-Host "Seleccione una opción..."

if ($x -eq 1)
{
    cls
    Search-ADAccount –AccountInactive –UsersOnly | Where-Object {$_.AccountInactive -eq $true }
}
if ($x -eq 2)
{
    cls
    Get-ADUser -Filter * -Properties LockedOut | Where-Object {$_.LockedOut -eq $true } | Select Name, SamAccountName, LockedOut
}
if ($x -eq 3)
{
    cls
    Get-Package
}
if ($x -eq 4)
{
    cls
    for ($i = 1; $i -le 100; $i++ ) {
    Write-Progress -Activity "Cargando información del equipo" -Status "$i% Complete:" -PercentComplete $i
    Start-Sleep -Milliseconds 25
    }
    Get-ComputerInfo
}
if ($x -eq 5)
{
    $nombre = Read-Host "Introduzca la IP o el nombre del Equipo"
    Stop-Computer -ComputerName $nombre -Confirm
}
if ($x -ne 6)
{
    Read-Host "Pulsa para continuar..."
}
} while ($x -ne 6)﻿
