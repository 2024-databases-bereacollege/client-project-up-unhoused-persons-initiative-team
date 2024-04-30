<template>
  <v-card>
    <v-toolbar color="primary">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>UP Initiative</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs
          v-model="tab"
          align-tabs="title"
        >
          <v-tab
            v-for="item in items"
            :key="item"
            :value="item"
          >
            {{ item }}
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <v-window v-model="tab">
      <v-window-item
        v-for="item in items"
        :key="item"
        :value="item"
      >
        <v-card flat>
          <v-card-title>{{ CRUDTableVue }}</v-card-title>
          <v-card-text v-text="text"></v-card-text>
        </v-card>
      </v-window-item>
    </v-window>
  </v-card>
</template>
<script>
//import CRUDTableVue from './CRUDTable.vue'
  export default {
    data () {
      return {
        tab: null,
        // items: [
        //   'Add Visit', 'Neighbors', 'Volunteers', 'Service Providers', 'Inventory',
        // ],
        //component: CRUDTableVue
        //text: 'hello',
      }
    },
  }
  
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
.content {
  margin-left: 16rem; /* Push content to the right of the sidebar */
  padding: 1rem; /* padding: 1rem; Padding around content */
}
</style>
