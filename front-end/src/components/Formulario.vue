<template>
  <html lang="es">
    <head>
      <title>CovControl Formulario</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    </head>

    <body>
      <div class="content">

        <h3>Formulario Covid-19 <strong>UCLA</strong></h3>

        <div class="form-container">
          <section id="ask-1">
            <h5>¿En los ultimos 7 dias usted ha estado en contacto con una persona con covid-19?</h5>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="answer_one" value="option1">
              <label class="form-check-label">Si</label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="answer_one" value="option2">
              <label class="form-check-label">No</label>
            </div>
          </section>

          <section id="ask-2">
            <h5>¿Cual de los siguientes sintomas ha presentado en el transcurso de estos 7 dias?</h5>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" value="option1">
              <label class="form-check-label" for="inlineCheckbox1">Tos</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Dolor de garganta</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Dolor de cabeza</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox4" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Fiebre</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox5" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Dolor muscular</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox6" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Vomito</label>
            </div>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" id="inlineCheckbox7" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Diarrea</label>
            </div>
          </section>

          <section id="ask-3">
            <h5>Durante el estado de alarma y hasta el dia de hoy ¿Has tenido Covid-19?</h5>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="answer_two" value="option1" checked>
              <label class="form-check-label"> Si </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="answer_two" value="option2">
              <label class="form-check-label"> No </label>
            </div>
          </section>

          <section id="ask-4">
            <h5>¿Convive usted con personas mayores de 60 años?</h5>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="answer_five" value="option1">
              <label class="form-check-label"> Si </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="answer_five" value="option2">
              <label class="form-check-label"> No </label>
            </div>
          </section>

          <section id="ask-5">
            <div>
              <h5 for="inputGroupSelect01">De acuerdo a su estado de vacunación</h5>
            </div>
            <select class="custom-select" id="inputGroupSelect01">
              <option disabled selected hidden>Escoja su dosis a dia de hoy...</option>
              <option value="1"> Primera dosis aplicada </option>
              <option value="2"> Segunda dosis aplicada</option>
              <option value="3"> Tercera dosis aplicada</option>
              <option value="4"> No me encuentro vacunado</option>
            </select>
          </section>

          <section id="ask-6">
            <h5>¿Utiliza alguno de los siguientes metodos para el cuidado personal para contrarrestar el Covid-19?</h5>
            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" value="option1">
              <label class="form-check-label" for="inlineCheckbox1">Tapabocas</label>
            </div>

            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Gel</label>
            </div>

            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Alcohol</label>
            </div>

            <div class="form-check form-check-inline">
              <input class="form-check-input" type="checkbox" value="option2">
              <label class="form-check-label" for="inlineCheckbox2">Lavado frecuente de manos</label>
            </div>
          </section>

          <button type="submit">Enviar datos</button>
        </div>
      </div>
    </body>
  </html>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Formulario"
}
</script>

<style scoped>

* {
  box-sizing: border-box;
}

body .content {
  background: #141E30;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #243B55, #141E30);  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #243B55, #141E30); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  color: white;
  padding: 0 1.5em;
}

.form-container {
  max-width: 1170px;
  margin-left: auto;
  margin-right: auto;
  padding: 1.5em;
}

#ask-1 {
  border: solid #00ff00;
  margin: 12px;
}

#ask-2 {
  border: dashed 3px #40f2fe;
  margin: 12px;
}

#ask-3 {
  border: dashed 3px #00ff00;
  margin: 12px;
}

#ask-4 {
  border: solid #40f2fe;
  margin: 12px;
}

#ask-5 {
  border: dashed 3px #00ff00;
  margin: 12px;
}

#ask-6 {
  border: solid #40f2fe;
  margin: 12px;
}

button {
  width: 90px;
  margin-left: 45%;
}
</style>