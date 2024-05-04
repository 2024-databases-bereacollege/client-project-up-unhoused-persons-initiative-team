import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store/auth'; // Import the authentication store module

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
import MainNeighborPage from '@/views/mainNeighborPage.vue';

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: HomeView },
  { path: '/login_page', component: LoginPage },
  { path: '/Service_Providers', component: ServiceProviders, meta: { requiresAuth: true } },
  { path: '/Services', component: Services, meta: { requiresAuth: true } },
  { path: '/Volunteers', component: VolunteerTable, meta: { requiresAuth: true } },
  { path: '/Neighbors', component: NeighborTable, meta: { requiresAuth: true } },
  { path: '/Visit_Records', component: VisitRecord, meta: { requiresAuth: true } },
  { path: '/Inventory', component: Inventory, meta: { requiresAuth: true } },
  { path: '/Add_Visit', component: AddVisit, meta: { requiresAuth: true } },
  { path: '/Instructions', component: Instructions },
  { path: '/Neighbors/:ID', component: NeighborProfile, props: true, meta: { requiresAuth: true } },
  { path: '/Neighbors/MNP', component: MainNeighborPage, meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', redirect: '/home' },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const isAuthenticated = store.getters.isAuthenticated; // Get the authentication state from the store
  
  if (requiresAuth && !isAuthenticated) {
    next('/login_page');
  } else {
    next();
  }
});

export default router;
