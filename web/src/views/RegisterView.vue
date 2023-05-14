<template>
  <div class="global">
  <div class="register-container">
    <h2>Registro</h2>
    <div class="form-group">
      <label>Nombre</label>
      <input type="text" v-model="nombre" class="form-control">
    </div>
    <div class="form-group">
      <label>Teléfono</label>
      <input type="text" v-model="telefono" class="form-control">
    </div>
    <div class="form-group">
      <label>Dirección</label>
      <input type="text" v-model="direccion" class="form-control">
    </div>
    <div class="form-group">
      <label>Usuario</label>
      <input type="text" v-model="nombre_usuario" class="form-control">
    </div>
    <div class="form-group">
      <label>Email</label>
      <input type="text" v-model="email" class="form-control">
    </div>
    <div class="form-group">
      <label>Contraseña</label>
      <input type="password" v-model="contrasenha" class="form-control">
    </div>
    <button v-on:click="registrar_usuario" class="btn btn-primary">Registrar</button>
  </div>
  </div>
</template>

<script>
export default {
  name: "RegisterView",
  data() {
    return {
      nombre: "",
      telefono: "",
      direccion: "",
      nombre_usuario: "",
      email: "",
      contrasenha: ""
    }
  },
  methods: {
    registrar_usuario() {
      // Lógica de registro de usuario
    }
  }
}
</script>

<style scoped>

.global{
  background-image: url('../assets/rojaso.jpeg');
  background-size: cover;
  height: 100vh;
 
}

.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 5px;
  background-size: cover;
  background-position: center;

}

h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #EFEFEF;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #EFEFEF;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  

}

.form-control:focus {
  outline: none;
  
}



.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 19px;
  cursor: pointer;
  font-size: 18px;
}

.btn-primary {
  background-color: #007bff;
  color: #fff;
}

.btn-primary:hover {
  background-color: #0056b3;
}

</style>
