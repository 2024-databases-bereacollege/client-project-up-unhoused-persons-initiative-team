import { createRouter, createWebHistory } from 'vue-router';

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
    { 
        path: '/', 
        redirect: '/home', // Redirect root to home as a default route
    },
    { 
        path: '/home', 
        component: HomeView,
    },
    { 
        path: '/login_page', 
        component: LoginPage,
    },
    { path: '/Service_Providers', component: ServiceProviders },
    { path: '/Services', component: Services },
    { path: '/Volunteers', component: VolunteerTable },
    { path: '/Neighbors', component: NeighborTable },
    { path: '/Visit_Records', component: VisitRecord },
    { path: '/Inventory', component: Inventory },
    { path: '/Add_Visit', component: AddVisit},
    { path: '/Instructions', component: Instructions},
    { path: '/Neighbors/:ID', component: NeighborProfile },//check syntax
    { path: '/:pathMatch(.*)*', redirect: '/home' }, // Redirect all other paths to home
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes 
});

export default router;
