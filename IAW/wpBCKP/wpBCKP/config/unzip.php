<?php
session_start();
include("../config/config.php");

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["backup_zip"])) {
    $zipFile = $_FILES["backup_zip"];
    $uploadPath = BACKUP_PATH . "/" . basename($zipFile["name"]);

    if (move_uploaded_file($zipFile["tmp_name"], $uploadPath)) {
        $zip = new ZipArchive();
        if ($zip->open($uploadPath) === TRUE) {
            $zip->extractTo(WP_PATH);
            $zip->close();
            unlink($uploadPath);

            // Restaurar la base de datos si hay un archivo SQL
            $sqlFile = WP_PATH . "/wordpress_backup.sql";
            if (file_exists($sqlFile)) {
                $db_user = escapeshellarg($_POST["db_user"]);
                $db_pass = escapeshellarg($_POST["db_pass"]);
                $db_name = escapeshellarg($_POST["db_name"]);
                $restore_command = "mysql -u$db_user -p$db_pass $db_name < $sqlFile";
                exec($restore_command, $output, $return_var);
                unlink($sqlFile);

                if ($return_var === 0) {
                    $_SESSION["success"] = "Backup restaurado correctamente.";
                } else {
                    $_SESSION["error"] = "Error al restaurar la base de datos.";
                }
            }
        } else {
            $_SESSION["error"] = "Error al abrir el archivo ZIP.";
        }
    } else {
        $_SESSION["error"] = "Error al subir el archivo ZIP.";
    }

    header("Location: index.php");
    exit();
}
?>
