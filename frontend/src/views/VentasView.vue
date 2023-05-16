<template>
  <div class="page-background">
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
    <router-link to="/registrar_producto" class="button">Registrar producto</router-link> |
    <router-link to="/home" class="button">Casa</router-link>
  </nav>
  </div>
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
      let usuario_p = { usuario: this.$store.state.mi_usuario };
      await fetch(`http://LB-ProyParcial-1528179989.us-east-1.elb.amazonaws.com:8081/utecshop/productos`, {
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
/* Clase global para el fondo de la página */
.page-background {
  background-image: url('../assets/fondotablas.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
}

.ventas {
  margin-top: 20px;
}

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

tbody {
  background: rgb(255, 255, 255, 0.5);
}

nav {
  margin-top: 20px;
}

nav a {
  margin-right: 10px;
  color: #fff;
  text-decoration: none;
  background-color: #000;
  padding: 8px 16px;
  border-radius: 4px;
}

.button:hover {
  background-color: #333;
}

.button:active {
  background-color: #555;
}
</style>