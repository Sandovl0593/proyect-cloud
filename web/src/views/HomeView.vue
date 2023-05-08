<template>
    <div class="home">
      <h1>"Bienvenido a Utec Shop"</h1>
      <div v-for="usuario of usuarios" v-bind:key="usuario">
        <h2 v-if="usuario.nombre_usuario === $store.state.mi_usuario">Usuario: {{usuario.nombre_usuario}}</h2>
        <h2 v-if="usuario.contrasenha === $store.state.mi_contrasenha">Contraseña: {{usuario.contrasenha}}</h2>
      </div>
    </div>
    <nav>
      <router-link to="/compras">Comprar</router-link> |
      <router-link to="/ventas">Vender</router-link> |
      <router-link to="/inventario">Inventario</router-link> <br>
      <router-link to="/">Logout</router-link>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'HomeView',
    data(){
      return{
        usuarios: []
      }
    },
    methods: {
      async obtener_usuarios(){
        await fetch('http://127.0.0.1:5000/utecshop/usuarios')
            .then((resp) => resp.json()).then((datos) => this.usuarios = datos)
      }
    },
    created(){
      this.obtener_usuarios()
    }
  }
  </script>
  