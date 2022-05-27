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

      <section class="formulario col-xl-6">
        <div class="form-container align-self-center">
          <form name="form" id="form" v-on:submit.prevent="validarCampos();">

            <h2 class="text-center"><strong>Registro</strong> de usuarios.</h2>

            <div class="row form-container">

              <div class="primer_nombre col-md">
                <div class="form-group">
                  <input v-model="registro.first_name" class="form-control" type="text" name="first_name" placeholder="Ingrese su Primer Nombre" id="first_name"
                  autocomplete="off" :class="{'is-invalid': submited && v$.registro.first_name.$error }">
                  <div v-if="submited && v$.registro.first_name.$error" class="invalid-feedback">
                    Su primer nombre es requerido.
                    <span v-if="!v$.registro.first_name.required"> Nombre 1 requerido</span>
                  </div>
                </div>
              </div>

              <div class="segundo_nombre col-md">
                <div class="form-group">
                  <input v-model="registro.second_name" class="form-control" type="text" name="second_name" placeholder="Ingrese su Segundo Nombre" id="second_name">
                </div>
              </div>

              <div class="w-100"></div>

              <div class="primer_apellido col-md">
                <div class="form-group">
                  <input v-model="registro.first_surname" class="form-control" type="text" name="first_surname" placeholder="Ingrese su Primer Apellido" id="first_surname"
                  autocomplete="off" :class="{'is-invalid': submited && v$.registro.first_surname.$error }">
                  <div v-if="submited && v$.registro.first_surname.$error" class="invalid-feedback">
                    Su primer apellido es requerido.
                    <span v-if="!v$.registro.first_surname.required"> Apellido 1 requerido</span>
                  </div>
                </div>
              </div>

              <div class="segundo_apellido col-md">
                <div class="form-group">
                  <input v-model="registro.second_surname" class="form-control" type="text" name="second_surname" placeholder="Ingrese su Segundo Apellido" id="second_surname">
                </div>
              </div>

              <div class="w-100"></div>

              <div class="fecha_nacimiento col-lg-9">
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

              <div class="w-100"></div>

              <div class="genero col-lg">
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-prepend">
                      <label class="input-group-text" for="sex">Opciones</label>
                    </div>
                    <select v-model="registro.sex" class="custom-select" id="sex"
                            :class="{'is-invalid': submited && v$.registro.sex.$error }">
                      <option disabled hidden value=""> Seleccione su sexo... </option>
                      <option value="1">Masculino</option>
                      <option value="2">Femenino</option>
                      <option value="3">No Binario</option>
                      <div v-if="submited && v$.registro.sex.$error" class="invalid-feedback">
                        Su genero es requerido
                        <span v-if="!v$.registro.sex.required"> Su sexo es requerido</span>
                      </div>
                    </select>
                  </div>
                </div>
              </div>

              <div class="numero_celular col-lg">
                <div class="form-group">
                  <input v-model.number="registro.number" class="form-control" type="number" name="phone" placeholder="Ingrese su Numero" id="number"
                         :class="{'is-invalid': submited && v$.registro.number.$error }">
                  <div v-if="submited && v$.registro.number.$error" class="invalid-feedback">
                    Su numero de celular es requerido.
                    <span v-if="!v$.registro.number.required"> Numero de celular solicitado</span>
                  </div>
                </div>
              </div>

              <div class="w-100"></div>

              <div class="correo col-md-7">
                <div class="form-group">
                  <input v-model="registro.email" class="form-control" type="email" placeholder="Ingrese su Correo" id="email"
                         :class="{'is-invalid': submited && v$.registro.email.$error }">
                  <div v-if="submited && v$.registro.email.$error" class="invalid-feedback">
                    El correo es requerido
                    <span v-if="!v$.registro.email.required"> Correo institucional requerido</span>
                  </div>
                </div>
              </div>

              <div class="w-100"></div>

              <div class="contraseña col-lg">
                <div class="form-group">
                  <input v-model="registro.password" class="form-control" type="password" placeholder="Ingrese una Contraseña" id="password"
                         :class="{'is-invalid': submited && v$.registro.password.$error }">
                  <div v-if="submited && v$.registro.password.$error" class="invalid-feedback">
                    La contraseña es requerida
                    <span v-if="!v$.registro.password.required"> Contraseña requerida</span>
                  </div>
                </div>
              </div>

              <div class="verificar_contraseña col-lg">
                <div class="form-group">
                  <input v-model="registro.verify_password" class="form-control" type="password" placeholder="Repita la Contraseña" id="verify_password"
                         :class="{'is-invalid': submited && v$.registro.verify_password.$error }">
                  <div v-if="submited && v$.registro.verify_password.$error" class="invalid-feedback">
                    La  verificación de la contraseña es requerida
                    <span v-if="!v$.registro.verify_password.required"> La verificación es requerida</span>
                  </div>
                </div>
              </div>

              <div class="w-100"></div>

              <div class="datos-personales col-lg-8">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="defaultCheck1" value="Si">
                  <label class="form-check-label" for="defaultCheck1">
                    Acepto el tratamiento de mis datos personales
                    <a  href="https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981">Ley 1581 de 2012</a>
                  </label>
                </div>
              </div>

              <div class="w-100"></div>

              <div class="boton-enviar col-lg">
                <div class="form-group">
                  <button class="btn btn-block" type="submit">Sign Up</button>
                </div>
              </div>

            </div>

          </form>
        </div>
      </section>
    </body>
  </html>
