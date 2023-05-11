<template>
    <div>
      <label>Nombre</label>
      <input type="text" v-bind:value="nombre" v-on:input="registrar_nombre"><br>
      <br>
      <label>Telefono</label>
      <input type="text" v-bind:value="telefono" v-on:input="registrar_telefono"><br>
      <br>
      <label>Dirección</label>
      <input type="text" v-bind:value="direccion" v-on:input="registrar_direccion"><br>
      <br>
      <label>Usuario</label>
      <input type="text" v-bind:value="nombre_usuario" v-on:input="registrar_nusuario"><br>
      <br>
      <label>Email</label>
      <input type="text" v-bind:value="email" v-on:input="registrar_email"><br>
      <br>
      <label>Contrasenha</label>
      <input type="password" v-bind:value="contrasenha" v-on:input="registrar_contrasenha"><br>
      <br>
      <button v-on:click="registrar_usuario">Registrar</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "RegisterView",
    data(){
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
      casa(){
        this.$store.dispatch("accion_act_usuario", this.nombre_usuario)
        this.$store.dispatch("accion_act_contra", this.contrasenha)
        this.$router.push('/home')
      },
      registrar_nombre(e){
        this.nombre = e.target.value
      },
      registrar_telefono(e){
        this.telefono = e.target.value
      },
      registrar_direccion(e){
        this.direccion = e.target.value
      },
      registrar_nusuario(e){
        this.nombre_usuario = e.target.value
      },
      registrar_email(e){
        this.email = e.target.value
      },
      registrar_contrasenha(e){
        this.contrasenha = e.target.value
      },
      async registrar_usuario(){
        let n_usuario =  {nombre_usuario: this.nombre_usuario, nombre: this.nombre, telefono: this.telefono, direccion: this.direccion,
           email: this.email, contrasenha: this.contrasenha}
        await fetch('http://127.0.0.1:8000/utecshop/register', {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(n_usuario)
        }).then(this.casa)
      }
    }
  }
  </script>
  
  <style scoped>
  
  </style>