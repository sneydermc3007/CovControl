<template>
  <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">

      <title>CovControl Formulario</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    </head>

    <body>
      <div class="content">

        <h3>Formulario Covid-19 <span>UCLA</span></h3>

        <form name="formulario" id="formulario" v-on:submit.prevent="getFormulario();">
          <div class="form-container">
            <section id="ask-1">
              <h5>¿En los ultimos 7 dias usted ha estado en contacto con una persona con covid-19?</h5>
              <div class="form-check">
                <input class="form-check-input" v-model="form.answer_one" type="radio" name="answer_one" id="answer_one-1" value="1">
                <label class="form-check-label" for="answer_one-1">Si</label>
              </div>
              <div class="form-check">
                <input class="form-check-input" v-model="form.answer_one" type="radio" name="answer_one" id="answer_one-2" value="2">
                <label class="form-check-label" for="answer_one-2">No</label>
              </div>
            </section>

            <section id="ask-2">
              <h5>¿Cual de los siguientes sintomas ha presentado en el transcurso de estos 7 dias?</h5>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_two-1" name="answer_two" value="1">
                <label class="form-check-label" for="answer_two-1">Tos</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_two-2" name="answer_two" value="2">
                <label class="form-check-label" for="answer_two-2">Dolor de garganta</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_two-3" name="answer_two" value="3">
                <label class="form-check-label" for="answer_two-3">Dolor de cabeza</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_two-4" name="answer_two" value="4">
                <label class="form-check-label" for="answer_two-4">Fiebre</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_two-5" name="answer_two" value="5">
                <label class="form-check-label" for="answer_two-5">Dolor muscular</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_two-6" name="answer_two" value="6">
                <label class="form-check-label" for="answer_two-6">Vomito</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_two" type="checkbox" id="answer_one-7" name="answer_two" value="7">
                <label class="form-check-label" for="answer_one-7">Diarrea</label>
              </div>
            </section>

            <section id="ask-3">
              <h5>Durante el estado de alarma y hasta el dia de hoy ¿Has tenido Covid-19?</h5>
              <div class="form-check">
                <input class="form-check-input" v-model="form.answer_three" type="radio" name="answer_three" id="answer_three-1" value="1">
                <label class="form-check-label" for="answer_three-1"> Si </label>
              </div>
              <div class="form-check">
                <input class="form-check-input" v-model="form.answer_three" type="radio" name="answer_three" id="answer_three-2" value="2">
                <label class="form-check-label" for="answer_three-2"> No </label>
              </div>
            </section>

            <section id="ask-4">
              <h5>¿Convive usted con personas mayores de 60 años?</h5>
              <div class="form-check">
                <input class="form-check-input" v-model="form.answer_four" type="radio" name="answer_four" id="answer_four-1" value="1">
                <label class="form-check-label" for="answer_four-1"> Si </label>
              </div>
              <div class="form-check">
                <input class="form-check-input" v-model="form.answer_four" type="radio" name="answer_four" id="answer_four-2" value="2">
                <label class="form-check-label" for="answer_four-2"> No </label>
              </div>
            </section>

            <section id="ask-5">
              <div>
                <h5 for="answer_five">De acuerdo a su estado de vacunación</h5>
              </div>
              <select class="custom-select" v-model="form.answer_five" name="answer_five" id="answer_five">
                <option disabled hidden value=null>Escoja su dosis a dia de hoy...</option>
                <option value="1"> Primera dosis aplicada </option>
                <option value="2"> Segunda dosis aplicada</option>
                <option value="3"> Tercera dosis aplicada</option>
                <option value="4"> No me encuentro vacunado</option>
              </select>
            </section>

            <section id="ask-6">
              <h5>¿Utiliza alguno de los siguientes metodos para el cuidado personal para contrarrestar el Covid-19?</h5>
              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_six" type="checkbox" name="answer_six" id="answer_six-1" value="1">
                <label class="form-check-label" for="answer_six-1">Tapabocas</label>
              </div>

              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_six" type="checkbox" name="answer_six" id="answer_six-2" value="2">
                <label class="form-check-label" for="answer_six-2">Gel</label>
              </div>

              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_six" type="checkbox" name="answer_six" id="answer_six-3" value="3">
                <label class="form-check-label" for="answer_six-3">Alcohol</label>
              </div>

              <div class="form-check form-check-inline">
                <input class="form-check-input" v-model="form.answer_six" type="checkbox" name="answer_six" id="answer_six-4" value="4">
                <label class="form-check-label" for="answer_six-4">Lavado frecuente de manos</label>
              </div>
            </section>

            <button type="submit" >Enviar datos</button>
          </div>
        </form>
      </div>
    </body>
  </html>
</template>

