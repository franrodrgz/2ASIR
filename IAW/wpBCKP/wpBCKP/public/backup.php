<?php
session_start();
include("../config/config.php");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $db_user = escapeshellarg($_POST["db_user"]);
    $db_pass = escapeshellarg($_POST["db_pass"]);
    $db_name = escapeshellarg($_POST["db_name"]);

    $timestamp = date("Ymd_His");
    $backup_file = BACKUP_PATH . "/wpBCK_$timestamp.zip";
    $sql_file = BACKUP_PATH . "/wordpress_backup_$timestamp.sql";

    // 1. Realizar la copia de seguridad de la base de datos con mysqldump
    $dump_command = "mysqldump -u$db_user -p$db_pass $db_name > $sql_file";
    exec($dump_command, $output, $return_var);

    if ($return_var !== 0) {
        $_SESSION["error"] = "Error al generar la copia de seguridad de la base de datos.";
        header("Location: index.php");
        exit();
    }

    // 2. Comprimir los archivos y la base de datos en un ZIP
    $zip = new ZipArchive();
    if ($zip->open($backup_file, ZipArchive::CREATE) === TRUE) {
        // Agregar la base de datos al ZIP
        $zip->addFile($sql_file, basename($sql_file));

        // Agregar todos los archivos de WordPress
        $files = new RecursiveIteratorIterator(
            new RecursiveDirectoryIterator(WP_PATH, RecursiveDirectoryIterator::SKIP_DOTS),
            RecursiveIteratorIterator::LEAVES_ONLY
        );

        foreach ($files as $file) {
            $filePath = $file->getRealPath();
            $relativePath = substr($filePath, strlen(WP_PATH) + 1);
            $zip->addFile($filePath, "wordpress_files/$relativePath");
        }

        $zip->close();

        // Eliminar el archivo SQL temporal
        unlink($sql_file);

        // Ofrecer el archivo ZIP para descarga
        header("Content-Type: application/zip");
        header("Content-Disposition: attachment; filename=" . basename($backup_file));
        header("Content-Length: " . filesize($backup_file));
        readfile($backup_file);

        // Eliminar el archivo ZIP tras la descarga
        unlink($backup_file);
        exit();
    } else {
        $_SESSION["error"] = "Error al crear el archivo ZIP.";
        header("Location: index.php");
        exit();
    }
}
?>
