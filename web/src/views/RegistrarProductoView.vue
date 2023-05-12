<template>
    <div>
      <label>Nombre</label>
      <input type="text" v-bind:value="nombre" v-on:input="registrar_nombre"><br>
      <br>
      <label>Precio</label>
      <input type="text" v-bind:value="precio" v-on:input="registrar_precio"><br>
      <br>
      <label>Marca</label>
      <input type="text" v-bind:value="marca" v-on:input="registrar_marca"><br>
      <br>
      <label>Categoria</label>
      <input type="text" v-bind:value="tipo" v-on:input="registrar_tipo"><br>
      <br>
      <button v-on:click="registrar_producto">Registrar producto</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "RegistrarProductoView",
    data(){
      return {
        codigo: "",
        usuario_nombre: this.$store.state.mi_usuario,
        nombre: "",
        precio: "",
        tipo: "",
        marca: ""
      }
    },
    methods: {
      productos(){
        this.$router.push('/productos')
      },
      registrar_nombre(e){
        this.nombre = e.target.value
      },
      registrar_precio(e){
        this.precio = e.target.value
      },
      registrar_marca(e){
        this.marca = e.target.value
      },
      registrar_tipo(e){
        this.tipo = e.target.value
      },
      async registrar_producto(){
        const apiUrl = import.meta.env.VITE_API_HOST;

        let n_producto = {usuario: this.usuario_nombre, nombre: this.nombre,
          precio: this.precio, marca: this.marca, categoria: this.tipo}
        await fetch(`http://${apiUrl}:8001/utecshop/registrar_producto`, {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(n_producto)
        }).then(this.productos)
      }
    }
  }
  </script>
  
  <style scoped>
  
  </style>