import axios from 'axios';
import Vue from 'vue';
import VueCompositionAPI from '@vue/composition-api';
import App from './App.vue';
import vuetify from '../plugins/vuetify';
import router from './router';
import { axiosInstance } from './store';

Vue.use(VueCompositionAPI);

const axiosIns = axios.create({
  baseURL: process.env.VUE_APP_API_ROOT,
});
axiosInstance.value = axiosIns;

new Vue({
  provide: {
    axios: axiosInstance,
  },
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
