import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Map from './components/Map.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: Map,
  },
  {
    path: '*',
    redirect: '/',
  },
];

const router = new VueRouter({
  routes,
});

export default router;
