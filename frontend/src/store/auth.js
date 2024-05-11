// store/auth.js
const authModule = {
  namespaced: true,
    state: {
      isAuthenticated: false,
      volunteer: null,
      hasRecordAccess: false, 
    },
    mutations: {
      setIsAuthenticated(state, value) {
        state.isAuthenticated = value;
      },
      setHasRecordAccess(state, hasRecordAccess) {
        state.hasRecordAccess = hasRecordAccess;
      },
    setVolunteer(state, volunteer) {
      state.volunteer = volunteer;
    },
    },
    actions: {
      setVolunteer({ commit }, volunteer) {
        commit('setVolunteer', volunteer);
      },
      setHasRecordAccess({ commit }, hasRecordAccess) {
        commit('setHasRecordAccess', hasRecordAccess);
      },
  
      login({ commit }) {
        // Perform login logic, e.g., send a request to the server
        commit('setIsAuthenticated', true);
      },
      logout({ commit }) {
        commit('setIsAuthenticated', false);
        commit('setVolunteer', null);
        commit('setHasRecordAccess', false);
        localStorage.removeItem('loggedInVolunteer');
      },
      checkLocalStorage({ commit }) {
        const loggedInVolunteer = localStorage.getItem('loggedInVolunteer');
        if (loggedInVolunteer) {
          const volunteer = JSON.parse(loggedInVolunteer);
          commit('setVolunteer', volunteer);
          commit('setIsAuthenticated', true);
          commit('setHasRecordAccess', volunteer.has_record_access);
        }
      },
    },
    getters: {
      isAuthenticated: state => state.isAuthenticated,
      hasRecordAccess: state => state.hasRecordAccess,
    },
  };
  
  export default authModule;
