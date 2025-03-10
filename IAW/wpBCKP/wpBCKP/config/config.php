<?php
define('WP_PATH', '/var/www/web/wordpress'); // Ruta de WordPress
define('BACKUP_PATH', __DIR__ . '/../backups'); // Carpeta donde se guardan los backups

if (!file_exists(BACKUP_PATH)) {
    mkdir(BACKUP_PATH, 0777, true);
}
?>