</template>

<script>
import axios from 'axios';
import useValidate from "@vuelidate/core"
import { required } from "@vuelidate/validators"

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
        //this.submited = true;

        console.log("Campos validos");

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
        console.log(parametros)

        axios.post('http://127.0.0.1:5000/Sing_Up', parametros)
            .then((response) => { console.log("Respuesta:", response);
              if(response.status === 200){
                console.log("Usuario creado");
                alert("Se ha registrado exitosamente el usuario con nombre: "
                    + this.registro.first_name + " " + this.registro.second_name
                    + " " + this.registro.first_surname + " " + this.registro.second_surname);

                document.form.reset();
                this.$router.push('/Sing_Up?s=1');
                setTimeout(function () { window.location.href = '/Log_in'; }, 3000);  //Redireccionar a la página de Inicio de sesion
              }})
            .catch((error) => {
              console.log("Error:", error);
            });
      },
      validarCampos(){
        this.submited = true;
        this.v$.registro.$touch();

        if(this.v$.registro.$invalid){
          console.error("Campos vacios");
          alert("Por favor, verifique los campos");
        } else {
          console.log("Campos validos");
          this.procesarUsuario();
        }

      }
    }
  };
</script>

<style scoped>

.bg-light {
  background: #141f2d!important;
  opacity: 0.9;
}


.navbar-brand{
  font-weight: bold;
}

.navbar-light .navbar-brand {
  color: #29e7d5;
  font-style: italic;
}

.navbar-light .navbar-brand:hover {
  color: #29e7d5;
}

.btn-link[type="button"]{
  font-weight: bold;
  color: #0ee363;
}

.btn-link[type="button"]:hover {
  background: #0ee363;
  color: #ffffff;
}

body{
  margin: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  background: #070914;
  background: -webkit-linear-gradient(to right, #223748, #070914);
  background: linear-gradient(to right, #223748, #070914);

  background-size: cover;

  min-height: 100vh;
}

.formulario {
  padding: 30px;
  border-radius: 10px;
  color: white;
  overflow: hidden;
  display: table;
  margin-left: auto;
  margin-right: auto;
  margin-top: 5em;
}

.formulario form h2 {
  font-size: 24px;
  line-height: 1.5;
  margin-bottom: 30px;
  text-transform: uppercase;
  font-style: italic;
}

b, strong {
  font-weight: bolder;
}

.formulario {
  box-shadow: 0 0 10px #1f5056;
  background: #0e1724;
  opacity: 0.87;
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
  color: blue;
  background: #1b96ff;
  margin-top: 1em;
}

.btn-block{
  display: block;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

#sex.custom-select {
  background: none;
  color: grey;
  border: 2px dashed #11d3b8;
}

.input-group-text {
  border: 1px solid #11d3b8;
  background: none;
  color: #ffffff;
  font-weight: bolder;
  border-radius: 20px;
}

.form-container input[type="text"],
.form-container input[type="number"],
.form-container input[type="email"],
.form-container input[type="password"],
.form-container button[type="submit"] {
  border-radius: 20px;
  /*background: none;  SI no queremos que se vea lo blanco cuando seleccionamos algún input */
  color: white;
  transition: 0.55s;
}

.form-container input[type="text"]:focus,
.form-container input[type="number"]:focus,
.form-container input[type="email"]:focus,
.form-container input[type="password"]:focus {
  width: 300px;
  border-color: #42b983;
  color: black;
  font-weight: bolder;
  font-style: italic;
}

.form-container button[type="submit"]:hover {
  background: none;
  border: 2px solid #42b983;
}

.datos-personales {
  margin-bottom: 20px;
  margin-top: 10px;
}

.datos-personales input[type=checkbox] {
  display: none;
}

.datos-personales input[type=checkbox] + label {
  cursor: pointer;
}

.datos-personales label:before{
  content: "";
  background: transparent;
  border: 3px solid #11d3b8;
  border-radius: 5px;
  display: inline-block;
  margin-right: 8px;
  text-shadow: 2px -2px 3px gray;
  text-align: center;
  vertical-align: center;
  height: 20px;
  width: 20px;
}

.datos-personales input[type=checkbox]:checked + label:before {
  content: '✓';
  font-size: 10px;
  color: #ffffff;
}

</style>