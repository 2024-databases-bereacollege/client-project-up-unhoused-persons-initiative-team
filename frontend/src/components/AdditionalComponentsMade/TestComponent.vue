<template>
  <div>
    <button @click="fetchFromRoot" class="btn btn-primary">Fetch from Root (/)</button>
    <button @click="fetchFromTest" class="btn btn-primary">Fetch from /test</button>
    <button @click="fetchFromNeighborTable" class="btn btn-primary">Fetch from /NeighborTable</button>

    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'TestComponent',
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    fetchFromRoot() {
      const path = 'http://127.0.0.1:5000/';
      this.fetchData(path);
    },
    fetchFromTest() {
      const path = 'http://127.0.0.1:5000/test';
      this.fetchData(path);
    },
    fetchFromNeighborTable() {
      const path = 'http://127.0.0.1:5000/NeighborTable';
      this.fetchData(path);
    },
    fetchData(path) {
      axios.get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data.message; 
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.fetchFromRoot();
  },
}
</script>
