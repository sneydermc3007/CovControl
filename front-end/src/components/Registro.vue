<template>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">

      <title>CovControl Sign Up</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css">
    </head>

    <body>
      <section class="barra-navegacion">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <a class="navbar-brand">CovControl</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <a class="btn btn-link px-3 me-2" href="/Log_in" type="button">Inicio de Sesion</a>
              </li>
              <li class="nav-item active">
                <a class="btn btn-link px-3 me-2" href="/Sing_up" type="button">Registro</a>
              </li>
            </ul>
          </div>
        </nav>
      </section>

      <section class="register-photo animated fadeInLeft">
        <div class="form-container">
          <div class="image-holder"></div>

          <form name="form" id="form" v-on:submit.prevent="procesarUsuario()">
            <h2 class="text-center"><strong>Registro</strong> de usuarios.</h2>

            <div class="primer_nombre">
              <div class="form-group">
                <input v-model="registro.first_name" class="form-control" type="text" name="first_name" placeholder="Ingrese su Primer Nombre" id="first_name"
                       autocomplete="off" :class="{'is-invalid': submited && v$.registro.first_name.$error }">
                <div v-if="submited && v$.registro.first_name.$error" class="invalid-feedback">
                  Su primer nombre es requerido.
                  <span v-if="!v$.registro.first_name.required"> Nombre 1 requerido</span>
                </div>
              </div>
            </div>

            <div class="segundo_nombre">
              <div class="form-group">
                <input v-model="registro.second_name" class="form-control" type="text" name="second_name" placeholder="Ingrese su Segundo Nombre" id="second_name">
              </div>
            </div>

            <div class="primer_apellido">
              <div class="form-group">
                <input v-model="registro.first_surname" class="form-control" type="text" name="first_surname" placeholder="Ingrese su Primer Apellido" id="first_surname"
                      autocomplete="off" :class="{'is-invalid': submited && v$.registro.first_surname.$error }">
                <div v-if="submited && v$.registro.first_surname.$error" class="invalid-feedback">
                  Su primer apellido es requerido.
                  <span v-if="!v$.registro.first_surname.required"> Apellido 1 requerido</span>
                </div>
              </div>
            </div>

            <div class="segundo_apellido">
              <div class="form-group">
                <input v-model="registro.second_surname" class="form-control" type="text" name="second_surname" placeholder="Ingrese su Segundo Apellido" id="second_surname">
              </div>
            </div>

            <div class="fecha_nacimiento">
              <div class="form-group">
                <label class="text-center" for="born"> <strong>Seleccione su fecha de nacimiento</strong></label>
                <input v-model="registro.born" class="form-control" type="date" name="born" id="born"
                       :class="{'is-invalid': submited && v$.registro.born.$error }">
                <div v-if="submited && v$.registro.born.$error" class="invalid-feedback">
                  Su fecha de nacimiento es requerida.
                  <span v-if="!v$.registro.born.required"> Fecha de nacimiento requerida</span>
                </div>
              </div>
            </div>

            <div class="genero">
              <div class="form-group">
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <label class="input-group-text" for="sex">Opciones</label>
                  </div>
                  <select v-model="registro.sex" class="custom-select" id="sex"
                          :class="{'is-invalid': submited && v$.registro.sex.$error}">
                    <div v-if="submited && v$.registro.sex.$error" class="invalid-feedback">
                      Su genero es requerido
                      <span v-if="!v$.registro.sex.required"> Su sexo es requerido</span>
                    </div>
                    <option disabled hidden value=""> Seleccione su sexo... </option>
                    <option value="1">Masculino</option>
                    <option value="2">Femenino</option>
                    <option value="3">No Binario</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="numero_celular">
              <div class="form-group">
                <input v-model.number="registro.number" class="form-control" type="number" name="phone" placeholder="Ingrese su Numero" id="number"
                 :class="{'is-invalid': submited && v$.registro.sex.$error }">
                <div v-if="submited && v$.registro.sex.$error" class="invalid-feedback">
                  Su fecha de nacimiento es requerida.
                  <span v-if="!v$.registro.sex.required"> Fecha de nacimiento requerida</span>
                </div>
              </div>
            </div>

            <div class="correo">
              <div class="form-group">
                <input v-model="registro.email" class="form-control" type="email" placeholder="Ingrese su Correo" id="email"
                       :class="{'is-invalid': submited && v$.registro.email.$error }">
                <div v-if="submited && v$.registro.email.$error" class="invalid-feedback">
                  El correo institucional es requerido
                  <span v-if="!v$.registro.email.required"> Correo institucional requerido</span>
                </div>
              </div>
            </div>

            <div class="contraseña">
              <div class="form-group">
                <input v-model="registro.password" class="form-control" type="password" placeholder="Ingrese una Contraseña" id="password"
                       :class="{'is-invalid': submited && v$.registro.password.$error }">
                <div v-if="submited && v$.registro.password.$error" class="invalid-feedback">
                  La contraseña es requerida
                  <span v-if="!v$.registro.password.required"> Contraseña requerida</span>
                </div>
              </div>
            </div>

            <div class="verificar_contraseña">
              <div class="form-group">
                <input v-model="registro.verify_password" class="form-control" type="password" placeholder="Repita la Contraseña" id="verify_password"
                       :class="{'is-invalid': submited && v$.registro.verify_password.$error }">
                <div v-if="submited && v$.registro.verify_password.$error" class="invalid-feedback">
                  La  verificación de la contraseña es requerida
                  <span v-if="!v$.registro.verify_password.required"> La verificación es requerida</span>
                </div>
              </div>
            </div>

            <div class="datos-personales">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="defaultCheck1" required>
                <label class="form-check-label" for="defaultCheck1">
                  Acepto el tratamiento de mis datos personales
                  <a  href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981">Ley 1581 de 2012</a>
                </label>
              </div>
            </div>

            <div class="form-group"><button class="btn btn-block" type="submit">Sign Up</button></div>

          </form>
        </div>
      </section>
    </body>
  </html>