<script>
import axios from 'axios';

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Formulario",
  data() {
    return {
      form: {
        answer_one: null,
        answer_two: [],
        answer_three: null,
        answer_four: null,
        answer_five: null,
        answer_six: []
      }
    };
  },
  methods: {
    getFormulario() {

      let parametros = {
        answer_one: this.form.answer_one,
        answer_two: this.form.answer_two,
        answer_three: this.form.answer_three,
        answer_four: this.form.answer_four,
        answer_five: this.form.answer_five,
        answer_six: this.form.answer_six
      }
      console.info("Formulario: ", this.form);

      axios.post('http://127.0.0.1:5000/Menu_one', parametros)
        .then((response) => {  console.log("Respuesta formulario:", response);
          if(response.status === 200){
            console.log("Formulario enviado con éxito");
          }
        })
      .catch((error) => {
        console.error("Error al enviar el formulario");
        console.error(error);
      });
    }
  }
}
</script>

<style scoped>

* {
  box-sizing: border-box;
}

body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  background: #141E30;
  background: -webkit-linear-gradient(to right, #243B55, #141E30);
  background: linear-gradient(to right, #243B55, #141E30);

  min-height: 100vh;
  color: white;

  padding-top: 30px;
  padding-left: 1.5em;
  padding-right: 1.5em;
}

h3 {
  text-align: center;
  font-size: 3em;
}

h3 span {
  color: #42b983;
  font-weight: bold;
}

.form-container {
  max-width: 1170px;
  margin-left: auto;
  margin-right: auto;
  padding: 1.5em;

  box-shadow: 0 0 20px 0 rgba(255, 255, 255, .3);

  background: #212c40;
}

.form-container > * {
  padding: 1em;
}

select {
  color: #42b983;
  font-family:"Script MT Bold", cursive;
  font-size: medium;
}

.custom-select:focus {
  width: 50%;
  transition: 0.5s;
  color: #0db2d7;
  background: none;
}

#ask-1 input[type=radio],
#ask-3 input[type=radio],
#ask-4 input[type=radio]{
  display: none;
}

#ask-1 .form-check-label,
#ask-3 .form-check-label,
#ask-4 .form-check-label{
  color: #ffffff;
  width: 10%;
  background: #212c40;
  padding: 5px 15px 5px 60px;
  display: inline-block;
  position: relative;
  font-size: 1em;
  border-radius: 3px;
  cursor: pointer;
  -webkit-transition: all 0.3s ease;
  -o-transition: all 0.3s ease;
  transition: all 0.3s ease;
}

#ask-1 .form-check-label:hover,
#ask-3 .form-check-label:hover,
#ask-4 .form-check-label:hover{
  background: rgba(0,166,217,0.2);
}

#ask-1 .form-check-label:before,
#ask-3 .form-check-label:before,
#ask-4 .form-check-label:before{
  content: "";
  width: 20px;
  height: 20px;
  display: inline-block;
  background: transparent;
  border: 3px solid #00cbab;
  position: absolute;
  left: 20px;
  top: 4px;
  border-radius: 20px;
}

#ask-1 input[type=radio]:checked + label,
#ask-3 input[type=radio]:checked + label,
#ask-4 input[type=radio]:checked + label{
  padding: 5px 15px;
  background: #42b983;
  border-radius: 2px;
  color: white;
}

#ask-1 input[type=radio]:checked + label:before,
#ask-3 input[type=radio]:checked + label:before,
#ask-4 input[type=radio]:checked + label:before {
  display: none;
}

#ask-2 input[type=checkbox],
#ask-6 input[type=checkbox]{
  display: none;
}

#ask-2 input[type=checkbox] + label,
#ask-6 input[type=checkbox] + label{
  cursor: pointer;
}

#ask-2 label:before,
#ask-6 label:before{
  content: "";
  background: transparent;
  border: 3px solid #42b983;
  border-radius: 5px;
  display: inline-block;
  height: 20px;
  margin-right: 8px;
  text-shadow: 2px -2px 3px gray;
  text-align: center;
  vertical-align: center;
  width: 20px;
}

#ask-2 input[type=checkbox]:checked + label:before,
#ask-6 input[type=checkbox]:checked + label:before{
  content: '✓';
  font-size: 13px;
  color: #11d3b8;
}

.form-container label,
.form-container select{
  width: 100%;
  padding: 0.5em;
  border: none;
  background: none;
  border-bottom: 1px solid #40f2fe;
}

.content button[type=submit] {
  background: #42b983;
  border-radius: 15px;
  padding: .7em;
  color: white;
  border-color: #39d9bd;
  box-shadow: 0 0 20px 0 rgb(30 217 213 / 65%);
  width: 30%;
  margin-top: 5px;
  margin-left: 35%;
}

.content button[type=submit]:hover {
  background: none;
  transition: 0.4s;
  border: 2px solid #10e0f6;
  font-weight: bolder;
  color: #42b983;
}
</style>