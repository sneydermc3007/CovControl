<template>
  <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">

      <title>CovControl Sing In</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css">
    </head>

    <body>
      <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #4e488b;">
        <a class="navbar-brand">CovControl</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="btn btn-link px-3 me-2" href="/Log_in" type="button">Inicio de Sesion</a>
            </li>
            <li class="nav-item">
              <a class="btn btn-link px-3 me-2" href="/Sing_up" type="button">Registro</a>
            </li>
          </ul>
        </div>
      </nav>

      <section class="snake">
        <form action="InicioSesion.vue" v-on:submit.prevent="getConsulta();" class="form-box animated fadeInUp">
          <h1 class="form-title"> Inicio de sesion</h1>

          <input v-model="consulta.email" type="email" placeholder="Correo" name="email" id="email">

          <input v-model="consulta.pass" type="password" placeholder="Password" name="pass" id="pass">

          <button type="submit">Login</button>
        </form>
      </section>
    </body>
  </html>
</template>

<script>
  import axios from 'axios';
  import useValidate from '@vuelidate/core';
  import { required, email, minLength } from 'vuelidate/lib/validators';

  export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "InicioSesion",
  data() {
    return {
      $v: useValidate(),
      consulta: {
        email: null,
        pass: null,
      },
      submited: false
    };
  },
  validations: {
      consulta: {
        email: { required, email },
        pass: { required, minLength: minLength(8) },
      }
  },
  methods: {
    getConsulta(){
      console.log("Capturando datos");
      let variables = {
        email: this.consulta.email,
        pass: this.consulta.pass
      }
      console.log(variables);

      axios.post('http://127.0.0.1:5000/Log_in', variables)
        .then((response) => { console.log("Respuesta: ", response);
          if(response.status === 200){
            console.log("Datos enviados");
          }
        }).catch((error) => {
          console.error("Error al capturar el usuario")
          console.error(error);
        });
    },

  }
};
</script>

<style scoped>

html {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100vh;
}

section, html {
  height: 100%;
  background: #0f0c29;
  background: -webkit-linear-gradient(to right, #24243e, #302b63, #0f0c29);
  background: linear-gradient(to right, #24243e, #302b63, #0f0c29);
}

section {
  margin: 0;
  padding: 0;

  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

/*Alternativa al body*/
.snake {
  padding: 130px;
  height: auto;
}

.form-box {
  width: 450px;
  height: 380px;
  padding-top: 45px;
  background: #1c223e;
  text-align: center;
}

.form-title {
  color: #fff;
  text-transform: uppercase;
  font-weight: 400;
}

label {
  color: #ffffff;
  text-transform: uppercase;
  font-weight: 250;
  padding-right: 6px;
  padding-bottom: 1px;
}

.form-box input[type="email"],
.form-box input[type="password"],
.form-box button[type="submit"] {
  background: none;
  display: block;
  margin: 30px auto;
  padding: 10px 20px;
  border: solid #3742fa;
  width: 200px;
  outline: none;
  color: #fff;
  border-radius: 20px;
  transition: 0.25s;
}

.form-box input[type="email"]:focus,
.form-box input[type="password"]:focus{
  width: 270px;
  border-color: white;
}

.form-box button[type="submit"] {
  background: #5352ed;
  cursor: pointer;
  border: 2px solid #3742fa;
}

.form-box button[type="submit"]:hover {
  background: none;
}

.btn-link[type="button"]{
  font-weight: bold;
}

.btn-link[type="button"]:hover{
  background: #44e8d1;
  color: #ffffff;
}

.navbar-brand{
  font-weight: bold;
}

.navbar-light .navbar-brand {
  color: #ffffff;
}

.navbar-light .navbar-brand:hover {
  color: #ffffff;
}

.navbar.navbar-expand-lg.navbar-light{
  opacity: 0.9;
}
</style>