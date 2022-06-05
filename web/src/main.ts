import Vue from 'vue';
import '../plugins/composition';
import App from './App.vue';
import vuetify from '../plugins/vuetify';
import router from './router';
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    // demo key from Google documentation
    key: 'AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg',
    libraries: 'places',
  }
});


new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