</template>

<script>
 import axios from 'axios';
 import useValidate from "@vuelidate/core";
 import { required } from 'vuelidate/lib/validators';

  export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Registro",
    setup() { return { v$: useValidate() } },
    data () {
      return {
        $v: useValidate(),
        registro: {
          first_name: null,
          second_name: null,
          first_surname: null,
          second_surname: null,
          born: null,
          sex: "",
          number: null,
          email: null,
          password: null,
          verify_password: null
        },
        submited: false
      }
    },
    validations: {
      registro: {
        first_name: { required },
        first_surname: { required },
        born: { required },
        sex: { required },
        number: { required },
        email: { required },
        password: { required },
        verify_password: { required }
      }
    },
    methods: {
      procesarUsuario(){
        this.submited = true;
        this.v$.$touch();

        if (this.v$.$invalid) {
          console.log('Campos invalidos');
          alert('Por favor, llene todos los campos correctamente');
        }
        else {
          console.log('Campos validos');
          console.log("Capturando datos");

          let parametros = {
            first_name: this.registro.first_name,
            second_name: this.registro.second_name,
            first_surname: this.registro.first_surname,
            second_surname: this.registro.second_surname,
            born: this.registro.born,
            sex: this.registro.sex,
            number: this.registro.number,
            email: this.registro.email,
            password: this.registro.password
          };
          console.log(parametros);
          axios.post('http://127.0.0.1:5000/Sing_up', parametros)
            .then((response) => { console.log("Respuesta:", response);
              if(response.status === 200) {
                console.log("Registro exitoso");
                alert("Se ha registrado exitosamente el usuario con nombre: " + this.registro.first_name);
                //window.location.href = "/Log_in";
                //document.form.reset();
                //this.$router.push('/Sing_Up?s=1');
              }})
            .catch((error) => {
              console.log("Error:", error);
            });
        }
      }
    }
  };
</script>

<style scoped>

.register-photo {
  background: #16222A;
  background: -webkit-linear-gradient(to right, #3A6073, #16222A);
  background: linear-gradient(to right, #3A6073, #16222A);

  background-size: cover;

  padding: 60px 0;
}

.register-photo{
  color: #ff9800;
  /*overflow: hidden; Para quitar la barra de bajada */
}

.register-photo .form-container { /* Tamaño y ubicación */
  display: table;
  max-width: 900px;
  width: 90%;
  margin: 0 auto;
  box-shadow: 7px 13px 37px #0db2d7;
}

.register-photo .image-holder { /* Muestra la imagen en el div */
  display: table-cell;
  width: auto;
  background: url(/src/assets/b.jpg);
  background-size: cover;
}

.register-photo form { /* Permite la union div-form */
  display: table-cell;
  width: 400px;
  background-color: #ffffff;
  padding: 40px 50px;
}

.register-photo form h2 {
  font-size: 24px;
  line-height: 1.5;
  margin-bottom: 30px;
  text-transform: uppercase;
}

b, strong {
  font-weight: bolder;
}

.form-container form{
  background: #050506;
  border: solid #fc7b00;
}

.form-control {
  background: none;
  border: solid #0db2d7;
}

.form-container a {
  color: #11d3b8;
  text-align: center;
  font-size: 16px;
  text-decoration: none;
}

.form-container a:hover {
  color: #11d3b8;
  text-align: center;
  font-size: 16px;
  text-decoration: underline;
}

.form-container .btn{
  color: #11d3b8;
  background: #fc7b00;
}

#sex.custom-select {
  background: none;
  color: grey;
  border: 2px dashed #11d3b8;
}

.input-group-text {
  border: 1px solid #11d3b8;
  background: none;
  color: #fc7b00;
  font-weight: bolder;
  border-radius: 20px;
}

.form-container input[type="text"],
.form-container input[type="number"],
.form-container input[type="email"],
.form-container input[type="password"],
.form-container button[type="submit"] {
  border-radius: 20px;
  /*background: none;  SI no queremos que se vea lo blanco cuando seleccionamos algún input*/
  color: white;
  transition: 0.55s;
}

.form-container input[type="text"]:focus,
.form-container input[type="number"]:focus,
.form-container input[type="email"]:focus,
.form-container input[type="password"]:focus {
  width: 200px;
  border-color: orangered;
  color: black;
  font-weight: bolder;
}

.datos-personales {
  margin-left: 10px;
  margin-top: 20px;
}

.form-container button{
  margin-top: 1.5em;
}

.form-container button[type="submit"]:hover {
  background: none;
  border: 2px solid orangered;
}

.bg-light {
  background: #3A6073!important;
  opacity: 0.9;
}

.navbar-brand{
  font-weight: bold;
}

.navbar-light .navbar-brand {
  color: #fc7b00;
}

.navbar-light .navbar-brand:hover {
  color: #fc7b00;
}

.btn-link[type="button"]{
  font-weight: bold;
}

.btn-link[type="button"]{
  font-weight: bold;
  color: #11d3b8;
}

.btn-link[type="button"]:hover {
  background: #11d3b8;
  color: #ffffff;
}
</style>