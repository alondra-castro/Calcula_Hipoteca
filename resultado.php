<!DOCTYPE html>
<html>
<head>
    <title>Resultado de la Hipoteca</title>
</head>
<body>
    <h1>Resultado de la Hipoteca</h1>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $valor_propiedad = $_POST["valor_propiedad"];
        $tasa_interes = $_POST["tasa_interes"] / 100; // Convertir a decimal
        $anos_financiamiento = $_POST["anos_financiamiento"];
        $abono_inicial = $_POST["abono_inicial"];

        // Calcular el monto del préstamo
        $monto_prestamo = $valor_propiedad - $abono_inicial;

        // Calcular la tasa de interés mensual
        $tasa_interes_mensual = $tasa_interes / 12;

        // Calcular el número de cuotas mensuales
        $numero_cuotas = $anos_financiamiento * 12;

        // Calcular la cuota mensual
        $cuota_mensual = $monto_prestamo * ($tasa_interes_mensual * pow(1 + $tasa_interes_mensual, $numero_cuotas)) / (pow(1 + $tasa_interes_mensual, $numero_cuotas) - 1);

        $mes = 1;
        $saldo_pendiente = $monto_prestamo;

        echo "<h2>Amortización:</h2>";
        echo "<table>";
        echo "<tr><th>Mes</th><th>Cuota</th><th>Interés</th><th>Principal</th><th>Saldo Pendiente</th></tr>";

        while ($saldo_pendiente > 0) {
            $interes_mensual = $saldo_pendiente * $tasa_interes_mensual;
            $principal_mensual = $cuota_mensual - $interes_mensual;
            $saldo_pendiente -= $principal_mensual;

            echo "<tr><td>$mes</td><td>$cuota_mensual</td><td>$interes_mensual</td><td>$principal_mensual</td><td>$saldo_pendiente</td></tr>";

            $mes++;

            if ($mes > 300) {
                // Evitar bucles infinitos, establecer un límite máximo de 300 meses
                break;
            }
        }

        echo "</table>";
    }
    ?>

</body>
</html>
