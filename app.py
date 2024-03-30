from flask import Flask, render_template, request
from calculadora_hipoteca import calcular_historial_de_pagos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular_hipoteca():
    if request.method == 'POST':
        valor_propiedad = float(request.form['valor_propiedad'])
        tasa_interes = float(request.form['tasa_interes'])
        anos_financiamiento = int(request.form['anos_financiamiento'])
        abono_inicial = float(request.form['abono_inicial'])
        nuevo = request.form.get('nuevo') == 'on'

        historial_pagos = calcular_historial_de_pagos(valor_propiedad, tasa_interes, anos_financiamiento, abono_inicial, nuevo)

        return render_template('resultado.html', cuota_mensual=historial_pagos[0][1], historial_pagos=historial_pagos)

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
