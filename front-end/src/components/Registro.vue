<template>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">

      <title>CovControl Sign Up</title>

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

</style>