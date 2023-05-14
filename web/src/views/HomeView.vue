<template>
  <div class="container">
    <div class="home">
      <h1 class="logo-text">Utec Shop</h1>
      <div v-for="usuario of usuarios" :key="usuario.id">
        <h2 v-if="usuario.nombre_usuario === $store.state.mi_usuario">Usuario: {{ usuario.nombre_usuario }}</h2>
        <h2 v-if="usuario.contrasenha === $store.state.mi_contrasenha">Contraseña: {{ usuario.contrasenha }}</h2>
      </div>
      <div class="button-container">
        <router-link to="/comprar" class="button">Comprar</router-link>
        <router-link to="/productos" class="button">Mis productos</router-link>
        <router-link to="/inventario" class="button">Mis compras</router-link>
        <router-link to="/" class="button">Logout</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 85vh;
}

.home {
  text-align: center;
}

.logo-text {
  font-family: 'BebasNeue-Regular', sans-serif;
  font-size: 100px;
  color: #000000;
  letter-spacing: -2px;
  margin-bottom: 20px;
}

h2 {
  font-size: 20px;
  margin-bottom: 10px;
}

.button-container {
  margin-top: 0px;
}

.button {
  display: inline-block;
  margin: 10px;
  padding: 13px 30px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 15px;
}

.button:hover {
  background-color: #0056b3;
}
</style>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      usuarios: []
    };
  },
  methods: {
    async obtenerUsuarios() {
      await fetch(`http://localhost:8000/utecshop/usuarios`)
        .then((resp) => resp.json())
        .then((datos) => (this.usuarios = datos));
    }
  },
  created() {
    this.obtenerUsuarios();
  }
};
</script>
