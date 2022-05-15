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
        <Form @submit="getConsultaUser" class="form-box animated fadeInUp">
          <h1 class="form-title"> Inicio de sesion</h1>

          <div class="correo">
            <Field name="correo" type="email" placeholder="Correo" :rules="validateEmail" ></Field>
            <ErrorMessage name="correo" id="error-correo"></ErrorMessage>
          </div>

          <div class="contraseña">
            <Field name="password" type="password" placeholder="Contraseña" :rules="validatePass" ></Field>
            <ErrorMessage name="password" id="error-contraseña"></ErrorMessage>
          </div>

          <button type="submit">Login</button>
        </form>
      </section>
    </body>
  </html>
</template>

<script>
  import axios from 'axios';
  import { Form, Field, ErrorMessage } from "vee-validate";

  export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "InicioSesion",
    components: {
    Form, Field, ErrorMessage
    },
    methods: {
      getConsultaUser(values) {
        console.log("Capturando los datos");

        let camposVariables = {
          email: values.correo,
          pass: values.password
        }
        console.log(camposVariables);

        axios.post('http://127.0.0.1:5000/Log_in', camposVariables)
            .then((response) => { console.log("Respuesta:", response);
              if (response.data.status === "OK") {
                console.log("Datos correctos");
                window.location.href = "/Menu_one";
              }})
            .catch((error) => {
              console.error("Error al capturar el usuario");
              console.error(error);
            });
      },
      validateEmail(value){
        //Cuando el campo email esta vacio
        if(!value){
          return 'El campo email no puede estar vacio';
        }

        //Cuando el email no tiene el formato correcto
        const emailregex = /^[a-z.]+@(amigo.edu.co)$/i;
        if(!emailregex.test(value)){
          return 'El email no tiene el formato correcto';
        }
        //Cuando el campo email está perfecto
        return true;
      },
      validatePass(value){
        //Cuando el campo pass esta vacio
        if(!value){
          return 'El campo contraseña no puede estar vacio';
        }

        //Cuando la contraseña no tiene el tamaño correcto
        if (value.length < 8) {
          return 'La contraseña debe tener al menos 6 caracteres';
        }

        //Cuando el campo pass está perfecto
        return true;
      }
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
  background: #0ee3d1;  /* fallback for old browsers */
  background: -webkit-linear-gradient(to right, #dce3dc, rgb(4, 228, 206));  /* Chrome 10-25, Safari 5.1-6 */
  background: linear-gradient(to right, #d7e7d7, #04e4ce); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

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
/* Alternativa al body */
.snake {
  padding: 100px;
  height: auto;
}

.form-box {
  width: 430px;
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
  margin: 15px auto;
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

#error-correo,
#error-contraseña {
  color: #ffffff;
  font-style: italic;
}

.form-box:hover {
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2);
  border: 0;
  opacity: 1;
}
</style>