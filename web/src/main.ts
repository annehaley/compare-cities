import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import vuetify from '../plugins/vuetify';
import router from './router';
import { axiosInstance } from './store';

const axiosIns = axios.create({
  baseURL: 'http://localhost:8000',
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
