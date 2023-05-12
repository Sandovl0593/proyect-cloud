<template>
    <div>
      <table>
        <tr>
          <th>Numero de compra</th>
          <th>Codigo de producto</th>
          <th>Vendedor</th>
        </tr>
        <tr v-for="compra of compras" v-bind:key="compra">
          <td>{{compra.codigo_c}}</td>
          <td>{{compra.codigo_p}}</td>
          <td>{{compra.usuario_v}}</td>
        </tr>
      </table>
    </div>
    <nav>
      <router-link to="/home">Casa</router-link>
    </nav>
  </template>
  
  <script>
  export default {
    name: "InventarioView",
    data(){
      return{
        compras: []
      }
    },
    methods: {
      async obtener_compras(){
        const apiUrl = import.meta.env.VITE_API_HOST;

        let usuario_c = {usuario: this.$store.state.mi_usuario}
        await fetch(`http://${apiUrl}:8081/utecshop/inventario`, {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(usuario_c)
        }).then((resp)=> resp.json()).then((datos)=> this.compras = datos)
      }
    },
    created(){
      this.obtener_compras()
    }
  }
  </script>
  
  <style scoped>
  
  </style>