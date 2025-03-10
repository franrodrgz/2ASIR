<?php session_start(); ?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurar Backup</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <h3 class="text-center">Restaurar Backup de WordPress</h3>
                <?php if(isset($_SESSION['error'])): ?>
                    <div class="alert alert-danger"><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></div>
                <?php endif; ?>
                <?php if(isset($_SESSION['success'])): ?>
                    <div class="alert alert-success"><?php echo $_SESSION['success']; unset($_SESSION['success']); ?></div>
                <?php endif; ?>
                <form action="restore_backup.php" method="POST" enctype="multipart/form-data">
                    <div class="mb-3">
                        <label class="form-label">Archivo ZIP del Backup</label>
                        <input type="file" class="form-control" name="backup_zip" accept=".zip" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Usuario MySQL</label>
                        <input type="text" class="form-control" name="db_user" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Contraseña MySQL</label>
                        <input type="password" class="form-control" name="db_pass" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Nombre de la Base de Datos</label>
                        <input type="text" class="form-control" name="db_name" required>
                    </div>
                    <button type="submit" class="btn btn-primary w-100">Subir y Restaurar</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
