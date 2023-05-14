<template>
  <div class="compras">
    <table>
      <thead>
        <tr>
          <th>Código</th>
          <th>Vendedor</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Marca</th>
          <th>Categoría</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in productos" :key="producto.codigo">
          <td>{{ producto.codigo }}</td>
          <td>{{ producto.usuario_nombre }}</td>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.precio }}</td>
          <td>{{ producto.marca }}</td>
          <td>{{ producto.tipo }}</td>
          <td><button @click="comprar(producto.codigo, producto.usuario_nombre)">Comprar</button></td>
        </tr>
      </tbody>
    </table>
  </div>
  <nav>
    <router-link to="/home">Casa</router-link>
  </nav>
</template>

<script>
export default {
  name: "ComprasView",
  data() {
    return {
      productos: []
    };
  },
  methods: {
    async obtener_productos() {
      const apiUrl = import.meta.env.VITE_API_HOST;
      let usuario_p = {
        usuario: this.$store.state.mi_usuario
      };
      await fetch(`http://${apiUrl}:8001/utecshop/tienda`, {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(usuario_p)
      })
        .then((resp) => resp.json())
        .then((datos) => (this.productos = datos));
    },
    async comprar(codigo_p, usuario_v) {
      const apiUrl = import.meta.env.VITE_API_HOST;
      let n_compra = {
        codigo_producto: codigo_p,
        usuario_comprador: this.$store.state.mi_usuario,
        usuario_vendedor: usuario_v
      };
      await fetch(`http://${apiUrl}:8001/utecshop/registrar_compra`, {
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(n_compra)
      });
      alert("Producto comprado");
      this.$router.push("/productos");
    }
  },
  created() {
    this.obtener_productos();
  }
};
</script>

<style scoped>
.compras {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

button {
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

nav {
  margin-top: 20px;
}

nav a {
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
}

nav a:hover {
  background-color: #0056b3;
}
</style>
