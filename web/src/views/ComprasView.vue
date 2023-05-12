<template>
    <div class="compras">
      <table>
        <tr>
          <th>Codigo</th>
          <th>Vendedor</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Marca</th>
          <th>Categoria</th>
        </tr>
        <tr v-for="producto of productos" v-bind:key="producto">
          <td>{{producto.codigo}}</td>
          <td>{{producto.usuario_nombre}}</td>
          <td>{{producto.nombre}}</td>
          <td>{{producto.precio}}</td>
          <td>{{producto.marca}}</td>
          <td>{{producto.tipo}}</td>
          <button v-on:click="comprar(producto.codigo, producto.usuario_nombre)">Comprar</button>
        </tr>
      </table>
    </div>
    <nav>
      <router-link to="/home">Casa</router-link>
    </nav>
  </template>
  
  <script>
  export default {
    name: "ComprasView",
    data(){
      return{
        productos: []
      }
    },
    methods: {
      async obtener_productos(){
        let usuario_p = {
          usuario: this.$store.state.mi_usuario
        }
        const apiUrl = import.meta.env.VITE_API_HOST;
        
        await fetch(`http://${apiUrl}:8001/utecshop/tienda`, {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(usuario_p)
        }).then((resp)=> resp.json()).then((datos)=> this.productos = datos)
      },
      async comprar(codigo_p, usuario_v){
        let n_compra = {
            codigo_producto: codigo_p, 
            usuario_comprador: this.$store.state.mi_usuario,
            usuario_vendedor: usuario_v
        }
        await fetch(`http://${apiUrl}:8001/utecshop/registrar_compra`, {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: JSON.stringify(n_compra)
        })
        alert("Producto comprado");
        this.$router.push('/productos');
      }
    },
    created(){
      this.obtener_productos()
    }
  }
  </script>
  
  <style scoped>
  
  </style>