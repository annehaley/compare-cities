<script lang="ts">
import Vue from 'vue';
import VueCompositionApi from '@vue/composition-api';

Vue.use(VueCompositionApi)

export default Vue.extend({
  name: 'App',

  data: () => ({
    //
  }),
});
</script>

<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    />

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
