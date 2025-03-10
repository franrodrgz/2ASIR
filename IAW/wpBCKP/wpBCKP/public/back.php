<?php session_start(); ?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Backup WordPress</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <h3 class="text-center">Generar Backup de WordPress</h3>
                <?php if(isset($_SESSION['error'])): ?>
                    <div class="alert alert-danger"><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></div>
                <?php endif; ?>
                <form action="backup.php" method="POST">
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
                    <button type="submit" class="btn btn-primary w-100">Generar Backup</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
