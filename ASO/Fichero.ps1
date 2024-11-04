cls
do {
    Clear-Host
    Write-Host "1. Muestra los usuarios del sistema"
    Write-Host "2. Dar de alta a un usuario"
    Write-Host "3. Mostrar los procesos que se esta ejecutando"
    Write-Host "4. Dar de baja a un usuario"
    Write-Host "5. Muestra el historial del sistema"
    Write-Host "6. Muestra la información del sistema"
    Write-Host "7. Salir"
    $x=Read-Host "Selecciona una opción"

if ($x -eq 1)
{
    cls
    Get-LocalUser|ft
}
if ($x -eq 2)
{
    cls
    $nombrecreate=Read-Host "Introduzca un nombre de usuario: "
    $contra=Read-Host "Introduzca una contraseña para el usuario: " -AsSecureString
    New-LocalUser $nombrecreate -Password $contra
}
if ($x -eq 3)
{
    cls
    Get-Process
}
if ($x -eq 4)
{
    cls
    $nombredelete=Read-Host "Introduzca un nombre de usuario para eliminar: "
    Remove-LocalUser $nombredelete -Confirm
}
if ($x -eq 5)
{
    cls
    Get-History
}
if ($x -eq 6)
{
    cls
    Get-ComputerInfo > pc_info.txt
}
if ($x -ne 7)
{
    Read-Host "Pulse para continuar"
}
} while ($x -ne 7)