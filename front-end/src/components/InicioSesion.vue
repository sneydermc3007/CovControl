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
              <a class="btn btn-link px-3 me-2" href="/" type="button">Inicio de Sesion</a>
            </li>
            <li class="nav-item">
              <a class="btn btn-link px-3 me-2" href="/" type="button">Registro</a>
            </li>
          </ul>
        </div>
      </nav>

      <section class="snake">
        <form action="InicioSesion.vue" class="form-box animated fadeInUp">
          <h1 class="form-title"> Inicio de sesion</h1>

          <input type="text" placeholder="Cedula">
            <label for="carrera"> Selecciona tu carrera: </label>
                <select required id="carrera">
                  <option value="" disabled selected hidden> Escoge una opción...</option>
                  <option value="0">Arquitectura</option>
                  <option value="1">Ingeniería Civil</option>
                  <option value="2">Ingeniería de Sistemas</option>
                  <option value="3">Ingeniería Industrial</option>
                </select>

          <input type="password" placeholder="Password">
          <button type="submit">Login</button>
        </form>
      </section>
    </body>

    <!-- Establecimiento de la conexion con el back-end en el html*
    <div>
      <h1>Hola Mundo</h1>
      <p> {{ msg }}</p>
    </div> -->
  </html>
</template>


<script>
/* Conexion con back-end
import axios from 'axios'
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "InicioSesion",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    getResponse(){
      const path = 'http://localhost:5000/Log_in';
      axios.get(path)
      .then((res) => {
        console.log(res.data)
        this.msg = res.data;
      })
      .catch((err) => { console.error(err); });
    }
  },
  created() {
    this.getResponse();
  }
}
*/
</script>

<style scoped>

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
  padding: 180px;
  height: auto;
}

.form-box {
  width: 450px;
  height: 530px;
  padding: 45px;
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

.form-box input[type="text"],
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

#carrera {
  color: grey;
  background: none;
  display: block;
  margin: 20px auto;
  padding: 12px 20px;
  border: solid #3742fa;
  width: 250px;
  outline: none;
  border-radius: 30px;
}

.form-box input[type="text"]:focus,
.form-box input[type="password"]:focus,
#carrera:focus {
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