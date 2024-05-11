import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store'; // Import the main Vuex store

// Import Views Components
import HomeView from "@/views/HomeView.vue";
import LoginPage from "@/views/LoginPage.vue";
//import ServiceProviders from '@/views/ServiceProviders.vue';
import ServicesAndProviders from '@/views/ServicesAndProviders.vue';
import VolunteerTable from '@/views/VolunteerTable.vue';
import NeighborTable from '@/views/NeighborTable.vue';
//import VisitLogs from '@/views/VisitLogs.vue';
import VisitLogs from '@/views/VisitLogs.vue';
//import VisitRecord from '@/views/VisitRecord.vue';
//import Inventory from '@/views/Inventory.vue';
import AddVisit from '@/views/AddVisit.vue';
import Instructions from '@/views/Instructions.vue';
import NeighborProfile from '@/components/NeighborProfile.vue';
import Queries from '@/views/Queries.vue';
import InvalidAccess from '@/components/InvalidAccess.vue';

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: HomeView },
  { path: '/login_page', component: LoginPage },
  { path: '/Instructions', component: Instructions },
  { path: '/Add_Visit', component: AddVisit, meta: { requiresAuth: true } }, //TODO: This needs to be a different security level.
  //{ path: '/Service_Providers', component: ServiceProviders, meta: { requiresAuth: true } },
  { path: '/ServicesAndProviders', component: ServicesAndProviders, meta: { requiresAuth: true, requiresRecordAccess: true } }, //TODO need to check in with client on which pages should be harder to access
  { path: '/Volunteers', component: VolunteerTable, meta: { requiresAuth: true, requiresRecordAccess: true } },
  { path: '/Neighbors', component: NeighborTable, meta: { requiresAuth: true } },
  { path: '/Visit_Logs', component: VisitLogs, meta: { requiresAuth: true } },
  //{ path: '/Visit_Records', component: VisitRecord, meta: { requiresAuth: true } },
  //{ path: '/Inventory', component: Inventory, meta: { requiresAuth: true } },
  { path: '/Neighbors/:ID', name: 'NeighborProfile', component: NeighborProfile, props: true, meta: { requiresAuth: true } },
  { path: '/Queries', component: Queries, meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', redirect: '/home' },
  { path: '/InvalidAccess', component: InvalidAccess, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresRecordAccess = to.matched.some(record => record.meta.requiresRecordAccess);
  const isAuthenticated = store.getters['auth/isAuthenticated'];
  const hasRecordAccess = store.getters['auth/hasRecordAccess'];

  if (requiresAuth && !isAuthenticated) {
    next('/login_page');
  } else if (requiresRecordAccess && !hasRecordAccess) {
    // Redirect to a page indicating insufficient access
    next('/InvalidAccess');
  } else {
    next();
  }
});

export default router;
