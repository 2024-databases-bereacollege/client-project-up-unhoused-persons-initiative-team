import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store'; // Import the main Vuex store

// Import Views Components
import HomeView from "@/views/HomeView.vue";
import LoginPage from "@/views/LoginPage.vue";
import ServiceProviders from '@/views/ServiceProviders.vue';
import Services from '@/views/Services.vue';
import VolunteerTable from '@/views/VolunteerTable.vue';
import NeighborTable from '@/views/NeighborTable.vue';
import VisitRecord from '@/views/VisitRecord.vue';
import Inventory from '@/views/Inventory.vue';
import AddVisit from '@/views/AddVisit.vue';
import Instructions from '@/views/Instructions.vue';
import NeighborProfile from '@/components/NeighborProfile.vue';

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: HomeView },
  { path: '/login_page', component: LoginPage },
  { path: '/Instructions', component: Instructions },
  { path: '/Add_Visit', component: AddVisit, meta: { requiresAuth: true } }, // This needs to be a different security level.
  { path: '/Service_Providers', component: ServiceProviders, meta: { requiresAuth: true } },
  { path: '/Services', component: Services, meta: { requiresAuth: true } },
  { path: '/Volunteers', component: VolunteerTable, meta: { requiresAuth: true } },
  { path: '/Neighbors', component: NeighborTable, meta: { requiresAuth: true } },
  { path: '/Visit_Records', component: VisitRecord, meta: { requiresAuth: true } },
  { path: '/Inventory', component: Inventory, meta: { requiresAuth: true } },
  { path: '/Neighbors/:ID', name: 'NeighborProfile', component: NeighborProfile, props: true, meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', redirect: '/home' },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = store.getters['auth/isAuthenticated'];


 // const isAuthenticated = store.getters['auth/isAuthenticated']; // Get the authentication state from the auth module

  if (requiresAuth && !isAuthenticated) {
    next('/login_page');
  } else {
    next();
  }
});

export default router;
