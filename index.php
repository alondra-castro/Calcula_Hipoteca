<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de Hipoteca</title>
</head>
<body>
    <h1>Calculadora de Hipoteca</h1>
    <form method="POST" action="resultado.php">
        <label for="valor_propiedad">Valor de la Propiedad:</label>
        <input type="number" name="valor_propiedad" required><br><br>

        <label for="tasa_interes">Tasa de Interés Anual (%):</label>
        <input type="number" name="tasa_interes" required><br><br>

        <label for="anos_financiamiento">Años de Financiamiento:</label>
        <input type="number" name="anos_financiamiento" required><br><br>

        <label for="abono_inicial">Abono Inicial:</label>
        <input type="number" name="abono_inicial" required><br><br>

        <input type="submit" value="Calcular">
    </form>
</body>
</html>
