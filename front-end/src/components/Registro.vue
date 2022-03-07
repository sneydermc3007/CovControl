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
                <a class="btn btn-link px-3 me-2" href="/" type="button">Inicio de Sesion</a>
              </li>
              <li class="nav-item active">
                <a class="btn btn-link px-3 me-2" href="/" type="button">Registro</a>
              </li>
            </ul>
          </div>
        </nav>
      </section>

      <section class="register-photo animated fadeInLeft">
        <div class="form-container">
          <div class="image-holder"></div>

          <form>
            <h2 class="text-center"><strong>Registro</strong> de usuarios.</h2>

            <div class="form-group"><input class="form-control" type="text" name="name-one" placeholder="Ingrese su Primer Nombre"></div>
            <div class="form-group"><input class="form-control" type="text" name="name-two" placeholder="Ingrese su Segundo Nombre"></div>
            <div class="form-group"><input class="form-control" type="text" name="name-two" placeholder="Ingrese su Primer Apellido"></div>
            <div class="form-group"><input class="form-control" type="text" name="name-two" placeholder="Ingrese su Segundo Apellido"></div>

            <div class="form-group">
              <label class="text-center" for="born"> <strong>Seleccione su fecha de nacimiento</strong></label>
              <input class="form-control" type="date" name="born">
            </div>

            <div class="form-group">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <label class="input-group-text" for="inputGroupSelect01">Opciones</label>
                </div>
                <select class="custom-select" id="inputGroupSelect01">
                  <option disabled selected hidden>Escoja su sexo...</option>
                  <option value="1">Masculino</option>
                  <option value="2">Femenino</option>
                  <option value="3">Binario</option>
                </select>
              </div>
            </div>

            <div class="form-group"><input class="form-control" type="number" name="phone" placeholder="Ingrese su Numero"></div>
            <div class="form-group"><input class="form-control" type="email" placeholder="Ingrese su Correo"/></div>
            <div class="form-group"><input class="form-control" type="password" placeholder="Ingrese una Contraseña"/></div>
            <div class="form-group"><input class="form-control" type="password" placeholder="Repita la Contraseña"/></div>

            <div class="form-group"><button class="btn btn-block" type="submit">Sign Up</button></div>
            <a class="already" href="/">Ya cuentas con una cuenta? Entra aquí.</a>
          </form>
        </div>
      </section>
    </body>
  </html>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Registro"
}
</script>

<style scoped>

.register-photo {
  background: #16222A;
  background: -webkit-linear-gradient(to right, #3A6073, #16222A);
  background: linear-gradient(to right, #3A6073, #16222A);

  //background: url(/src/assets/d.jpeg);
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

.custom-select {
  background: none;
  color: grey;
  border: 2px dashed #11d3b8;
  border-radius: 20px;
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