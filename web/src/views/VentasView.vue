<template>
  <div class="ventas">
    <table class="table">
      <thead>
        <tr>
          <th>Código</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Marca</th>
          <th>Categoría</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto of productos" :key="producto.codigo">
          <td>{{ producto.codigo }}</td>
          <td>{{ producto.nombre }}</td>
          <td>S/ {{ producto.precio }}</td>
          <td>{{ producto.marca }}</td>
          <td>{{ producto.categoria }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <nav>
    <router-link to="/registrar_producto">Registrar producto</router-link> |
    <router-link to="/home">Casa</router-link>
  </nav>
</template>

<script>
export default {
  name: "VentasView",
  data() {
    return {
      productos: [],
    };
  },
  methods: {
    async obtener_productos() {
      const apiUrl = import.meta.env.VITE_API_HOST;

      let usuario_p = { usuario: this.$store.state.mi_usuario };
      await fetch(`http://${apiUrl}:8081/utecshop/productos`, {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(usuario_p),
      })
        .then((resp) => resp.json())
        .then((datos) => (this.productos = datos));
    },
  },
  created() {
    this.obtener_productos();
  },
};
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.table th,
.table td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

.table th {
  background-color: #f2f2f2;
  font-weight: bold;
}

nav {
  margin-top: 20px;
}

nav a {
  margin-right: 10px;
  color: #000;
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}
</style>
